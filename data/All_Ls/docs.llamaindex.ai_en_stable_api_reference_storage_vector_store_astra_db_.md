Title: Astra db - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/astra_db/

Markdown Content:
Astra db - LlamaIndex


AstraDBVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/astra_db/#llama_index.vector_stores.astra_db.AstraDBVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Astra DB Vector Store.

An abstraction of a Astra DB collection with vector-similarity-search. Documents, and their embeddings, are stored in an Astra DB collection equipped with a vector index. The collection, if necessary, is created when the vector store is initialized.

All Astra operations are done through the AstraPy library.

Visit https://astra.datastax.com/signup to create an account and get started.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
collection name to use. If not existing, it will be created.



 | _required_ |
| `token` | `str` | 

The Astra DB Application Token to use.



 | _required_ |
| `api_endpoint` | `str` | 

The Astra DB JSON API endpoint for your database.



 | _required_ |
| `embedding_dimension` | `int` | 

length of the embedding vectors in use.



 | _required_ |
| `namespace` | `Optional[str]` | 

The namespace to use. If not provided, 'default\_keyspace'



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-astra`

```
from llama_index.vector_stores.astra import AstraDBVectorStore

# Create the Astra DB Vector Store object
astra_db_store = AstraDBVectorStore(
    collection_name="astra_v_store",
    token=token,
    api_endpoint=api_endpoint,
    embedding_dimension=1536,
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-astra-db/llama_index/vector_stores/astra_db/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
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
<span class="normal">449</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AstraDBVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Astra DB Vector Store.</span>

<span class="sd">    An abstraction of a Astra DB collection with</span>
<span class="sd">    vector-similarity-search. Documents, and their embeddings, are stored</span>
<span class="sd">    in an Astra DB collection equipped with a vector index.</span>
<span class="sd">    The collection, if necessary, is created when the vector store is initialized.</span>

<span class="sd">    All Astra operations are done through the AstraPy library.</span>

<span class="sd">    Visit https://astra.datastax.com/signup to create an account and get started.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): collection name to use. If not existing, it will be created.</span>
<span class="sd">        token (str): The Astra DB Application Token to use.</span>
<span class="sd">        api_endpoint (str): The Astra DB JSON API endpoint for your database.</span>
<span class="sd">        embedding_dimension (int): length of the embedding vectors in use.</span>
<span class="sd">        namespace (Optional[str]): The namespace to use. If not provided, 'default_keyspace'</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-astra`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.astra import AstraDBVectorStore</span>

<span class="sd">        # Create the Astra DB Vector Store object</span>
<span class="sd">        astra_db_store = AstraDBVectorStore(</span>
<span class="sd">            collection_name="astra_v_store",</span>
<span class="sd">            token=token,</span>
<span class="sd">            api_endpoint=api_endpoint,</span>
<span class="sd">            embedding_dimension=1536,</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_embedding_dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_database</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">api_endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ttl_seconds</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="c1"># Set all the required class parameters</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_dimension</span> <span class="o">=</span> <span class="n">embedding_dimension</span>

        <span class="k">if</span> <span class="n">ttl_seconds</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">warn</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="s2">"Parameter `ttl_seconds` is not supported for "</span>
                    <span class="s2">"`AstraDBVectorStore` and will be ignored."</span>
                <span class="p">),</span>
                <span class="ne">UserWarning</span><span class="p">,</span>
                <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Creating the Astra DB client and database instances"</span><span class="p">)</span>

        <span class="c1"># Build the Database object</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">DataAPIClient</span><span class="p">(</span>
            <span class="n">caller_name</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">llama_index</span><span class="p">,</span> <span class="s2">"__name__"</span><span class="p">,</span> <span class="s2">"llama_index"</span><span class="p">),</span>
            <span class="n">caller_version</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">llama_index</span><span class="o">.</span><span class="n">core</span><span class="p">,</span> <span class="s2">"__version__"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
        <span class="p">)</span><span class="o">.</span><span class="n">get_database</span><span class="p">(</span>
            <span class="n">api_endpoint</span><span class="p">,</span>
            <span class="n">token</span><span class="o">=</span><span class="n">token</span><span class="p">,</span>
            <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="kn">from</span> <span class="nn">astrapy.exceptions</span> <span class="kn">import</span> <span class="n">DataAPIException</span>

        <span class="n">collection_indexing</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"deny"</span><span class="p">:</span> <span class="n">NON_INDEXED_FIELDS</span><span class="p">}</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Creating the Astra DB collection"</span><span class="p">)</span>
            <span class="c1"># Create and connect to the newly created collection</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="o">.</span><span class="n">create_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
                <span class="n">dimension</span><span class="o">=</span><span class="n">embedding_dimension</span><span class="p">,</span>
                <span class="n">indexing</span><span class="o">=</span><span class="n">collection_indexing</span><span class="p">,</span>
                <span class="n">check_exists</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">DataAPIException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># possibly the collection is preexisting and has legacy</span>
            <span class="c1"># indexing settings: verify</span>
            <span class="n">preexisting</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">coll_descriptor</span>
                <span class="k">for</span> <span class="n">coll_descriptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="o">.</span><span class="n">list_collections</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">coll_descriptor</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="n">collection_indexing</span><span class="p">:</span>
                        <span class="k">raise</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">options_json</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">pre_col_idx_opts</span><span class="p">)</span>
                        <span class="n">warn</span><span class="p">(</span>
                            <span class="p">(</span>
                                <span class="sa">f</span><span class="s2">"Collection '</span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">' has unexpected 'indexing'"</span>
                                <span class="sa">f</span><span class="s2">" settings (options.indexing = </span><span class="si">{</span><span class="n">options_json</span><span class="si">}</span><span class="s2">)."</span>
                                <span class="s2">" This can result in odd behaviour when running "</span>
                                <span class="s2">" metadata filtering and/or unwarranted limitations"</span>
                                <span class="s2">" on storing long texts. Consider indexing anew on a"</span>
                                <span class="s2">" fresh collection."</span>
                            <span class="p">),</span>
                            <span class="ne">UserWarning</span><span class="p">,</span>
                            <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
                        <span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span>
                            <span class="n">collection_name</span><span class="p">,</span>
                        <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># other exception</span>
                <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of node with embeddings</span>

<span class="sd">        """</span>
        <span class="c1"># Initialize list of documents to insert</span>
        <span class="n">documents_to_insert</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># Process each node individually</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="c1"># Get the metadata</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># One dictionary of node data per node</span>
            <span class="n">documents_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"_id"</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="s2">"content"</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                    <span class="s2">"metadata"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
                    <span class="s2">"$vector"</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
                <span class="p">}</span>
            <span class="p">)</span>

        <span class="c1"># Log the number of documents being added</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Adding </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents_to_insert</span><span class="p">)</span><span class="si">}</span><span class="s2"> documents to the collection"</span><span class="p">)</span>

        <span class="c1"># perform an AstraPy insert_many, catching exceptions for overwriting docs</span>
        <span class="n">ids_to_replace</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
                <span class="n">documents_to_insert</span><span class="p">,</span>
                <span class="n">ordered</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">ids_to_replace</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">except</span> <span class="n">InsertManyException</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="n">inserted_ids_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">err</span><span class="o">.</span><span class="n">partial_result</span><span class="o">.</span><span class="n">inserted_ids</span><span class="p">)</span>
            <span class="n">ids_to_replace</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">document</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents_to_insert</span>
                <span class="k">if</span> <span class="n">document</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">inserted_ids_set</span>
            <span class="p">]</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Detected </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">ids_to_replace</span><span class="p">)</span><span class="si">}</span><span class="s2"> non-inserted documents, trying replace_one"</span>
            <span class="p">)</span>

        <span class="c1"># if necessary, replace docs for the non-inserted ids</span>
        <span class="k">if</span> <span class="n">ids_to_replace</span><span class="p">:</span>
            <span class="n">documents_to_replace</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">document</span>
                <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents_to_insert</span>
                <span class="k">if</span> <span class="n">document</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">ids_to_replace</span>
            <span class="p">]</span>

            <span class="k">with</span> <span class="n">ThreadPoolExecutor</span><span class="p">(</span>
                <span class="n">max_workers</span><span class="o">=</span><span class="n">REPLACE_DOCUMENTS_MAX_THREADS</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">executor</span><span class="p">:</span>

                <span class="k">def</span> <span class="nf">_replace_document</span><span class="p">(</span><span class="n">document</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">UpdateResult</span><span class="p">:</span>
                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">replace_one</span><span class="p">(</span>
                        <span class="p">{</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">document</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]},</span>
                        <span class="n">document</span><span class="p">,</span>
                    <span class="p">)</span>

                <span class="n">replace_results</span> <span class="o">=</span> <span class="n">executor</span><span class="o">.</span><span class="n">map</span><span class="p">(</span>
                    <span class="n">_replace_document</span><span class="p">,</span>
                    <span class="n">documents_to_replace</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">replaced_count</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">r_res</span><span class="o">.</span><span class="n">update_info</span><span class="p">[</span><span class="s2">"n"</span><span class="p">]</span> <span class="k">for</span> <span class="n">r_res</span> <span class="ow">in</span> <span class="n">replace_results</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">replaced_count</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">ids_to_replace</span><span class="p">):</span>
                <span class="n">missing</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">ids_to_replace</span><span class="p">)</span> <span class="o">-</span> <span class="n">replaced_count</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"AstraDBVectorStore.add could not insert all requested "</span>
                    <span class="sa">f</span><span class="s2">"documents (</span><span class="si">{</span><span class="n">missing</span><span class="si">}</span><span class="s2"> failed replace_one calls)"</span>
                <span class="p">)</span>

        <span class="c1"># Return the list of ids</span>
        <span class="k">return</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">n</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">])</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">documents_to_insert</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Deleting a document from the Astra DB collection"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">delete_kwargs</span><span class="p">:</span>
            <span class="n">args_desc</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"'</span><span class="si">{</span><span class="n">kwarg</span><span class="si">}</span><span class="s2">'"</span> <span class="k">for</span> <span class="n">kwarg</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">delete_kwargs</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
            <span class="p">)</span>
            <span class="n">warn</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="s2">"AstraDBVectorStore.delete call got unsupported "</span>
                    <span class="sa">f</span><span class="s2">"named argument(s): </span><span class="si">{</span><span class="n">args_desc</span><span class="si">}</span><span class="s2">."</span>
                <span class="p">),</span>
                <span class="ne">UserWarning</span><span class="p">,</span>
                <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the underlying Astra DB `astrapy.Collection` object."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_query_filters_to_dict</span><span class="p">(</span><span class="n">query_filters</span><span class="p">:</span> <span class="n">MetadataFilters</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="c1"># Allow only legacy ExactMatchFilter and MetadataFilter with FilterOperator.EQ</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="p">(</span>
                <span class="nb">isinstance</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">ExactMatchFilter</span><span class="p">)</span>
                <span class="ow">or</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">MetadataFilter</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="o">.</span><span class="n">operator</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="c1"># Call the vector_find method of AstraPy</span>
            <span class="n">matches</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
                    <span class="nb">filter</span><span class="o">=</span><span class="n">query_metadata</span><span class="p">,</span>
                    <span class="n">projection</span><span class="o">=</span><span class="p">{</span><span class="s2">"*"</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
                    <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                    <span class="n">sort</span><span class="o">=</span><span class="p">{</span><span class="s2">"$vector"</span><span class="p">:</span> <span class="n">query_embedding</span><span class="p">},</span>
                    <span class="n">include_similarity</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

            <span class="c1"># Get the scores associated with each</span>
            <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">match</span><span class="p">[</span><span class="s2">"$similarity"</span><span class="p">]</span> <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">]</span>
        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="c1"># Call the vector_find method of AstraPy</span>
        <span class="n">matches</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
                <span class="nb">filter</span><span class="o">=</span><span class="n">query_metadata</span><span class="p">,</span>
                <span class="n">projection</span><span class="o">=</span><span class="p">{</span><span class="s2">"*"</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">sort</span><span class="o">=</span><span class="p">{</span><span class="s2">"$vector"</span><span class="p">:</span> <span class="n">query_embedding</span><span class="p">},</span>
                <span class="n">include_similarity</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># Get the scores associated with each</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">match</span><span class="p">[</span><span class="s2">"$similarity"</span><span class="p">]</span> <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">]</span>
    <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">MMR</span><span class="p">:</span>
        <span class="c1"># Querying a larger number of vectors and then doing MMR on them.</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mmr_prefetch_factor"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="ow">and</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mmr_prefetch_k"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"'mmr_prefetch_factor' and 'mmr_prefetch_k' "</span>
                <span class="s2">"cannot coexist in a call to query()"</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mmr_prefetch_k"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">prefetch_k0</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s2">"mmr_prefetch_k"</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">prefetch_k0</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span>
                    <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
                    <span class="o">*</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mmr_prefetch_factor"</span><span class="p">,</span> <span class="n">DEFAULT_MMR_PREFETCH_FACTOR</span><span class="p">)</span>
                <span class="p">)</span>
        <span class="c1"># Get the most we can possibly need to fetch</span>
        <span class="n">prefetch_k</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">prefetch_k0</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">)</span>

        <span class="c1"># Call AstraPy to fetch them (similarity from DB not needed here)</span>
        <span class="n">prefetch_matches</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
                <span class="nb">filter</span><span class="o">=</span><span class="n">query_metadata</span><span class="p">,</span>
                <span class="n">projection</span><span class="o">=</span><span class="p">{</span><span class="s2">"*"</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">prefetch_k</span><span class="p">,</span>
                <span class="n">sort</span><span class="o">=</span><span class="p">{</span><span class="s2">"$vector"</span><span class="p">:</span> <span class="n">query_embedding</span><span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># Get the MMR threshold</span>
        <span class="n">mmr_threshold</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">mmr_threshold</span> <span class="ow">or</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mmr_threshold"</span><span class="p">)</span>

        <span class="c1"># If we have found documents, we can proceed</span>
        <span class="k">if</span> <span class="n">prefetch_matches</span><span class="p">:</span>
            <span class="n">zipped_indices</span><span class="p">,</span> <span class="n">zipped_embeddings</span> <span class="o">=</span> <span class="nb">zip</span><span class="p">(</span>
                <span class="o">*</span><span class="nb">enumerate</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="s2">"$vector"</span><span class="p">]</span> <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">prefetch_matches</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">pf_match_indices</span><span class="p">,</span> <span class="n">pf_match_embeddings</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">zipped_indices</span><span class="p">),</span> <span class="nb">list</span><span class="p">(</span>
                <span class="n">zipped_embeddings</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">pf_match_indices</span><span class="p">,</span> <span class="n">pf_match_embeddings</span> <span class="o">=</span> <span class="p">[],</span> <span class="p">[]</span>

        <span class="c1"># Call the Llama utility function to get the top  k</span>
        <span class="n">mmr_similarities</span><span class="p">,</span> <span class="n">mmr_indices</span> <span class="o">=</span> <span class="n">get_top_k_mmr_embeddings</span><span class="p">(</span>
            <span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">pf_match_embeddings</span><span class="p">,</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">embedding_ids</span><span class="o">=</span><span class="n">pf_match_indices</span><span class="p">,</span>
            <span class="n">mmr_threshold</span><span class="o">=</span><span class="n">mmr_threshold</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Finally, build the final results based on the mmr values</span>
        <span class="n">matches</span> <span class="o">=</span> <span class="p">[</span><span class="n">prefetch_matches</span><span class="p">[</span><span class="n">mmr_index</span><span class="p">]</span> <span class="k">for</span> <span class="n">mmr_index</span> <span class="ow">in</span> <span class="n">mmr_indices</span><span class="p">]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="n">mmr_similarities</span>

    <span class="c1"># We have three lists to return</span>
    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># Get every match</span>
    <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">:</span>
        <span class="c1"># Check whether we have a llama-generated node content field</span>
        <span class="k">if</span> <span class="s2">"_node_content"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">match</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]:</span>
            <span class="k">match</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">][</span><span class="s2">"_node_content"</span><span class="p">]</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">match</span><span class="p">)</span>

        <span class="c1"># Create a new node object from the node metadata</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">],</span> <span class="n">text</span><span class="o">=</span><span class="n">match</span><span class="p">[</span><span class="s2">"content"</span><span class="p">])</span>

        <span class="c1"># Append to the respective lists</span>
        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">])</span>

    <span class="c1"># return our final result</span>
    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span>
        <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span>
        <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Analyticdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/analyticdb/)[Next Awadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awadb/)
