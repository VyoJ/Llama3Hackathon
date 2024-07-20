Title: Jaguar - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/

Markdown Content:
Jaguar - LlamaIndex


JaguarVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Jaguar vector store.

See http://www.jaguardb.com See http://github.com/fserv/jaguar-sdk

**Examples:**

`pip install llama-index-vector-stores-jaguar`

```
from llama_index.vector_stores.jaguar import JaguarVectorStore
vectorstore = JaguarVectorStore(
    pod = 'vdb',
    store = 'mystore',
    vector_index = 'v',
    vector_type = 'cosine_fraction_float',
    vector_dimension = 1536,
    url='http://192.168.8.88:8080/fwww/',
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

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
<span class="normal">510</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JaguarVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Jaguar vector store.</span>

<span class="sd">    See http://www.jaguardb.com</span>
<span class="sd">    See http://github.com/fserv/jaguar-sdk</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-jaguar`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.jaguar import JaguarVectorStore</span>
<span class="sd">        vectorstore = JaguarVectorStore(</span>
<span class="sd">            pod = 'vdb',</span>
<span class="sd">            store = 'mystore',</span>
<span class="sd">            vector_index = 'v',</span>
<span class="sd">            vector_type = 'cosine_fraction_float',</span>
<span class="sd">            vector_dimension = 1536,</span>
<span class="sd">            url='http://192.168.8.88:8080/fwww/',</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_pod</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_store</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_vector_index</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_vector_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_vector_dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_jag</span><span class="p">:</span> <span class="n">JaguarHttpClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">pod</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">store</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_index</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Constructor of JaguarVectorStore.</span>

<span class="sd">        Args:</span>
<span class="sd">            pod: str:  name of the pod (database)</span>
<span class="sd">            store: str:  name of vector store in the pod</span>
<span class="sd">            vector_index: str:  name of vector index of the store</span>
<span class="sd">            vector_type: str:  type of the vector index</span>
<span class="sd">            vector_dimension: int:  dimension of the vector index</span>
<span class="sd">            url: str:  URL end point of jaguar http server</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">=</span> <span class="n">pod</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_store</span> <span class="o">=</span> <span class="n">store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span> <span class="o">=</span> <span class="n">vector_index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_type</span> <span class="o">=</span> <span class="n">vector_type</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_dimension</span> <span class="o">=</span> <span class="n">vector_dimension</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span> <span class="o">=</span> <span class="n">JaguarHttpClient</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"JaguarVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>
<span class="sd">        """</span>
        <span class="n">use_node_metadata</span> <span class="o">=</span> <span class="n">add_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"use_node_metadata"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">use_node_metadata</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">zid</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">embedding</span><span class="p">,</span> <span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">zid</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>
<span class="sd">        """</span>
        <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
        <span class="n">q</span> <span class="o">=</span> <span class="s2">"delete from "</span> <span class="o">+</span> <span class="n">podstore</span> <span class="o">+</span> <span class="s2">" where zid='"</span> <span class="o">+</span> <span class="n">ref_doc_id</span> <span class="o">+</span> <span class="s2">"'"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query: VectorStoreQuery object</span>
<span class="sd">            kwargs:  may contain 'where', 'metadata_fields', 'args', 'fetch_k'</span>
<span class="sd">        """</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
        <span class="n">k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
        <span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="p">,</span> <span class="n">simscores</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_search_with_score</span><span class="p">(</span>
            <span class="n">embedding</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">form</span><span class="o">=</span><span class="s2">"node"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">simscores</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">embedding</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">k</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Query index to load top k most similar documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            embedding: a list of floats</span>
<span class="sd">            k: topK number</span>
<span class="sd">            kwargs:  may contain 'where', 'metadata_fields', 'args', 'fetch_k'</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">similarity_search_with_score</span><span class="p">(</span><span class="n">embedding</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">form</span><span class="o">=</span><span class="s2">"doc"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">create</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        create the vector store on the backend database.</span>

<span class="sd">        Args:</span>
<span class="sd">            metadata_fields (str):  exrta metadata columns and types</span>
<span class="sd">        Returns:</span>
<span class="sd">            True if successful; False if not successful</span>
<span class="sd">        """</span>
        <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>

<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        v:text column is required.</span>
<span class="sd">        """</span>
        <span class="n">q</span> <span class="o">=</span> <span class="s2">"create store "</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="n">podstore</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">" (</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span><span class="si">}</span><span class="s2"> vector(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_dimension</span><span class="si">}</span><span class="s2">,"</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">" '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_type</span><span class="si">}</span><span class="s2">'),"</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"  v:text char(</span><span class="si">{</span><span class="n">text_size</span><span class="si">}</span><span class="s2">),"</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="n">metadata_fields</span> <span class="o">+</span> <span class="s2">")"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_text</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add  texts through the embeddings and add to the vectorstore.</span>

<span class="sd">        Args:</span>
<span class="sd">          texts: text string to add to the jaguar vector store.</span>
<span class="sd">          embedding: embedding vector of the text, list of floats</span>
<span class="sd">          metadata: {'file_path': '../data/paul_graham/paul_graham_essay.txt',</span>
<span class="sd">                          'file_name': 'paul_graham_essay.txt',</span>
<span class="sd">                          'file_type': 'text/plain',</span>
<span class="sd">                          'file_size': 75042,</span>
<span class="sd">                          'creation_date': '2023-12-24',</span>
<span class="sd">                          'last_modified_date': '2023-12-24',</span>
<span class="sd">                          'last_accessed_date': '2023-12-28'}</span>
<span class="sd">          kwargs: vector_index=name_of_vector_index</span>
<span class="sd">                  file_column=name_of_file_column</span>
<span class="sd">                  metadata={...}</span>

<span class="sd">        Returns:</span>
<span class="sd">            id from adding the text into the vectorstore</span>
<span class="sd">        """</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"'"</span><span class="p">,</span> <span class="s2">"</span><span class="se">\\</span><span class="s2">'"</span><span class="p">)</span>
        <span class="n">vcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span>
        <span class="n">filecol</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_column"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
        <span class="n">text_tag</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text_tag"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">text_tag</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">text_tag</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">text</span>

        <span class="n">podstorevcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="n">vcol</span>
        <span class="n">q</span> <span class="o">=</span> <span class="s2">"textcol "</span> <span class="o">+</span> <span class="n">podstorevcol</span>
        <span class="n">js</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">js</span> <span class="o"></span> <span class="s2">"node"</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">zid</span><span class="p">)</span>
                <span class="n">simscores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">score</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">form</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="n">jd</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">js</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">if</span> <span class="n">jd</span><span class="p">[</span><span class="s2">"anomalous"</span><span class="p">]</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"E0005 error run(</span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span><span class="p">,</span> <span class="n">withFile</span><span class="p">)</span>
        <span class="n">txt</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">text</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">txt</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Count records of a store in jaguardb.</span>

<span class="sd">        Args: no args</span>
<span class="sd">        Returns: (int) number of records in pod store</span>
<span class="sd">        """</span>
        <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
        <span class="n">q</span> <span class="o">=</span> <span class="s2">"select count() from "</span> <span class="o">+</span> <span class="n">podstore</span>
        <span class="n">js</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">js</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">js</span><span class="p">)</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="n">jaguar_api_key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">getApiKey</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_jaguar_api_key</span> <span class="o">=</span> <span class="n">jaguar_api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">jaguar_api_key</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="n">nvec</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">nvmap</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
            <span class="n">vvec</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">nvmap</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nvec</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">vvec</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">if</span> <span class="n">filecol</span> <span class="ow">in</span> <span class="n">nvmap</span><span class="p">:</span>
                <span class="n">nvec</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">filecol</span><span class="p">)</span>
                <span class="n">vvec</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nvmap</span><span class="p">[</span><span class="n">filecol</span><span class="p">])</span>
                <span class="n">filepath</span> <span class="o">=</span> <span class="n">nvmap</span><span class="p">[</span><span class="n">filecol</span><span class="p">]</span>

            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">nvmap</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">k</span> <span class="o">!=</span> <span class="n">filecol</span><span class="p">:</span>
                    <span class="n">nvec</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
                    <span class="n">vvec</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nvec</span><span class="p">,</span> <span class="n">vvec</span><span class="p">,</span> <span class="n">filepath</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.add "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
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
<span class="normal">126</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>
<span class="sd">    """</span>
    <span class="n">use_node_metadata</span> <span class="o">=</span> <span class="n">add_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"use_node_metadata"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">use_node_metadata</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">zid</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">embedding</span><span class="p">,</span> <span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">zid</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>
<span class="sd">    """</span>
    <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
    <span class="n">q</span> <span class="o">=</span> <span class="s2">"delete from "</span> <span class="o">+</span> <span class="n">podstore</span> <span class="o">+</span> <span class="s2">" where zid='"</span> <span class="o">+</span> <span class="n">ref_doc_id</span> <span class="o">+</span> <span class="s2">"'"</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
VectorStoreQuery object



 | _required_ |
| `kwargs` | `Any` | 

may contain 'where', 'metadata\_fields', 'args', 'fetch\_k'



 | `{}` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">139</span>
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
<span class="normal">151</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query: VectorStoreQuery object</span>
<span class="sd">        kwargs:  may contain 'where', 'metadata_fields', 'args', 'fetch_k'</span>
<span class="sd">    """</span>
    <span class="n">embedding</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
    <span class="n">k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
    <span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="p">,</span> <span class="n">simscores</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_search_with_score</span><span class="p">(</span>
        <span class="n">embedding</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">form</span><span class="o">=</span><span class="s2">"node"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">simscores</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.load_documents "Permanent link")

```
load_documents(embedding: List[float], k: int, **kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Query index to load top k most similar documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `embedding` | `List[float]` | 
a list of floats



 | _required_ |
| `k` | `int` | 

topK number



 | _required_ |
| `kwargs` | `Any` | 

may contain 'where', 'metadata\_fields', 'args', 'fetch\_k'



 | `{}` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">153</span>
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
<span class="normal">166</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">embedding</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">k</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Query index to load top k most similar documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        embedding: a list of floats</span>
<span class="sd">        k: topK number</span>
<span class="sd">        kwargs:  may contain 'where', 'metadata_fields', 'args', 'fetch_k'</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">cast</span><span class="p">(</span>
        <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_search_with_score</span><span class="p">(</span><span class="n">embedding</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">form</span><span class="o">=</span><span class="s2">"doc"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.create "Permanent link")

```
create(metadata_fields: str, text_size: int) -> None
```

create the vector store on the backend database.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metadata_fields` | `str` | 
exrta metadata columns and types



 | _required_ |

Returns: True if successful; False if not successful

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">168</span>
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
<span class="normal">192</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">metadata_fields</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    create the vector store on the backend database.</span>

<span class="sd">    Args:</span>
<span class="sd">        metadata_fields (str):  exrta metadata columns and types</span>
<span class="sd">    Returns:</span>
<span class="sd">        True if successful; False if not successful</span>
<span class="sd">    """</span>
    <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>

<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    v:text column is required.</span>
<span class="sd">    """</span>
    <span class="n">q</span> <span class="o">=</span> <span class="s2">"create store "</span>
    <span class="n">q</span> <span class="o">+=</span> <span class="n">podstore</span>
    <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">" (</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span><span class="si">}</span><span class="s2"> vector(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_dimension</span><span class="si">}</span><span class="s2">,"</span>
    <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">" '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_type</span><span class="si">}</span><span class="s2">'),"</span>
    <span class="n">q</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"  v:text char(</span><span class="si">{</span><span class="n">text_size</span><span class="si">}</span><span class="s2">),"</span>
    <span class="n">q</span> <span class="o">+=</span> <span class="n">metadata_fields</span> <span class="o">+</span> <span class="s2">")"</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.add_text "Permanent link")

```
add_text(text: str, embedding: List[float], metadata: Optional[dict] = None, **kwargs: Any) -> str
```

Add texts through the embeddings and add to the vectorstore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `texts` |  | 
text string to add to the jaguar vector store.



 | _required_ |
| `embedding` | `List[float]` | 

embedding vector of the text, list of floats



 | _required_ |
| `metadata` | `Optional[dict]` | 

{'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75042, 'creation\_date': '2023-12-24', 'last\_modified\_date': '2023-12-24', 'last\_accessed\_date': '2023-12-28'}



 | `None` |
| `kwargs` | `Any` | 

vector\_index=name\_of\_vector\_index file\_column=name\_of\_file\_column metadata={...}



 | `{}` |

**Returns:**

| Type | Description |
| --- | --- |
| `str` | 
id from adding the text into the vectorstore



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">194</span>
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
<span class="normal">276</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_text</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">embedding</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add  texts through the embeddings and add to the vectorstore.</span>

<span class="sd">    Args:</span>
<span class="sd">      texts: text string to add to the jaguar vector store.</span>
<span class="sd">      embedding: embedding vector of the text, list of floats</span>
<span class="sd">      metadata: {'file_path': '../data/paul_graham/paul_graham_essay.txt',</span>
<span class="sd">                      'file_name': 'paul_graham_essay.txt',</span>
<span class="sd">                      'file_type': 'text/plain',</span>
<span class="sd">                      'file_size': 75042,</span>
<span class="sd">                      'creation_date': '2023-12-24',</span>
<span class="sd">                      'last_modified_date': '2023-12-24',</span>
<span class="sd">                      'last_accessed_date': '2023-12-28'}</span>
<span class="sd">      kwargs: vector_index=name_of_vector_index</span>
<span class="sd">              file_column=name_of_file_column</span>
<span class="sd">              metadata={...}</span>

<span class="sd">    Returns:</span>
<span class="sd">        id from adding the text into the vectorstore</span>
<span class="sd">    """</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"'"</span><span class="p">,</span> <span class="s2">"</span><span class="se">\\</span><span class="s2">'"</span><span class="p">)</span>
    <span class="n">vcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span>
    <span class="n">filecol</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_column"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
    <span class="n">text_tag</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text_tag"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">text_tag</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">text_tag</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">text</span>

    <span class="n">podstorevcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="n">vcol</span>
    <span class="n">q</span> <span class="o">=</span> <span class="s2">"textcol "</span> <span class="o">+</span> <span class="n">podstorevcol</span>
    <span class="n">js</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">js</span> <span class="o"></span> <span class="s2">"node"</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">zid</span><span class="p">)</span>
            <span class="n">simscores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">score</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">form</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
    <span class="n">jd</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">js</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">jd</span><span class="p">[</span><span class="s2">"anomalous"</span><span class="p">]</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"E0005 error run(</span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span><span class="p">,</span> <span class="n">withFile</span><span class="p">)</span>
    <span class="n">txt</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">text</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">txt</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>
</code></pre></div></td></tr></tbody></table>

### count [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.count "Permanent link")

```
count() -> int
```

Count records of a store in jaguardb.

Args: no args Returns: (int) number of records in pod store

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

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
<span class="normal">436</span>
<span class="normal">437</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Count records of a store in jaguardb.</span>

<span class="sd">    Args: no args</span>
<span class="sd">    Returns: (int) number of records in pod store</span>
<span class="sd">    """</span>
    <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
    <span class="n">q</span> <span class="o">=</span> <span class="s2">"select count() from "</span> <span class="o">+</span> <span class="n">podstore</span>
    <span class="n">js</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">js</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">js</span><span class="p">)</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
        <span class="n">jaguar_api_key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">getApiKey</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_jaguar_api_key</span> <span class="o">=</span> <span class="n">jaguar_api_key</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">jaguar_api_key</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">==</span> <span class="s2">""</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"E0001 error init(): invalid jaguar_api_key"</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">False</span>
    <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### logout [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/#llama_index.vector_stores.jaguar.JaguarVectorStore.logout "Permanent link")

```
logout() -> None
```

Logout to cleanup resources.

Args: no args Returns: None

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-jaguar/llama_index/vector_stores/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">logout</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logout to cleanup resources.</span>

<span class="sd">    Args: no args</span>
<span class="sd">    Returns: None</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">logout</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_token</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/)[Next Kdbai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/kdbai/)
