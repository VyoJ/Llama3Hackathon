Title: Mongodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/

Markdown Content:
Mongodb - LlamaIndex


MongoDBAtlasVectorSearch [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/#llama_index.vector_stores.mongodb.MongoDBAtlasVectorSearch "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

MongoDB Atlas Vector Store.

To use, you should have both: - the `pymongo` python package installed - a connection string associated with a MongoDB Atlas Cluster that has an Atlas Vector Search index

To get started head over to the [Atlas quick start](https://www.mongodb.com/docs/atlas/getting-started/).

Once your store is created, be sure to enable indexing in the Atlas GUI.

Please refer to the [documentation](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/) to get more details on how to define an Atlas Vector Search index. You can name the index {ATLAS\_VECTOR\_SEARCH\_INDEX\_NAME} and create the index on the namespace {DB\_NAME}.{COLLECTION\_NAME}. Finally, write the following definition in the JSON editor on MongoDB Atlas:

```
{
    "name": "vector_index",
    "type": "vectorSearch",
    "fields":[
        {
        "type": "vector",
        "path": "embedding",
        "numDimensions": 1536,
        "similarity": "cosine"
        }
    ]
}
```

**Examples:**

`pip install llama-index-vector-stores-mongodb`

```
import pymongo
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

# Ensure you have the MongoDB URI with appropriate credentials
mongo_uri = "mongodb+srv://<username>:<password>@<host>?retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(mongo_uri)

# Create an instance of MongoDBAtlasVectorSearch
vector_store = MongoDBAtlasVectorSearch(mongodb_client)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-mongodb/llama_index/vector_stores/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 63</span>
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
<span class="normal">417</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MongoDBAtlasVectorSearch</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""MongoDB Atlas Vector Store.</span>

<span class="sd">    To use, you should have both:</span>
<span class="sd">    - the ``pymongo`` python package installed</span>
<span class="sd">    - a connection string associated with a MongoDB Atlas Cluster</span>
<span class="sd">    that has an Atlas Vector Search index</span>

<span class="sd">    To get started head over to the [Atlas quick start](https://www.mongodb.com/docs/atlas/getting-started/).</span>

<span class="sd">    Once your store is created, be sure to enable indexing in the Atlas GUI.</span>

<span class="sd">    Please refer to the [documentation](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/)</span>
<span class="sd">    to get more details on how to define an Atlas Vector Search index. You can name the index {ATLAS_VECTOR_SEARCH_INDEX_NAME}</span>
<span class="sd">    and create the index on the namespace {DB_NAME}.{COLLECTION_NAME}.</span>
<span class="sd">    Finally, write the following definition in the JSON editor on MongoDB Atlas:</span>

<span class="sd">    ```</span>
<span class="sd">    {</span>
<span class="sd">        "name": "vector_index",</span>
<span class="sd">        "type": "vectorSearch",</span>
<span class="sd">        "fields":[</span>
<span class="sd">            {</span>
<span class="sd">            "type": "vector",</span>
<span class="sd">            "path": "embedding",</span>
<span class="sd">            "numDimensions": 1536,</span>
<span class="sd">            "similarity": "cosine"</span>
<span class="sd">            }</span>
<span class="sd">        ]</span>
<span class="sd">    }</span>
<span class="sd">    ```</span>


<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-mongodb`</span>

<span class="sd">        ```python</span>
<span class="sd">        import pymongo</span>
<span class="sd">        from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch</span>

<span class="sd">        # Ensure you have the MongoDB URI with appropriate credentials</span>
<span class="sd">        mongo_uri = "mongodb+srv://&lt;username&gt;:&lt;password&gt;@&lt;host&gt;?retryWrites=true&amp;w=majority"</span>
<span class="sd">        mongodb_client = pymongo.MongoClient(mongo_uri)</span>

<span class="sd">        # Create an instance of MongoDBAtlasVectorSearch</span>
<span class="sd">        vector_store = MongoDBAtlasVectorSearch(mongodb_client)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_mongodb_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_vector_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_fulltext_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_insert_kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>  <span class="c1"># DEPRECATED</span>
    <span class="n">_oversampling_factor</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">mongodb_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_db"</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_collection"</span><span class="p">,</span>
        <span class="n">vector_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"vector_index"</span><span class="p">,</span>
        <span class="n">id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"_id"</span><span class="p">,</span>
        <span class="n">embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embedding"</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">fulltext_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"fulltext_index"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">oversampling_factor</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            mongodb_client: A MongoDB client.</span>
<span class="sd">            db_name: A MongoDB database name.</span>
<span class="sd">            collection_name: A MongoDB collection name.</span>
<span class="sd">            vector_index_name: A MongoDB Atlas *Vector* Search index name. ($vectorSearch)</span>
<span class="sd">            id_key: The data field to use as the id.</span>
<span class="sd">            embedding_key: A MongoDB field that will contain</span>
<span class="sd">            the embedding for each document.</span>
<span class="sd">            text_key: A MongoDB field that will contain the text for each document.</span>
<span class="sd">            metadata_key: A MongoDB field that will contain</span>
<span class="sd">            the metadata for each document.</span>
<span class="sd">            insert_kwargs: The kwargs used during `insert`.</span>
<span class="sd">            fulltext_index_name: A MongoDB Atlas *full-text* Search index name. ($search)</span>
<span class="sd">            oversampling_factor: This times n_results is 'ef' in the HNSW algorithm.</span>
<span class="sd">                'ef' determines the number of nearest neighbor candidates to consider during the search phase.</span>
<span class="sd">                A higher value leads to more accuracy, but is slower. Default = 10</span>
<span class="sd">            index_name: DEPRECATED: Please use vector_index_name.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">mongodb_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">MongoClient</span><span class="p">,</span> <span class="n">mongodb_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"MONGODB_URI"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify MONGODB_URI via env variable "</span>
                    <span class="s2">"if not directly passing in client."</span>
                <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span>
                <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"MONGODB_URI"</span><span class="p">],</span>
                <span class="n">driver</span><span class="o">=</span><span class="n">DriverInfo</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">"llama-index"</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="n">version</span><span class="p">(</span><span class="s2">"llama-index"</span><span class="p">)),</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">index_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"index_name is deprecated. Please use vector_index_name"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">vector_index_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">vector_index_name</span> <span class="o">=</span> <span class="n">index_name</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                    <span class="s2">"vector_index_name and index_name both specified. Will use vector_index_name"</span>
                <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span> <span class="n">Collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span><span class="p">[</span><span class="n">db_name</span><span class="p">][</span><span class="n">collection_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index_name</span> <span class="o">=</span> <span class="n">vector_index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span> <span class="o">=</span> <span class="n">embedding_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span> <span class="o">=</span> <span class="n">id_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="o">=</span> <span class="n">text_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">=</span> <span class="n">metadata_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_fulltext_index_name</span> <span class="o">=</span> <span class="n">fulltext_index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span> <span class="o">=</span> <span class="n">insert_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_oversampling_factor</span> <span class="o">=</span> <span class="n">oversampling_factor</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        Returns:</span>
<span class="sd">            A List of ids for successfully added nodes.</span>

<span class="sd">        """</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">data_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>

            <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="n">data_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into MongoDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
        <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
            <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="c1"># delete by filtering on the doc_id metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_many</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span> <span class="o">**</span><span class="n">delete_kwargs</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return MongoDB client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">TEXT_SEARCH</span><span class="p">:</span>
            <span class="c1"># Atlas Full-Text Search, potentially with filter</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str in VectorStoreQueryMode.TEXT_SEARCH "</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Running </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2"> mode query pipeline"</span><span class="p">)</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="n">filters_to_mql</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
            <span class="n">pipeline</span> <span class="o">=</span> <span class="n">fulltext_search_stage</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">search_field</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">,</span>
                <span class="n">index_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_fulltext_index_name</span><span class="p">,</span>
                <span class="n">operator</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span>
                <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">pipeline</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">"$set"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"score"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$meta"</span><span class="p">:</span> <span class="s2">"searchScore"</span><span class="p">}}})</span>

        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"> 'default',</span>
<span class="sd">        which does vector search, see:</span>
<span class="sd">            https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-stage/</span>

<span class="sd">        For details on VectorStoreQueryMode.TEXT_SEARCH  "hybrid",</span>
<span class="sd">        which combines the two with Reciprocal Rank Fusion, see the following.</span>
<span class="sd">            https://www.mongodb.com/docs/atlas/atlas-vector-search/tutorials/reciprocal-rank-fusion/</span>

<span class="sd">        In the scoring algorithm used, Reciprocal Rank Fusion,</span>
<span class="sd">            scores := \frac{1}{rank + penalty} with rank in [1,2,..,n]</span>

<span class="sd">        Args:</span>
<span class="sd">            query: a VectorStoreQuery object.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/#llama_index.vector_stores.mongodb.MongoDBAtlasVectorSearch.client "Permanent link")

```
client: Any
```

Return MongoDB client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/#llama_index.vector_stores.mongodb.MongoDBAtlasVectorSearch.add "Permanent link")

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

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
A List of ids for successfully added nodes.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-mongodb/llama_index/vector_stores/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">197</span>
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
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    Returns:</span>
<span class="sd">        A List of ids for successfully added nodes.</span>

<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">data_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
        <span class="p">)</span>

        <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">data_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into MongoDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
    <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
        <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
    <span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/#llama_index.vector_stores.mongodb.MongoDBAtlasVectorSearch.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-mongodb/llama_index/vector_stores/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">233</span>
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
<span class="normal">244</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="c1"># delete by filtering on the doc_id metadata</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_many</span><span class="p">(</span>
        <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span> <span class="o">**</span><span class="n">delete_kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/#llama_index.vector_stores.mongodb.MongoDBAtlasVectorSearch.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

The type of search to be performed is based on the VectorStoreQuery.mode. Choose from DEFAULT (vector), HYBRID (hybrid), or TEXT\_SEARCH (full-text). When the mode is one of HYBRID or TEXT\_SEARCH, VectorStoreQuery.query\_str is used for the full-text search. See MongoDB Atlas documentation for full details on these.

For details on VectorStoreQueryMode.DEFAULT  "text\_search", which performs full-text search, see: https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search

For details on VectorStoreQueryMode.HYBRID  'default',</span>
<span class="sd">    which does vector search, see:</span>
<span class="sd">        https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-stage/</span>

<span class="sd">    For details on VectorStoreQueryMode.TEXT_SEARCH  "hybrid",</span>
<span class="sd">    which combines the two with Reciprocal Rank Fusion, see the following.</span>
<span class="sd">        https://www.mongodb.com/docs/atlas/atlas-vector-search/tutorials/reciprocal-rank-fusion/</span>

<span class="sd">    In the scoring algorithm used, Reciprocal Rank Fusion,</span>
<span class="sd">        scores := \frac{1}{rank + penalty} with rank in [1,2,..,n]</span>

<span class="sd">    Args:</span>
<span class="sd">        query: a VectorStoreQuery object.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Milvus](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/)[Next Myscale](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/myscale/)
