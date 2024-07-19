Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/

Markdown Content:
Index - LlamaIndex


Base index classes.

BaseIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `Generic[IS]`, `ABC`

Base LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[Node]` | 
List of nodes to index



 | `None` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `service_context` | `ServiceContext` | 

Service context container (contains components like LLM, Embeddings, etc.).



 | `None` |

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 31</span>
<span class="normal"> 32</span>
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
<span class="normal">505</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="k">class</span> <span class="nc">BaseIndex</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">IS</span><span class="p">],</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[Node]): List of nodes to index</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">        service_context (ServiceContext): Service context container (contains</span>
<span class="sd">            components like LLM, Embeddings, etc.).</span>

<span class="sd">    """</span>

    <span class="n">index_struct_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IS</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IS</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">index_struct</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">objects</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"One of nodes, objects, or index_struct must be provided."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">index_struct</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Only one of nodes or index_struct can be provided."</span><span class="p">)</span>
        <span class="c1"># This is to explicitly make sure that the old UX is not used</span>
        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">1</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">Document</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"The constructor now takes in a list of Node objects. "</span>
                    <span class="s2">"Since you are passing in a list of Document objects, "</span>
                    <span class="s2">"please use `from_documents` instead."</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"nodes must be a list of Node objects."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span> <span class="o">=</span> <span class="n">storage_context</span> <span class="ow">or</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
        <span class="c1"># deprecated</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span> <span class="o">=</span> <span class="n">service_context</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">docstore</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">vector_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">graph_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">objects</span> <span class="o">=</span> <span class="n">objects</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span> <span class="o">=</span> <span class="p">{</span><span class="n">obj</span><span class="o">.</span><span class="n">index_id</span><span class="p">:</span> <span class="n">obj</span><span class="o">.</span><span class="n">obj</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">objects</span><span class="p">}</span>
        <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">objects</span><span class="p">:</span>
            <span class="n">obj</span><span class="o">.</span><span class="n">obj</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># clear the object to avoid serialization issues</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"index_construction"</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">index_struct</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="n">nodes</span> <span class="ow">or</span> <span class="p">[]</span>
                <span class="n">index_struct</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_index_from_nodes</span><span class="p">(</span>
                    <span class="n">nodes</span> <span class="o">+</span> <span class="n">objects</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>  <span class="c1"># type: ignore</span>
                <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="n">index_struct</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_transformations</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">transformations</span>
            <span class="ow">or</span> <span class="n">transformations_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create index from documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (Optional[Sequence[BaseDocument]]): List of documents to</span>
<span class="sd">                build the index from.</span>

<span class="sd">        """</span>
        <span class="n">storage_context</span> <span class="o">=</span> <span class="n">storage_context</span> <span class="ow">or</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
        <span class="n">docstore</span> <span class="o">=</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">docstore</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="n">transformations_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>

        <span class="k">with</span> <span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"index_construction"</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
                <span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span> <span class="n">doc</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

            <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
                <span class="n">documents</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
                <span class="n">transformations</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
                <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
                <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">index_struct</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IS</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the index struct."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">index_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the index struct."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">index_id</span>

    <span class="k">def</span> <span class="nf">set_index_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set the index id.</span>

<span class="sd">        NOTE: if you decide to set the index_id on the index_struct manually,</span>
<span class="sd">        you will need to explicitly call `add_index_struct` on the `index_store`</span>
<span class="sd">        to update the index store.</span>

<span class="sd">        Args:</span>
<span class="sd">            index_id (str): Index id to set.</span>

<span class="sd">        """</span>
        <span class="c1"># delete the old index struct</span>
        <span class="n">old_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">index_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">delete_index_struct</span><span class="p">(</span><span class="n">old_id</span><span class="p">)</span>
        <span class="c1"># add the new index struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">index_id</span> <span class="o">=</span> <span class="n">index_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">docstore</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseDocumentStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the docstore corresponding to the index."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">service_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">storage_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StorageContext</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">summary</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">summary</span><span class="p">)</span>

    <span class="nd">@summary</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">summary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_summary</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">summary</span> <span class="o">=</span> <span class="n">new_summary</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">build_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IS</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes."""</span>

    <span class="k">def</span> <span class="nf">build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">build_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IS</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_index_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">build_kwargs</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Index-specific logic for inserting nodes to the index struct."""</span>

    <span class="k">def</span> <span class="nf">insert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert nodes."""</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
                <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">obj</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">obj</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert_nodes"</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_insert</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert"</span><span class="p">):</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
                <span class="p">[</span><span class="n">document</span><span class="p">],</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_transformations</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span> <span class="n">document</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a node."""</span>

    <span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a list of nodes from the index.</span>

<span class="sd">        Args:</span>
<span class="sd">            doc_ids (List[str]): A list of doc_ids from the nodes to delete</span>

<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_delete_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document from the index.</span>
<span class="sd">        All nodes in the index related to the index will be deleted.</span>

<span class="sd">        Args:</span>
<span class="sd">            doc_id (str): A doc_id of the ingested document</span>

<span class="sd">        """</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"delete() is now deprecated, please refer to delete_ref_doc() to delete "</span>
            <span class="s2">"ingested documents+nodes or delete_nodes to delete a list of nodes."</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">doc_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document and it's nodes by using ref_doc_id."""</span>
        <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">ref_doc_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"ref_doc_id </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2"> not found, nothing deleted."</span><span class="p">)</span>
            <span class="k">return</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span>
            <span class="n">ref_doc_info</span><span class="o">.</span><span class="n">node_ids</span><span class="p">,</span>
            <span class="n">delete_from_docstore</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update a document and it's corresponding nodes.</span>

<span class="sd">        This is equivalent to deleting the document and then inserting it again.</span>

<span class="sd">        Args:</span>
<span class="sd">            document (Union[BaseDocument, BaseIndex]): document to update</span>
<span class="sd">            insert_kwargs (Dict): kwargs to pass to insert</span>
<span class="sd">            delete_kwargs (Dict): kwargs to pass to delete</span>

<span class="sd">        """</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"update() is now deprecated, please refer to update_ref_doc() to update "</span>
            <span class="s2">"ingested documents+nodes."</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">update_ref_doc</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update a document and it's corresponding nodes.</span>

<span class="sd">        This is equivalent to deleting the document and then inserting it again.</span>

<span class="sd">        Args:</span>
<span class="sd">            document (Union[BaseDocument, BaseIndex]): document to update</span>
<span class="sd">            insert_kwargs (Dict): kwargs to pass to insert</span>
<span class="sd">            delete_kwargs (Dict): kwargs to pass to delete</span>

<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"update"</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span>
                <span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span>
                <span class="n">delete_from_docstore</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"delete_kwargs"</span><span class="p">,</span> <span class="p">{}),</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"insert_kwargs"</span><span class="p">,</span> <span class="p">{}))</span>

    <span class="k">def</span> <span class="nf">refresh</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Refresh an index with documents that have changed.</span>

<span class="sd">        This allows users to save LLM and Embedding model calls, while only</span>
<span class="sd">        updating documents that have any changes in text or metadata. It</span>
<span class="sd">        will also insert any documents that previously were not stored.</span>
<span class="sd">        """</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"refresh() is now deprecated, please refer to refresh_ref_docs() to "</span>
            <span class="s2">"refresh ingested documents+nodes with an updated list of documents."</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">refresh_ref_docs</span><span class="p">(</span><span class="n">documents</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">refresh_ref_docs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Refresh an index with documents that have changed.</span>

<span class="sd">        This allows users to save LLM and Embedding model calls, while only</span>
<span class="sd">        updating documents that have any changes in text or metadata. It</span>
<span class="sd">        will also insert any documents that previously were not stored.</span>
<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"refresh"</span><span class="p">):</span>
            <span class="n">refreshed_documents</span> <span class="o">=</span> <span class="p">[</span><span class="kc">False</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">document</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">documents</span><span class="p">):</span>
                <span class="n">existing_doc_hash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_document_hash</span><span class="p">(</span>
                    <span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">()</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="n">existing_doc_hash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"insert_kwargs"</span><span class="p">,</span> <span class="p">{}))</span>
                    <span class="n">refreshed_documents</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">elif</span> <span class="n">existing_doc_hash</span> <span class="o">!=</span> <span class="n">document</span><span class="o">.</span><span class="n">hash</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">update_ref_doc</span><span class="p">(</span>
                        <span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"update_kwargs"</span><span class="p">,</span> <span class="p">{})</span>
                    <span class="p">)</span>
                    <span class="n">refreshed_documents</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>

            <span class="k">return</span> <span class="n">refreshed_documents</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert the index to a query engine.</span>

<span class="sd">        Calls `index.as_retriever(**kwargs)` to get the retriever and then wraps it in a</span>
<span class="sd">        `RetrieverQueryEngine.from_args(retriever, **kwrags)` call.</span>
<span class="sd">        """</span>
        <span class="c1"># NOTE: lazy import</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">llm</span>
            <span class="k">else</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="n">retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_chat_engine</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chat_mode</span><span class="p">:</span> <span class="n">ChatMode</span> <span class="o">=</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">BEST</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseChatEngine</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert the index to a chat engine.</span>

<span class="sd">        Calls `index.as_query_engine(llm=llm, **kwargs)` to get the query engine and then</span>
<span class="sd">        wraps it in a chat engine based on the chat mode.</span>

<span class="sd">        Chat modes:</span>
<span class="sd">            - `ChatMode.BEST` (default): Chat engine that uses an agent (react or openai) with a query engine tool</span>
<span class="sd">            - `ChatMode.CONTEXT`: Chat engine that uses a retriever to get context</span>
<span class="sd">            - `ChatMode.CONDENSE_QUESTION`: Chat engine that condenses questions</span>
<span class="sd">            - `ChatMode.CONDENSE_PLUS_CONTEXT`: Chat engine that condenses questions and uses a retriever to get context</span>
<span class="sd">            - `ChatMode.SIMPLE`: Simple chat engine that uses the LLM directly</span>
<span class="sd">            - `ChatMode.REACT`: Chat engine that uses a react agent with a query engine tool</span>
<span class="sd">            - `ChatMode.OPENAI`: Chat engine that uses an openai agent with a query engine tool</span>
<span class="sd">        """</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"service_context"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">llm</span>
                <span class="k">else</span> <span class="n">service_context</span><span class="o">.</span><span class="n">llm</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">llm</span>
                <span class="k">else</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
            <span class="p">)</span>

        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="c1"># resolve chat mode</span>
        <span class="k">if</span> <span class="n">chat_mode</span> <span class="ow">in</span> <span class="p">[</span><span class="n">ChatMode</span><span class="o">.</span><span class="n">REACT</span><span class="p">,</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">OPENAI</span><span class="p">,</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">BEST</span><span class="p">]:</span>
            <span class="c1"># use an agent with query engine tool in these chat modes</span>
            <span class="c1"># NOTE: lazy import</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.agent</span> <span class="kn">import</span> <span class="n">AgentRunner</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.tools.query_engine</span> <span class="kn">import</span> <span class="n">QueryEngineTool</span>

            <span class="c1"># convert query engine to tool</span>
            <span class="n">query_engine_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">)</span>

            <span class="k">return</span> <span class="n">AgentRunner</span><span class="o">.</span><span class="n">from_llm</span><span class="p">(</span>
                <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">query_engine_tool</span><span class="p">],</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">chat_mode</span> <span class="o"></span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">CONTEXT</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.chat_engine</span> <span class="kn">import</span> <span class="n">ContextChatEngine</span>

            <span class="k">return</span> <span class="n">ContextChatEngine</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">elif</span> <span class="n">chat_mode</span> <span class="o"></span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">SIMPLE</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.chat_engine</span> <span class="kn">import</span> <span class="n">SimpleChatEngine</span>

            <span class="k">return</span> <span class="n">SimpleChatEngine</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown chat mode: </span><span class="si">{</span><span class="n">chat_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### index\_struct `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.index_struct "Permanent link")

```
index_struct: IS
```

Get the index struct.

### index\_id `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.index_id "Permanent link")

```
index_id: str
```

Get the index struct.

### docstore `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.docstore "Permanent link")

```
docstore: [BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.types.BaseDocumentStore")
```

Get the docstore corresponding to the index.

### ref\_doc\_info `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.ref_doc_info "Permanent link")

```
ref_doc_info: Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Retrieve a dict mapping of ingested documents and their nodes+metadata.

### from\_documents `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.from_documents "Permanent link")

```
from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], storage_context: Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")] = None, show_progress: bool = False, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, transformations: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, service_context: Optional[ServiceContext] = None, **kwargs: Any) -> IndexType
```

Create index from documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `documents` | `Optional[Sequence[BaseDocument]]` | 
List of documents to build the index from.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># deprecated</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create index from documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        documents (Optional[Sequence[BaseDocument]]): List of documents to</span>
<span class="sd">            build the index from.</span>

<span class="sd">    """</span>
    <span class="n">storage_context</span> <span class="o">=</span> <span class="n">storage_context</span> <span class="ow">or</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
    <span class="n">docstore</span> <span class="o">=</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">docstore</span>
    <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">callback_manager</span>
        <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="n">transformations_from_settings_or_context</span><span class="p">(</span>
        <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
    <span class="p">)</span>

    <span class="k">with</span> <span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"index_construction"</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span> <span class="n">doc</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
            <span class="n">transformations</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set\_index\_id [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.set_index_id "Permanent link")

```
set_index_id(index_id: str) -> None
```

Set the index id.

NOTE: if you decide to set the index\_id on the index\_struct manually, you will need to explicitly call `add_index_struct` on the `index_store` to update the index store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index_id` | `str` | 
Index id to set.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">165</span>
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
<span class="normal">181</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="k">def</span> <span class="nf">set_index_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the index id.</span>

<span class="sd">    NOTE: if you decide to set the index_id on the index_struct manually,</span>
<span class="sd">    you will need to explicitly call `add_index_struct` on the `index_store`</span>
<span class="sd">    to update the index store.</span>

<span class="sd">    Args:</span>
<span class="sd">        index_id (str): Index id to set.</span>

<span class="sd">    """</span>
    <span class="c1"># delete the old index struct</span>
    <span class="n">old_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">index_id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">delete_index_struct</span><span class="p">(</span><span class="n">old_id</span><span class="p">)</span>
    <span class="c1"># add the new index struct</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">index_id</span> <span class="o">=</span> <span class="n">index_id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### build\_index\_from\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.build_index_from_nodes "Permanent link")

```
build_index_from_nodes(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **build_kwargs: Any) -> IS
```

Build the index from nodes.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span></pre></div></td><td class="code"><div><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="k">def</span> <span class="nf">build_index_from_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">build_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IS</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build the index from nodes."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_index_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">build_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.insert_nodes "Permanent link")

```
insert_nodes(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **insert_kwargs: Any) -> None
```

Insert nodes.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">222</span>
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
<span class="normal">235</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="k">def</span> <span class="nf">insert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert nodes."""</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">obj</span>
                <span class="n">node</span><span class="o">.</span><span class="n">obj</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert_nodes"</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.insert "Permanent link")

```
insert(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **insert_kwargs: Any) -> None
```

Insert a document.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="k">def</span> <span class="nf">insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert a document."""</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert"</span><span class="p">):</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
            <span class="p">[</span><span class="n">document</span><span class="p">],</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_transformations</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">set_document_hash</span><span class="p">(</span><span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span> <span class="n">document</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.delete_nodes "Permanent link")

```
delete_nodes(node_ids: List[str], delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a list of nodes from the index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `doc_ids` | `List[str]` | 
A list of doc\_ids from the nodes to delete



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
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
<span class="normal">270</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a list of nodes from the index.</span>

<span class="sd">    Args:</span>
<span class="sd">        doc_ids (List[str]): A list of doc_ids from the nodes to delete</span>

<span class="sd">    """</span>
    <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_delete_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.delete "Permanent link")

```
delete(doc_id: str, **delete_kwargs: Any) -> None
```

Delete a document from the index. All nodes in the index related to the index will be deleted.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `doc_id` | `str` | 
A doc\_id of the ingested document



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">272</span>
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
<span class="normal">284</span></pre></div></td><td class="code"><div><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document from the index.</span>
<span class="sd">    All nodes in the index related to the index will be deleted.</span>

<span class="sd">    Args:</span>
<span class="sd">        doc_id (str): A doc_id of the ingested document</span>

<span class="sd">    """</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
        <span class="s2">"delete() is now deprecated, please refer to delete_ref_doc() to delete "</span>
        <span class="s2">"ingested documents+nodes or delete_nodes to delete a list of nodes."</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">doc_id</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a document and it's nodes by using ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">286</span>
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
<span class="normal">302</span></pre></div></td><td class="code"><div><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document and it's nodes by using ref_doc_id."""</span>
    <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">ref_doc_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"ref_doc_id </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2"> not found, nothing deleted."</span><span class="p">)</span>
        <span class="k">return</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span>
        <span class="n">ref_doc_info</span><span class="o">.</span><span class="n">node_ids</span><span class="p">,</span>
        <span class="n">delete_from_docstore</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.update "Permanent link")

```
update(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **update_kwargs: Any) -> None
```

Update a document and it's corresponding nodes.

This is equivalent to deleting the document and then inserting it again.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `document` | `Union[BaseDocument, [BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]` | 
document to update



 | _required_ |
| `insert_kwargs` | `Dict` | 

kwargs to pass to insert



 | _required_ |
| `delete_kwargs` | `Dict` | 

kwargs to pass to delete



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

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
<span class="normal">319</span></pre></div></td><td class="code"><div><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update a document and it's corresponding nodes.</span>

<span class="sd">    This is equivalent to deleting the document and then inserting it again.</span>

<span class="sd">    Args:</span>
<span class="sd">        document (Union[BaseDocument, BaseIndex]): document to update</span>
<span class="sd">        insert_kwargs (Dict): kwargs to pass to insert</span>
<span class="sd">        delete_kwargs (Dict): kwargs to pass to delete</span>

<span class="sd">    """</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
        <span class="s2">"update() is now deprecated, please refer to update_ref_doc() to update "</span>
        <span class="s2">"ingested documents+nodes."</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">update_ref_doc</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.update_ref_doc "Permanent link")

```
update_ref_doc(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **update_kwargs: Any) -> None
```

Update a document and it's corresponding nodes.

This is equivalent to deleting the document and then inserting it again.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `document` | `Union[BaseDocument, [BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]` | 
document to update



 | _required_ |
| `insert_kwargs` | `Dict` | 

kwargs to pass to insert



 | _required_ |
| `delete_kwargs` | `Dict` | 

kwargs to pass to delete



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">321</span>
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
<span class="normal">338</span></pre></div></td><td class="code"><div><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update a document and it's corresponding nodes.</span>

<span class="sd">    This is equivalent to deleting the document and then inserting it again.</span>

<span class="sd">    Args:</span>
<span class="sd">        document (Union[BaseDocument, BaseIndex]): document to update</span>
<span class="sd">        insert_kwargs (Dict): kwargs to pass to insert</span>
<span class="sd">        delete_kwargs (Dict): kwargs to pass to delete</span>

<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"update"</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span>
            <span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">(),</span>
            <span class="n">delete_from_docstore</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"delete_kwargs"</span><span class="p">,</span> <span class="p">{}),</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"insert_kwargs"</span><span class="p">,</span> <span class="p">{}))</span>
</code></pre></div></td></tr></tbody></table>

### refresh [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.refresh "Permanent link")

```
refresh(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], **update_kwargs: Any) -> List[bool]
```

Refresh an index with documents that have changed.

This allows users to save LLM and Embedding model calls, while only updating documents that have any changes in text or metadata. It will also insert any documents that previously were not stored.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">340</span>
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
<span class="normal">353</span></pre></div></td><td class="code"><div><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="k">def</span> <span class="nf">refresh</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">bool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Refresh an index with documents that have changed.</span>

<span class="sd">    This allows users to save LLM and Embedding model calls, while only</span>
<span class="sd">    updating documents that have any changes in text or metadata. It</span>
<span class="sd">    will also insert any documents that previously were not stored.</span>
<span class="sd">    """</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
        <span class="s2">"refresh() is now deprecated, please refer to refresh_ref_docs() to "</span>
        <span class="s2">"refresh ingested documents+nodes with an updated list of documents."</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">refresh_ref_docs</span><span class="p">(</span><span class="n">documents</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### refresh\_ref\_docs [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.refresh_ref_docs "Permanent link")

```
refresh_ref_docs(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], **update_kwargs: Any) -> List[bool]
```

Refresh an index with documents that have changed.

This allows users to save LLM and Embedding model calls, while only updating documents that have any changes in text or metadata. It will also insert any documents that previously were not stored.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">355</span>
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
<span class="normal">379</span></pre></div></td><td class="code"><div><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="k">def</span> <span class="nf">refresh_ref_docs</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">bool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Refresh an index with documents that have changed.</span>

<span class="sd">    This allows users to save LLM and Embedding model calls, while only</span>
<span class="sd">    updating documents that have any changes in text or metadata. It</span>
<span class="sd">    will also insert any documents that previously were not stored.</span>
<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"refresh"</span><span class="p">):</span>
        <span class="n">refreshed_documents</span> <span class="o">=</span> <span class="p">[</span><span class="kc">False</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">document</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">documents</span><span class="p">):</span>
            <span class="n">existing_doc_hash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_document_hash</span><span class="p">(</span>
                <span class="n">document</span><span class="o">.</span><span class="n">get_doc_id</span><span class="p">()</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">existing_doc_hash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"insert_kwargs"</span><span class="p">,</span> <span class="p">{}))</span>
                <span class="n">refreshed_documents</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">elif</span> <span class="n">existing_doc_hash</span> <span class="o">!=</span> <span class="n">document</span><span class="o">.</span><span class="n">hash</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">update_ref_doc</span><span class="p">(</span>
                    <span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"update_kwargs"</span><span class="p">,</span> <span class="p">{})</span>
                <span class="p">)</span>
                <span class="n">refreshed_documents</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="k">return</span> <span class="n">refreshed_documents</span>
</code></pre></div></td></tr></tbody></table>

### as\_query\_engine [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.as_query_engine "Permanent link")

```
as_query_engine(llm: Optional[LLMType] = None, **kwargs: Any) -> [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")
```

Convert the index to a query engine.

Calls `index.as_retriever(**kwargs)` to get the retriever and then wraps it in a `RetrieverQueryEngine.from_args(retriever, **kwrags)` call.

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">391</span>
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
<span class="normal">415</span></pre></div></td><td class="code"><div><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert the index to a query engine.</span>

<span class="sd">    Calls `index.as_retriever(**kwargs)` to get the retriever and then wraps it in a</span>
<span class="sd">    `RetrieverQueryEngine.from_args(retriever, **kwrags)` call.</span>
<span class="sd">    """</span>
    <span class="c1"># NOTE: lazy import</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">llm</span>
        <span class="k">else</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
        <span class="n">retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_chat\_engine [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex.as_chat_engine "Permanent link")

```
as_chat_engine(chat_mode: [ChatMode](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode "llama_index.core.chat_engine.types.ChatMode") = ChatMode.BEST, llm: Optional[LLMType] = None, **kwargs: Any) -> [BaseChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "llama_index.core.chat_engine.types.BaseChatEngine")
```

Convert the index to a chat engine.

Calls `index.as_query_engine(llm=llm, **kwargs)` to get the query engine and then wraps it in a chat engine based on the chat mode.

Chat modes

*   `ChatMode.BEST` (default): Chat engine that uses an agent (react or openai) with a query engine tool
*   `ChatMode.CONTEXT`: Chat engine that uses a retriever to get context
*   `ChatMode.CONDENSE_QUESTION`: Chat engine that condenses questions
*   `ChatMode.CONDENSE_PLUS_CONTEXT`: Chat engine that condenses questions and uses a retriever to get context
*   `ChatMode.SIMPLE`: Simple chat engine that uses the LLM directly
*   `ChatMode.REACT`: Chat engine that uses a react agent with a query engine tool
*   `ChatMode.OPENAI`: Chat engine that uses an openai agent with a query engine tool

Source code in `llama-index-core/llama_index/core/indices/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">417</span>
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
<span class="normal">505</span></pre></div></td><td class="code"><div><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="k">def</span> <span class="nf">as_chat_engine</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">chat_mode</span><span class="p">:</span> <span class="n">ChatMode</span> <span class="o">=</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">BEST</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseChatEngine</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert the index to a chat engine.</span>

<span class="sd">    Calls `index.as_query_engine(llm=llm, **kwargs)` to get the query engine and then</span>
<span class="sd">    wraps it in a chat engine based on the chat mode.</span>

<span class="sd">    Chat modes:</span>
<span class="sd">        - `ChatMode.BEST` (default): Chat engine that uses an agent (react or openai) with a query engine tool</span>
<span class="sd">        - `ChatMode.CONTEXT`: Chat engine that uses a retriever to get context</span>
<span class="sd">        - `ChatMode.CONDENSE_QUESTION`: Chat engine that condenses questions</span>
<span class="sd">        - `ChatMode.CONDENSE_PLUS_CONTEXT`: Chat engine that condenses questions and uses a retriever to get context</span>
<span class="sd">        - `ChatMode.SIMPLE`: Simple chat engine that uses the LLM directly</span>
<span class="sd">        - `ChatMode.REACT`: Chat engine that uses a react agent with a query engine tool</span>
<span class="sd">        - `ChatMode.OPENAI`: Chat engine that uses an openai agent with a query engine tool</span>
<span class="sd">    """</span>
    <span class="n">service_context</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"service_context"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">llm</span>
            <span class="k">else</span> <span class="n">service_context</span><span class="o">.</span><span class="n">llm</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">llm</span>
            <span class="k">else</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="p">)</span>

    <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="c1"># resolve chat mode</span>
    <span class="k">if</span> <span class="n">chat_mode</span> <span class="ow">in</span> <span class="p">[</span><span class="n">ChatMode</span><span class="o">.</span><span class="n">REACT</span><span class="p">,</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">OPENAI</span><span class="p">,</span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">BEST</span><span class="p">]:</span>
        <span class="c1"># use an agent with query engine tool in these chat modes</span>
        <span class="c1"># NOTE: lazy import</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.agent</span> <span class="kn">import</span> <span class="n">AgentRunner</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.tools.query_engine</span> <span class="kn">import</span> <span class="n">QueryEngineTool</span>

        <span class="c1"># convert query engine to tool</span>
        <span class="n">query_engine_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentRunner</span><span class="o">.</span><span class="n">from_llm</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">query_engine_tool</span><span class="p">],</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">chat_mode</span> <span class="o"></span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">CONTEXT</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.chat_engine</span> <span class="kn">import</span> <span class="n">ContextChatEngine</span>

        <span class="k">return</span> <span class="n">ContextChatEngine</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">elif</span> <span class="n">chat_mode</span> <span class="o"></span> <span class="n">ChatMode</span><span class="o">.</span><span class="n">SIMPLE</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.chat_engine</span> <span class="kn">import</span> <span class="n">SimpleChatEngine</span>

        <span class="k">return</span> <span class="n">SimpleChatEngine</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown chat mode: </span><span class="si">{</span><span class="n">chat_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Google](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/)[Next Keyword](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/)

Hi, how can I help you?

🦙
