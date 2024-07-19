Title: Diff private simple dataset - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/

Markdown Content:
Diff private simple dataset - LlamaIndex


DiffPrivateSimpleDatasetPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/#llama_index.packs.diff_private_simple_dataset.DiffPrivateSimpleDatasetPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

A pack for creating differentially private simple llama-dataset.

Source code in `llama-index-packs/llama-index-packs-diff-private-simple-dataset/llama_index/packs/diff_private_simple_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 65</span>
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
<span class="normal">501</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DiffPrivateSimpleDatasetPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A pack for creating differentially private simple llama-dataset."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>  <span class="c1"># currently only supports OpenAI completion LLMs</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">prompt_bundle</span><span class="p">:</span> <span class="n">PromptBundle</span><span class="p">,</span>
        <span class="n">simple_dataset</span><span class="p">:</span> <span class="n">LabelledSimpleDataset</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">sephamore_counter_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">cache_checkpoints</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span> <span class="o">=</span> <span class="n">prompt_bundle</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">simple_dataset</span> <span class="o">=</span> <span class="n">simple_dataset</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">simple_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">labels</span> <span class="o">=</span> <span class="nb">list</span><span class="p">({</span><span class="n">el</span><span class="o">.</span><span class="n">reference_label</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_dataset</span><span class="p">[:]})</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">sleep_time_in_seconds</span> <span class="o">=</span> <span class="n">sleep_time_in_seconds</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_semaphore</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="n">sephamore_counter_size</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span> <span class="o">=</span> <span class="n">batch_size</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cache_checkpoints</span> <span class="o">=</span> <span class="n">cache_checkpoints</span>

    <span class="k">def</span> <span class="nf">sigma_to_eps</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sigma</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span>
        <span class="n">mechanism</span><span class="p">:</span> <span class="n">PrivacyMechanism</span><span class="p">,</span>
        <span class="n">size</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">max_token_cnt</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">max_self_compositions</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span>
        <span class="n">eps_error</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.01</span><span class="p">,</span>
        <span class="n">delta_error</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1e-10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the epsilon value given a sigma.</span>

<span class="sd">        Args:</span>
<span class="sd">            sigma (float): The parameter associated with noise mechanism.</span>
<span class="sd">            mechanism (PrivacyMechanism): Noise mechanism.</span>
<span class="sd">            size (int): Number of samples to be generated.</span>
<span class="sd">            max_token_cnt (int): Number of tokens generated per sample.</span>
<span class="sd">            max_self_compositions (int, optional): PRV algorithm parameter. Defaults to 1000.</span>
<span class="sd">            eps_error (float, optional): PRV algorithm parameter. Defaults to 0.01.</span>
<span class="sd">            delta_error (float, optional): PRV algorithm parameter. Defaults to 1e-10.</span>

<span class="sd">        Returns:</span>
<span class="sd">            float: The epsilon value.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">max_token_cnt</span> <span class="o">&gt;</span> <span class="n">max_self_compositions</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"`max_token_cnt` cannot be greater than `max_self_composition`."</span>
            <span class="p">)</span>

        <span class="n">sample_rate</span> <span class="o">=</span> <span class="n">size</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span>
        <span class="k">if</span> <span class="n">mechanism</span> <span class="o"></span> <span class="n">PrivacyMechanism</span><span class="o">.</span><span class="n">EXPONENTIAL</span><span class="p">:</span>
            <span class="n">sigma_bar</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">sample_rate</span> <span class="o">*</span> <span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">sigma</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
            <span class="n">prv_0</span> <span class="o">=</span> <span class="n">PureDPMechanism</span><span class="p">(</span><span class="n">eps</span><span class="o">=</span><span class="n">sigma_bar</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Invalid value for mechanism entered."</span>
                <span class="s2">" Please use either 'gaussian' or 'exponential'."</span>
            <span class="p">)</span>
        <span class="n">accountant</span> <span class="o">=</span> <span class="n">PRVAccountant</span><span class="p">(</span>
            <span class="n">prvs</span><span class="o">=</span><span class="p">[</span>
                <span class="n">prv_0</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">max_self_compositions</span><span class="o">=</span><span class="p">[</span><span class="n">max_self_compositions</span><span class="p">],</span>
            <span class="n">eps_error</span><span class="o">=</span><span class="n">eps_error</span><span class="p">,</span>
            <span class="n">delta_error</span><span class="o">=</span><span class="n">delta_error</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">_eps_low</span><span class="p">,</span> <span class="n">eps_est</span><span class="p">,</span> <span class="n">_eps_up</span> <span class="o">=</span> <span class="n">accountant</span><span class="o">.</span><span class="n">compute_epsilon</span><span class="p">(</span>
            <span class="n">delta</span><span class="o">=</span><span class="mi">1</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span><span class="p">,</span> <span class="n">num_self_compositions</span><span class="o">=</span><span class="p">[</span><span class="n">max_token_cnt</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">eps_est</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_worker</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">job</span><span class="p">:</span> <span class="n">Coroutine</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_semaphore</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
            <span class="k">return</span> <span class="k">await</span> <span class="n">job</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">_filter_dataset_by_label</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LabelledSimpleDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Filter simple_dataset by label."""</span>
        <span class="k">if</span> <span class="n">label</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"There are no examples with `label` in the associated `simple_dataset`."</span>
            <span class="p">)</span>
        <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_dataset</span><span class="p">[:]</span> <span class="k">if</span> <span class="n">el</span><span class="o">.</span><span class="n">reference_label</span> <span class="o"></span> <span class="n">num_samples_per_split</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Not able to create disjoint sets with current values of `num_splits` and `num_samples_per_split`."</span>
                <span class="p">)</span>
            <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="n">dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">[</span><span class="n">ix</span><span class="p">]</span> <span class="k">for</span> <span class="n">ix</span> <span class="ow">in</span> <span class="n">sample</span><span class="p">]</span>
            <span class="n">splits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">LabelledSimpleDataset</span><span class="p">(</span><span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">splits</span>

    <span class="k">def</span> <span class="nf">_get_public_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">synthetic_example</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">label</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get completion prompt for token universe."""</span>
        <span class="k">return</span> <span class="n">zero_shot_completion_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">synthetic_text</span><span class="o">=</span><span class="n">synthetic_example</span><span class="p">,</span>
            <span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
            <span class="n">instruction</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">instruction</span><span class="p">,</span>
            <span class="n">label_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">label_heading</span><span class="p">,</span>
            <span class="n">text_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">text_heading</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_private_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">split</span><span class="p">:</span> <span class="n">LabelledSimpleDataset</span><span class="p">,</span>
        <span class="n">synthetic_example</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">label</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt for completion endpoint."""</span>
        <span class="n">single_templates</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">single_example_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">label_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">label_heading</span><span class="p">,</span>
                <span class="n">text_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">text_heading</span><span class="p">,</span>
                <span class="n">example_label</span><span class="o">=</span><span class="n">x</span><span class="o">.</span><span class="n">reference_label</span><span class="p">,</span>
                <span class="n">example_text</span><span class="o">=</span><span class="n">x</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">split</span><span class="o">.</span><span class="n">examples</span>
        <span class="p">]</span>

        <span class="n">few_shot_examples</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">single_templates</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">few_shot_completion_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">instruction</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">instruction</span><span class="p">,</span>
            <span class="n">label_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">label_heading</span><span class="p">,</span>
            <span class="n">text_heading</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_bundle</span><span class="o">.</span><span class="n">text_heading</span><span class="p">,</span>
            <span class="n">few_shot_examples</span><span class="o">=</span><span class="n">few_shot_examples</span><span class="p">,</span>
            <span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
            <span class="n">synthetic_text</span><span class="o">=</span><span class="n">synthetic_example</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_normalize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">split_probs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">],</span> <span class="n">token_universe_proba</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Normalize a probability distribution over tokens to become a valid probability distribution."""</span>
        <span class="n">scale</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">proba</span> <span class="k">for</span> <span class="n">proba</span> <span class="ow">in</span> <span class="n">split_probs</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">scale</span> <span class="o"></span> <span class="n">PrivacyMechanism</span><span class="o">.</span><span class="n">GAUSSIAN</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">noise_rng</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">sigma</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">size</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">mechanism</span> <span class="o"></span> <span class="n">PrivacyMechanism</span><span class="o">.</span><span class="n">GAUSSIAN</span><span class="p">:</span>
        <span class="n">prv_0</span> <span class="o">=</span> <span class="n">PoissonSubsampledGaussianMechanism</span><span class="p">(</span>
            <span class="n">noise_multiplier</span><span class="o">=</span><span class="n">sigma</span><span class="p">,</span> <span class="n">sampling_probability</span><span class="o">=</span><span class="n">sample_rate</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">mechanism</span> <span class="o">==</span> <span class="n">PrivacyMechanism</span><span class="o">.</span><span class="n">EXPONENTIAL</span><span class="p">:</span>
        <span class="n">sigma_bar</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">sample_rate</span> <span class="o">*</span> <span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">sigma</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
        <span class="n">prv_0</span> <span class="o">=</span> <span class="n">PureDPMechanism</span><span class="p">(</span><span class="n">eps</span><span class="o">=</span><span class="n">sigma_bar</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Invalid value for mechanism entered."</span>
            <span class="s2">" Please use either 'gaussian' or 'exponential'."</span>
        <span class="p">)</span>
    <span class="n">accountant</span> <span class="o">=</span> <span class="n">PRVAccountant</span><span class="p">(</span>
        <span class="n">prvs</span><span class="o">=</span><span class="p">[</span>
            <span class="n">prv_0</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">max_self_compositions</span><span class="o">=</span><span class="p">[</span><span class="n">max_self_compositions</span><span class="p">],</span>
        <span class="n">eps_error</span><span class="o">=</span><span class="n">eps_error</span><span class="p">,</span>
        <span class="n">delta_error</span><span class="o">=</span><span class="n">delta_error</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">_eps_low</span><span class="p">,</span> <span class="n">eps_est</span><span class="p">,</span> <span class="n">_eps_up</span> <span class="o">=</span> <span class="n">accountant</span><span class="o">.</span><span class="n">compute_epsilon</span><span class="p">(</span>
        <span class="n">delta</span><span class="o">=</span><span class="mi">1</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span><span class="p">,</span> <span class="n">num_self_compositions</span><span class="o">=</span><span class="p">[</span><span class="n">max_token_cnt</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">eps_est</span>
</code></pre></div></td></tr></tbody></table>

### generate\_dp\_synthetic\_example [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/#llama_index.packs.diff_private_simple_dataset.DiffPrivateSimpleDatasetPack.generate_dp_synthetic_example "Permanent link")

```
generate_dp_synthetic_example(label: str, t_max: int = 1, sigma: float = 0.5, num_splits: int = 5, num_samples_per_split: int = 1) -> LabelledSimpleDataExample
```

Generates a differentially private synthetic example.

Source code in `llama-index-packs/llama-index-packs-diff-private-simple-dataset/llama_index/packs/diff_private_simple_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">299</span>
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
<span class="normal">317</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">generate_dp_synthetic_example</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">label</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">t_max</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">sigma</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
    <span class="n">num_splits</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">num_samples_per_split</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LabelledSimpleDataExample</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generates a differentially private synthetic example."""</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agenerate_dp_synthetic_example</span><span class="p">(</span>
            <span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
            <span class="n">t_max</span><span class="o">=</span><span class="n">t_max</span><span class="p">,</span>
            <span class="n">sigma</span><span class="o">=</span><span class="n">sigma</span><span class="p">,</span>
            <span class="n">num_splits</span><span class="o">=</span><span class="n">num_splits</span><span class="p">,</span>
            <span class="n">num_samples_per_split</span><span class="o">=</span><span class="n">num_samples_per_split</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### agenerate\_dp\_synthetic\_example `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/#llama_index.packs.diff_private_simple_dataset.DiffPrivateSimpleDatasetPack.agenerate_dp_synthetic_example "Permanent link")

```
agenerate_dp_synthetic_example(label: str, t_max: int = 1, sigma: float = 0.5, num_splits: int = 5, num_samples_per_split: int = 1) -> LabelledSimpleDataExample
```

Generates a differentially private synthetic example.

Source code in `llama-index-packs/llama-index-packs-diff-private-simple-dataset/llama_index/packs/diff_private_simple_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">319</span>
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
<span class="normal">406</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_dp_synthetic_example</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">label</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">t_max</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">sigma</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
    <span class="n">num_splits</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">num_samples_per_split</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LabelledSimpleDataExample</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generates a differentially private synthetic example."""</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">SyntheticExampleStartEvent</span><span class="p">())</span>
    <span class="n">synthetic_example</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="n">iterator</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">t_max</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">:</span>
        <span class="n">iterator</span> <span class="o">=</span> <span class="n">tqdm</span><span class="o">.</span><span class="n">tqdm</span><span class="p">(</span><span class="n">iterator</span><span class="p">,</span> <span class="n">position</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">leave</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">iterator</span><span class="p">:</span>
        <span class="n">token_universe_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_public_prompt</span><span class="p">(</span>
            <span class="n">synthetic_example</span><span class="o">=</span><span class="n">synthetic_example</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="n">label</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_worker</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span><span class="n">token_universe_prompt</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">token_universe_probas</span> <span class="o">=</span> <span class="p">{</span>
                <span class="n">el</span><span class="o">.</span><span class="n">token</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">el</span><span class="o">.</span><span class="n">logprob</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">logprobs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># only for next immediate token</span>
            <span class="p">}</span>
        <span class="k">except</span> <span class="ne">IndexError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">continue</span>  <span class="c1"># try again in next iteration</span>

        <span class="c1"># filter dataset by label</span>
        <span class="n">filtered_simple_dataset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_dataset_by_label</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">)</span>

        <span class="c1"># split the private dataset</span>
        <span class="n">disjoint_splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_dataset</span><span class="p">(</span>
            <span class="n">dataset</span><span class="o">=</span><span class="n">filtered_simple_dataset</span><span class="p">,</span>
            <span class="n">num_splits</span><span class="o">=</span><span class="n">num_splits</span><span class="p">,</span>
            <span class="n">num_samples_per_split</span><span class="o">=</span><span class="n">num_samples_per_split</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># generate next token probability distributions per split</span>
        <span class="n">split_tasks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">split</span> <span class="ow">in</span> <span class="n">disjoint_splits</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_private_prompt</span><span class="p">(</span><span class="n">split</span><span class="p">,</span> <span class="n">synthetic_example</span><span class="p">,</span> <span class="n">label</span><span class="p">)</span>
            <span class="n">split_tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_async_worker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span><span class="n">prompt</span><span class="p">)))</span>

        <span class="n">split_responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CompletionResponse</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="o">*</span><span class="n">split_tasks</span>
        <span class="p">)</span>

        <span class="c1"># get and normalized next-token probas per split</span>
        <span class="n">splits</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_extract_and_normalize_next_token_probas</span><span class="p">(</span>
                <span class="n">response</span><span class="p">,</span> <span class="n">token_universe_probas</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="n">split_responses</span>
        <span class="p">]</span>

        <span class="c1"># noisy aggrergation</span>
        <span class="n">sigma_calib</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="n">num_splits</span> <span class="o">*</span> <span class="n">sigma</span>
        <span class="n">noise_array</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_noise</span><span class="p">(</span>
            <span class="n">sigma</span><span class="o">=</span><span class="n">sigma_calib</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">token_universe_probas</span><span class="p">),</span> <span class="n">mechanism</span><span class="o">=</span><span class="s2">"gaussian"</span>
        <span class="p">)</span>
        <span class="n">merged_probas</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_merge_probas</span><span class="p">(</span><span class="n">splits</span><span class="p">)</span>
        <span class="n">noisy_probs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_noise</span><span class="p">(</span><span class="n">merged_probas</span><span class="p">,</span> <span class="n">noise_array</span><span class="p">)</span>

        <span class="c1"># next token</span>
        <span class="n">next_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mode_of_distribution</span><span class="p">(</span><span class="n">noisy_probs</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">next_token</span> <span class="ow">in</span> <span class="n">STOP_TOKENS</span><span class="p">:</span>
            <span class="k">break</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">synthetic_example</span> <span class="o">+=</span> <span class="n">next_token</span>

    <span class="c1"># synthetic example remove [RESULT]</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">synthetic_example</span> <span class="o">=</span> <span class="n">synthetic_example</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"[RESULT]"</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">synthetic_example</span> <span class="o">=</span> <span class="n">synthetic_example</span>

    <span class="n">simple_example</span> <span class="o">=</span> <span class="n">LabelledSimpleDataExample</span><span class="p">(</span>
        <span class="n">reference_label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
        <span class="n">text</span><span class="o">=</span><span class="n">synthetic_example</span><span class="p">,</span>
        <span class="n">text_by</span><span class="o">=</span><span class="n">CreatedBy</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="n">CreatedByType</span><span class="o">.</span><span class="n">AI</span><span class="p">,</span> <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">SyntheticExampleEndEvent</span><span class="p">())</span>
    <span class="k">return</span> <span class="n">simple_example</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/#llama_index.packs.diff_private_simple_dataset.DiffPrivateSimpleDatasetPack.run "Permanent link")

```
run(sizes: Union[int, Dict[str, int]], t_max: int = 1, sigma: float = 0.5, num_splits: int = 5, num_samples_per_split: int = 1) -> LabelledSimpleDataset
```

Main run method.

Source code in `llama-index-packs/llama-index-packs-diff-private-simple-dataset/llama_index/packs/diff_private_simple_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">408</span>
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
<span class="normal">448</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">sizes</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span>
    <span class="n">t_max</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">sigma</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
    <span class="n">num_splits</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">num_samples_per_split</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LabelledSimpleDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Main run method."""</span>
    <span class="k">if</span> <span class="n">num_samples_per_split</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"`num_samples_per_split` must be an integer greater than 1."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sizes</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
        <span class="n">sizes_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">d</span><span class="p">:</span> <span class="n">sizes</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">}</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sizes</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="n">sizes_dict</span> <span class="o">=</span> <span class="n">sizes</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span>
            <span class="s2">"Invalid type of `sizes`. Must be either an `int` or `dict`."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span><span class="n">c</span> <span class="ow">in</span> <span class="n">sizes_dict</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Not all labels have sizes."</span><span class="p">)</span>

    <span class="n">examples</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">:</span>
        <span class="n">size</span> <span class="o">=</span> <span class="n">sizes_dict</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">size</span><span class="p">):</span>
            <span class="n">example</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_dp_synthetic_example</span><span class="p">(</span>
                <span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
                <span class="n">t_max</span><span class="o">=</span><span class="n">t_max</span><span class="p">,</span>
                <span class="n">sigma</span><span class="o">=</span><span class="n">sigma</span><span class="p">,</span>
                <span class="n">num_splits</span><span class="o">=</span><span class="n">num_splits</span><span class="p">,</span>
                <span class="n">num_samples_per_split</span><span class="o">=</span><span class="n">num_samples_per_split</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">examples</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">example</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">LabelledSimpleDataset</span><span class="p">(</span><span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### arun `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/#llama_index.packs.diff_private_simple_dataset.DiffPrivateSimpleDatasetPack.arun "Permanent link")

```
arun(sizes: Dict[str, int], t_max: int = 1, sigma: float = 0.5, num_splits: int = 5, num_samples_per_split: int = 1) -> LabelledSimpleDataset
```

Main async run method.

Source code in `llama-index-packs/llama-index-packs-diff-private-simple-dataset/llama_index/packs/diff_private_simple_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">450</span>
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
<span class="normal">501</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">arun</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">sizes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">],</span>
    <span class="n">t_max</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">sigma</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
    <span class="n">num_splits</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">num_samples_per_split</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LabelledSimpleDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Main async run method."""</span>
    <span class="k">if</span> <span class="n">num_samples_per_split</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"`num_samples_per_split` must be an integer greater than 1."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sizes</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
        <span class="n">sizes_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">d</span><span class="p">:</span> <span class="n">sizes</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">}</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sizes</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="n">sizes_dict</span> <span class="o">=</span> <span class="n">sizes</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span>
            <span class="s2">"Invalid type of `sizes`. Must be either an `int` or `dict`."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span><span class="n">c</span> <span class="ow">in</span> <span class="n">sizes_dict</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Not all labels have sizes."</span><span class="p">)</span>

    <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">labels</span><span class="p">:</span>
        <span class="n">size</span> <span class="o">=</span> <span class="n">sizes_dict</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">size</span><span class="p">):</span>
            <span class="n">example_task</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agenerate_dp_synthetic_example</span><span class="p">(</span>
                <span class="n">label</span><span class="o">=</span><span class="n">label</span><span class="p">,</span>
                <span class="n">t_max</span><span class="o">=</span><span class="n">t_max</span><span class="p">,</span>
                <span class="n">sigma</span><span class="o">=</span><span class="n">sigma</span><span class="p">,</span>
                <span class="n">num_splits</span><span class="o">=</span><span class="n">num_splits</span><span class="p">,</span>
                <span class="n">num_samples_per_split</span><span class="o">=</span><span class="n">num_samples_per_split</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">example_task</span><span class="p">)</span>

    <span class="n">asyncio_runner</span> <span class="o">=</span> <span class="n">asyncio_module</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">)</span>

    <span class="c1"># run in batch</span>
    <span class="n">examples</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="n">_batch</span><span class="p">(</span><span class="n">tasks</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
        <span class="n">batch_examples</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio_runner</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">batch</span><span class="p">)</span>
        <span class="n">examples</span> <span class="o">+=</span> <span class="n">batch_examples</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache_checkpoints</span><span class="p">:</span>
            <span class="n">checkpoint</span> <span class="o">=</span> <span class="n">LabelledSimpleDataset</span><span class="p">(</span><span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">)</span>
            <span class="n">checkpoint</span><span class="o">.</span><span class="n">save_json</span><span class="p">(</span><span class="s2">"checkpoint.json"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">LabelledSimpleDataset</span><span class="p">(</span><span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dense x retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/)[Next Docugami kg rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/docugami_kg_rag/)
