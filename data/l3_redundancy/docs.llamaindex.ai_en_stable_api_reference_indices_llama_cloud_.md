Title: Llama cloud - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/

Markdown Content:
Llama cloud - LlamaIndex


LlamaCloudIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

LlamaIndex Platform Index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-llama-cloud/llama_index/indices/managed/llama_cloud/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 53</span>
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
<span class="normal">445</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LlamaCloudIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LlamaIndex Platform Index."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">60</span><span class="p">,</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PROJECT_NAME</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">app_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the Platform Index."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">project_name</span> <span class="o">=</span> <span class="n">project_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># TODO: How to handle uploading nodes without running transforms on them?</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"LlamaCloudIndex does not support nodes on initialization"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">get_client</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">base_url</span><span class="p">,</span> <span class="n">app_url</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="o">=</span> <span class="n">get_aclient</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">base_url</span><span class="p">,</span> <span class="n">app_url</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="n">base_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_app_url</span> <span class="o">=</span> <span class="n">app_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span> <span class="o">=</span> <span class="n">timeout</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span>

    <span class="k">def</span> <span class="nf">_wait_for_pipeline_ingestion</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">raise_on_partial_success</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
        <span class="n">client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Syncing pipeline: "</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">)</span>

        <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="n">status</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">get_pipeline_status</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span>
            <span class="p">)</span><span class="o">.</span><span class="n">status</span>
            <span class="k">if</span> <span class="n">status</span> <span class="o"></span> <span class="n">ManagedIngestionStatus</span><span class="o">.</span><span class="n">PARTIAL_SUCCESS</span>
            <span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Pipeline ingestion failed for </span><span class="si">{</span><span class="n">pipeline_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">status</span> <span class="ow">in</span> <span class="p">[</span>
                <span class="n">ManagedIngestionStatus</span><span class="o">.</span><span class="n">NOT_STARTED</span><span class="p">,</span>
                <span class="n">ManagedIngestionStatus</span><span class="o">.</span><span class="n">IN_PROGRESS</span><span class="p">,</span>
            <span class="p">]:</span>
                <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"."</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">)</span>
                <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.5</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"Done!"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_wait_for_documents_ingestion</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">doc_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">raise_on_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
        <span class="n">client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Loading data: "</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">)</span>

        <span class="c1"># wait until all documents are loaded</span>
        <span class="n">pending_docs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">doc_ids</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">pending_docs</span><span class="p">:</span>
            <span class="n">docs_to_remove</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">pending_docs</span><span class="p">:</span>
                <span class="c1"># we have to quote the doc id twice because it is used as a path parameter</span>
                <span class="n">status</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">get_pipeline_document_status</span><span class="p">(</span>
                    <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">doc</span><span class="p">))</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="n">status</span> <span class="ow">in</span> <span class="p">[</span>
                    <span class="n">ManagedIngestionStatus</span><span class="o">.</span><span class="n">NOT_STARTED</span><span class="p">,</span>
                    <span class="n">ManagedIngestionStatus</span><span class="o">.</span><span class="n">IN_PROGRESS</span><span class="p">,</span>
                <span class="p">]:</span>
                    <span class="k">continue</span>

                <span class="k">if</span> <span class="n">status</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Unknown index name </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">. Please confirm a "</span>
                <span class="s2">"managed index with this name exists."</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">pipelines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Multiple pipelines found with name </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> in project </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="n">pipeline</span> <span class="o">=</span> <span class="n">pipelines</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

        <span class="k">if</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"No pipeline found with name </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> in project </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">id</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s2">"LlamaCloudIndex"</span><span class="p">],</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PROJECT_NAME</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">app_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">60</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">raise_on_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LlamaCloudIndex"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build a LlamaCloud managed index from a sequence of documents."""</span>
        <span class="n">app_url</span> <span class="o">=</span> <span class="n">app_url</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"LLAMA_CLOUD_APP_URL"</span><span class="p">,</span> <span class="n">DEFAULT_APP_URL</span><span class="p">)</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">get_client</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">base_url</span><span class="p">,</span> <span class="n">app_url</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>

        <span class="n">pipeline_create</span> <span class="o">=</span> <span class="n">get_pipeline_create</span><span class="p">(</span>
            <span class="n">name</span><span class="p">,</span>
            <span class="n">client</span><span class="p">,</span>
            <span class="n">PipelineType</span><span class="o">.</span><span class="n">MANAGED</span><span class="p">,</span>
            <span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span> <span class="ow">or</span> <span class="n">default_transformations</span><span class="p">(),</span>
            <span class="n">input_nodes</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">project</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">projects</span><span class="o">.</span><span class="n">upsert_project</span><span class="p">(</span>
            <span class="n">request</span><span class="o">=</span><span class="n">ProjectCreate</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">project_name</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to create/get project </span><span class="si">{</span><span class="n">project_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Created project </span><span class="si">{</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="si">}</span><span class="s2"> with name </span><span class="si">{</span><span class="n">project</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">pipeline</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">upsert_pipeline</span><span class="p">(</span>
            <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">request</span><span class="o">=</span><span class="n">pipeline_create</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to create/get pipeline </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Created pipeline </span><span class="si">{</span><span class="n">pipeline</span><span class="o">.</span><span class="n">id</span><span class="si">}</span><span class="s2"> with name </span><span class="si">{</span><span class="n">pipeline</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">name</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span>
            <span class="n">app_url</span><span class="o">=</span><span class="n">app_url</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># this kicks off document ingestion</span>
        <span class="n">upserted_documents</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">upsert_batch_pipeline_documents</span><span class="p">(</span>
            <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">request</span><span class="o">=</span><span class="p">[</span>
                <span class="n">CloudDocumentCreate</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                    <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                    <span class="nb">id</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span>
            <span class="p">],</span>
        <span class="p">)</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">upserted_documents</span><span class="p">]</span>
        <span class="n">index</span><span class="o">.</span><span class="n">_wait_for_documents_ingestion</span><span class="p">(</span>
            <span class="n">doc_ids</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">raise_on_error</span><span class="o">=</span><span class="n">raise_on_error</span>
        <span class="p">)</span>

        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Find your index at </span><span class="si">{</span><span class="n">app_url</span><span class="si">}</span><span class="s2">/project/</span><span class="si">{</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="si">}</span><span class="s2">/deploy/</span><span class="si">{</span><span class="n">pipeline</span><span class="o">.</span><span class="n">id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">index</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a Retriever for this managed index."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.indices.managed.llama_cloud.retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">LlamaCloudRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"similarity_top_k"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">dense_similarity_top_k</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"dense_similarity_top_k"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">similarity_top_k</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">dense_similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>

        <span class="k">return</span> <span class="n">LlamaCloudRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">project_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span>
            <span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span><span class="p">,</span>
            <span class="n">app_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_app_url</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span><span class="p">,</span>
            <span class="n">dense_similarity_top_k</span><span class="o">=</span><span class="n">dense_similarity_top_k</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their metadata. The nodes list is empty."""</span>
        <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
        <span class="n">pipeline_documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CloudDocument</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">skip</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">limit</span> <span class="o">=</span> <span class="n">batch_size</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">list_pipeline_documents</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span>
                <span class="n">skip</span><span class="o">=</span><span class="n">skip</span><span class="p">,</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">batch</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="n">pipeline_documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">batch</span><span class="p">)</span>
            <span class="n">skip</span> <span class="o">+=</span> <span class="n">limit</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">id</span><span class="p">:</span> <span class="n">RefDocInfo</span><span class="p">(</span><span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="n">node_ids</span><span class="o">=</span><span class="p">[])</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">pipeline_documents</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">insert</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert"</span><span class="p">):</span>
            <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
            <span class="n">upserted_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">create_batch_pipeline_documents</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">CloudDocumentCreate</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                        <span class="nb">id</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">],</span>
            <span class="p">)</span>
            <span class="n">upserted_document</span> <span class="o">=</span> <span class="n">upserted_documents</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_documents_ingestion</span><span class="p">(</span>
                <span class="p">[</span><span class="n">upserted_document</span><span class="o">.</span><span class="n">id</span><span class="p">],</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">raise_on_error</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Upserts a document and its corresponding nodes."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"update"</span><span class="p">):</span>
            <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
            <span class="n">upserted_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">upsert_batch_pipeline_documents</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">CloudDocumentCreate</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                        <span class="nb">id</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">],</span>
            <span class="p">)</span>
            <span class="n">upserted_document</span> <span class="o">=</span> <span class="n">upserted_documents</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_documents_ingestion</span><span class="p">(</span>
                <span class="p">[</span><span class="n">upserted_document</span><span class="o">.</span><span class="n">id</span><span class="p">],</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">raise_on_error</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">refresh_ref_docs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Refresh an index with documents that have changed."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"refresh"</span><span class="p">):</span>
            <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
            <span class="n">upserted_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">upsert_batch_pipeline_documents</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">CloudDocumentCreate</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                        <span class="nb">id</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span>
                <span class="p">],</span>
            <span class="p">)</span>
            <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">upserted_documents</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_documents_ingestion</span><span class="p">(</span>
                <span class="n">doc_ids</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">raise_on_error</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="kc">True</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">doc_ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">raise_if_not_found</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document and its nodes by using ref_doc_id."""</span>
        <span class="n">pipeline_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_pipeline_id</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># we have to quote the ref_doc_id twice because it is used as a path parameter</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">pipelines</span><span class="o">.</span><span class="n">delete_pipeline_document</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">))</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">ApiError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="mi">404</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">raise_if_not_found</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"ref_doc_id </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2"> not found, nothing deleted."</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span>

    <span class="c1"># we have to wait for the pipeline instead of the document, because the document is already deleted</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_pipeline_ingestion</span><span class="p">(</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">raise_on_partial_success</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### build\_index\_from\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.build_index_from_nodes "Permanent link")

```
build_index_from_nodes(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> None
```

Build the index from nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-llama-cloud/llama_index/indices/managed/llama_cloud/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">build_index_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build the index from nodes."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
        <span class="s2">"build_index_from_nodes not implemented for LlamaCloudIndex."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.insert_nodes "Permanent link")

```
insert_nodes(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **insert_kwargs: Any) -> None
```

Insert a set of nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-llama-cloud/llama_index/indices/managed/llama_cloud/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">insert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert a set of nodes."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"insert_nodes not implemented for LlamaCloudIndex."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/#llama_index.indices.managed.llama_cloud.LlamaCloudIndex.delete_nodes "Permanent link")

```
delete_nodes(node_ids: List[str], delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a set of nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-llama-cloud/llama_index/indices/managed/llama_cloud/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a set of nodes."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"delete_nodes not implemented for LlamaCloudIndex."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/)[Next Postgresml](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/)
