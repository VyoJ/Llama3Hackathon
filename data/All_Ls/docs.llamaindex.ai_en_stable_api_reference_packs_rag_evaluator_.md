Title: Rag evaluator - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/

Markdown Content:
Rag evaluator - LlamaIndex


RagEvaluatorPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/#llama_index.packs.rag_evaluator.RagEvaluatorPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

A pack for performing evaluation with your own RAG pipeline.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.query_engine.BaseQueryEngine")` | 
The RAG pipeline to evaluate.



 | _required_ |
| `rag_dataset` | `[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.BaseLlamaDataset")` | 

The BaseLlamaDataset to evaluate on.



 | _required_ |
| `judge_llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.LLM")]` | 

The LLM to use as the evaluator.



 | `None` |

Source code in `llama-index-packs/llama-index-packs-rag-evaluator/llama_index/packs/rag_evaluator/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 33</span>
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
<span class="normal">456</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RagEvaluatorPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A pack for performing evaluation with your own RAG pipeline.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine: The RAG pipeline to evaluate.</span>
<span class="sd">        rag_dataset: The BaseLlamaDataset to evaluate on.</span>
<span class="sd">        judge_llm: The LLM to use as the evaluator.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">rag_dataset</span><span class="p">:</span> <span class="n">BaseLlamaDataset</span><span class="p">,</span>
        <span class="n">judge_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">result_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span> <span class="o">=</span> <span class="n">rag_dataset</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">judge_llm</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">judge_llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4-1106-preview"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">judge_llm</span><span class="p">,</span> <span class="n">LLM</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">judge_llm</span> <span class="o">=</span> <span class="n">judge_llm</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">embed_model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">evals</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"correctness"</span><span class="p">:</span> <span class="p">[],</span>
            <span class="s2">"relevancy"</span><span class="p">:</span> <span class="p">[],</span>
            <span class="s2">"faithfulness"</span><span class="p">:</span> <span class="p">[],</span>
            <span class="s2">"context_similarity"</span><span class="p">:</span> <span class="p">[],</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">eval_queue</span> <span class="o">=</span> <span class="n">deque</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">)))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">result_path</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">result_path</span> <span class="o">=</span> <span class="n">Path</span><span class="o">.</span><span class="n">cwd</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">result_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">result_path</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_path</span><span class="o">.</span><span class="n">is_absolute</span><span class="p">():</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">result_path</span> <span class="o">=</span> <span class="n">Path</span><span class="o">.</span><span class="n">cwd</span><span class="p">()</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_path</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result_path</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result_path</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_amake_predictions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Async make predictions with query engine."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">:</span> <span class="n">BaseLlamaPredictionDataset</span> <span class="o">=</span> <span class="p">(</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">amake_predictions_with</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_make_predictions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Sync make predictions with query engine."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">:</span> <span class="n">BaseLlamaPredictionDataset</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">make_predictions_with</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_prepare_judges</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Construct the evaluators."""</span>
        <span class="n">judges</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">judges</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]</span> <span class="o">=</span> <span class="n">CorrectnessEvaluator</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">judge_llm</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">judges</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]</span> <span class="o">=</span> <span class="n">RelevancyEvaluator</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">judge_llm</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">judges</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]</span> <span class="o">=</span> <span class="n">FaithfulnessEvaluator</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">judge_llm</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">judges</span><span class="p">[</span><span class="s2">"semantic_similarity"</span><span class="p">]</span> <span class="o">=</span> <span class="n">SemanticSimilarityEvaluator</span><span class="p">(</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">judges</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_areturn_null_eval_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""A dummy async method that returns None.</span>

<span class="sd">        NOTE: this is used to handle case when creating async tasks for evaluating</span>
<span class="sd">        predictions where contexts do not exist.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_return_null_eval_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""A dummy async method that returns None.</span>

<span class="sd">        NOTE: this is used to handle case when creating async tasks for evaluating</span>
<span class="sd">        predictions where contexts do not exist.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_async_evaluate_example_prediction_tasks</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">judges</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">prediction</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Collect the co-routines."""</span>
        <span class="n">correctness_task</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">reference_answer</span><span class="p">,</span>
            <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">relevancy_task</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">faithfulness_task</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">example</span><span class="o">.</span><span class="n">reference_contexts</span> <span class="ow">and</span> <span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">:</span>
            <span class="n">semantic_similarity_task</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"semantic_similarity"</span><span class="p">]</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">),</span>
                <span class="n">reference</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">reference_contexts</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">semantic_similarity_task</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_areturn_null_eval_result</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="n">correctness_task</span><span class="p">,</span>
            <span class="n">relevancy_task</span><span class="p">,</span>
            <span class="n">faithfulness_task</span><span class="p">,</span>
            <span class="n">semantic_similarity_task</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_evaluate_example_prediction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">judges</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">prediction</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Collect the co-routines."""</span>
        <span class="n">correctness_result</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">reference_answer</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">relevancy_result</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">faithfulness_result</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">example</span><span class="o">.</span><span class="n">reference_contexts</span> <span class="ow">and</span> <span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">:</span>
            <span class="n">semantic_similarity_result</span> <span class="o">=</span> <span class="n">judges</span><span class="p">[</span><span class="s2">"semantic_similarity"</span><span class="p">]</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prediction</span><span class="o">.</span><span class="n">contexts</span><span class="p">),</span>
                <span class="n">reference</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">reference_contexts</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">semantic_similarity_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_return_null_eval_result</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="n">correctness_result</span><span class="p">,</span>
            <span class="n">relevancy_result</span><span class="p">,</span>
            <span class="n">faithfulness_result</span><span class="p">,</span>
            <span class="n">semantic_similarity_result</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_save_evaluations</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Save evaluation json object."""</span>
        <span class="c1"># saving evaluations</span>
        <span class="n">evaluations_objects</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"context_similarity"</span><span class="p">:</span> <span class="p">[</span><span class="n">e</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"context_similarity"</span><span class="p">]],</span>
            <span class="s2">"correctness"</span><span class="p">:</span> <span class="p">[</span><span class="n">e</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]],</span>
            <span class="s2">"faithfulness"</span><span class="p">:</span> <span class="p">[</span><span class="n">e</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]],</span>
            <span class="s2">"relevancy"</span><span class="p">:</span> <span class="p">[</span><span class="n">e</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]],</span>
        <span class="p">}</span>

        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span>
            <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result_path</span><span class="p">,</span> <span class="s2">"_evaluations.json"</span><span class="p">),</span> <span class="s2">"w"</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">json_file</span><span class="p">:</span>
            <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">evaluations_objects</span><span class="p">,</span> <span class="n">json_file</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_prepare_and_save_benchmark_results</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Get mean score across all of the evaluated examples-predictions."""</span>
        <span class="n">_</span><span class="p">,</span> <span class="n">mean_correctness_df</span> <span class="o">=</span> <span class="n">get_eval_results_df</span><span class="p">(</span>
            <span class="p">[</span><span class="s2">"base_rag"</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">],</span>
            <span class="n">metric</span><span class="o">=</span><span class="s2">"correctness"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">_</span><span class="p">,</span> <span class="n">mean_relevancy_df</span> <span class="o">=</span> <span class="n">get_eval_results_df</span><span class="p">(</span>
            <span class="p">[</span><span class="s2">"base_rag"</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">],</span>
            <span class="n">metric</span><span class="o">=</span><span class="s2">"relevancy"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">_</span><span class="p">,</span> <span class="n">mean_faithfulness_df</span> <span class="o">=</span> <span class="n">get_eval_results_df</span><span class="p">(</span>
            <span class="p">[</span><span class="s2">"base_rag"</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">],</span>
            <span class="n">metric</span><span class="o">=</span><span class="s2">"faithfulness"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">_</span><span class="p">,</span> <span class="n">mean_context_similarity_df</span> <span class="o">=</span> <span class="n">get_eval_results_df</span><span class="p">(</span>
            <span class="p">[</span><span class="s2">"base_rag"</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"context_similarity"</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"context_similarity"</span><span class="p">],</span>
            <span class="n">metric</span><span class="o">=</span><span class="s2">"context_similarity"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">mean_scores_df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="n">mean_correctness_df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(),</span>
                <span class="n">mean_relevancy_df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(),</span>
                <span class="n">mean_faithfulness_df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(),</span>
                <span class="n">mean_context_similarity_df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(),</span>
            <span class="p">],</span>
            <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="n">ignore_index</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">mean_scores_df</span> <span class="o">=</span> <span class="n">mean_scores_df</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s2">"index"</span><span class="p">)</span>
        <span class="n">mean_scores_df</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">mean_scores_df</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">set_names</span><span class="p">([</span><span class="s2">"metrics"</span><span class="p">])</span>

        <span class="c1"># save mean_scores_df</span>
        <span class="n">mean_scores_df</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result_path</span><span class="p">,</span> <span class="s2">"benchmark.csv"</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">mean_scores_df</span>

    <span class="k">def</span> <span class="nf">_make_evaluations</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Sync make evaluations."""</span>
        <span class="n">judges</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_judges</span><span class="p">()</span>

        <span class="n">start_ix</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_queue</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples_and_preds</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="o">.</span><span class="n">predictions</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">start_position</span><span class="o">=</span><span class="n">start_ix</span><span class="p">,</span>
        <span class="p">):</span>
            <span class="n">examples</span><span class="p">,</span> <span class="n">predictions</span> <span class="o">=</span> <span class="n">batch</span>
            <span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">prediction</span> <span class="ow">in</span> <span class="n">tqdm</span><span class="o">.</span><span class="n">tqdm</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">examples</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)):</span>
                <span class="p">(</span>
                    <span class="n">correctness_result</span><span class="p">,</span>
                    <span class="n">relevancy_result</span><span class="p">,</span>
                    <span class="n">faithfulness_result</span><span class="p">,</span>
                    <span class="n">semantic_similarity_result</span><span class="p">,</span>
                <span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluate_example_prediction</span><span class="p">(</span>
                    <span class="n">judges</span><span class="o">=</span><span class="n">judges</span><span class="p">,</span> <span class="n">example</span><span class="o">=</span><span class="n">example</span><span class="p">,</span> <span class="n">prediction</span><span class="o">=</span><span class="n">prediction</span>
                <span class="p">)</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">correctness_result</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">relevancy_result</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">faithfulness_result</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"context_similarity"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">semantic_similarity_result</span><span class="p">)</span>
            <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_save_evaluations</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_and_save_benchmark_results</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_batch_examples_and_preds</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">examples</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">start_position</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Batches examples and predictions with a given batch_size."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">predictions</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">ndx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start_position</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
            <span class="k">yield</span> <span class="n">examples</span><span class="p">[</span>
                <span class="n">ndx</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span><span class="n">ndx</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span><span class="p">)</span>
            <span class="p">],</span> <span class="n">predictions</span><span class="p">[</span><span class="n">ndx</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span><span class="n">ndx</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span><span class="p">)]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_amake_evaluations</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Async make evaluations."""</span>
        <span class="n">judges</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_judges</span><span class="p">()</span>

        <span class="n">ix</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_queue</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">batch_iterator</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples_and_preds</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rag_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="o">.</span><span class="n">predictions</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">start_position</span><span class="o">=</span><span class="n">ix</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">total_batches</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">-</span> <span class="n">ix</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">/</span> <span class="n">batch_size</span> <span class="o">+</span> <span class="p">(</span>
            <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">-</span> <span class="n">ix</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="n">batch_size</span> <span class="o">!=</span> <span class="mi">0</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">:</span>
            <span class="n">batch_iterator</span> <span class="o">=</span> <span class="n">tqdm_asyncio</span><span class="p">(</span>
                <span class="n">batch_iterator</span><span class="p">,</span>
                <span class="n">desc</span><span class="o">=</span><span class="s2">"Batch processing of evaluations"</span><span class="p">,</span>
                <span class="n">total</span><span class="o">=</span><span class="n">total_batches</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="n">batch_iterator</span><span class="p">:</span>
            <span class="n">examples</span><span class="p">,</span> <span class="n">predictions</span> <span class="o">=</span> <span class="n">batch</span>
            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">prediction</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">examples</span><span class="p">,</span> <span class="n">predictions</span><span class="p">):</span>
                <span class="p">(</span>
                    <span class="n">correctness_task</span><span class="p">,</span>
                    <span class="n">relevancy_task</span><span class="p">,</span>
                    <span class="n">faithfulness_task</span><span class="p">,</span>
                    <span class="n">semantic_similarity_task</span><span class="p">,</span>
                <span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_async_evaluate_example_prediction_tasks</span><span class="p">(</span>
                    <span class="n">judges</span><span class="o">=</span><span class="n">judges</span><span class="p">,</span>
                    <span class="n">example</span><span class="o">=</span><span class="n">example</span><span class="p">,</span>
                    <span class="n">prediction</span><span class="o">=</span><span class="n">prediction</span><span class="p">,</span>
                    <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="n">tasks</span> <span class="o">+=</span> <span class="p">[</span>
                    <span class="n">correctness_task</span><span class="p">,</span>
                    <span class="n">relevancy_task</span><span class="p">,</span>
                    <span class="n">faithfulness_task</span><span class="p">,</span>
                    <span class="n">semantic_similarity_task</span><span class="p">,</span>
                <span class="p">]</span>

            <span class="c1"># do this in batches to avoid RateLimitError</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">eval_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
            <span class="k">except</span> <span class="n">RateLimitError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">:</span>
                    <span class="n">batch_iterator</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"You've hit rate limits on your OpenAI subscription. This"</span>
                    <span class="s2">" `RagEvaluatorPack` maintains state of evaluations. Simply"</span>
                    <span class="s2">" re-invoke .arun() in order to continue from where you left"</span>
                    <span class="s2">" off."</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
            <span class="c1"># store in memory</span>
            <span class="c1"># since final result of eval_results respects order of inputs</span>
            <span class="c1"># just take appropriate slices</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"correctness"</span><span class="p">]</span> <span class="o">+=</span> <span class="n">eval_results</span><span class="p">[::</span><span class="mi">4</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"relevancy"</span><span class="p">]</span> <span class="o">+=</span> <span class="n">eval_results</span><span class="p">[</span><span class="mi">1</span><span class="p">::</span><span class="mi">4</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"faithfulness"</span><span class="p">]</span> <span class="o">+=</span> <span class="n">eval_results</span><span class="p">[</span><span class="mi">2</span><span class="p">::</span><span class="mi">4</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">evals</span><span class="p">[</span><span class="s2">"context_similarity"</span><span class="p">]</span> <span class="o">+=</span> <span class="n">eval_results</span><span class="p">[</span><span class="mi">3</span><span class="p">::</span><span class="mi">4</span><span class="p">]</span>
            <span class="c1"># update queue</span>
            <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">batch_size</span><span class="p">):</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_queue</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">eval_queue</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
            <span class="n">ix</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">:</span>
                <span class="n">batch_iterator</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
                <span class="n">batch_iterator</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_save_evaluations</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_and_save_benchmark_results</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">batch_size</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"You've set a large batch_size (&gt;10). If using OpenAI GPT-4 as "</span>
                <span class="s2">" `judge_llm` (which is the default judge_llm),"</span>
                <span class="s2">" you may experience a RateLimitError. Previous successful eval "</span>
                <span class="s2">" responses are cached per batch. So hitting a RateLimitError"</span>
                <span class="s2">" would mean you'd lose all of the current batches successful "</span>
                <span class="s2">" GPT-4 calls."</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_make_predictions</span><span class="p">(</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="c1"># evaluate predictions</span>
        <span class="n">eval_sleep_time_in_seconds</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sleep_time_in_seconds</span> <span class="o">*</span> <span class="mi">2</span>
        <span class="p">)</span>  <span class="c1"># since we make 3 evaluator llm calls</span>
        <span class="n">eval_batch_size</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">batch_size</span> <span class="o">/</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_evaluations</span><span class="p">(</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">eval_batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">eval_sleep_time_in_seconds</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">batch_size</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"You've set a large batch_size (&gt;10). If using OpenAI GPT-4 as "</span>
                <span class="s2">" `judge_llm` (which is the default judge_llm),"</span>
                <span class="s2">" you may experience a RateLimitError. Previous successful eval "</span>
                <span class="s2">" responses are cached per batch. So hitting a RateLimitError"</span>
                <span class="s2">" would mean you'd lose all of the current batches successful "</span>
                <span class="s2">" GPT-4 calls."</span>
            <span class="p">)</span>

        <span class="c1"># make predictions</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_amake_predictions</span><span class="p">(</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="c1"># evaluate predictions</span>
        <span class="n">eval_sleep_time_in_seconds</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sleep_time_in_seconds</span> <span class="o">*</span> <span class="mi">2</span>
        <span class="p">)</span>  <span class="c1"># since we make 3 evaluator llm calls and default is gpt-4</span>
        <span class="c1"># which is heavily rate-limited</span>
        <span class="n">eval_batch_size</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">batch_size</span> <span class="o">/</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_amake_evaluations</span><span class="p">(</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">eval_batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">eval_sleep_time_in_seconds</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Rag cli local](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/)[Next Rag fusion query pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/)
