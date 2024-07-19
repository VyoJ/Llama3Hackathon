Title: Zilliz - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/

Markdown Content:
Zilliz - LlamaIndex


ZillizCloudPipelineIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/#llama_index.indices.managed.zilliz.ZillizCloudPipelineIndex "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

Zilliz Cloud Pipeline's Index.

The Zilliz Cloud Pipeline's index implements a managed index that uses Zilliz Cloud Pipelines as the backend.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pipeline_ids` | `dict` | 
A dictionary of pipeline ids for INGESTION, SEARCH, DELETION.



 | _required_ |
| `api_key` | `str` | 

Zilliz Cloud's API key.



 | `None` |
| `cloud_region` | `str='gcp-us-west1'` | 

The region of Zilliz Cloud's cluster. Defaults to 'gcp-us-west1'.



 | `'gcp-us-west1'` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-zilliz/llama_index/indices/managed/zilliz/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 46</span>
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
<span class="normal">426</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ZillizCloudPipelineIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Zilliz Cloud Pipeline's Index.</span>

<span class="sd">    The Zilliz Cloud Pipeline's index implements a managed index that uses Zilliz Cloud Pipelines as the backend.</span>

<span class="sd">    Args:</span>
<span class="sd">        pipeline_ids (dict): A dictionary of pipeline ids for INGESTION, SEARCH, DELETION.</span>
<span class="sd">        api_key (str): Zilliz Cloud's API key.</span>
<span class="sd">        cloud_region (str='gcp-us-west1'): The region of Zilliz Cloud's cluster. Defaults to 'gcp-us-west1'.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">pipeline_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cloud_region</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gcp-us-west1"</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">token</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cloud_region</span> <span class="o">=</span> <span class="n">cloud_region</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">domain</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"https://controller.api.</span><span class="si">{</span><span class="n">cloud_region</span><span class="si">}</span><span class="s2">.zillizcloud.com/v1/pipelines"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"Accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pipeline_ids</span> <span class="o">=</span> <span class="n">pipeline_ids</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pipeline_ids</span><span class="p">)</span> <span class="o"></span> <span class="s2">"text"</span><span class="p">:</span>
            <span class="n">ingest_action</span> <span class="o">=</span> <span class="s2">"INDEX_TEXT"</span>
            <span class="n">search_action</span> <span class="o">=</span> <span class="s2">"SEARCH_TEXT"</span>
        <span class="k">elif</span> <span class="n">data_type</span> <span class="o"></span> <span class="s2">"text"</span><span class="p">:</span>
        <span class="n">ingest_action</span> <span class="o">=</span> <span class="s2">"INDEX_TEXT"</span>
        <span class="n">search_action</span> <span class="o">=</span> <span class="s2">"SEARCH_TEXT"</span>
    <span class="k">elif</span> <span class="n">data_type</span> <span class="o">==</span> <span class="s2">"doc"</span><span class="p">:</span>
        <span class="n">ingest_action</span> <span class="o">=</span> <span class="s2">"INDEX_DOC"</span>
        <span class="n">search_action</span> <span class="o">=</span> <span class="s2">"SEARCH_DOC_CHUNK"</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Only text or doc is supported as the data type."</span><span class="p">)</span>

    <span class="n">params_dict</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">additional_params</span> <span class="o">=</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="n">language</span> <span class="o">=</span> <span class="n">additional_params</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"language"</span><span class="p">,</span> <span class="s2">"ENGLISH"</span><span class="p">)</span>
    <span class="n">embedding</span> <span class="o">=</span> <span class="n">additional_params</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"embedding"</span><span class="p">,</span> <span class="s2">"zilliz/bge-base-en-v1.5"</span><span class="p">)</span>
    <span class="n">reranker</span> <span class="o">=</span> <span class="n">additional_params</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"reranker"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">index_func</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="s2">"llamaindex_index"</span><span class="p">,</span>
        <span class="s2">"action"</span><span class="p">:</span> <span class="n">ingest_action</span><span class="p">,</span>
        <span class="s2">"language"</span><span class="p">:</span> <span class="n">language</span><span class="p">,</span>
        <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">embedding</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">index_func</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">additional_params</span><span class="p">)</span>
    <span class="n">ingest_functions</span> <span class="o">=</span> <span class="p">[</span><span class="n">index_func</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">metadata_schema</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">metadata_schema</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">preserve_func</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"name"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"keep_</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="s2">"action"</span><span class="p">:</span> <span class="s2">"PRESERVE"</span><span class="p">,</span>
                <span class="s2">"inputField"</span><span class="p">:</span> <span class="n">k</span><span class="p">,</span>
                <span class="s2">"outputField"</span><span class="p">:</span> <span class="n">k</span><span class="p">,</span>
                <span class="s2">"fieldType"</span><span class="p">:</span> <span class="n">v</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="n">ingest_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">preserve_func</span><span class="p">)</span>
    <span class="n">params_dict</span><span class="p">[</span><span class="s2">"INGESTION"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">_ingestion"</span><span class="p">,</span>
        <span class="s2">"projectId"</span><span class="p">:</span> <span class="n">project_id</span><span class="p">,</span>
        <span class="s2">"clusterId"</span><span class="p">:</span> <span class="n">cluster_id</span><span class="p">,</span>
        <span class="s2">"collectionName"</span><span class="p">:</span> <span class="n">collection_name</span><span class="p">,</span>
        <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"INGESTION"</span><span class="p">,</span>
        <span class="s2">"functions"</span><span class="p">:</span> <span class="n">ingest_functions</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">search_function</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="s2">"llamaindex_search"</span><span class="p">,</span>
        <span class="s2">"action"</span><span class="p">:</span> <span class="n">search_action</span><span class="p">,</span>
        <span class="s2">"clusterId"</span><span class="p">:</span> <span class="n">cluster_id</span><span class="p">,</span>
        <span class="s2">"collectionName"</span><span class="p">:</span> <span class="n">collection_name</span><span class="p">,</span>
        <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">embedding</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">if</span> <span class="n">reranker</span><span class="p">:</span>
        <span class="n">search_function</span><span class="p">[</span><span class="s2">"reranker"</span><span class="p">]</span> <span class="o">=</span> <span class="n">reranker</span>
    <span class="n">params_dict</span><span class="p">[</span><span class="s2">"SEARCH"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">_search"</span><span class="p">,</span>
        <span class="s2">"projectId"</span><span class="p">:</span> <span class="n">project_id</span><span class="p">,</span>
        <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"SEARCH"</span><span class="p">,</span>
        <span class="s2">"functions"</span><span class="p">:</span> <span class="p">[</span><span class="n">search_function</span><span class="p">],</span>
    <span class="p">}</span>

    <span class="n">params_dict</span><span class="p">[</span><span class="s2">"DELETION"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">_deletion"</span><span class="p">,</span>
        <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"DELETION"</span><span class="p">,</span>
        <span class="s2">"functions"</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">"name"</span><span class="p">:</span> <span class="s2">"purge_by_expression"</span><span class="p">,</span>
                <span class="s2">"action"</span><span class="p">:</span> <span class="s2">"PURGE_BY_EXPRESSION"</span><span class="p">,</span>
            <span class="p">}</span>
        <span class="p">],</span>
        <span class="s2">"projectId"</span><span class="p">:</span> <span class="n">project_id</span><span class="p">,</span>
        <span class="s2">"clusterId"</span><span class="p">:</span> <span class="n">cluster_id</span><span class="p">,</span>
        <span class="s2">"collectionName"</span><span class="p">:</span> <span class="n">collection_name</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">domain</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://controller.api.</span><span class="si">{</span><span class="n">cloud_region</span><span class="si">}</span><span class="s2">.zillizcloud.com/v1/pipelines"</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">api_key</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="s2">"Accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">pipeline_ids</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">params_dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">domain</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">v</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>
        <span class="n">response_dict</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">response_dict</span><span class="p">[</span><span class="s2">"code"</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">response_dict</span><span class="p">)</span>
        <span class="n">pipeline_ids</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">response_dict</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"pipelineId"</span><span class="p">]</span>

    <span class="k">return</span> <span class="n">pipeline_ids</span>
</code></pre></div></td></tr></tbody></table>

### from\_document\_url `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/#llama_index.indices.managed.zilliz.ZillizCloudPipelineIndex.from_document_url "Permanent link")

```
from_document_url(url: str, pipeline_ids: Optional[Dict] = None, api_key: Optional[str] = None, metadata: Optional[Dict] = None, show_progress: bool = False, **kwargs: Any) -> BaseManagedIndex
```

Zilliz Cloud Pipeline loads document from a signed url and then builds auto index for it.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `str` | 
a gcs or s3 signed url.



 | _required_ |
| `pipeline_ids` | `dict=None` | 

A dictionary of pipeline ids for INGESTION, SEARCH, DELETION. Defaults to None.



 | `None` |
| `api_key` | `str` | 

Zilliz Cloud's API Key.



 | `None` |
| `metadata` | `Dict=None` | 

A dictionary of metadata. Defaults to None. The key must be string and the value must be a string, float, integer, or boolean.



 | `None` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |

**Returns:**

| Type | Description |
| --- | --- |
| `BaseManagedIndex` | 
An initialized ZillizCloudPipelineIndex



 |

Example

> > > from llama\_index.indices import ZillizCloudPipelineIndex api\_key = "{YOUR\_ZILLIZ\_CLOUD\_API\_KEY}" pipeline\_ids = ZillizCloudPipelineIndex.create\_pipelines( project\_id="{YOUR\_ZILLIZ\_PROJECT\_ID}", cluster\_id="{YOUR\_ZILLIZ\_CLUSTER\_ID}", api\_key=api\_key, data\_type="doc" ) ZillizCloudPipelineIndex.from\_document\_url( url='https://oss\_bucket.test\_doc.ext', pipeline\_ids=pipeline\_ids, api\_key=api\_key )

Source code in `llama-index-integrations/indices/llama-index-indices-managed-zilliz/llama_index/indices/managed/zilliz/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">314</span>
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
<span class="normal">365</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_document_url</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">pipeline_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseManagedIndex</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Zilliz Cloud Pipeline loads document from a signed url and then builds auto index for it.</span>

<span class="sd">    Args:</span>
<span class="sd">        url: a gcs or s3 signed url.</span>
<span class="sd">        pipeline_ids (dict=None): A dictionary of pipeline ids for INGESTION, SEARCH, DELETION. Defaults to None.</span>
<span class="sd">        api_key (str): Zilliz Cloud's API Key.</span>
<span class="sd">        metadata (Dict=None): A dictionary of metadata. Defaults to None. The key must be string and the value must be a string, float, integer, or boolean.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An initialized ZillizCloudPipelineIndex</span>

<span class="sd">    Example:</span>
<span class="sd">        &gt;&gt;&gt; from llama_index.indices import ZillizCloudPipelineIndex</span>
<span class="sd">        &gt;&gt;&gt; api_key = "{YOUR_ZILLIZ_CLOUD_API_KEY}"</span>
<span class="sd">        &gt;&gt;&gt; pipeline_ids = ZillizCloudPipelineIndex.create_pipelines(</span>
<span class="sd">        &gt;&gt;&gt;     project_id="{YOUR_ZILLIZ_PROJECT_ID}",</span>
<span class="sd">        &gt;&gt;&gt;     cluster_id="{YOUR_ZILLIZ_CLUSTER_ID}",</span>
<span class="sd">        &gt;&gt;&gt;     api_key=api_key,</span>
<span class="sd">        &gt;&gt;&gt;     data_type="doc"</span>
<span class="sd">        &gt;&gt;&gt; )</span>
<span class="sd">        &gt;&gt;&gt; ZillizCloudPipelineIndex.from_document_url(</span>
<span class="sd">        &gt;&gt;&gt;     url='https://oss_bucket.test_doc.ext',</span>
<span class="sd">        &gt;&gt;&gt;     pipeline_ids=pipeline_ids,</span>
<span class="sd">        &gt;&gt;&gt;     api_key=api_key</span>
<span class="sd">        &gt;&gt;&gt; )</span>
<span class="sd">    """</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">index</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">pipeline_ids</span><span class="o">=</span><span class="n">pipeline_ids</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">index</span><span class="o">.</span><span class="n">_insert_doc_url</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
            <span class="s2">"Failed to build managed index given document url (</span><span class="si">%s</span><span class="s2">):</span><span class="se">\n</span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">e</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">index</span>
</code></pre></div></td></tr></tbody></table>

### from\_documents `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/#llama_index.indices.managed.zilliz.ZillizCloudPipelineIndex.from_documents "Permanent link")

```
from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], pipeline_ids: Optional[Dict] = None, api_key: Optional[str] = None, show_progress: bool = False, metadata: Optional[Dict] = None, **kwargs: Any) -> IndexType
```

Build a Zilliz Cloud Pipeline index from a sequence of documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `documents` | `Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
a sequence of llamaindex documents.



 | _required_ |
| `pipeline_ids` | `dict=None` | 

A dictionary of pipeline ids for INGESTION, SEARCH, DELETION. Defaults to None.



 | `None` |
| `api_key` | `str` | 

Zilliz Cloud's API Key.



 | `None` |
| `metadata` | `Dict=None` | 

A dictionary of metadata. Defaults to None. The key must be string and the value must be a string, float, integer, or boolean.



 | `None` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |

**Returns:**

| Type | Description |
| --- | --- |
| `IndexType` | 
An initialized ZillizCloudPipelineIndex



 |

Example

> > > from llama\_index.indices import ZillizCloudPipelineIndex api\_key = "{YOUR\_ZILLIZ\_CLOUD\_API\_KEY}" pipeline\_ids = ZillizCloudPipelineIndex.create\_pipelines( project\_id="{YOUR\_ZILLIZ\_PROJECT\_ID}", cluster\_id="{YOUR\_ZILLIZ\_CLUSTER\_ID}", api\_key=api\_key, data\_type="text" ) ZillizCloudPipelineIndex.from\_documents( documents=my\_documents, pipeline\_ids=pipeline\_ids, api\_key=api\_key )

Source code in `llama-index-integrations/indices/llama-index-indices-managed-zilliz/llama_index/indices/managed/zilliz/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">367</span>
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
<span class="normal">416</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">pipeline_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build a Zilliz Cloud Pipeline index from a sequence of documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        documents: a sequence of llamaindex documents.</span>
<span class="sd">        pipeline_ids (dict=None): A dictionary of pipeline ids for INGESTION, SEARCH, DELETION. Defaults to None.</span>
<span class="sd">        api_key (str): Zilliz Cloud's API Key.</span>
<span class="sd">        metadata (Dict=None): A dictionary of metadata. Defaults to None. The key must be string and the value must be a string, float, integer, or boolean.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An initialized ZillizCloudPipelineIndex</span>

<span class="sd">    Example:</span>
<span class="sd">        &gt;&gt;&gt; from llama_index.indices import ZillizCloudPipelineIndex</span>
<span class="sd">        &gt;&gt;&gt; api_key = "{YOUR_ZILLIZ_CLOUD_API_KEY}"</span>
<span class="sd">        &gt;&gt;&gt; pipeline_ids = ZillizCloudPipelineIndex.create_pipelines(</span>
<span class="sd">        &gt;&gt;&gt;     project_id="{YOUR_ZILLIZ_PROJECT_ID}",</span>
<span class="sd">        &gt;&gt;&gt;     cluster_id="{YOUR_ZILLIZ_CLUSTER_ID}",</span>
<span class="sd">        &gt;&gt;&gt;     api_key=api_key,</span>
<span class="sd">        &gt;&gt;&gt;     data_type="text"</span>
<span class="sd">        &gt;&gt;&gt; )</span>
<span class="sd">        &gt;&gt;&gt; ZillizCloudPipelineIndex.from_documents(</span>
<span class="sd">        &gt;&gt;&gt;     documents=my_documents,</span>
<span class="sd">        &gt;&gt;&gt;     pipeline_ids=pipeline_ids,</span>
<span class="sd">        &gt;&gt;&gt;     api_key=api_key</span>
<span class="sd">        &gt;&gt;&gt; )</span>
<span class="sd">    """</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">index</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">pipeline_ids</span><span class="o">=</span><span class="n">pipeline_ids</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">index</span><span class="o">.</span><span class="n">_insert</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"Failed to build managed index given documents:</span><span class="se">\n</span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">index</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vertexai](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/)
