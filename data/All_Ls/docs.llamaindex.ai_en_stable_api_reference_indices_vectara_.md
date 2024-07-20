Title: Vectara - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/

Markdown Content:
Vectara - LlamaIndex


VectaraIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/#llama_index.indices.managed.vectara.VectaraIndex "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

Vectara Index.

The Vectara index implements a managed index that uses Vectara as the backend. Vectara performs a lot of the functions in traditional indexes in the backend: - breaks down a document into chunks (nodes) - Creates the embedding for each chunk (node) - Performs the search for the top k most similar nodes to a query - Optionally can perform summarization of the top k nodes

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Whether to show tqdm progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vectara/llama_index/indices/managed/vectara/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 48</span>
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
<span class="normal">430</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectaraIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Vectara Index.</span>

<span class="sd">    The Vectara index implements a managed index that uses Vectara as the backend.</span>
<span class="sd">    Vectara performs a lot of the functions in traditional indexes in the backend:</span>
<span class="sd">    - breaks down a document into chunks (nodes)</span>
<span class="sd">    - Creates the embedding for each chunk (node)</span>
<span class="sd">    - Performs the search for the top k most similar nodes to a query</span>
<span class="sd">    - Optionally can perform summarization of the top k nodes</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vectara_customer_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vectara_corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vectara_api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_core_api</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">parallelize_ingest</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the Vectara API."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">parallelize_ingest</span> <span class="o">=</span> <span class="n">parallelize_ingest</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="n">VectaraIndexStruct</span><span class="p">(</span>
            <span class="n">index_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">vectara_corpus_id</span><span class="p">),</span>
            <span class="n">summary</span><span class="o">=</span><span class="s2">"Vectara Index"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span> <span class="o">=</span> <span class="n">vectara_customer_id</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s2">"VECTARA_CUSTOMER_ID"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_corpus_id</span> <span class="o">=</span> <span class="n">vectara_corpus_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span>
            <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"VECTARA_CORPUS_ID"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_api_key</span> <span class="o">=</span> <span class="n">vectara_api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"VECTARA_API_KEY"</span><span class="p">)</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_corpus_id</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_api_key</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"Can't find Vectara credentials, customer_id or corpus_id in "</span>
                <span class="s2">"environment."</span>
            <span class="p">)</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing Vectara credentials"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Using corpus id </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vectara_corpus_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># setup requests session with max 3 retries and 90s timeout</span>
        <span class="c1"># for calling Vectara API</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>  <span class="c1"># to reuse connections</span>
        <span class="n">adapter</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">adapters</span><span class="o">.</span><span class="n">HTTPAdapter</span><span class="p">(</span><span class="n">max_retries</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">mount</span><span class="p">(</span><span class="s2">"https://"</span><span class="p">,</span> <span class="n">adapter</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vectara_api_timeout</span> <span class="o">=</span> <span class="mi">90</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_core_api</span> <span class="o">=</span> <span class="n">use_core_api</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># if nodes is specified, consider each node as a single document</span>
        <span class="c1"># and use _build_index_from_nodes() to add them to the index</span>
        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_build_index_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">use_core_api</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">use_core_api</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexDict</span><span class="p">:</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
        <span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="n">use_core_api</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span>

    <span class="k">def</span> <span class="nf">_get_corpus_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get the corpus id to use for the index.</span>
<span class="sd">        If corpus_id is provided, check if it is one of the valid corpus ids.</span>
<span class="sd">        If not, use the first corpus id in the list.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">corpus_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">corpus_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_corpus_id</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">","</span><span class="p">):</span>
                <span class="k">return</span> <span class="n">corpus_id</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_corpus_id</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">","</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_post_headers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns headers that should be attached to each post request."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"x-api-key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_api_key</span><span class="p">,</span>
            <span class="s2">"customer-id"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"X-Source"</span><span class="p">:</span> <span class="s2">"llama_index"</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_delete_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete a document from the Vectara corpus.</span>

<span class="sd">        Args:</span>
<span class="sd">            url (str): URL of the page to delete.</span>
<span class="sd">            doc_id (str): ID of the document to delete.</span>
<span class="sd">            corpus_id (str): corpus ID to delete the document from.</span>

<span class="sd">        Returns:</span>
<span class="sd">            bool: True if deletion was successful, False otherwise.</span>
<span class="sd">        """</span>
        <span class="n">valid_corpus_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_corpus_id</span><span class="p">(</span><span class="n">corpus_id</span><span class="p">)</span>
        <span class="n">body</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"customerId"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span><span class="p">,</span>
            <span class="s2">"corpusId"</span><span class="p">:</span> <span class="n">valid_corpus_id</span><span class="p">,</span>
            <span class="s2">"documentId"</span><span class="p">:</span> <span class="n">doc_id</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="s2">"https://api.vectara.io/v1/delete-doc"</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">body</span><span class="p">),</span>
            <span class="n">verify</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_post_headers</span><span class="p">(),</span>
            <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vectara_api_timeout</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Delete request failed for doc_id = </span><span class="si">{</span><span class="n">doc_id</span><span class="si">}</span><span class="s2"> with status code "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">, reason </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">, text "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_index_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">request</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">request</span><span class="p">[</span><span class="s2">"customerId"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span>
        <span class="n">request</span><span class="p">[</span><span class="s2">"corpusId"</span><span class="p">]</span> <span class="o">=</span> <span class="n">corpus_id</span>
        <span class="n">request</span><span class="p">[</span><span class="s2">"document"</span><span class="p">]</span> <span class="o">=</span> <span class="n">doc</span>

        <span class="k">if</span> <span class="s2">"parts"</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
            <span class="n">api_url</span> <span class="o">=</span> <span class="s2">"https://api.vectara.io/v1/core/index"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">api_url</span> <span class="o">=</span> <span class="s2">"https://api.vectara.io/v1/index"</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_post_headers</span><span class="p">(),</span>
            <span class="n">url</span><span class="o">=</span><span class="n">api_url</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">request</span><span class="p">),</span>
            <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vectara_api_timeout</span><span class="p">,</span>
            <span class="n">verify</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">status_code</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="n">status_str</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"status"</span><span class="p">][</span><span class="s2">"code"</span><span class="p">]</span> <span class="k">if</span> <span class="s2">"status"</span> <span class="ow">in</span> <span class="n">result</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">status_code</span> <span class="o"></span> <span class="s2">"ALREADY_EXISTS"</span><span class="p">):</span>
            <span class="k">return</span> <span class="s2">"E_ALREADY_EXISTS"</span>
        <span class="k">elif</span> <span class="n">status_code</span> <span class="o"></span> <span class="s2">"INVALID_ARGUMENT"</span><span class="p">):</span>
            <span class="k">return</span> <span class="s2">"E_INVALID_ARGUMENT"</span>
        <span class="k">elif</span> <span class="n">status_str</span> <span class="ow">and</span> <span class="p">(</span><span class="n">status_str</span> <span class="o"></span> <span class="mi">409</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"File </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> already exists on Vectara, skipping indexing"</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"File Upload for </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> returned 0 quota consumed, please check your Vectara account quota"</span>
                <span class="p">)</span>
            <span class="n">doc_id</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"documentId"</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">doc_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc_id</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">doc_id</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error indexing file </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">res</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Vectara does not support deleting a reference document"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Vectara does not support updating a reference document"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a Retriever for this managed index."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vectara.retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">VectaraRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">VectaraRetriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_chat_engine</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseChatEngine</span><span class="p">:</span>
        <span class="n">kwargs</span><span class="p">[</span><span class="s2">"summary_enabled"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"summary_enabled"</span><span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vectara.query</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">VectaraChatEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">VectaraChatEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="n">retriever</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

    <span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"summary_enabled"</span><span class="p">,</span> <span class="kc">True</span><span class="p">):</span>
            <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vectara.query</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">VectaraQueryEngine</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"summary_enabled"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">VectaraQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">llm</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">)</span>
                <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
            <span class="p">)</span>

            <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
                <span class="n">response_mode</span><span class="o">=</span><span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
                <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
                <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build a Vectara index from a sequence of documents."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
            <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert\_file [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/#llama_index.indices.managed.vectara.VectaraIndex.insert_file "Permanent link")

```
insert_file(file_path: str, metadata: Optional[dict] = None, corpus_id: Optional[str] = None, **insert_kwargs: Any) -> Optional[str]
```

Vectara provides a way to add files (binary or text) directly via our API where pre-processing and chunking occurs internally in an optimal way This method provides a way to use that API in Llama\_index.

#### ruff: noqa: E501[#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/#llama_index.indices.managed.vectara.VectaraIndex.insert_file--ruff-noqa-e501 "Permanent link")

Full API Docs: https://docs.vectara.com/docs/api-reference/indexing-apis/ file-upload/file-upload-filetypes

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file_path` | `str` | 
local file path Files could be text, HTML, PDF, markdown, doc/docx, ppt/pptx, etc. see API docs for full list



 | _required_ |
| `metadata` | `Optional[dict]` | 

Optional list of metadata associated with the file



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `Optional[str]` | 
List of ids associated with each of the files indexed



 |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vectara/llama_index/indices/managed/vectara/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">285</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">insert_file</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Vectara provides a way to add files (binary or text) directly via our API</span>
<span class="sd">    where pre-processing and chunking occurs internally in an optimal way</span>
<span class="sd">    This method provides a way to use that API in Llama_index.</span>

<span class="sd">    # ruff: noqa: E501</span>
<span class="sd">    Full API Docs: https://docs.vectara.com/docs/api-reference/indexing-apis/</span>
<span class="sd">    file-upload/file-upload-filetypes</span>

<span class="sd">    Args:</span>
<span class="sd">        file_path: local file path</span>
<span class="sd">            Files could be text, HTML, PDF, markdown, doc/docx, ppt/pptx, etc.</span>
<span class="sd">            see API docs for full list</span>
<span class="sd">        metadata: Optional list of metadata associated with the file</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of ids associated with each of the files indexed</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">file_path</span><span class="p">):</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"File </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> does not exist"</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">metadata</span><span class="p">[</span><span class="s2">"framework"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"llama_index"</span>
    <span class="n">files</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"file"</span><span class="p">:</span> <span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)),</span>
        <span class="s2">"doc_metadata"</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">metadata</span><span class="p">),</span>
    <span class="p">}</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_post_headers</span><span class="p">()</span>
    <span class="n">headers</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"Content-Type"</span><span class="p">)</span>
    <span class="n">valid_corpus_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_corpus_id</span><span class="p">(</span><span class="n">corpus_id</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"https://api.vectara.io/upload?c=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_vectara_customer_id</span><span class="si">}</span><span class="s2">&amp;o=</span><span class="si">{</span><span class="n">valid_corpus_id</span><span class="si">}</span><span class="s2">&amp;d=True"</span><span class="p">,</span>
        <span class="n">files</span><span class="o">=</span><span class="n">files</span><span class="p">,</span>
        <span class="n">verify</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vectara_api_timeout</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">res</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="mi">200</span><span class="p">:</span>
        <span class="n">quota</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"response"</span><span class="p">][</span><span class="s2">"quotaConsumed"</span><span class="p">][</span><span class="s2">"numChars"</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">quota</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"File Upload for </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> returned 0 quota consumed, please check your Vectara account quota"</span>
            <span class="p">)</span>
        <span class="n">doc_id</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"documentId"</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">doc_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">doc_id</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error indexing file </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">res</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### as\_retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/#llama_index.indices.managed.vectara.VectaraIndex.as_retriever "Permanent link")

```
as_retriever(**kwargs: Any) -> [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Return a Retriever for this managed index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vectara/llama_index/indices/managed/vectara/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a Retriever for this managed index."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vectara.retriever</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">VectaraRetriever</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">VectaraRetriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_documents `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/#llama_index.indices.managed.vectara.VectaraIndex.from_documents "Permanent link")

```
from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], show_progress: bool = False, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, transformations: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, **kwargs: Any) -> IndexType
```

Build a Vectara index from a sequence of documents.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vectara/llama_index/indices/managed/vectara/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">412</span>
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
<span class="normal">430</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build a Vectara index from a sequence of documents."""</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span>
    <span class="p">]</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tree](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/)[Next Vector](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/)
