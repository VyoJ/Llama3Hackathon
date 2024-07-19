Title: Wandb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/

Markdown Content:
Wandb - LlamaIndex


WandbCallbackHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`

Callback handler that logs events to wandb.

NOTE: this is a beta feature. The usage within our codebase, and the interface may change.

Use the `WandbCallbackHandler` to log trace events to wandb. This handler is useful for debugging and visualizing the trace events. It captures the payload of the events and logs them to wandb. The handler also tracks the start and end of events. This is particularly useful for debugging your LLM calls.

The `WandbCallbackHandler` can also be used to log the indices and graphs to wandb using the `persist_index` method. This will save the indexes as artifacts in wandb. The `load_storage_context` method can be used to load the indexes from wandb artifacts. This method will return a `StorageContext` object that can be used to build the index, using `load_index_from_storage`, `load_indices_from_storage` or `load_graph_from_storage` functions.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_starts_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 
list of event types to ignore when tracking event starts.



 | `None` |
| `event_ends_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

list of event types to ignore when tracking event ends.



 | `None` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 87</span>
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
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WandbCallbackHandler</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback handler that logs events to wandb.</span>

<span class="sd">    NOTE: this is a beta feature. The usage within our codebase, and the interface</span>
<span class="sd">    may change.</span>

<span class="sd">    Use the `WandbCallbackHandler` to log trace events to wandb. This handler is</span>
<span class="sd">    useful for debugging and visualizing the trace events. It captures the payload of</span>
<span class="sd">    the events and logs them to wandb. The handler also tracks the start and end of</span>
<span class="sd">    events. This is particularly useful for debugging your LLM calls.</span>

<span class="sd">    The `WandbCallbackHandler` can also be used to log the indices and graphs to wandb</span>
<span class="sd">    using the `persist_index` method. This will save the indexes as artifacts in wandb.</span>
<span class="sd">    The `load_storage_context` method can be used to load the indexes from wandb</span>
<span class="sd">    artifacts. This method will return a `StorageContext` object that can be used to</span>
<span class="sd">    build the index, using `load_index_from_storage`, `load_indices_from_storage` or</span>
<span class="sd">    `load_graph_from_storage` functions.</span>


<span class="sd">    Args:</span>
<span class="sd">        event_starts_to_ignore (Optional[List[CBEventType]]): list of event types to</span>
<span class="sd">            ignore when tracking event starts.</span>
<span class="sd">        event_ends_to_ignore (Optional[List[CBEventType]]): list of event types to</span>
<span class="sd">            ignore when tracking event ends.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">run_args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WandbRunArgs</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_starts_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_ends_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">wandb</span>
            <span class="kn">from</span> <span class="nn">wandb.sdk.data_types</span> <span class="kn">import</span> <span class="n">trace_tree</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span> <span class="o">=</span> <span class="n">wandb</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span> <span class="o">=</span> <span class="n">trace_tree</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"WandbCallbackHandler requires wandb. "</span>
                <span class="s2">"Please install it with `pip install wandb`."</span>
            <span class="p">)</span>

        <span class="kn">from</span> <span class="nn">llama_index.core.indices</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">ComposableGraph</span><span class="p">,</span>
            <span class="n">GPTEmptyIndex</span><span class="p">,</span>
            <span class="n">GPTKeywordTableIndex</span><span class="p">,</span>
            <span class="n">GPTRAKEKeywordTableIndex</span><span class="p">,</span>
            <span class="n">GPTSimpleKeywordTableIndex</span><span class="p">,</span>
            <span class="n">GPTSQLStructStoreIndex</span><span class="p">,</span>
            <span class="n">GPTTreeIndex</span><span class="p">,</span>
            <span class="n">GPTVectorStoreIndex</span><span class="p">,</span>
            <span class="n">SummaryIndex</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_IndexType</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">ComposableGraph</span><span class="p">,</span>
            <span class="n">GPTKeywordTableIndex</span><span class="p">,</span>
            <span class="n">GPTSimpleKeywordTableIndex</span><span class="p">,</span>
            <span class="n">GPTRAKEKeywordTableIndex</span><span class="p">,</span>
            <span class="n">SummaryIndex</span><span class="p">,</span>
            <span class="n">GPTEmptyIndex</span><span class="p">,</span>
            <span class="n">GPTTreeIndex</span><span class="p">,</span>
            <span class="n">GPTVectorStoreIndex</span><span class="p">,</span>
            <span class="n">GPTSQLStructStoreIndex</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_run_args</span> <span class="o">=</span> <span class="n">run_args</span>
        <span class="c1"># Check if a W&amp;B run is already initialized; if not, initialize one</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_run</span><span class="p">(</span><span class="n">should_print_url</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">))</span>  <span class="c1"># type: ignore[attr-defined]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_token_counter</span> <span class="o">=</span> <span class="n">TokenCounter</span><span class="p">(</span><span class="n">tokenizer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">)</span>

        <span class="n">event_starts_to_ignore</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">event_starts_to_ignore</span> <span class="k">if</span> <span class="n">event_starts_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>
        <span class="n">event_ends_to_ignore</span> <span class="o">=</span> <span class="n">event_ends_to_ignore</span> <span class="k">if</span> <span class="n">event_ends_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="n">event_starts_to_ignore</span><span class="p">,</span>
            <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="n">event_ends_to_ignore</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Store event start data by event type.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>
<span class="sd">            parent_id (str): parent event id.</span>

<span class="sd">        """</span>
        <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">event</span><span class="o">.</span><span class="n">id_</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Store event end data by event type.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>

<span class="sd">        """</span>
        <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Launch a trace."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="o">=</span> <span class="n">trace_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Ensure W&amp;B run is initialized</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_run</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">trace_map</span> <span class="ow">or</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>

        <span class="c1"># Log the trace map to wandb</span>
        <span class="c1"># We can control what trace ids we want to log here.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">log_trace_tree</span><span class="p">()</span>

        <span class="c1"># TODO (ayulockin): Log the LLM token counts to wandb when weave is ready</span>

    <span class="k">def</span> <span class="nf">log_trace_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Log the trace tree to wandb."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">child_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">[</span><span class="s2">"root"</span><span class="p">]</span>
            <span class="n">root_span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_convert_event_pair_to_wb_span</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">child_nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]],</span>
                <span class="n">trace_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">)</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span><span class="p">:</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
            <span class="c1"># TODO: add span kind for EMBEDDING when it's available</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">:</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span><span class="o">.</span><span class="n">SpanKind</span><span class="o">.</span><span class="n">AGENT</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">:</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span><span class="o">.</span><span class="n">SpanKind</span><span class="o">.</span><span class="n">TOOL</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">TREE</span><span class="p">:</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span><span class="o">.</span><span class="n">SpanKind</span><span class="o">.</span><span class="n">CHAIN</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">RERANKING</span><span class="p">:</span>
            <span class="n">span_kind</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span><span class="o">.</span><span class="n">SpanKind</span><span class="o">.</span><span class="n">CHAIN</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="mi">2</span>
        <span class="n">event_type</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">event_type</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
            <span class="n">inputs</span><span class="p">,</span> <span class="n">outputs</span><span class="p">,</span> <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_llm_payload</span><span class="p">(</span><span class="n">event_pair</span><span class="p">,</span> <span class="n">span</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
            <span class="n">inputs</span><span class="p">,</span> <span class="n">outputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_embedding_payload</span><span class="p">(</span><span class="n">event_pair</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">outputs</span><span class="p">,</span> <span class="n">span</span>

    <span class="k">def</span> <span class="nf">_handle_node_parsing_payload</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_pair</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Handle the payload of a NODE_PARSING event."""</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>

        <span class="k">if</span> <span class="n">inputs</span> <span class="ow">and</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span> <span class="ow">in</span> <span class="n">inputs</span><span class="p">:</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="n">inputs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">)</span>
            <span class="n">inputs</span><span class="p">[</span><span class="s2">"num_documents"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">outputs</span> <span class="ow">and</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span> <span class="ow">in</span> <span class="n">outputs</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">)</span>
            <span class="n">outputs</span><span class="p">[</span><span class="s2">"num_nodes"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">inputs</span> <span class="ow">or</span> <span class="p">{},</span> <span class="n">outputs</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_handle_llm_payload</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_pair</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">],</span> <span class="n">span</span><span class="p">:</span> <span class="s2">"trace_tree.Span"</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="s2">"trace_tree.Span"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Handle the payload of a LLM event."""</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">inputs</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">outputs</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span>

        <span class="c1"># Get `original_template` from Prompt</span>
        <span class="k">if</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span> <span class="ow">in</span> <span class="n">inputs</span><span class="p">:</span>
            <span class="n">inputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">]</span> <span class="o">=</span> <span class="n">inputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">]</span>

        <span class="c1"># Format messages</span>
        <span class="k">if</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span> <span class="ow">in</span> <span class="n">inputs</span><span class="p">:</span>
            <span class="n">inputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">inputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">]]</span>
            <span class="p">)</span>

        <span class="n">token_counts</span> <span class="o">=</span> <span class="n">get_llm_token_counts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_token_counter</span><span class="p">,</span> <span class="n">outputs</span><span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"formatted_prompt_tokens_count"</span><span class="p">:</span> <span class="n">token_counts</span><span class="o">.</span><span class="n">prompt_token_count</span><span class="p">,</span>
            <span class="s2">"prediction_tokens_count"</span><span class="p">:</span> <span class="n">token_counts</span><span class="o">.</span><span class="n">completion_token_count</span><span class="p">,</span>
            <span class="s2">"total_tokens_used"</span><span class="p">:</span> <span class="n">token_counts</span><span class="o">.</span><span class="n">total_token_count</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">span</span><span class="o">.</span><span class="n">attributes</span> <span class="o">=</span> <span class="n">metadata</span>

        <span class="c1"># Make `response` part of `outputs`</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">outputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">])}</span>

        <span class="k">return</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">outputs</span><span class="p">,</span> <span class="n">span</span>

    <span class="k">def</span> <span class="nf">_handle_query_payload</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_pair</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Handle the payload of a QUERY event."""</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>

        <span class="k">if</span> <span class="n">outputs</span><span class="p">:</span>
            <span class="n">response_obj</span> <span class="o">=</span> <span class="n">outputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">]</span>
            <span class="n">response</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">outputs</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">])</span>

            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">response</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span> <span class="o"></span> <span class="s2">"StreamingResponse"</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">response_obj</span><span class="o">.</span><span class="n">get_response</span><span class="p">()</span><span class="o">.</span><span class="n">response</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">" "</span>

        <span class="n">outputs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"response"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

        <span class="k">return</span> <span class="n">inputs</span><span class="p">,</span> <span class="n">outputs</span>

    <span class="k">def</span> <span class="nf">_handle_embedding_payload</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_pair</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
        <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="n">event_pair</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">payload</span>

        <span class="n">chunks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">outputs</span><span class="p">:</span>
            <span class="n">chunks</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">,</span> <span class="p">[])</span>

        <span class="k">return</span> <span class="p">{},</span> <span class="p">{</span><span class="s2">"num_chunks"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)}</span>

    <span class="k">def</span> <span class="nf">_get_time_in_ms</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event_pair</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the start and end time of an event pair in milliseconds."""</span>
        <span class="n">start_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">TIMESTAMP_FORMAT</span><span class="p">)</span>
        <span class="n">end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">event_pair</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">TIMESTAMP_FORMAT</span><span class="p">)</span>

        <span class="n">start_time_in_ms</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span>
            <span class="p">(</span><span class="n">start_time</span> <span class="o">-</span> <span class="n">datetime</span><span class="p">(</span><span class="mi">1970</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span> <span class="o">*</span> <span class="mi">1000</span>
        <span class="p">)</span>
        <span class="n">end_time_in_ms</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="n">end_time</span> <span class="o">-</span> <span class="n">datetime</span><span class="p">(</span><span class="mi">1970</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span> <span class="o">*</span> <span class="mi">1000</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">start_time_in_ms</span><span class="p">,</span> <span class="n">end_time_in_ms</span>

    <span class="k">def</span> <span class="nf">_ensure_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">should_print_url</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Ensures an active W&amp;B run exists.</span>

<span class="sd">        If not, will start a new run with the provided run_args.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore[attr-defined]</span>
            <span class="c1"># Make a shallow copy of the run args, so we don't modify the original</span>
            <span class="n">run_args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_args</span> <span class="ow">or</span> <span class="p">{}</span>  <span class="c1"># type: ignore</span>
            <span class="n">run_args</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">run_args</span><span class="p">}</span>  <span class="c1"># type: ignore</span>

            <span class="c1"># Prefer to run in silent mode since W&amp;B has a lot of output</span>
            <span class="c1"># which can be undesirable when dealing with text-based models.</span>
            <span class="k">if</span> <span class="s2">"settings"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">run_args</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
                <span class="n">run_args</span><span class="p">[</span><span class="s2">"settings"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"silent"</span><span class="p">:</span> <span class="kc">True</span><span class="p">}</span>  <span class="c1"># type: ignore</span>

            <span class="c1"># Start the run and add the stream table</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">init</span><span class="p">(</span><span class="o">**</span><span class="n">run_args</span><span class="p">)</span>  <span class="c1"># type: ignore[attr-defined]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">_label</span><span class="p">(</span><span class="n">repo</span><span class="o">=</span><span class="s2">"llama_index"</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

            <span class="k">if</span> <span class="n">should_print_url</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_print_wandb_init_message</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">run_url</span>  <span class="c1"># type: ignore</span>
                <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_print_wandb_init_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Print a message to the terminal when W&amp;B is initialized."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">termlog</span><span class="p">(</span>  <span class="c1"># type: ignore[attr-defined]</span>
            <span class="sa">f</span><span class="s2">"Streaming LlamaIndex events to W&amp;B at </span><span class="si">{</span><span class="n">run_url</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"`WandbCallbackHandler` is currently in beta.</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"Please report any issues to https://github.com/wandb/wandb/issues "</span>
            <span class="s2">"with the tag `llamaindex`."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_print_upload_index_fail_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Print a message to the terminal when uploading the index fails."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">termlog</span><span class="p">(</span>  <span class="c1"># type: ignore[attr-defined]</span>
            <span class="sa">f</span><span class="s2">"Failed to upload index to W&amp;B with the following error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Finish the callback handler."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>  <span class="c1"># type: ignore[attr-defined]</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_start [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.on_event_start "Permanent link")

```
on_event_start(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', parent_id: str = '', **kwargs: Any) -> str
```

Store event start data by event type.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_type` | `[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")` | 
event type to store.



 | _required_ |
| `payload` | `Optional[Dict[str, Any]]` | 

payload to store.



 | `None` |
| `event_id` | `str` | 

event id to store.



 | `''` |
| `parent_id` | `str` | 

parent event id.



 | `''` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">176</span>
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
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Store event start data by event type.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>
<span class="sd">        parent_id (str): parent event id.</span>

<span class="sd">    """</span>
    <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">event</span><span class="o">.</span><span class="n">id_</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_end [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.on_event_end "Permanent link")

```
on_event_end(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', **kwargs: Any) -> None
```

Store event end data by event type.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_type` | `[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")` | 
event type to store.



 | _required_ |
| `payload` | `Optional[Dict[str, Any]]` | 

payload to store.



 | `None` |
| `event_id` | `str` | 

event id to store.



 | `''` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

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
<span class="normal">214</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Store event end data by event type.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>

<span class="sd">    """</span>
    <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### start\_trace [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.start_trace "Permanent link")

```
start_trace(trace_id: Optional[str] = None) -> None
```

Launch a trace.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Launch a trace."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="o">=</span> <span class="n">trace_id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### log\_trace\_tree [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.log_trace_tree "Permanent link")

```
log_trace_tree() -> None
```

Log the trace tree to wandb.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">239</span>
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
<span class="normal">259</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">log_trace_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Log the trace tree to wandb."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">child_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">[</span><span class="s2">"root"</span><span class="p">]</span>
        <span class="n">root_span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_convert_event_pair_to_wb_span</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">child_nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]],</span>
            <span class="n">trace_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">child_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">[</span><span class="n">child_nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span>
            <span class="n">root_span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_trace_tree</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">,</span> <span class="n">root_span</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">root_span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_trace_tree</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">,</span> <span class="n">root_span</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">root_span</span><span class="p">:</span>
            <span class="n">root_trace</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_tree</span><span class="o">.</span><span class="n">WBTraceTree</span><span class="p">(</span><span class="n">root_span</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span><span class="p">:</span>  <span class="c1"># type: ignore[attr-defined]</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">log</span><span class="p">({</span><span class="s2">"trace"</span><span class="p">:</span> <span class="n">root_trace</span><span class="p">})</span>  <span class="c1"># type: ignore[attr-defined]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">termlog</span><span class="p">(</span><span class="s2">"Logged trace tree to W&amp;B."</span><span class="p">)</span>  <span class="c1"># type: ignore[attr-defined]</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to log trace tree to W&amp;B: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### persist\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.persist_index "Permanent link")

```
persist_index(index: IndexType, index_name: str, persist_dir: Union[str, None] = None) -> None
```

Upload an index to wandb as an artifact. You can learn more about W&B artifacts here: https://docs.wandb.ai/guides/artifacts.

For the `ComposableGraph` index, the root id is stored as artifact metadata.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `IndexType` | 
index to upload.



 | _required_ |
| `index_name` | `str` | 

name of the index. This will be used as the artifact name.



 | _required_ |
| `persist_dir` | `Union[str, None]` | 

directory to persist the index. If None, a temporary directory will be created and used.



 | `None` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">262</span>
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
<span class="normal">300</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist_index</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="s2">"IndexType"</span><span class="p">,</span> <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Upload an index to wandb as an artifact. You can learn more about W&amp;B</span>
<span class="sd">    artifacts here: https://docs.wandb.ai/guides/artifacts.</span>

<span class="sd">    For the `ComposableGraph` index, the root id is stored as artifact metadata.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (IndexType): index to upload.</span>
<span class="sd">        index_name (str): name of the index. This will be used as the artifact name.</span>
<span class="sd">        persist_dir (Union[str, None]): directory to persist the index. If None, a</span>
<span class="sd">            temporary directory will be created and used.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">persist_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">persist_dir</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">dir</span><span class="si">}</span><span class="s2">/storage"</span>  <span class="c1"># type: ignore</span>
        <span class="n">_default_persist_dir</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">):</span>
        <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_IndexType</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">index</span><span class="o">.</span><span class="n">storage_context</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="c1"># For the `ComposableGraph` index, store the root id as metadata</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_IndexType</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
                <span class="n">root_id</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">root_id</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"root_id"</span><span class="p">:</span> <span class="n">root_id</span><span class="p">}</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_upload_index_as_wb_artifact</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">index_name</span><span class="p">,</span> <span class="n">metadata</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># Silently ignore errors to not break user code</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_print_upload_index_fail_message</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>

    <span class="c1"># clear the default storage dir</span>
    <span class="k">if</span> <span class="n">_default_persist_dir</span><span class="p">:</span>
        <span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">ignore_errors</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_storage\_context [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.load_storage_context "Permanent link")

```
load_storage_context(artifact_url: str, index_download_dir: Union[str, None] = None) -> [StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")
```

Download an index from wandb and return a storage context.

Use this storage context to load the index into memory using `load_index_from_storage`, `load_indices_from_storage` or `load_graph_from_storage` functions.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `artifact_url` | `str` | 
url of the artifact to download. The artifact url will be of the form: `entity/project/index_name:version` and can be found in the W&B UI.



 | _required_ |
| `index_download_dir` | `Union[str, None]` | 

directory to download the index to.



 | `None` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">302</span>
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
<span class="normal">322</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_storage_context</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">artifact_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">index_download_dir</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StorageContext"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Download an index from wandb and return a storage context.</span>

<span class="sd">    Use this storage context to load the index into memory using</span>
<span class="sd">    `load_index_from_storage`, `load_indices_from_storage` or</span>
<span class="sd">    `load_graph_from_storage` functions.</span>

<span class="sd">    Args:</span>
<span class="sd">        artifact_url (str): url of the artifact to download. The artifact url will</span>
<span class="sd">            be of the form: `entity/project/index_name:version` and can be found in</span>
<span class="sd">            the W&amp;B UI.</span>
<span class="sd">        index_download_dir (Union[str, None]): directory to download the index to.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.storage.storage_context</span> <span class="kn">import</span> <span class="n">StorageContext</span>

    <span class="n">artifact</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">use_artifact</span><span class="p">(</span><span class="n">artifact_url</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"storage_context"</span><span class="p">)</span>  <span class="c1"># type: ignore[attr-defined]</span>
    <span class="n">artifact_dir</span> <span class="o">=</span> <span class="n">artifact</span><span class="o">.</span><span class="n">download</span><span class="p">(</span><span class="n">root</span><span class="o">=</span><span class="n">index_download_dir</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">artifact_dir</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### finish [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/#llama_index.callbacks.wandb.WandbCallbackHandler.finish "Permanent link")

```
finish() -> None
```

Finish the callback handler.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-wandb/llama_index/callbacks/wandb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Finish the callback handler."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_wandb</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>  <span class="c1"># type: ignore[attr-defined]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Uptrain](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/)[Next Condense plus context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_plus_context/)
