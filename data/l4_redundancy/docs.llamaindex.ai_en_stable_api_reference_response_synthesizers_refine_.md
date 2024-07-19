Title: Refine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/

Markdown Content:
Refine - LlamaIndex


Init file.

Refine [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/#llama_index.core.response_synthesizers.Refine "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.base.BaseSynthesizer")`

Refine a response to a query across text chunks.

Source code in `llama-index-core/llama_index/core/response_synthesizers/refine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
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
<span class="normal">516</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Refine</span><span class="p">(</span><span class="n">BaseSynthesizer</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Refine a response to a query across text chunks."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_helper</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptHelper</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">structured_answer_filtering</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">program_factory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">BasePromptTemplate</span><span class="p">],</span> <span class="n">BasePydanticProgram</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt_helper</span> <span class="o">=</span> <span class="n">service_context</span><span class="o">.</span><span class="n">prompt_helper</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span> <span class="o">=</span> <span class="n">text_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT_SEL</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">refine_template</span> <span class="ow">or</span> <span class="n">DEFAULT_REFINE_PROMPT_SEL</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_structured_answer_filtering</span> <span class="o">=</span> <span class="n">structured_answer_filtering</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_structured_answer_filtering</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Streaming not supported with structured answer filtering."</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_structured_answer_filtering</span> <span class="ow">and</span> <span class="n">program_factory</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Program factory not supported without structured answer filtering."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_program_factory</span> <span class="o">=</span> <span class="n">program_factory</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_program_factory</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"text_qa_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="p">,</span>
            <span class="s2">"refine_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"text_qa_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"text_qa_template"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"refine_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"refine_template"</span><span class="p">]</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">prev_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Give response over chunks."""</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">GetResponseStartEvent</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunks</span><span class="o">=</span><span class="n">text_chunks</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">for</span> <span class="n">text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prev_response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="c1"># if this is the first chunk, and text chunk already</span>
                <span class="c1"># is an answer, then return it</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_give_response_single</span><span class="p">(</span>
                    <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># refine response if possible</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_response_single</span><span class="p">(</span>
                    <span class="n">prev_response</span><span class="p">,</span> <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
                <span class="p">)</span>
            <span class="n">prev_response</span> <span class="o">=</span> <span class="n">response</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="ow">or</span> <span class="s2">"Empty Response"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Generator</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">GetResponseEndEvent</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">_default_program_factory</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="n">PromptTemplate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePydanticProgram</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_structured_answer_filtering</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.program.utils</span> <span class="kn">import</span> <span class="n">get_program_for_llm</span>

            <span class="k">return</span> <span class="n">get_program_for_llm</span><span class="p">(</span>
                <span class="n">StructuredRefineResponse</span><span class="p">,</span>
                <span class="n">prompt</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">DefaultRefineProgram</span><span class="p">(</span>
                <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
                <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
                <span class="n">output_cls</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_give_response_single</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Give response given a query and a corresponding text chunk."""</span>
        <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">text_chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="p">[</span><span class="n">text_chunk</span><span class="p">])</span>

        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">program</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program_factory</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">)</span>
        <span class="c1"># TODO: consolidate with loop in get_response_default</span>
        <span class="k">for</span> <span class="n">cur_text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="n">query_satisfied</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                        <span class="n">StructuredRefineResponse</span><span class="p">,</span>
                        <span class="n">program</span><span class="p">(</span>
                            <span class="n">context_str</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                            <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                        <span class="p">),</span>
                    <span class="p">)</span>
                    <span class="n">query_satisfied</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">query_satisfied</span>
                    <span class="k">if</span> <span class="n">query_satisfied</span><span class="p">:</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">answer</span>
                <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Validation error on structured response: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">elif</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span>
                    <span class="n">text_qa_template</span><span class="p">,</span>
                    <span class="n">context_str</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">query_satisfied</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_response_single</span><span class="p">(</span>
                    <span class="n">cast</span><span class="p">(</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">,</span> <span class="n">response</span><span class="p">),</span>
                    <span class="n">query_str</span><span class="p">,</span>
                    <span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">"Empty Response"</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="ow">or</span> <span class="s2">"Empty Response"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Generator</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">_refine_response_single</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Refine response."""</span>
        <span class="c1"># TODO: consolidate with logic in response/schema.py</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Generator</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">get_response_text</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

        <span class="n">fmt_text_chunk</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span><span class="n">text_chunk</span><span class="p">,</span> <span class="mi">50</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Refine context: </span><span class="si">{</span><span class="n">fmt_text_chunk</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Refine context: </span><span class="si">{</span><span class="n">fmt_text_chunk</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># NOTE: partial format refine template with query_str and existing_answer here</span>
        <span class="n">refine_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">existing_answer</span><span class="o">=</span><span class="n">response</span>
        <span class="p">)</span>

        <span class="c1"># compute available chunk size to see if there is any available space</span>
        <span class="c1"># determine if the refine template is too big (which can happen if</span>
        <span class="c1"># prompt template + query + existing answer is too large)</span>
        <span class="n">avail_chunk_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">_get_available_chunk_size</span><span class="p">(</span>
            <span class="n">refine_template</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">avail_chunk_size</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="c1"># if the available chunk size is negative, then the refine template</span>
            <span class="c1"># is too big and we just return the original response</span>
            <span class="k">return</span> <span class="n">response</span>

        <span class="c1"># obtain text chunks to add to the refine template</span>
        <span class="n">text_chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span>
            <span class="n">refine_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text_chunk</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="n">program</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program_factory</span><span class="p">(</span><span class="n">refine_template</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">cur_text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="n">query_satisfied</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                        <span class="n">StructuredRefineResponse</span><span class="p">,</span>
                        <span class="n">program</span><span class="p">(</span>
                            <span class="n">context_msg</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                            <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                        <span class="p">),</span>
                    <span class="p">)</span>
                    <span class="n">query_satisfied</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">query_satisfied</span>
                    <span class="k">if</span> <span class="n">query_satisfied</span><span class="p">:</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">answer</span>
                <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Validation error on structured response: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># TODO: structured response not supported for streaming</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Generator</span><span class="p">):</span>
                    <span class="n">response</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

                <span class="n">refine_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                    <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">existing_answer</span><span class="o">=</span><span class="n">response</span>
                <span class="p">)</span>

                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span>
                    <span class="n">refine_template</span><span class="p">,</span>
                    <span class="n">context_msg</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">prev_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">GetResponseStartEvent</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunks</span><span class="o">=</span><span class="n">text_chunks</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">for</span> <span class="n">text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prev_response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="c1"># if this is the first chunk, and text chunk already</span>
                <span class="c1"># is an answer, then return it</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agive_response_single</span><span class="p">(</span>
                    <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arefine_response_single</span><span class="p">(</span>
                    <span class="n">prev_response</span><span class="p">,</span> <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
                <span class="p">)</span>
            <span class="n">prev_response</span> <span class="o">=</span> <span class="n">response</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">"Empty Response"</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="ow">or</span> <span class="s2">"Empty Response"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">AsyncGenerator</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">GetResponseEndEvent</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arefine_response_single</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Refine response."""</span>
        <span class="c1"># TODO: consolidate with logic in response/schema.py</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AsyncGenerator</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">aget_response_text</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

        <span class="n">fmt_text_chunk</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span><span class="n">text_chunk</span><span class="p">,</span> <span class="mi">50</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Refine context: </span><span class="si">{</span><span class="n">fmt_text_chunk</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># NOTE: partial format refine template with query_str and existing_answer here</span>
        <span class="n">refine_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">existing_answer</span><span class="o">=</span><span class="n">response</span>
        <span class="p">)</span>

        <span class="c1"># compute available chunk size to see if there is any available space</span>
        <span class="c1"># determine if the refine template is too big (which can happen if</span>
        <span class="c1"># prompt template + query + existing answer is too large)</span>
        <span class="n">avail_chunk_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">_get_available_chunk_size</span><span class="p">(</span>
            <span class="n">refine_template</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">avail_chunk_size</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="c1"># if the available chunk size is negative, then the refine template</span>
            <span class="c1"># is too big and we just return the original response</span>
            <span class="k">return</span> <span class="n">response</span>

        <span class="c1"># obtain text chunks to add to the refine template</span>
        <span class="n">text_chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span>
            <span class="n">refine_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text_chunk</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="n">program</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program_factory</span><span class="p">(</span><span class="n">refine_template</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">cur_text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="n">query_satisfied</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">program</span><span class="o">.</span><span class="n">acall</span><span class="p">(</span>
                        <span class="n">context_msg</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                        <span class="n">StructuredRefineResponse</span><span class="p">,</span> <span class="n">structured_response</span>
                    <span class="p">)</span>
                    <span class="n">query_satisfied</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">query_satisfied</span>
                    <span class="k">if</span> <span class="n">query_satisfied</span><span class="p">:</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">answer</span>
                <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Validation error on structured response: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Generator</span><span class="p">):</span>
                    <span class="n">response</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AsyncGenerator</span><span class="p">):</span>
                    <span class="n">_r</span> <span class="o">=</span> <span class="s2">""</span>
                    <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
                        <span class="n">_r</span> <span class="o">+=</span> <span class="n">text</span>
                    <span class="n">response</span> <span class="o">=</span> <span class="n">_r</span>

                <span class="n">refine_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                    <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">existing_answer</span><span class="o">=</span><span class="n">response</span>
                <span class="p">)</span>

                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">astream</span><span class="p">(</span>
                    <span class="n">refine_template</span><span class="p">,</span>
                    <span class="n">context_msg</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="k">if</span> <span class="n">query_satisfied</span><span class="p">:</span>
                <span class="n">refine_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                    <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">existing_answer</span><span class="o">=</span><span class="n">response</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_agive_response_single</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Give response given a query and a corresponding text chunk."""</span>
        <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">text_chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="p">[</span><span class="n">text_chunk</span><span class="p">])</span>

        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">program</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program_factory</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">)</span>
        <span class="c1"># TODO: consolidate with loop in get_response_default</span>
        <span class="k">for</span> <span class="n">cur_text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">program</span><span class="o">.</span><span class="n">acall</span><span class="p">(</span>
                        <span class="n">context_str</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="n">structured_response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                        <span class="n">StructuredRefineResponse</span><span class="p">,</span> <span class="n">structured_response</span>
                    <span class="p">)</span>
                    <span class="n">query_satisfied</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">query_satisfied</span>
                    <span class="k">if</span> <span class="n">query_satisfied</span><span class="p">:</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">structured_response</span><span class="o">.</span><span class="n">answer</span>
                <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Validation error on structured response: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">elif</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">astream</span><span class="p">(</span>
                    <span class="n">text_qa_template</span><span class="p">,</span>
                    <span class="n">context_str</span><span class="o">=</span><span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">query_satisfied</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arefine_response_single</span><span class="p">(</span>
                    <span class="n">cast</span><span class="p">(</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">,</span> <span class="n">response</span><span class="p">),</span>
                    <span class="n">query_str</span><span class="p">,</span>
                    <span class="n">cur_text_chunk</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">"Empty Response"</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="ow">or</span> <span class="s2">"Empty Response"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">AsyncGenerator</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### get\_response [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/#llama_index.core.response_synthesizers.Refine.get_response "Permanent link")

```
get_response(query_str: str, text_chunks: Sequence[str], prev_response: Optional[RESPONSE_TEXT_TYPE] = None, **response_kwargs: Any) -> RESPONSE_TEXT_TYPE
```

Give response over chunks.

Source code in `llama-index-core/llama_index/core/response_synthesizers/refine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
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
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">prev_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Give response over chunks."""</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">GetResponseStartEvent</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunks</span><span class="o">=</span><span class="n">text_chunks</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">for</span> <span class="n">text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">prev_response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># if this is the first chunk, and text chunk already</span>
            <span class="c1"># is an answer, then return it</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_give_response_single</span><span class="p">(</span>
                <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># refine response if possible</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_response_single</span><span class="p">(</span>
                <span class="n">prev_response</span><span class="p">,</span> <span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunk</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span>
            <span class="p">)</span>
        <span class="n">prev_response</span> <span class="o">=</span> <span class="n">response</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="ow">or</span> <span class="s2">"Empty Response"</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Generator</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">GetResponseEndEvent</span><span class="p">())</span>
    <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/)[Next Simple summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/simple_summarize/)
