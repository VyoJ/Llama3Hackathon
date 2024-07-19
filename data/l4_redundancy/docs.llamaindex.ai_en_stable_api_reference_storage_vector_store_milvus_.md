Title: Milvus - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/

Markdown Content:
Milvus - LlamaIndex


MilvusVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/#llama_index.vector_stores.milvus.MilvusVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

The Milvus Vector Store.

In this vector store we store the text, its embedding and a its metadata in a Milvus collection. This implementation allows the use of an already existing collection. It also supports creating a new one if the collection doesn't exist or if `overwrite` is set to True.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `uri` | `str` | 
The URI to connect to, comes in the form of "https://address:port" for Milvus or Zilliz Cloud service, or "path/to/local/milvus.db" for the lite local Milvus. Defaults to "./milvus\_llamaindex.db".



 | `'./milvus_llamaindex.db'` |
| `token` | `str` | 

The token for log in. Empty if not using rbac, if using rbac it will most likely be "username:password".



 | `''` |
| `collection_name` | `str` | 

The name of the collection where data will be stored. Defaults to "llamalection".



 | `'llamacollection'` |
| `dim` | `int` | 

The dimension of the embedding vectors for the collection. Required if creating a new collection.



 | `None` |
| `embedding_field` | `str` | 

The name of the embedding field for the collection, defaults to DEFAULT\_EMBEDDING\_KEY.



 | `DEFAULT_EMBEDDING_KEY` |
| `doc_id_field` | `str` | 

The name of the doc\_id field for the collection, defaults to DEFAULT\_DOC\_ID\_KEY.



 | `DEFAULT_DOC_ID_KEY` |
| `similarity_metric` | `str` | 

The similarity metric to use, currently supports IP and L2.



 | `'IP'` |
| `consistency_level` | `str` | 

Which consistency level to use for a newly created collection. Defaults to "Strong".



 | `'Strong'` |
| `overwrite` | `bool` | 

Whether to overwrite existing collection with same name. Defaults to False.



 | `False` |
| `text_key` | `str` | 

What key text is stored in in the passed collection. Used when bringing your own collection. Defaults to None.



 | `None` |
| `index_config` | `dict` | 

The configuration used for building the Milvus index. Defaults to None.



 | `None` |
| `search_config` | `dict` | 

The configuration used for searching the Milvus index. Note that this must be compatible with the index type specified by `index_config`. Defaults to None.



 | `None` |
| `batch_size` | `int` | 

Configures the number of documents processed in one batch when inserting data into Milvus. Defaults to DEFAULT\_BATCH\_SIZE.



 | `DEFAULT_BATCH_SIZE` |
| `enable_sparse` | `bool` | 

A boolean flag indicating whether to enable support for sparse embeddings for hybrid retrieval. Defaults to False.



 | `False` |
| `sparse_embedding_function` | `BaseSparseEmbeddingFunction` | 

If enable\_sparse is True, this object should be provided to convert text to a sparse embedding.



 | `None` |
| `hybrid_ranker` | `str` | 

Specifies the type of ranker used in hybrid search queries. Currently only supports \['RRFRanker','WeightedRanker'\]. Defaults to "RRFRanker".



 | `'RRFRanker'` |
| `hybrid_ranker_params` | `dict` | 

Configuration parameters for the hybrid ranker. The structure of this dictionary depends on the specific ranker being used: - For "RRFRanker", it should include: - 'k' (int): A parameter used in Reciprocal Rank Fusion (RRF). This value is used to calculate the rank scores as part of the RRF algorithm, which combines multiple ranking strategies into a single score to improve search relevance. - For "WeightedRanker", it expects: - 'weights' (list of float): A list of exactly two weights: 1. The weight for the dense embedding component. 2. The weight for the sparse embedding component. These weights are used to adjust the importance of the dense and sparse components of the embeddings in the hybrid retrieval process. Defaults to an empty dictionary, implying that the ranker will operate with its predefined default settings.



 | `{}` |

**Raises:**

| Type | Description |
| --- | --- |
| `ImportError` | 
Unable to import `pymilvus`.



 |
| `MilvusException` | 

Error communicating with Milvus, more can be found in logging under Debug.



 |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `MilvusVectorstore` |  | 
Vectorstore that supports add, delete, and query.



 |

**Examples:**

`pip install llama-index-vector-stores-milvus`

```
from llama_index.vector_stores.milvus import MilvusVectorStore

# Setup MilvusVectorStore
vector_store = MilvusVectorStore(
    dim=1536,
    collection_name="your_collection_name",
    uri="http://milvus_address:port",
    token="your_milvus_token_here",
    overwrite=True
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-milvus/llama_index/vector_stores/milvus/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 76</span>
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
<span class="normal">632</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MilvusVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""The Milvus Vector Store.</span>

<span class="sd">    In this vector store we store the text, its embedding and</span>
<span class="sd">    a its metadata in a Milvus collection. This implementation</span>
<span class="sd">    allows the use of an already existing collection.</span>
<span class="sd">    It also supports creating a new one if the collection doesn't</span>
<span class="sd">    exist or if `overwrite` is set to True.</span>

<span class="sd">    Args:</span>
<span class="sd">        uri (str, optional): The URI to connect to, comes in the form of</span>
<span class="sd">            "https://address:port" for Milvus or Zilliz Cloud service,</span>
<span class="sd">            or "path/to/local/milvus.db" for the lite local Milvus. Defaults to</span>
<span class="sd">            "./milvus_llamaindex.db".</span>
<span class="sd">        token (str, optional): The token for log in. Empty if not using rbac, if</span>
<span class="sd">            using rbac it will most likely be "username:password".</span>
<span class="sd">        collection_name (str, optional): The name of the collection where data will be</span>
<span class="sd">            stored. Defaults to "llamalection".</span>
<span class="sd">        dim (int, optional): The dimension of the embedding vectors for the collection.</span>
<span class="sd">            Required if creating a new collection.</span>
<span class="sd">        embedding_field (str, optional): The name of the embedding field for the</span>
<span class="sd">            collection, defaults to DEFAULT_EMBEDDING_KEY.</span>
<span class="sd">        doc_id_field (str, optional): The name of the doc_id field for the collection,</span>
<span class="sd">            defaults to DEFAULT_DOC_ID_KEY.</span>
<span class="sd">        similarity_metric (str, optional): The similarity metric to use,</span>
<span class="sd">            currently supports IP and L2.</span>
<span class="sd">        consistency_level (str, optional): Which consistency level to use for a newly</span>
<span class="sd">            created collection. Defaults to "Strong".</span>
<span class="sd">        overwrite (bool, optional): Whether to overwrite existing collection with same</span>
<span class="sd">            name. Defaults to False.</span>
<span class="sd">        text_key (str, optional): What key text is stored in in the passed collection.</span>
<span class="sd">            Used when bringing your own collection. Defaults to None.</span>
<span class="sd">        index_config (dict, optional): The configuration used for building the</span>
<span class="sd">            Milvus index. Defaults to None.</span>
<span class="sd">        search_config (dict, optional): The configuration used for searching</span>
<span class="sd">            the Milvus index. Note that this must be compatible with the index</span>
<span class="sd">            type specified by `index_config`. Defaults to None.</span>
<span class="sd">        batch_size (int): Configures the number of documents processed in one</span>
<span class="sd">            batch when inserting data into Milvus. Defaults to DEFAULT_BATCH_SIZE.</span>
<span class="sd">        enable_sparse (bool): A boolean flag indicating whether to enable support</span>
<span class="sd">            for sparse embeddings for hybrid retrieval. Defaults to False.</span>
<span class="sd">        sparse_embedding_function (BaseSparseEmbeddingFunction, optional): If enable_sparse</span>
<span class="sd">             is True, this object should be provided to convert text to a sparse embedding.</span>
<span class="sd">        hybrid_ranker (str): Specifies the type of ranker used in hybrid search queries.</span>
<span class="sd">            Currently only supports ['RRFRanker','WeightedRanker']. Defaults to "RRFRanker".</span>
<span class="sd">        hybrid_ranker_params (dict, optional): Configuration parameters for the hybrid ranker.</span>
<span class="sd">            The structure of this dictionary depends on the specific ranker being used:</span>
<span class="sd">            - For "RRFRanker", it should include:</span>
<span class="sd">                - 'k' (int): A parameter used in Reciprocal Rank Fusion (RRF). This value is used</span>
<span class="sd">                             to calculate the rank scores as part of the RRF algorithm, which combines</span>
<span class="sd">                             multiple ranking strategies into a single score to improve search relevance.</span>
<span class="sd">            - For "WeightedRanker", it expects:</span>
<span class="sd">                - 'weights' (list of float): A list of exactly two weights:</span>
<span class="sd">                     1. The weight for the dense embedding component.</span>
<span class="sd">                     2. The weight for the sparse embedding component.</span>
<span class="sd">                  These weights are used to adjust the importance of the dense and sparse components of the embeddings</span>
<span class="sd">                  in the hybrid retrieval process.</span>
<span class="sd">            Defaults to an empty dictionary, implying that the ranker will operate with its predefined default settings.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ImportError: Unable to import `pymilvus`.</span>
<span class="sd">        MilvusException: Error communicating with Milvus, more can be found in logging</span>
<span class="sd">            under Debug.</span>

<span class="sd">    Returns:</span>
<span class="sd">        MilvusVectorstore: Vectorstore that supports add, delete, and query.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-milvus`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.milvus import MilvusVectorStore</span>

<span class="sd">        # Setup MilvusVectorStore</span>
<span class="sd">        vector_store = MilvusVectorStore(</span>
<span class="sd">            dim=1536,</span>
<span class="sd">            collection_name="your_collection_name",</span>
<span class="sd">            uri="http://milvus_address:port",</span>
<span class="sd">            token="your_milvus_token_here",</span>
<span class="sd">            overwrite=True</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">stores_node</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./milvus_llamaindex.db"</span>
    <span class="n">token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llamacollection"</span>
    <span class="n">dim</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>
    <span class="n">embedding_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_EMBEDDING_KEY</span>
    <span class="n">doc_id_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_DOC_ID_KEY</span>
    <span class="n">similarity_metric</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"IP"</span>
    <span class="n">consistency_level</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Strong"</span>
    <span class="n">overwrite</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">output_fields</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">index_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span>
    <span class="n">search_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span>
    <span class="n">enable_sparse</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">sparse_embedding_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"sparse_embedding"</span>
    <span class="n">sparse_embedding_function</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">hybrid_ranker</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">hybrid_ranker_params</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="n">_milvusclient</span><span class="p">:</span> <span class="n">MilvusClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./milvus_llamaindex.db"</span><span class="p">,</span>
        <span class="n">token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llamacollection"</span><span class="p">,</span>
        <span class="n">dim</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embedding_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_EMBEDDING_KEY</span><span class="p">,</span>
        <span class="n">doc_id_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_DOC_ID_KEY</span><span class="p">,</span>
        <span class="n">similarity_metric</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"IP"</span><span class="p">,</span>
        <span class="n">consistency_level</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Strong"</span><span class="p">,</span>
        <span class="n">overwrite</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">search_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">enable_sparse</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">sparse_embedding_function</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSparseEmbeddingFunction</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">hybrid_ranker</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"RRFRanker"</span><span class="p">,</span>
        <span class="n">hybrid_ranker_params</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">dim</span><span class="o">=</span><span class="n">dim</span><span class="p">,</span>
            <span class="n">embedding_field</span><span class="o">=</span><span class="n">embedding_field</span><span class="p">,</span>
            <span class="n">doc_id_field</span><span class="o">=</span><span class="n">doc_id_field</span><span class="p">,</span>
            <span class="n">consistency_level</span><span class="o">=</span><span class="n">consistency_level</span><span class="p">,</span>
            <span class="n">overwrite</span><span class="o">=</span><span class="n">overwrite</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="n">output_fields</span><span class="o">=</span><span class="n">output_fields</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">index_config</span><span class="o">=</span><span class="n">index_config</span> <span class="k">if</span> <span class="n">index_config</span> <span class="k">else</span> <span class="p">{},</span>
            <span class="n">search_config</span><span class="o">=</span><span class="n">search_config</span> <span class="k">if</span> <span class="n">search_config</span> <span class="k">else</span> <span class="p">{},</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">enable_sparse</span><span class="o">=</span><span class="n">enable_sparse</span><span class="p">,</span>
            <span class="n">sparse_embedding_function</span><span class="o">=</span><span class="n">sparse_embedding_function</span><span class="p">,</span>
            <span class="n">hybrid_ranker</span><span class="o">=</span><span class="n">hybrid_ranker</span><span class="p">,</span>
            <span class="n">hybrid_ranker_params</span><span class="o">=</span><span class="n">hybrid_ranker_params</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Select the similarity metric</span>
        <span class="n">similarity_metrics_map</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"ip"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span>
            <span class="s2">"l2"</span><span class="p">:</span> <span class="s2">"L2"</span><span class="p">,</span>
            <span class="s2">"euclidean"</span><span class="p">:</span> <span class="s2">"L2"</span><span class="p">,</span>
            <span class="s2">"cosine"</span><span class="p">:</span> <span class="s2">"COSINE"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_metric</span> <span class="o">=</span> <span class="n">similarity_metrics_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">similarity_metric</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span> <span class="s2">"L2"</span>
        <span class="p">)</span>
        <span class="c1"># Connect to Milvus instance</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span> <span class="o">=</span> <span class="n">MilvusClient</span><span class="p">(</span>
            <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span>
            <span class="n">token</span><span class="o">=</span><span class="n">token</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>  <span class="c1"># pass additional arguments such as server_pem_path</span>
        <span class="p">)</span>
        <span class="c1"># Delete previous collection if overwriting</span>
        <span class="k">if</span> <span class="n">overwrite</span> <span class="ow">and</span> <span class="n">collection_name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">list_collections</span><span class="p">():</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">drop_collection</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>

        <span class="c1"># Create the collection if it does not exist</span>
        <span class="k">if</span> <span class="n">collection_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">list_collections</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">dim</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Dim argument required for collection creation."</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">create_collection</span><span class="p">(</span>
                    <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
                    <span class="n">dimension</span><span class="o">=</span><span class="n">dim</span><span class="p">,</span>
                    <span class="n">primary_field_name</span><span class="o">=</span><span class="n">MILVUS_ID_FIELD</span><span class="p">,</span>
                    <span class="n">vector_field_name</span><span class="o">=</span><span class="n">embedding_field</span><span class="p">,</span>
                    <span class="n">id_type</span><span class="o">=</span><span class="s2">"string"</span><span class="p">,</span>
                    <span class="n">metric_type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">similarity_metric</span><span class="p">,</span>
                    <span class="n">max_length</span><span class="o">=</span><span class="mi">65_535</span><span class="p">,</span>
                    <span class="n">consistency_level</span><span class="o">=</span><span class="n">consistency_level</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">_</span> <span class="o">=</span> <span class="n">DataType</span><span class="o">.</span><span class="n">SPARSE_FLOAT_VECTOR</span>
                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                        <span class="s2">"Hybrid retrieval is only supported in Milvus 2.4.0 or later."</span>
                    <span class="p">)</span>
                    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                        <span class="s2">"Hybrid retrieval requires Milvus 2.4.0 or later."</span>
                    <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_hybrid_index</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="n">Collection</span><span class="p">(</span><span class="n">collection_name</span><span class="p">,</span> <span class="n">using</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">_using</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_required</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="o">=</span> <span class="n">enable_sparse</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">True</span> <span class="ow">and</span> <span class="n">sparse_embedding_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Sparse embedding function is not provided, using default."</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_function</span> <span class="o">=</span> <span class="n">get_default_sparse_embedding_function</span><span class="p">()</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">True</span> <span class="ow">and</span> <span class="n">sparse_embedding_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_function</span> <span class="o">=</span> <span class="n">sparse_embedding_function</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">pass</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Successfully created a new collection: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add the embeddings and their nodes into Milvus.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[BaseNode]): List of nodes with embeddings</span>
<span class="sd">                to insert.</span>

<span class="sd">        Raises:</span>
<span class="sd">            MilvusException: Failed to insert data.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[str]: List of ids inserted.</span>
<span class="sd">        """</span>
        <span class="n">insert_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">insert_ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">True</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span>
                <span class="s2">"sparse_embedding_function is None when enable_sparse is True."</span>
            <span class="p">)</span>

        <span class="c1"># Process that data we are going to insert</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">entry</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">entry</span><span class="p">[</span><span class="n">MILVUS_ID_FIELD</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
            <span class="n">entry</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_field</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">entry</span><span class="p">[</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_field</span>
                <span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_function</span><span class="o">.</span><span class="n">encode_documents</span><span class="p">([</span><span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span>

            <span class="n">insert_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">insert_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>

        <span class="c1"># Insert the data into milvus</span>
        <span class="k">for</span> <span class="n">insert_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">insert_list</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">insert_batch</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">add_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"force_flush"</span><span class="p">,</span> <span class="kc">False</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_required</span><span class="p">()</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Successfully inserted embeddings into: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="si">}</span><span class="s2"> "</span>
            <span class="sa">f</span><span class="s2">"Num Inserted: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">insert_list</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">insert_ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        Raises:</span>
<span class="sd">            MilvusException: Failed to delete the doc.</span>
<span class="sd">        """</span>
        <span class="c1"># Adds ability for multiple doc delete in future.</span>
        <span class="n">doc_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="n">doc_ids</span> <span class="o">=</span> <span class="n">ref_doc_id</span>  <span class="c1"># type: ignore</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span>

        <span class="c1"># Begin by querying for the primary keys to delete</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'"'</span> <span class="o">+</span> <span class="n">entry</span> <span class="o">+</span> <span class="s1">'"'</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">doc_ids</span><span class="p">]</span>
        <span class="n">entries</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">doc_id_field</span><span class="si">}</span><span class="s2"> in [</span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">doc_ids</span><span class="p">)</span><span class="si">}</span><span class="s2">]"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">entries</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">entry</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">entries</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span> <span class="n">pks</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Successfully deleted embedding with doc_id: </span><span class="si">{</span><span class="n">doc_ids</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_embedding (List[float]): query embedding</span>
<span class="sd">            similarity_top_k (int): top k most similar nodes</span>
<span class="sd">            doc_ids (Optional[List[str]]): list of doc_ids to filter by</span>
<span class="sd">            node_ids (Optional[List[str]]): list of node_ids to filter by</span>
<span class="sd">            output_fields (Optional[List[str]]): list of fields to return</span>
<span class="sd">            embedding_field (Optional[str]): name of embedding field</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_sparse</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"QueryMode is HYBRID, but enable_sparse is False."</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Milvus does not support </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2"> yet."</span><span class="p">)</span>

        <span class="n">expr</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">output_fields</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"*"</span><span class="p">]</span>

        <span class="c1"># Parse the filter</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="s2">"milvus_scalar_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="n">expr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">_to_milvus_filter</span><span class="p">(</span>
                    <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
                    <span class="n">kwargs</span><span class="p">[</span><span class="s2">"milvus_scalar_filters"</span><span class="p">]</span>
                    <span class="k">if</span> <span class="s2">"milvus_scalar_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span>
                    <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="c1"># Parse any docs we are filtering on</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">expr_list</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'"'</span> <span class="o">+</span> <span class="n">entry</span> <span class="o">+</span> <span class="s1">'"'</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">]</span>
            <span class="n">expr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">doc_id_field</span><span class="si">}</span><span class="s2"> in [</span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">expr_list</span><span class="p">)</span><span class="si">}</span><span class="s2">]"</span><span class="p">)</span>

        <span class="c1"># Parse any nodes we are filtering on</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">node_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">expr_list</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'"'</span> <span class="o">+</span> <span class="n">entry</span> <span class="o">+</span> <span class="s1">'"'</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">]</span>
            <span class="n">expr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">MILVUS_ID_FIELD</span><span class="si">}</span><span class="s2"> in [</span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">expr_list</span><span class="p">)</span><span class="si">}</span><span class="s2">]"</span><span class="p">)</span>

        <span class="c1"># Limit output fields</span>
        <span class="n">outputs_limited</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">output_fields</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">output_fields</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">output_fields</span>
            <span class="n">outputs_limited</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">output_fields</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">output_fields</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">output_fields</span><span class="p">]</span>
            <span class="n">outputs_limited</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="c1"># Add the text key to output fields if necessary</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">output_fields</span> <span class="ow">and</span> <span class="n">outputs_limited</span><span class="p">:</span>
            <span class="n">output_fields</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">)</span>

        <span class="c1"># Convert to string expression</span>
        <span class="n">string_expr</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">string_expr</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">" and "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>

        <span class="c1"># Perform the search</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="s2">"WeightedRanker"</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span> <span class="o"></span> <span class="s2">"RRFRanker"</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="c1"># Perform default search</span>
        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_milvusclient</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">],</span>
            <span class="nb">filter</span><span class="o">=</span><span class="n">string_expr</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">output_fields</span><span class="o">=</span><span class="n">output_fields</span><span class="p">,</span>
            <span class="n">search_params</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">search_config</span><span class="p">,</span>
            <span class="n">anns_field</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_field</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Successfully searched embedding in collection: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="sa">f</span><span class="s2">" Num Results: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Parse the results</span>
        <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span>
                    <span class="p">{</span>
                        <span class="s2">"_node_content"</span><span class="p">:</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"entity"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"_node_content"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                        <span class="s2">"_node_type"</span><span class="p">:</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"entity"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"_node_type"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="p">}</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"entity"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"The passed in text_key value does not exist "</span>
                        <span class="s2">"in the retrieved entity."</span>
                    <span class="p">)</span>

                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="n">key</span><span class="p">:</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"entity"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">)</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_fields</span>
                <span class="p">}</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>

            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hit</span><span class="p">[</span><span class="s2">"distance"</span><span class="p">])</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hit</span><span class="p">[</span><span class="s2">"id"</span><span class="p">])</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># Perform hybrid search</span>
        <span class="n">sparse_emb</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_function</span><span class="o">.</span><span class="n">encode_queries</span><span class="p">(</span>
            <span class="p">[</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">]</span>
        <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">sparse_search_params</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">}</span>

        <span class="n">sparse_req</span> <span class="o">=</span> <span class="n">AnnSearchRequest</span><span class="p">(</span>
            <span class="p">[</span><span class="n">sparse_emb</span><span class="p">],</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sparse_embedding_field</span><span class="p">,</span>
            <span class="n">sparse_search_params</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">dense_search_params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"metric_type"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_metric</span><span class="p">,</span>
            <span class="s2">"params"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_config</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">dense_emb</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
        <span class="n">dense_req</span> <span class="o">=</span> <span class="n">AnnSearchRequest</span><span class="p">(</span>
            <span class="p">[</span><span class="n">dense_emb</span><span class="p">],</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">embedding_field</span><span class="p">,</span>
            <span class="n">dense_search_params</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">ranker</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="n">WeightedRanker</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">RRFRanker</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="s2">"Hybrid retrieval is only supported in Milvus 2.4.0 or later."</span>
            <span class="p">)</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Hybrid retrieval is only supported in Milvus 2.4.0 or later."</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker</span> <span class="o"></span> <span class="p">{}:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"weights"</span><span class="p">:</span> <span class="p">[</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">]}</span>
            <span class="n">ranker</span> <span class="o">=</span> <span class="n">WeightedRanker</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span><span class="p">[</span><span class="s2">"weights"</span><span class="p">])</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker</span> <span class="o"></span> <span class="p">{}:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"k"</span><span class="p">:</span> <span class="mi">60</span><span class="p">}</span>
            <span class="n">ranker</span> <span class="o">=</span> <span class="n">RRFRanker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker_params</span><span class="p">[</span><span class="s2">"k"</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unsupported ranker: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">hybrid_ranker</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">hybrid_search</span><span class="p">(</span>
            <span class="p">[</span><span class="n">dense_req</span><span class="p">,</span> <span class="n">sparse_req</span><span class="p">],</span>
            <span class="n">rerank</span><span class="o">=</span><span class="n">ranker</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">output_fields</span><span class="o">=</span><span class="n">output_fields</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Successfully searched embedding in collection: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="sa">f</span><span class="s2">" Num Results: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Parse the results</span>
        <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span>
                    <span class="p">{</span>
                        <span class="s2">"_node_content"</span><span class="p">:</span> <span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"_node_content"</span><span class="p">),</span>
                        <span class="s2">"_node_type"</span><span class="p">:</span> <span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"_node_type"</span><span class="p">),</span>
                    <span class="p">}</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"The passed in text_key value does not exist "</span>
                        <span class="s2">"in the retrieved entity."</span>
                    <span class="p">)</span>

                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="n">key</span><span class="p">:</span> <span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">)</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_fields</span><span class="p">}</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>

            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hit</span><span class="o">.</span><span class="n">distance</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hit</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Metal](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/metal/)[Next Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/)
