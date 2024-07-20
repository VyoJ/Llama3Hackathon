Title: Azureaisearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/

Markdown Content:
Azureaisearch - LlamaIndex


CognitiveSearchVectorStore `module-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.CognitiveSearchVectorStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
CognitiveSearchVectorStore = [AzureAISearchVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore "llama_index.vector_stores.azureaisearch.base.AzureAISearchVectorStore")
```

AzureAISearchVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Azure AI Search vector store.

**Examples:**

`pip install llama-index-vector-stores-azureaisearch`

```
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from llama_index.vector_stores.azureaisearch import AzureAISearchVectorStore
from llama_index.vector_stores.azureaisearch import IndexManagement, MetadataIndexFieldType

# Azure AI Search setup
search_service_api_key = "YOUR-AZURE-SEARCH-SERVICE-ADMIN-KEY"
search_service_endpoint = "YOUR-AZURE-SEARCH-SERVICE-ENDPOINT"
search_service_api_version = "2023-11-01"
credential = AzureKeyCredential(search_service_api_key)

# Index name to use
index_name = "llamaindex-vector-demo"

# Use index client to demonstrate creating an index
index_client = SearchIndexClient(
    endpoint=search_service_endpoint,
    credential=credential,
)

metadata_fields = {
    "author": "author",
    "theme": ("topic", MetadataIndexFieldType.STRING),
    "director": "director",
}

# Creating an Azure AI Search Vector Store
vector_store = AzureAISearchVectorStore(
    search_or_index_client=index_client,
    filterable_metadata_field_keys=metadata_fields,
    index_name=index_name,
    index_management=IndexManagement.CREATE_IF_NOT_EXISTS,
    id_field_key="id",
    chunk_field_key="chunk",
    embedding_field_key="embedding",
    embedding_dimensionality=1536,
    metadata_string_field_key="metadata",
    doc_id_field_key="doc_id",
    language_analyzer="en.lucene",
    vector_algorithm_type="exhaustiveKnn",
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch/llama_index/vector_stores/azureaisearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
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
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span>
<span class="normal">819</span>
<span class="normal">820</span>
<span class="normal">821</span>
<span class="normal">822</span>
<span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span>
<span class="normal">842</span>
<span class="normal">843</span>
<span class="normal">844</span>
<span class="normal">845</span>
<span class="normal">846</span>
<span class="normal">847</span>
<span class="normal">848</span>
<span class="normal">849</span>
<span class="normal">850</span>
<span class="normal">851</span>
<span class="normal">852</span>
<span class="normal">853</span>
<span class="normal">854</span>
<span class="normal">855</span>
<span class="normal">856</span>
<span class="normal">857</span>
<span class="normal">858</span>
<span class="normal">859</span>
<span class="normal">860</span>
<span class="normal">861</span>
<span class="normal">862</span>
<span class="normal">863</span>
<span class="normal">864</span>
<span class="normal">865</span>
<span class="normal">866</span>
<span class="normal">867</span>
<span class="normal">868</span>
<span class="normal">869</span>
<span class="normal">870</span>
<span class="normal">871</span>
<span class="normal">872</span>
<span class="normal">873</span>
<span class="normal">874</span>
<span class="normal">875</span>
<span class="normal">876</span>
<span class="normal">877</span>
<span class="normal">878</span>
<span class="normal">879</span>
<span class="normal">880</span>
<span class="normal">881</span>
<span class="normal">882</span>
<span class="normal">883</span>
<span class="normal">884</span>
<span class="normal">885</span>
<span class="normal">886</span>
<span class="normal">887</span>
<span class="normal">888</span>
<span class="normal">889</span>
<span class="normal">890</span>
<span class="normal">891</span>
<span class="normal">892</span>
<span class="normal">893</span>
<span class="normal">894</span>
<span class="normal">895</span>
<span class="normal">896</span>
<span class="normal">897</span>
<span class="normal">898</span>
<span class="normal">899</span>
<span class="normal">900</span>
<span class="normal">901</span>
<span class="normal">902</span>
<span class="normal">903</span>
<span class="normal">904</span>
<span class="normal">905</span>
<span class="normal">906</span>
<span class="normal">907</span>
<span class="normal">908</span>
<span class="normal">909</span>
<span class="normal">910</span>
<span class="normal">911</span>
<span class="normal">912</span>
<span class="normal">913</span>
<span class="normal">914</span>
<span class="normal">915</span>
<span class="normal">916</span>
<span class="normal">917</span>
<span class="normal">918</span>
<span class="normal">919</span>
<span class="normal">920</span>
<span class="normal">921</span>
<span class="normal">922</span>
<span class="normal">923</span>
<span class="normal">924</span>
<span class="normal">925</span>
<span class="normal">926</span>
<span class="normal">927</span>
<span class="normal">928</span>
<span class="normal">929</span>
<span class="normal">930</span>
<span class="normal">931</span>
<span class="normal">932</span>
<span class="normal">933</span>
<span class="normal">934</span>
<span class="normal">935</span>
<span class="normal">936</span>
<span class="normal">937</span>
<span class="normal">938</span>
<span class="normal">939</span>
<span class="normal">940</span>
<span class="normal">941</span>
<span class="normal">942</span>
<span class="normal">943</span>
<span class="normal">944</span>
<span class="normal">945</span>
<span class="normal">946</span>
<span class="normal">947</span>
<span class="normal">948</span>
<span class="normal">949</span>
<span class="normal">950</span>
<span class="normal">951</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureAISearchVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Azure AI Search vector store.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-azureaisearch`</span>

<span class="sd">        ```python</span>
<span class="sd">        from azure.core.credentials import AzureKeyCredential</span>
<span class="sd">        from azure.search.documents import SearchClient</span>
<span class="sd">        from azure.search.documents.indexes import SearchIndexClient</span>
<span class="sd">        from llama_index.vector_stores.azureaisearch import AzureAISearchVectorStore</span>
<span class="sd">        from llama_index.vector_stores.azureaisearch import IndexManagement, MetadataIndexFieldType</span>

<span class="sd">        # Azure AI Search setup</span>
<span class="sd">        search_service_api_key = "YOUR-AZURE-SEARCH-SERVICE-ADMIN-KEY"</span>
<span class="sd">        search_service_endpoint = "YOUR-AZURE-SEARCH-SERVICE-ENDPOINT"</span>
<span class="sd">        search_service_api_version = "2023-11-01"</span>
<span class="sd">        credential = AzureKeyCredential(search_service_api_key)</span>

<span class="sd">        # Index name to use</span>
<span class="sd">        index_name = "llamaindex-vector-demo"</span>

<span class="sd">        # Use index client to demonstrate creating an index</span>
<span class="sd">        index_client = SearchIndexClient(</span>
<span class="sd">            endpoint=search_service_endpoint,</span>
<span class="sd">            credential=credential,</span>
<span class="sd">        )</span>

<span class="sd">        metadata_fields = {</span>
<span class="sd">            "author": "author",</span>
<span class="sd">            "theme": ("topic", MetadataIndexFieldType.STRING),</span>
<span class="sd">            "director": "director",</span>
<span class="sd">        }</span>

<span class="sd">        # Creating an Azure AI Search Vector Store</span>
<span class="sd">        vector_store = AzureAISearchVectorStore(</span>
<span class="sd">            search_or_index_client=index_client,</span>
<span class="sd">            filterable_metadata_field_keys=metadata_fields,</span>
<span class="sd">            index_name=index_name,</span>
<span class="sd">            index_management=IndexManagement.CREATE_IF_NOT_EXISTS,</span>
<span class="sd">            id_field_key="id",</span>
<span class="sd">            chunk_field_key="chunk",</span>
<span class="sd">            embedding_field_key="embedding",</span>
<span class="sd">            embedding_dimensionality=1536,</span>
<span class="sd">            metadata_string_field_key="metadata",</span>
<span class="sd">            doc_id_field_key="doc_id",</span>
<span class="sd">            language_analyzer="en.lucene",</span>
<span class="sd">            vector_algorithm_type="exhaustiveKnn",</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_index_client</span><span class="p">:</span> <span class="n">SearchIndexClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_async_index_client</span><span class="p">:</span> <span class="n">AsyncSearchIndexClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_search_client</span><span class="p">:</span> <span class="n">SearchClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_async_search_client</span><span class="p">:</span> <span class="n">AsyncSearchClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_embedding_dimensionality</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_language_analyzer</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_field_mapping</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_management</span><span class="p">:</span> <span class="n">IndexManagement</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_mapping</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span>
        <span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_metadata_to_index_field_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span>
        <span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_vector_profile_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_normalise_metadata_to_index_fields</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">filterable_metadata_field_keys</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
            <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
            <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
            <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="p">]],</span>
            <span class="kc">None</span><span class="p">,</span>
        <span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="p">]]:</span>
        <span class="n">index_field_spec</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">filterable_metadata_field_keys</span><span class="p">,</span> <span class="n">List</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">filterable_metadata_field_keys</span><span class="p">:</span>
                <span class="c1"># Index field name and the metadata field name are the same</span>
                <span class="c1"># Use String as the default index field type</span>
                <span class="n">index_field_spec</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">field</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="o">.</span><span class="n">STRING</span><span class="p">)</span>

        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">filterable_metadata_field_keys</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">filterable_metadata_field_keys</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
                    <span class="c1"># Index field name and metadata field name may differ</span>
                    <span class="c1"># The index field type used is as supplied</span>
                    <span class="n">index_field_spec</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">v</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># Index field name and metadata field name may differ</span>
                    <span class="c1"># Use String as the default index field type</span>
                    <span class="n">index_field_spec</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">MetadataIndexFieldType</span><span class="o">.</span><span class="n">STRING</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">index_field_spec</span>

    <span class="k">def</span> <span class="nf">_create_index_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">index_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_client</span><span class="o">.</span><span class="n">list_index_names</span><span class="p">():</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="n">index_name</span><span class="si">}</span><span class="s2"> does not exist in Azure AI Search, creating index"</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_create_index</span><span class="p">(</span><span class="n">index_name</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_acreate_index_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">list_index_names</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>

        <span class="k">async</span> <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_index_client</span><span class="o">.</span><span class="n">list_index_names</span><span class="p">():</span>
            <span class="n">list_index_names</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">index_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">list_index_names</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="n">index_name</span><span class="si">}</span><span class="s2"> does not exist in Azure AI Search, creating index"</span>
            <span class="p">)</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_acreate_index</span><span class="p">(</span><span class="n">index_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_metadata_index_fields</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create a list of index fields for storing metadata values."""</span>
        <span class="kn">from</span> <span class="nn">azure.search.documents.indexes.models</span> <span class="kn">import</span> <span class="n">SimpleField</span>

        <span class="n">index_fields</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># create search fields</span>
        <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_to_index_field_map</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">field_name</span><span class="p">,</span> <span class="n">field_type</span> <span class="o">=</span> <span class="n">v</span>

            <span class="k">if</span> <span class="n">field_type</span> <span class="o"></span> <span class="n">MetadataIndexFieldType</span><span class="o">.</span><span class="n">INT32</span><span class="p">:</span>
                <span class="n">index_field_type</span> <span class="o">=</span> <span class="s2">"Edm.Int32"</span>
            <span class="k">elif</span> <span class="n">field_type</span> <span class="o"></span> <span class="n">MetadataIndexFieldType</span><span class="o">.</span><span class="n">DOUBLE</span><span class="p">:</span>
                <span class="n">index_field_type</span> <span class="o">=</span> <span class="s2">"Edm.Double"</span>
            <span class="k">elif</span> <span class="n">field_type</span> <span class="o">11.4.0`"</span>
        <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">azure.search.documents</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">azure.search.documents</span> <span class="kn">import</span> <span class="n">SearchClient</span>
            <span class="kn">from</span> <span class="nn">azure.search.documents.indexes</span> <span class="kn">import</span> <span class="n">SearchIndexClient</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_index_client</span><span class="p">:</span> <span class="n">SearchIndexClient</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SearchIndexClient</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_index_client</span><span class="p">:</span> <span class="n">AsyncSearchIndexClient</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">AsyncSearchIndexClient</span><span class="p">,</span> <span class="kc">None</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="p">:</span> <span class="n">SearchClient</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SearchClient</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="p">:</span> <span class="n">AsyncSearchClient</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">AsyncSearchClient</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_dimensionality</span> <span class="o">=</span> <span class="n">embedding_dimensionality</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="o">=</span> <span class="n">index_name</span>

        <span class="k">if</span> <span class="n">vector_algorithm_type</span> <span class="o"></span> <span class="s2">"hnsw"</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_vector_profile_name</span> <span class="o">=</span> <span class="s2">"myHnswProfile"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Only 'exhaustiveKnn' and 'hnsw' are supported for vector_algorithm_type"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_language_analyzer</span> <span class="o">=</span> <span class="n">language_analyzer</span>

        <span class="c1"># Validate search_or_index_client</span>
        <span class="k">if</span> <span class="n">search_or_index_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">SearchIndexClient</span><span class="p">):</span>
                <span class="c1"># If SearchIndexClient is supplied so must index_name</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SearchIndexClient</span><span class="p">,</span> <span class="n">search_or_index_client</span><span class="p">)</span>

                <span class="k">if</span> <span class="ow">not</span> <span class="n">index_name</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"index_name must be supplied if search_or_index_client is of "</span>
                        <span class="s2">"type azure.search.documents.SearchIndexClient"</span>
                    <span class="p">)</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_client</span><span class="o">.</span><span class="n">get_search_client</span><span class="p">(</span>
                    <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span>
                <span class="p">)</span>

            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">AsyncSearchIndexClient</span><span class="p">):</span>
                <span class="c1"># If SearchIndexClient is supplied so must index_name</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_async_index_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                    <span class="n">AsyncSearchIndexClient</span><span class="p">,</span> <span class="n">search_or_index_client</span>
                <span class="p">)</span>

                <span class="k">if</span> <span class="ow">not</span> <span class="n">index_name</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"index_name must be supplied if search_or_index_client is of "</span>
                        <span class="s2">"type azure.search.documents.aio.SearchIndexClient"</span>
                    <span class="p">)</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_index_client</span><span class="o">.</span><span class="n">get_search_client</span><span class="p">(</span>
                    <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span>
                <span class="p">)</span>

            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">SearchClient</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SearchClient</span><span class="p">,</span> <span class="n">search_or_index_client</span><span class="p">)</span>

                <span class="c1"># Validate index_name</span>
                <span class="k">if</span> <span class="n">index_name</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"index_name cannot be supplied if search_or_index_client "</span>
                        <span class="s2">"is of type azure.search.documents.SearchClient"</span>
                    <span class="p">)</span>

            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">AsyncSearchClient</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                    <span class="n">AsyncSearchClient</span><span class="p">,</span> <span class="n">search_or_index_client</span>
                <span class="p">)</span>

                <span class="c1"># Validate index_name</span>
                <span class="k">if</span> <span class="n">index_name</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"index_name cannot be supplied if search_or_index_client "</span>
                        <span class="s2">"is of type azure.search.documents.SearchClient"</span>
                    <span class="p">)</span>

            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">AsyncSearchIndexClient</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_index_client</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"search_or_index_client must be of type "</span>
                        <span class="s2">"azure.search.documents.SearchIndexClient or "</span>
                        <span class="s2">"azure.search.documents.SearchClient"</span>
                    <span class="p">)</span>

            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">search_or_index_client</span><span class="p">,</span> <span class="n">SearchIndexClient</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_client</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"search_or_index_client must be of type "</span>
                        <span class="s2">"azure.search.documents.SearchIndexClient or "</span>
                        <span class="s2">"azure.search.documents.SearchClient"</span>
                    <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"search_or_index_client not specified"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">index_management</span> <span class="o"></span> <span class="n">IndexManagement</span><span class="o">.</span><span class="n">CREATE_IF_NOT_EXISTS</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">index_name</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_not_exists</span><span class="p">(</span><span class="n">index_name</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_management</span> <span class="o"></span> <span class="n">IndexManagement</span><span class="o">.</span><span class="n">CREATE_IF_NOT_EXISTS</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">:</span>
                    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_acreate_index_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_management</span> <span class="o"></span> <span class="s2">"'"</span> <span class="k">else</span> <span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">f</span><span class="o">.</span><span class="n">value</span><span class="p">])</span>
                <span class="n">odata_filter</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index_field</span><span class="si">}</span><span class="s2"> eq '</span><span class="si">{</span><span class="n">escaped_value</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">odata_filter</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index_field</span><span class="si">}</span><span class="s2"> eq </span><span class="si">{</span><span class="n">f</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">odata_expr</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">odata_filter</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Odata filter: </span><span class="si">{</span><span class="n">odata_expr</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">odata_expr</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">odata_filter</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">odata_filter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_odata_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="n">azure_query_result_search</span><span class="p">:</span> <span class="n">AzureQueryResultSearchBase</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">AzureQueryResultSearchDefault</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">,</span> <span class="n">odata_filter</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
            <span class="n">azure_query_result_search</span> <span class="o">=</span> <span class="n">AzureQueryResultSearchHybrid</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">,</span> <span class="n">odata_filter</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">SPARSE</span><span class="p">:</span>
            <span class="n">azure_query_result_search</span> <span class="o">=</span> <span class="n">AzureQueryResultSearchSparse</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">,</span> <span class="n">odata_filter</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">SEMANTIC_HYBRID</span><span class="p">:</span>
            <span class="n">azure_query_result_search</span> <span class="o">=</span> <span class="n">AzureQueryResultSearchSemanticHybrid</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">,</span> <span class="n">odata_filter</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">azure_query_result_search</span><span class="o">.</span><span class="n">asearch</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### aclient `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.aclient "Permanent link")

```
aclient: Any
```

Get async client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index associated with the configured search client.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch/llama_index/vector_stores/azureaisearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">677</span>
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
<span class="normal">735</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to index associated with the configured search client.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">azure.search.documents</span> <span class="kn">import</span> <span class="n">IndexDocumentsBatch</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Search client not initialized"</span><span class="p">)</span>

    <span class="n">accumulator</span> <span class="o">=</span> <span class="n">IndexDocumentsBatch</span><span class="p">()</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">accumulated_size</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">max_size</span> <span class="o">=</span> <span class="mi">16</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">*</span> <span class="mi">1024</span>  <span class="c1"># 16MB in bytes</span>
    <span class="n">max_docs</span> <span class="o">=</span> <span class="mi">1000</span>

    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Processing embedding: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

        <span class="n">index_document</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_document</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">document_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">))</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_document</span><span class="p">)</span>
        <span class="n">accumulated_size</span> <span class="o">+=</span> <span class="n">document_size</span>

        <span class="n">accumulator</span><span class="o">.</span><span class="n">add_upload_actions</span><span class="p">(</span><span class="n">index_document</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">max_docs</span> <span class="ow">or</span> <span class="n">accumulated_size</span> <span class="o">&gt;=</span> <span class="n">max_size</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Uploading batch of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
                <span class="sa">f</span><span class="s2">"current progress </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
                <span class="sa">f</span><span class="s2">"accumulated size </span><span class="si">{</span><span class="n">accumulated_size</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> MB"</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="o">.</span><span class="n">index_documents</span><span class="p">(</span><span class="n">accumulator</span><span class="p">)</span>
            <span class="n">accumulator</span><span class="o">.</span><span class="n">dequeue_actions</span><span class="p">()</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">accumulated_size</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="c1"># Upload remaining batch</span>
    <span class="k">if</span> <span class="n">documents</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Uploading remaining batch of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"current progress </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"accumulated size </span><span class="si">{</span><span class="n">accumulated_size</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> MB"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="o">.</span><span class="n">index_documents</span><span class="p">(</span><span class="n">accumulator</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### async\_add `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.async_add "Permanent link")

```
async_add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index associated with the configured search client.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch/llama_index/vector_stores/azureaisearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to index associated with the configured search client.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">azure.search.documents</span> <span class="kn">import</span> <span class="n">IndexDocumentsBatch</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Async Search client not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_management</span> <span class="o"></span> <span class="n">IndexManagement</span><span class="o">.</span><span class="n">VALIDATE_INDEX</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_avalidate_index</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">)</span>

    <span class="n">accumulator</span> <span class="o">=</span> <span class="n">IndexDocumentsBatch</span><span class="p">()</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">accumulated_size</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">max_size</span> <span class="o">=</span> <span class="mi">16</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">*</span> <span class="mi">1024</span>  <span class="c1"># 16MB in bytes</span>
    <span class="n">max_docs</span> <span class="o">=</span> <span class="mi">1000</span>

    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Processing embedding: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

        <span class="n">index_document</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_document</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">document_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">))</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_document</span><span class="p">)</span>
        <span class="n">accumulated_size</span> <span class="o">+=</span> <span class="n">document_size</span>

        <span class="n">accumulator</span><span class="o">.</span><span class="n">add_upload_actions</span><span class="p">(</span><span class="n">index_document</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">max_docs</span> <span class="ow">or</span> <span class="n">accumulated_size</span> <span class="o">&gt;=</span> <span class="n">max_size</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Uploading batch of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
                <span class="sa">f</span><span class="s2">"current progress </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
                <span class="sa">f</span><span class="s2">"accumulated size </span><span class="si">{</span><span class="n">accumulated_size</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> MB"</span>
            <span class="p">)</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="o">.</span><span class="n">index_documents</span><span class="p">(</span><span class="n">accumulator</span><span class="p">)</span>
            <span class="n">accumulator</span><span class="o">.</span><span class="n">dequeue_actions</span><span class="p">()</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">accumulated_size</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="c1"># Upload remaining batch</span>
    <span class="k">if</span> <span class="n">documents</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Uploading remaining batch of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"current progress </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"accumulated size </span><span class="si">{</span><span class="n">accumulated_size</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> MB"</span>
        <span class="p">)</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="o">.</span><span class="n">index_documents</span><span class="p">(</span><span class="n">accumulator</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete documents from the AI Search Index with doc\_id\_field\_key field equal to ref\_doc\_id.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch/llama_index/vector_stores/azureaisearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span>
<span class="normal">842</span>
<span class="normal">843</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete documents from the AI Search Index</span>
<span class="sd">    with doc_id_field_key field equal to ref_doc_id.</span>
<span class="sd">    """</span>
    <span class="c1"># Locate documents to delete</span>
    <span class="nb">filter</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span><span class="si">}</span><span class="s1"> eq </span><span class="se">\'</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="se">\'</span><span class="s1">'</span>
    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">search_text</span><span class="o">=</span><span class="s2">"*"</span><span class="p">,</span> <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">)</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Searching with filter </span><span class="si">{</span><span class="nb">filter</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">docs_to_delete</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">doc</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]]</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Found document to delete: </span><span class="si">{</span><span class="n">doc</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">docs_to_delete</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Deleting </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span><span class="si">}</span><span class="s2"> documents"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="o">.</span><span class="n">delete_documents</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/#llama_index.vector_stores.azureaisearch.AzureAISearchVectorStore.adelete "Permanent link")

```
adelete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete documents from the AI Search Index with doc\_id\_field\_key field equal to ref\_doc\_id.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch/llama_index/vector_stores/azureaisearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">845</span>
<span class="normal">846</span>
<span class="normal">847</span>
<span class="normal">848</span>
<span class="normal">849</span>
<span class="normal">850</span>
<span class="normal">851</span>
<span class="normal">852</span>
<span class="normal">853</span>
<span class="normal">854</span>
<span class="normal">855</span>
<span class="normal">856</span>
<span class="normal">857</span>
<span class="normal">858</span>
<span class="normal">859</span>
<span class="normal">860</span>
<span class="normal">861</span>
<span class="normal">862</span>
<span class="normal">863</span>
<span class="normal">864</span>
<span class="normal">865</span>
<span class="normal">866</span>
<span class="normal">867</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete documents from the AI Search Index</span>
<span class="sd">    with doc_id_field_key field equal to ref_doc_id.</span>
<span class="sd">    """</span>
    <span class="c1"># Locate documents to delete</span>
    <span class="nb">filter</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span><span class="si">}</span><span class="s1"> eq </span><span class="se">\'</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="se">\'</span><span class="s1">'</span>

    <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_search_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">search_text</span><span class="o">=</span><span class="s2">"*"</span><span class="p">,</span> <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">)</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Searching with filter </span><span class="si">{</span><span class="nb">filter</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">docs_to_delete</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">doc</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_field_mapping</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]]</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Found document to delete: </span><span class="si">{</span><span class="n">doc</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">docs_to_delete</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Deleting </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span><span class="si">}</span><span class="s2"> documents"</span><span class="p">)</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_client</span><span class="o">.</span><span class="n">delete_documents</span><span class="p">(</span><span class="n">docs_to_delete</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Awsdocdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/)[Next Azurecosmosmongo](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/)
