Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/ingestion/

Markdown Content:
Index - LlamaIndex


IngestionPipeline [#](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.IngestionPipeline "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

An ingestion pipeline that can be applied to data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | 
Unique name of the ingestion pipeline. Defaults to DEFAULT\_PIPELINE\_NAME.



 | `DEFAULT_PIPELINE_NAME` |
| `project_name` | `str` | 

Unique name of the project. Defaults to DEFAULT\_PROJECT\_NAME.



 | `DEFAULT_PROJECT_NAME` |
| `transformations` | `List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]` | 

Transformations to apply to the data. Defaults to None.



 | `None` |
| `documents` | `Optional[Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]]` | 

Documents to ingest. Defaults to None.



 | `None` |
| `readers` | `Optional[List[ReaderConfig]]` | 

Reader to use to read the data. Defaults to None.



 | `None` |
| `vector_store` | `Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")]` | 

Vector store to use to store the data. Defaults to None.



 | `None` |
| `cache` | `Optional[IngestionCache]` | 

Cache to use to store the data. Defaults to None.



 | `None` |
| `docstore` | `Optional[[BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.BaseDocumentStore")]` | 

Document store to use for de-duping with a vector store. Defaults to None.



 | `None` |
| `docstore_strategy` | `[DocstoreStrategy](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.DocstoreStrategy "llama_index.core.ingestion.pipeline.DocstoreStrategy")` | 

Document de-dup strategy. Defaults to DocstoreStrategy.UPSERTS.



 | `UPSERTS` |
| `disable_cache` | `bool` | 

Disable the cache. Defaults to False.



 | `False` |
| `base_url` | `str` | 

Base URL for the LlamaCloud API. Defaults to DEFAULT\_BASE\_URL.



 | _required_ |
| `app_url` | `str` | 

Base URL for the LlamaCloud app. Defaults to DEFAULT\_APP\_URL.



 | _required_ |
| `api_key` | `Optional[str]` | 

LlamaCloud API key. Defaults to None.



 | _required_ |

**Examples:**

```
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=20),
        OpenAIEmbedding(),
    ],
)

nodes = pipeline.run(documents=documents)
```

Source code in `llama-index-core/llama_index/core/ingestion/pipeline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">188</span>
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
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IngestionPipeline</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    An ingestion pipeline that can be applied to data.</span>

<span class="sd">    Args:</span>
<span class="sd">        name (str, optional):</span>
<span class="sd">            Unique name of the ingestion pipeline. Defaults to DEFAULT_PIPELINE_NAME.</span>
<span class="sd">        project_name (str, optional):</span>
<span class="sd">            Unique name of the project. Defaults to DEFAULT_PROJECT_NAME.</span>
<span class="sd">        transformations (List[TransformComponent], optional):</span>
<span class="sd">            Transformations to apply to the data. Defaults to None.</span>
<span class="sd">        documents (Optional[Sequence[Document]], optional):</span>
<span class="sd">            Documents to ingest. Defaults to None.</span>
<span class="sd">        readers (Optional[List[ReaderConfig]], optional):</span>
<span class="sd">            Reader to use to read the data. Defaults to None.</span>
<span class="sd">        vector_store (Optional[BasePydanticVectorStore], optional):</span>
<span class="sd">            Vector store to use to store the data. Defaults to None.</span>
<span class="sd">        cache (Optional[IngestionCache], optional):</span>
<span class="sd">            Cache to use to store the data. Defaults to None.</span>
<span class="sd">        docstore (Optional[BaseDocumentStore], optional):</span>
<span class="sd">            Document store to use for de-duping with a vector store. Defaults to None.</span>
<span class="sd">        docstore_strategy (DocstoreStrategy, optional):</span>
<span class="sd">            Document de-dup strategy. Defaults to DocstoreStrategy.UPSERTS.</span>
<span class="sd">        disable_cache (bool, optional):</span>
<span class="sd">            Disable the cache. Defaults to False.</span>
<span class="sd">        base_url (str, optional):</span>
<span class="sd">            Base URL for the LlamaCloud API. Defaults to DEFAULT_BASE_URL.</span>
<span class="sd">        app_url (str, optional):</span>
<span class="sd">            Base URL for the LlamaCloud app. Defaults to DEFAULT_APP_URL.</span>
<span class="sd">        api_key (Optional[str], optional):</span>
<span class="sd">            LlamaCloud API key. Defaults to None.</span>

<span class="sd">    Examples:</span>
<span class="sd">        ```python</span>
<span class="sd">        from llama_index.core.ingestion import IngestionPipeline</span>
<span class="sd">        from llama_index.core.node_parser import SentenceSplitter</span>
<span class="sd">        from llama_index.embeddings.openai import OpenAIEmbedding</span>

<span class="sd">        pipeline = IngestionPipeline(</span>
<span class="sd">            transformations=[</span>
<span class="sd">                SentenceSplitter(chunk_size=512, chunk_overlap=20),</span>
<span class="sd">                OpenAIEmbedding(),</span>
<span class="sd">            ],</span>
<span class="sd">        )</span>

<span class="sd">        nodes = pipeline.run(documents=documents)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_PIPELINE_NAME</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Unique name of the ingestion pipeline"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_PROJECT_NAME</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Unique name of the project"</span>
    <span class="p">)</span>

    <span class="n">transformations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Transformations to apply to the data"</span>
    <span class="p">)</span>

    <span class="n">documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Documents to ingest"</span><span class="p">)</span>
    <span class="n">readers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ReaderConfig</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Reader to use to read the data"</span>
    <span class="p">)</span>
    <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Vector store to use to store the data"</span>
    <span class="p">)</span>
    <span class="n">cache</span><span class="p">:</span> <span class="n">IngestionCache</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">IngestionCache</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Cache to use to store the data"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">docstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseDocumentStore</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Document store to use for de-duping with a vector store."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">docstore_strategy</span><span class="p">:</span> <span class="n">DocstoreStrategy</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Document de-dup strategy."</span>
    <span class="p">)</span>
    <span class="n">disable_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Disable the cache"</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PIPELINE_NAME</span><span class="p">,</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PROJECT_NAME</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">readers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ReaderConfig</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cache</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IngestionCache</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseDocumentStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstore_strategy</span><span class="p">:</span> <span class="n">DocstoreStrategy</span> <span class="o">=</span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS</span><span class="p">,</span>
        <span class="n">disable_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">transformations</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">transformations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_transformations</span><span class="p">()</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">readers</span><span class="o">=</span><span class="n">readers</span><span class="p">,</span>
            <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="n">vector_store</span><span class="p">,</span>
            <span class="n">cache</span><span class="o">=</span><span class="n">cache</span> <span class="ow">or</span> <span class="n">IngestionCache</span><span class="p">(),</span>
            <span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">,</span>
            <span class="n">docstore_strategy</span><span class="o">=</span><span class="n">docstore_strategy</span><span class="p">,</span>
            <span class="n">disable_cache</span><span class="o">=</span><span class="n">disable_cache</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./pipeline_storage"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cache_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CACHE_NAME</span><span class="p">,</span>
        <span class="n">docstore_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the pipeline to disk."""</span>
        <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">persist_dir</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>  <span class="c1"># NOTE: doesn't support Windows here</span>
            <span class="n">docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">)</span>
            <span class="n">cache_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">cache_name</span><span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">persist_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
            <span class="n">docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_path</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
            <span class="n">cache_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_path</span> <span class="o">/</span> <span class="n">cache_name</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">cache_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">docstore_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./pipeline_storage"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cache_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CACHE_NAME</span><span class="p">,</span>
        <span class="n">docstore_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load the pipeline from disk."""</span>
        <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">IngestionCache</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">cache_name</span><span class="p">),</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>
            <span class="n">persist_docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_docstore_path</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                    <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">),</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">IngestionCache</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">cache_name</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">persist_docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_docstore_path</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                    <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
                <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_default_transformations</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">SentenceSplitter</span><span class="p">(),</span>
            <span class="n">Settings</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">_prepare_inputs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]],</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">input_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">documents</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">input_nodes</span> <span class="o">+=</span> <span class="n">documents</span>

        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">input_nodes</span> <span class="o">+=</span> <span class="n">nodes</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">documents</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">input_nodes</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">documents</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">reader</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers</span><span class="p">:</span>
                <span class="n">input_nodes</span> <span class="o">+=</span> <span class="n">reader</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">input_nodes</span>

    <span class="k">def</span> <span class="nf">_handle_duplicates</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">store_doc_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Handle docstore duplicates by checking all hashes."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="n">existing_hashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_all_document_hashes</span><span class="p">()</span>
        <span class="n">current_hashes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">existing_hashes</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">current_hashes</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
                <span class="n">nodes_to_run</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">current_hashes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes_to_run</span><span class="p">,</span> <span class="n">store_text</span><span class="o">=</span><span class="n">store_doc_text</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes_to_run</span>

    <span class="k">def</span> <span class="nf">_handle_upserts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">store_doc_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Handle docstore upserts by checking hashes and ids."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="n">existing_doc_ids_before</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_all_document_hashes</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="n">doc_ids_from_nodes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">deduped_nodes_to_run</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span> <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span> <span class="k">else</span> <span class="n">node</span><span class="o">.</span><span class="n">id_</span>
            <span class="n">doc_ids_from_nodes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
            <span class="n">existing_hash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">existing_hash</span><span class="p">:</span>
                <span class="c1"># document doesn't exist, so add it</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
                <span class="n">deduped_nodes_to_run</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="k">elif</span> <span class="n">existing_hash</span> <span class="ow">and</span> <span class="n">existing_hash</span> <span class="o">!=</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

                <span class="n">deduped_nodes_to_run</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">continue</span>  <span class="c1"># document exists and is unchanged, so skip it</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span><span class="p">:</span>
                <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_duplicates</span><span class="p">(</span>
                    <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid docstore strategy: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS_AND_DELETE</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span>
                    <span class="s2">"Docstore strategy set to upserts and delete, but no vector store. "</span>
                    <span class="s2">"Switching to duplicates_only strategy."</span>
                <span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o">=</span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_duplicates</span><span class="p">(</span>
                <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="n">input_nodes</span>

        <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">():</span>
                <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                    <span class="s2">"Specified num_workers exceed number of CPUs in the system. "</span>
                    <span class="s2">"Setting `num_workers` down to the maximum CPU count."</span>
                <span class="p">)</span>

            <span class="k">with</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">get_context</span><span class="p">(</span><span class="s2">"spawn"</span><span class="p">)</span><span class="o">.</span><span class="n">Pool</span><span class="p">(</span><span class="n">num_workers</span><span class="p">)</span> <span class="k">as</span> <span class="n">p</span><span class="p">:</span>
                <span class="n">node_batches</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_batcher</span><span class="p">(</span>
                    <span class="n">num_batches</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span> <span class="n">nodes</span><span class="o">=</span><span class="n">nodes_to_run</span>
                <span class="p">)</span>
                <span class="n">nodes_parallel</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">starmap</span><span class="p">(</span>
                    <span class="n">run_transformations</span><span class="p">,</span>
                    <span class="nb">zip</span><span class="p">(</span>
                        <span class="n">node_batches</span><span class="p">,</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="n">in_place</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="n">cache_collection</span><span class="p">),</span>
                    <span class="p">),</span>
                <span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">nodes_parallel</span><span class="p">,</span> <span class="p">[])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
                <span class="n">nodes_to_run</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                <span class="n">cache_collection</span><span class="o">=</span><span class="n">cache_collection</span><span class="p">,</span>
                <span class="n">in_place</span><span class="o">=</span><span class="n">in_place</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">add</span><span class="p">([</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span> <span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="c1"># ------ async methods ------</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_ahandle_duplicates</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">store_doc_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Handle docstore duplicates by checking all hashes."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="n">existing_hashes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aget_all_document_hashes</span><span class="p">()</span>
        <span class="n">current_hashes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">existing_hashes</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">current_hashes</span><span class="p">:</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aset_document_hash</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
                <span class="n">nodes_to_run</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">current_hashes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">async_add_documents</span><span class="p">(</span><span class="n">nodes_to_run</span><span class="p">,</span> <span class="n">store_text</span><span class="o">=</span><span class="n">store_doc_text</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes_to_run</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_ahandle_upserts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">store_doc_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Handle docstore upserts by checking hashes and ids."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="n">existing_doc_ids_before</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span>
            <span class="p">(</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aget_all_document_hashes</span><span class="p">())</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">doc_ids_from_nodes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">deduped_nodes_to_run</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span> <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span> <span class="k">else</span> <span class="n">node</span><span class="o">.</span><span class="n">id_</span>
            <span class="n">doc_ids_from_nodes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
            <span class="n">existing_hash</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aget_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">existing_hash</span><span class="p">:</span>
                <span class="c1"># document doesn't exist, so add it</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aset_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
                <span class="n">deduped_nodes_to_run</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="k">elif</span> <span class="n">existing_hash</span> <span class="ow">and</span> <span class="n">existing_hash</span> <span class="o">!=</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">:</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">adelete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">adelete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">aset_document_hash</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

                <span class="n">deduped_nodes_to_run</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">continue</span>  <span class="c1"># document exists and is unchanged, so skip it</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span><span class="p">:</span>
                <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ahandle_duplicates</span><span class="p">(</span>
                    <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid docstore strategy: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS_AND_DELETE</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span>
                    <span class="s2">"Docstore strategy set to upserts and delete, but no vector store. "</span>
                    <span class="s2">"Switching to duplicates_only strategy."</span>
                <span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o">=</span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ahandle_duplicates</span><span class="p">(</span>
                <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="n">input_nodes</span>

        <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">():</span>
                <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                    <span class="s2">"Specified num_workers exceed number of CPUs in the system. "</span>
                    <span class="s2">"Setting `num_workers` down to the maximum CPU count."</span>
                <span class="p">)</span>

            <span class="n">loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
            <span class="k">with</span> <span class="n">ProcessPoolExecutor</span><span class="p">(</span><span class="n">max_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">)</span> <span class="k">as</span> <span class="n">p</span><span class="p">:</span>
                <span class="n">node_batches</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_batcher</span><span class="p">(</span>
                    <span class="n">num_batches</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span> <span class="n">nodes</span><span class="o">=</span><span class="n">nodes_to_run</span>
                <span class="p">)</span>
                <span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span>
                        <span class="n">p</span><span class="p">,</span>
                        <span class="n">partial</span><span class="p">(</span>
                            <span class="n">arun_transformations_wrapper</span><span class="p">,</span>
                            <span class="n">transformations</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">,</span>
                            <span class="n">in_place</span><span class="o">=</span><span class="n">in_place</span><span class="p">,</span>
                            <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                            <span class="n">cache_collection</span><span class="o">=</span><span class="n">cache_collection</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">batch</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="n">node_batches</span>
                <span class="p">]</span>
                <span class="n">result</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="p">[])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="n">arun_transformations</span><span class="p">(</span>
                <span class="n">nodes_to_run</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                <span class="n">cache_collection</span><span class="o">=</span><span class="n">cache_collection</span><span class="p">,</span>
                <span class="n">in_place</span><span class="o">=</span><span class="n">in_place</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">async_add</span><span class="p">(</span>
                <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span> <span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">]</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.IngestionPipeline.persist "Permanent link")

```
persist(persist_dir: str = './pipeline_storage', fs: Optional[AbstractFileSystem] = None, cache_name: str = DEFAULT_CACHE_NAME, docstore_name: str = DOCSTORE_FNAME) -> None
```

Persist the pipeline to disk.

Source code in `llama-index-core/llama_index/core/ingestion/pipeline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">301</span>
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
<span class="normal">321</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./pipeline_storage"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cache_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CACHE_NAME</span><span class="p">,</span>
    <span class="n">docstore_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the pipeline to disk."""</span>
    <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">persist_dir</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>  <span class="c1"># NOTE: doesn't support Windows here</span>
        <span class="n">docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">)</span>
        <span class="n">cache_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">cache_name</span><span class="p">)</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="n">persist_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
        <span class="n">docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_path</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
        <span class="n">cache_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_path</span> <span class="o">/</span> <span class="n">cache_name</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">cache_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">docstore_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load [#](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.IngestionPipeline.load "Permanent link")

```
load(persist_dir: str = './pipeline_storage', fs: Optional[AbstractFileSystem] = None, cache_name: str = DEFAULT_CACHE_NAME, docstore_name: str = DOCSTORE_FNAME) -> None
```

Load the pipeline from disk.

Source code in `llama-index-core/llama_index/core/ingestion/pipeline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">323</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./pipeline_storage"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cache_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CACHE_NAME</span><span class="p">,</span>
    <span class="n">docstore_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load the pipeline from disk."""</span>
    <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">IngestionCache</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
            <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">cache_name</span><span class="p">),</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
        <span class="p">)</span>
        <span class="n">persist_docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_docstore_path</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_name</span><span class="p">),</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">IngestionCache</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">cache_name</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">persist_docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_docstore_path</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">docstore_name</span><span class="p">)</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.IngestionPipeline.run "Permanent link")

```
run(show_progress: bool = False, documents: Optional[List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]] = None, nodes: Optional[List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]] = None, cache_collection: Optional[str] = None, in_place: bool = True, store_doc_text: bool = True, num_workers: Optional[int] = None, **kwargs: Any) -> Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Run a series of transformations on a set of nodes.

If a vector store is provided, nodes with embeddings will be added to the vector store.

If a vector store + docstore are provided, the docstore will be used to de-duplicate documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Shows execution progress bar(s). Defaults to False.



 | `False` |
| `documents` | `Optional[List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]]` | 

Set of documents to be transformed. Defaults to None.



 | `None` |
| `nodes` | `Optional[List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]]` | 

Set of nodes to be transformed. Defaults to None.



 | `None` |
| `cache_collection` | `Optional[str]` | 

Cache for transformations. Defaults to None.



 | `None` |
| `in_place` | `bool` | 

Whether transformations creates a new list for transformed nodes or modifies the array passed to `run_transformations`. Defaults to True.



 | `True` |
| `num_workers` | `Optional[int]` | 

The number of parallel processes to use. If set to None, then sequential compute is used. Defaults to None.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
Sequence\[BaseNode\]: The set of transformed Nodes/Documents



 |

Source code in `llama-index-core/llama_index/core/ingestion/pipeline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">450</span>
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
<span class="normal">554</span>
<span class="normal">555</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cache_collection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">in_place</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">store_doc_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Run a series of transformations on a set of nodes.</span>

<span class="sd">    If a vector store is provided, nodes with embeddings will be added to the vector store.</span>

<span class="sd">    If a vector store + docstore are provided, the docstore will be used to de-duplicate documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool, optional): Shows execution progress bar(s). Defaults to False.</span>
<span class="sd">        documents (Optional[List[Document]], optional): Set of documents to be transformed. Defaults to None.</span>
<span class="sd">        nodes (Optional[List[BaseNode]], optional): Set of nodes to be transformed. Defaults to None.</span>
<span class="sd">        cache_collection (Optional[str], optional): Cache for transformations. Defaults to None.</span>
<span class="sd">        in_place (bool, optional): Whether transformations creates a new list for transformed nodes or modifies the</span>
<span class="sd">            array passed to `run_transformations`. Defaults to True.</span>
<span class="sd">        num_workers (Optional[int], optional): The number of parallel processes to use.</span>
<span class="sd">            If set to None, then sequential compute is used. Defaults to None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Sequence[BaseNode]: The set of transformed Nodes/Documents</span>
<span class="sd">    """</span>
    <span class="n">input_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_inputs</span><span class="p">(</span><span class="n">documents</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>

    <span class="c1"># check if we need to dedup</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS</span><span class="p">,</span>
            <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS_AND_DELETE</span><span class="p">,</span>
        <span class="p">):</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_upserts</span><span class="p">(</span>
                <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="s2">"Docstore strategy set to upserts, but no vector store. "</span>
                <span class="s2">"Switching to duplicates_only strategy."</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o">=</span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span><span class="p">:</span>
            <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ahandle_duplicates</span><span class="p">(</span>
                <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid docstore strategy: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o"></span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">UPSERTS_AND_DELETE</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="s2">"Docstore strategy set to upserts and delete, but no vector store. "</span>
                <span class="s2">"Switching to duplicates_only strategy."</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore_strategy</span> <span class="o">=</span> <span class="n">DocstoreStrategy</span><span class="o">.</span><span class="n">DUPLICATES_ONLY</span>
        <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ahandle_duplicates</span><span class="p">(</span>
            <span class="n">input_nodes</span><span class="p">,</span> <span class="n">store_doc_text</span><span class="o">=</span><span class="n">store_doc_text</span>
        <span class="p">)</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="n">nodes_to_run</span> <span class="o">=</span> <span class="n">input_nodes</span>

    <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">():</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"Specified num_workers exceed number of CPUs in the system. "</span>
                <span class="s2">"Setting `num_workers` down to the maximum CPU count."</span>
            <span class="p">)</span>

        <span class="n">loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">ProcessPoolExecutor</span><span class="p">(</span><span class="n">max_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">)</span> <span class="k">as</span> <span class="n">p</span><span class="p">:</span>
            <span class="n">node_batches</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_batcher</span><span class="p">(</span>
                <span class="n">num_batches</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span> <span class="n">nodes</span><span class="o">=</span><span class="n">nodes_to_run</span>
            <span class="p">)</span>
            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span>
                    <span class="n">p</span><span class="p">,</span>
                    <span class="n">partial</span><span class="p">(</span>
                        <span class="n">arun_transformations_wrapper</span><span class="p">,</span>
                        <span class="n">transformations</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">,</span>
                        <span class="n">in_place</span><span class="o">=</span><span class="n">in_place</span><span class="p">,</span>
                        <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                        <span class="n">cache_collection</span><span class="o">=</span><span class="n">cache_collection</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">batch</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="n">node_batches</span>
            <span class="p">]</span>
            <span class="n">result</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="p">[])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="n">arun_transformations</span><span class="p">(</span>
            <span class="n">nodes_to_run</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_cache</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="n">cache_collection</span><span class="o">=</span><span class="n">cache_collection</span><span class="p">,</span>
            <span class="n">in_place</span><span class="o">=</span><span class="n">in_place</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">async_add</span><span class="p">(</span>
            <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span> <span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">]</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

DocstoreStrategy [#](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/#llama_index.core.ingestion.pipeline.DocstoreStrategy "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Document de-duplication de-deduplication strategies work by comparing the hashes or ids stored in the document store. They require a document store to be set which must be persisted across pipeline runs.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `UPSERTS` |  | 
('upserts') Use upserts to handle duplicates. Checks if the a document is already in the doc store based on its id. If it is not, or if the hash of the document is updated, it will update the document in the doc store and run the transformations.



 |
| `DUPLICATES_ONLY` |  | 

('duplicates\_only') Only handle duplicates. Checks if the hash of a document is already in the doc store. Only then it will add the document to the doc store and run the transformations



 |
| `UPSERTS_AND_DELETE` |  | 

('upserts\_and\_delete') Use upserts and delete to handle duplicates. Like the upsert strategy but it will also delete non-existing documents from the doc store



 |

Source code in `llama-index-core/llama_index/core/ingestion/pipeline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">169</span>
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
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DocstoreStrategy</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Document de-duplication de-deduplication strategies work by comparing the hashes or ids stored in the document store.</span>
<span class="sd">       They require a document store to be set which must be persisted across pipeline runs.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        UPSERTS:</span>
<span class="sd">            ('upserts') Use upserts to handle duplicates. Checks if the a document is already in the doc store based on its id. If it is not, or if the hash of the document is updated, it will update the document in the doc store and run the transformations.</span>
<span class="sd">        DUPLICATES_ONLY:</span>
<span class="sd">            ('duplicates_only') Only handle duplicates. Checks if the hash of a document is already in the doc store. Only then it will add the document to the doc store and run the transformations</span>
<span class="sd">        UPSERTS_AND_DELETE:</span>
<span class="sd">            ('upserts_and_delete') Use upserts and delete to handle duplicates. Like the upsert strategy but it will also delete non-existing documents from the doc store</span>
<span class="sd">    """</span>

    <span class="n">UPSERTS</span> <span class="o">=</span> <span class="s2">"upserts"</span>
    <span class="n">DUPLICATES_ONLY</span> <span class="o">=</span> <span class="s2">"duplicates_only"</span>
    <span class="n">UPSERTS_AND_DELETE</span> <span class="o">=</span> <span class="s2">"upserts_and_delete"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Zilliz](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/)[Next Event handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/)
