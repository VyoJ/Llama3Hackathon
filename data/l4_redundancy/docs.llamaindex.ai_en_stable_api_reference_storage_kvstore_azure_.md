Title: Azure - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/

Markdown Content:
Azure - LlamaIndex


AzureKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

Provides a key-value store interface for Azure Table Storage and Cosmos DB. This class supports both synchronous and asynchronous operations on Azure Table Storage and Cosmos DB. It supports connecting to the service using different credentials and manages table creation and data serialization to conform to the storage requirements.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
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
<span class="normal">514</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Provides a key-value store interface for Azure Table Storage and Cosmos</span>
<span class="sd">    DB. This class supports both synchronous and asynchronous operations on</span>
<span class="sd">    Azure Table Storage and Cosmos DB. It supports connecting to the service</span>
<span class="sd">    using different credentials and manages table creation and data</span>
<span class="sd">    serialization to conform to the storage requirements.</span>
<span class="sd">    """</span>

    <span class="n">partition_key</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">table_service_client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">atable_service_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initializes the AzureKVStore with Azure Table Storage clients."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TableServiceClient</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables.aio</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">TableServiceClient</span> <span class="k">as</span> <span class="n">AsyncTableServiceClient</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span> <span class="o">=</span> <span class="n">service_mode</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_PARTITION_KEY</span> <span class="k">if</span> <span class="n">partition_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">partition_key</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">TableServiceClient</span><span class="p">,</span> <span class="n">table_service_client</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncTableServiceClient</span><span class="p">],</span> <span class="n">atable_service_client</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an instance of AzureKVStore using a connection string."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TableServiceClient</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables.aio</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">TableServiceClient</span> <span class="k">as</span> <span class="n">AsyncTableServiceClient</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_service_client</span> <span class="o">=</span> <span class="n">TableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span>
        <span class="p">)</span>
        <span class="n">atable_service_client</span> <span class="o">=</span> <span class="n">AsyncTableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">table_service_client</span><span class="p">,</span>
            <span class="n">atable_service_client</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="p">,</span>
            <span class="n">partition_key</span><span class="p">,</span>
            <span class="o">*</span><span class="n">args</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an instance of AzureKVStore from an account name and key."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.credentials</span> <span class="kn">import</span> <span class="n">AzureNamedKeyCredential</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">endpoint</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://</span><span class="si">{</span><span class="n">account_name</span><span class="si">}</span><span class="s2">.table.core.windows.net"</span>
        <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureNamedKeyCredential</span><span class="p">(</span><span class="n">account_name</span><span class="p">,</span> <span class="n">account_key</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an instance of AzureKVStore using a SAS token."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.credentials</span> <span class="kn">import</span> <span class="n">AzureSasCredential</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureSasCredential</span><span class="p">(</span><span class="n">sas_token</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Creates an instance of AzureKVStore using Azure Active Directory</span>
<span class="sd">        (AAD) tokens.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.identity</span> <span class="kn">import</span> <span class="n">DefaultAzureCredential</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">credential</span> <span class="o">=</span> <span class="n">DefaultAzureCredential</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Inserts or replaces a key-value pair in the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">UpdateMode</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
        <span class="n">table_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
                <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
            <span class="p">},</span>
            <span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Inserts or replaces a key-value pair in the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">UpdateMode</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>
        <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
                <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
            <span class="p">},</span>
            <span class="n">mode</span><span class="o">=</span><span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">put_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Inserts or replaces multiple key-value pairs in the specified table.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TransactionOperation</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>

        <span class="n">entities</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
                <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
            <span class="p">}</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span>
        <span class="p">]</span>

        <span class="n">entities_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">start</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
            <span class="n">table_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span>
                <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">UPSERT</span><span class="p">,</span> <span class="n">entities</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="n">start</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">))</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Inserts or replaces multiple key-value pairs in the specified table.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TransactionOperation</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>

        <span class="n">entities</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
                <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
            <span class="p">}</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span>
        <span class="p">]</span>

        <span class="n">entities_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">start</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
            <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span>
                <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">UPSERT</span><span class="p">,</span> <span class="n">entities</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="n">start</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">))</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">entity</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
                <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">entity</span> <span class="o">=</span> <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
                <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves all key-value pairs from a specified partition in the table.</span>
<span class="sd">        """</span>
        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">list_entities</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="n">select</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">entity</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]:</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
        <span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves all key-value pairs from a specified partition in the table.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>
        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">list_entities</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="n">select</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">entity</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]:</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Deletes a specific key-value pair from the store based on the</span>
<span class="sd">        provided key and partition key.</span>
<span class="sd">        """</span>
        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
        <span class="n">table_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronously deletes a specific key-value pair from the store."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>
        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>
        <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_filter</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">entities</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span>
                <span class="n">query_filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
            <span class="p">)</span>

            <span class="k">return</span> <span class="p">(</span><span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_filter</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncGenerator</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="kc">None</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Asynchronously retrieves a value by key from the specified table."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="n">table_name</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">entities</span> <span class="o">=</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span>
                <span class="n">query_filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
            <span class="p">)</span>

            <span class="k">return</span> <span class="p">(</span><span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">async</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">)</span>

        <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">_from_clients</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">credential</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Private method to create synchronous and asynchronous table service</span>
<span class="sd">        clients.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TableServiceClient</span>
            <span class="kn">from</span> <span class="nn">azure.data.tables.aio</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">TableServiceClient</span> <span class="k">as</span> <span class="n">AsyncTableServiceClient</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">table_client</span> <span class="o">=</span> <span class="n">TableServiceClient</span><span class="p">(</span><span class="n">endpoint</span><span class="o">=</span><span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="o">=</span><span class="n">credential</span><span class="p">)</span>
        <span class="n">atable_client</span> <span class="o">=</span> <span class="n">AsyncTableServiceClient</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="o">=</span><span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="o">=</span><span class="n">credential</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">table_client</span><span class="p">,</span> <span class="n">atable_client</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_connection\_string `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.from_connection_string "Permanent link")

```
from_connection_string(connection_string: str, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, *args: Any, **kwargs: Any) -> [AzureKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "llama_index.storage.kvstore.azure.base.AzureKVStore")
```

Creates an instance of AzureKVStore using a connection string.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 72</span>
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
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Creates an instance of AzureKVStore using a connection string."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TableServiceClient</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables.aio</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">TableServiceClient</span> <span class="k">as</span> <span class="n">AsyncTableServiceClient</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_service_client</span> <span class="o">=</span> <span class="n">TableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
        <span class="n">connection_string</span>
    <span class="p">)</span>
    <span class="n">atable_service_client</span> <span class="o">=</span> <span class="n">AsyncTableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
        <span class="n">connection_string</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">table_service_client</span><span class="p">,</span>
        <span class="n">atable_service_client</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_account\_and\_key `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.from_account_and_key "Permanent link")

```
from_account_and_key(account_name: str, account_key: str, endpoint: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, *args: Any, **kwargs: Any) -> [AzureKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "llama_index.storage.kvstore.azure.base.AzureKVStore")
```

Creates an instance of AzureKVStore from an account name and key.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">105</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Creates an instance of AzureKVStore from an account name and key."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.credentials</span> <span class="kn">import</span> <span class="n">AzureNamedKeyCredential</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">endpoint</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">endpoint</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://</span><span class="si">{</span><span class="n">account_name</span><span class="si">}</span><span class="s2">.table.core.windows.net"</span>
    <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureNamedKeyCredential</span><span class="p">(</span><span class="n">account_name</span><span class="p">,</span> <span class="n">account_key</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_sas\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.from_sas_token "Permanent link")

```
from_sas_token(endpoint: str, sas_token: str, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, *args: Any, **kwargs: Any) -> [AzureKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "llama_index.storage.kvstore.azure.base.AzureKVStore")
```

Creates an instance of AzureKVStore using a SAS token.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">129</span>
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
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Creates an instance of AzureKVStore using a SAS token."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.credentials</span> <span class="kn">import</span> <span class="n">AzureSasCredential</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureSasCredential</span><span class="p">(</span><span class="n">sas_token</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_aad\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.from_aad_token "Permanent link")

```
from_aad_token(endpoint: str, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, *args: Any, **kwargs: Any) -> [AzureKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "llama_index.storage.kvstore.azure.base.AzureKVStore")
```

Creates an instance of AzureKVStore using Azure Active Directory (AAD) tokens.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">150</span>
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
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Creates an instance of AzureKVStore using Azure Active Directory</span>
<span class="sd">    (AAD) tokens.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.identity</span> <span class="kn">import</span> <span class="n">DefaultAzureCredential</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">credential</span> <span class="o">=</span> <span class="n">DefaultAzureCredential</span><span class="p">()</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span> <span class="n">credential</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.put "Permanent link")

```
put(key: str, val: dict, collection: str = None) -> None
```

Inserts or replaces a key-value pair in the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">173</span>
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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Inserts or replaces a key-value pair in the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">UpdateMode</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
    <span class="n">table_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
        <span class="p">{</span>
            <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
            <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
        <span class="p">},</span>
        <span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.aput "Permanent link")

```
aput(key: str, val: dict, collection: str = None) -> None
```

Inserts or replaces a key-value pair in the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
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
<span class="normal">226</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Inserts or replaces a key-value pair in the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">UpdateMode</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>
    <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
        <span class="p">{</span>
            <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
            <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
        <span class="p">},</span>
        <span class="n">mode</span><span class="o">=</span><span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.put_all "Permanent link")

```
put_all(kv_pairs: List[Tuple[str, dict]], collection: str = None, batch_size: int = DEFAULT_BATCH_SIZE) -> None
```

Inserts or replaces multiple key-value pairs in the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
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
<span class="normal">261</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Inserts or replaces multiple key-value pairs in the specified table.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TransactionOperation</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>

    <span class="n">entities</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
            <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span>
    <span class="p">]</span>

    <span class="n">entities_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">start</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
        <span class="n">table_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span>
            <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">UPSERT</span><span class="p">,</span> <span class="n">entities</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="n">start</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">))</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.aput_all "Permanent link")

```
aput_all(kv_pairs: List[Tuple[str, dict]], collection: str = None, batch_size: int = DEFAULT_BATCH_SIZE) -> None
```

Inserts or replaces multiple key-value pairs in the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">263</span>
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
<span class="normal">302</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Inserts or replaces multiple key-value pairs in the specified table.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.data.tables</span> <span class="kn">import</span> <span class="n">TransactionOperation</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>

    <span class="n">entities</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span>
            <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">serialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">val</span><span class="p">),</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span>
    <span class="p">]</span>

    <span class="n">entities_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">start</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
        <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span>
            <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">UPSERT</span><span class="p">,</span> <span class="n">entities</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="n">start</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">entities_len</span><span class="p">))</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.get "Permanent link")

```
get(key: str, collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Optional[dict]
```

Retrieves a value by key from the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">304</span>
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
<span class="normal">327</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">entity</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.aget "Permanent link")

```
aget(key: str, collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Optional[dict]
```

Retrieves a value by key from the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">329</span>
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
<span class="normal">356</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">entity</span> <span class="o">=</span> <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.get_all "Permanent link")

```
get_all(collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Dict[str, dict]
```

Retrieves all key-value pairs from a specified partition in the table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">358</span>
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
<span class="normal">377</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieves all key-value pairs from a specified partition in the table.</span>
<span class="sd">    """</span>
    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
    <span class="n">entities</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">list_entities</span><span class="p">(</span>
        <span class="nb">filter</span><span class="o">=</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
        <span class="n">select</span><span class="o">=</span><span class="n">select</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="n">entity</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]:</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.aget_all "Permanent link")

```
aget_all(collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Dict[str, dict]
```

Retrieves all key-value pairs from a specified partition in the table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">379</span>
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
<span class="normal">402</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieves all key-value pairs from a specified partition in the table.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>
    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>
    <span class="n">entities</span> <span class="o">=</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">list_entities</span><span class="p">(</span>
        <span class="nb">filter</span><span class="o">=</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
        <span class="n">select</span><span class="o">=</span><span class="n">select</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="n">entity</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]:</span> <span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.delete "Permanent link")

```
delete(key: str, collection: str = None) -> bool
```

Deletes a specific key-value pair from the store based on the provided key and partition key.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">404</span>
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
<span class="normal">418</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Deletes a specific key-value pair from the store based on the</span>
<span class="sd">    provided key and partition key.</span>
<span class="sd">    """</span>
    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
    <span class="n">table_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.adelete "Permanent link")

```
adelete(key: str, collection: str = None) -> bool
```

Asynchronously deletes a specific key-value pair from the store.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">420</span>
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
<span class="normal">435</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Asynchronously deletes a specific key-value pair from the store."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>
    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>
    <span class="k">await</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.query "Permanent link")

```
query(query_filter: str, collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Generator[dict, None, None]
```

Retrieves a value by key from the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">437</span>
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
<span class="normal">461</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_filter</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieves a value by key from the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">table_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span><span class="n">table_name</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">table_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span>
            <span class="n">query_filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span><span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### aquery `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore.aquery "Permanent link")

```
aquery(query_filter: str, collection: str = None, select: Optional[Union[str, List[str]]] = None) -> Optional[AsyncGenerator[dict, None]]
```

Asynchronously retrieves a value by key from the specified table.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-azure/llama_index/storage/kvstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">463</span>
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
<span class="normal">492</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_filter</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">select</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncGenerator</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="kc">None</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Asynchronously retrieves a value by key from the specified table."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.core.exceptions</span> <span class="kn">import</span> <span class="n">ResourceNotFoundError</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">MISSING_ASYNC_CLIENT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">table_name</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">DEFAULT_COLLECTION</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span> <span class="k">else</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">atable_client</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="n">table_name</span>
    <span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">atable_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span>
            <span class="n">query_filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="n">select</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span><span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">async</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">)</span>

    <span class="k">except</span> <span class="n">ResourceNotFoundError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/simple/)[Next Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/)
