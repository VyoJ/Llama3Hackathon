Title: Llm compiler - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/

Markdown Content:
Llm compiler - LlamaIndex


LLMCompilerAgentWorker [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.BaseAgentWorker "llama_index.core.agent.types.BaseAgentWorker")`

LLMCompiler Agent Worker.

LLMCompiler is an agent framework that allows async multi-function calling and query planning. Here is the implementation.

Source Repo (paper linked): https://github.com/SqueezeAILab/LLMCompiler?tab=readme-ov-file

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
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
<span class="normal">430</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMCompilerAgentWorker</span><span class="p">(</span><span class="n">BaseAgentWorker</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMCompiler Agent Worker.</span>

<span class="sd">    LLMCompiler is an agent framework that allows async multi-function calling and query planning.</span>
<span class="sd">    Here is the implementation.</span>

<span class="sd">    Source Repo (paper linked): https://github.com/SqueezeAILab/LLMCompiler?tab=readme-ov-file</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">planner_example_prompt_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">stop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">joiner_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_replans</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">planner_example_prompt_str</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">planner_example_prompt_str</span> <span class="ow">or</span> <span class="n">PLANNER_EXAMPLE_PROMPT</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt</span> <span class="o">=</span> <span class="n">generate_llm_compiler_prompt</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span> <span class="n">example_prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">planner_example_prompt_str</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt_replan</span> <span class="o">=</span> <span class="n">generate_llm_compiler_prompt</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span> <span class="n">is_replan</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">example_prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">planner_example_prompt_str</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="c1"># TODO: make tool_retriever work</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">LLMCompilerPlanParser</span><span class="p">(</span><span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stop</span> <span class="o">=</span> <span class="n">stop</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_replans</span> <span class="o">=</span> <span class="n">max_replans</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="c1"># joiner program</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">joiner_prompt</span> <span class="o">=</span> <span class="n">joiner_prompt</span> <span class="ow">or</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">OUTPUT_PROMPT</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">joiner_program</span> <span class="o">=</span> <span class="n">LLMTextCompletionProgram</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">LLMCompilerJoinerParser</span><span class="p">(),</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">JoinerOutput</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">joiner_prompt</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># if len(tools) &gt; 0 and tool_retriever is not None:</span>
        <span class="c1">#     raise ValueError("Cannot specify both tools and tool_retriever")</span>
        <span class="c1"># elif len(tools) &gt; 0:</span>
        <span class="c1">#     self._get_tools = lambda _: tools</span>
        <span class="c1"># elif tool_retriever is not None:</span>
        <span class="c1">#     tool_retriever_c = cast(ObjectRetriever[BaseTool], tool_retriever)</span>
        <span class="c1">#     self._get_tools = lambda message: tool_retriever_c.retrieve(message)</span>
        <span class="c1"># else:</span>
        <span class="c1">#     self._get_tools = lambda _: []</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LLMCompilerAgentWorker"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convenience constructor method from set of of BaseTools (Optional).</span>

<span class="sd">        Returns:</span>
<span class="sd">            LLMCompilerAgentWorker: the LLMCompilerAgentWorker instance</span>

<span class="sd">        """</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">DEFAULT_MODEL_NAME</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize step from task."""</span>
        <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># temporary memory for new messages</span>
        <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

        <span class="c1"># put user message in memory</span>
        <span class="n">new_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">))</span>

        <span class="c1"># initialize task state</span>
        <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
            <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
            <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
            <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
            <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
            <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"is_replan"</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span> <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"replans"</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="c1"># return [adapt_to_async_tool(t) for t in self._get_tools(input)]</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_llm</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">previous_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">is_replan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run LLM."""</span>
        <span class="k">if</span> <span class="n">is_replan</span><span class="p">:</span>
            <span class="n">system_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt_replan</span>
            <span class="k">assert</span> <span class="n">previous_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s2">"previous_context cannot be None"</span>
            <span class="n">human_prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Question: </span><span class="si">{</span><span class="nb">input</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">previous_context</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">system_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt</span>
            <span class="n">human_prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Question: </span><span class="si">{</span><span class="nb">input</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">),</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">human_prompt</span><span class="p">),</span>
        <span class="p">]</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">ajoin</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tasks</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">LLMCompilerTask</span><span class="p">],</span>
        <span class="n">is_final</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">JoinerOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Join answer using LLM/agent."""</span>
        <span class="n">agent_scratchpad</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span>
        <span class="n">agent_scratchpad</span> <span class="o">+=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="n">task</span><span class="o">.</span><span class="n">get_thought_action_observation</span><span class="p">(</span>
                    <span class="n">include_action</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_thought</span><span class="o">=</span><span class="kc">True</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">task</span> <span class="ow">in</span> <span class="n">tasks</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">task</span><span class="o">.</span><span class="n">is_join</span>
            <span class="p">]</span>
        <span class="p">)</span>
        <span class="n">agent_scratchpad</span> <span class="o">=</span> <span class="n">agent_scratchpad</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">joiner_program</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span>
            <span class="n">context_str</span><span class="o">=</span><span class="n">agent_scratchpad</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">output</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">JoinerOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Thought: </span><span class="si">{</span><span class="n">output</span><span class="o">.</span><span class="n">thought</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Answer: </span><span class="si">{</span><span class="n">output</span><span class="o">.</span><span class="n">answer</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">is_final</span><span class="p">:</span>
            <span class="n">output</span><span class="o">.</span><span class="n">is_replan</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">_get_task_step_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
        <span class="n">llmc_tasks</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">LLMCompilerTask</span><span class="p">],</span>
        <span class="n">answer</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">joiner_thought</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">is_replan</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get task step response."""</span>
        <span class="n">agent_answer</span> <span class="o">=</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">answer</span><span class="p">,</span> <span class="n">sources</span><span class="o">=</span><span class="p">[])</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">is_replan</span><span class="p">:</span>
            <span class="c1"># generate final answer</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="c1"># put in memory</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">answer</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Collect contexts for the subsequent replanner</span>
            <span class="n">context</span> <span class="o">=</span> <span class="n">generate_context_for_replanner</span><span class="p">(</span>
                <span class="n">tasks</span><span class="o">=</span><span class="n">llmc_tasks</span><span class="p">,</span> <span class="n">joiner_thought</span><span class="o">=</span><span class="n">joiner_thought</span>
            <span class="p">)</span>
            <span class="n">new_contexts</span> <span class="o">=</span> <span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"contexts"</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="n">context</span><span class="p">]</span>
            <span class="c1"># TODO: generate new steps</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">step</span><span class="o">.</span><span class="n">get_next_step</span><span class="p">(</span>
                    <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
                    <span class="nb">input</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
                    <span class="n">step_state</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"is_replan"</span><span class="p">:</span> <span class="n">is_replan</span><span class="p">,</span>
                        <span class="s2">"contexts"</span><span class="p">:</span> <span class="n">new_contexts</span><span class="p">,</span>
                        <span class="s2">"replans"</span><span class="p">:</span> <span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"replans"</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">]</span>

        <span class="k">return</span> <span class="n">TaskStepOutput</span><span class="p">(</span>
            <span class="n">output</span><span class="o">=</span><span class="n">agent_answer</span><span class="p">,</span>
            <span class="n">task_step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span>
            <span class="n">next_steps</span><span class="o">=</span><span class="n">new_steps</span><span class="p">,</span>
            <span class="n">is_last</span><span class="o">=</span><span class="ow">not</span> <span class="n">is_replan</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; Running step </span><span class="si">{</span><span class="n">step</span><span class="o">.</span><span class="n">step_id</span><span class="si">}</span><span class="s2"> for task </span><span class="si">{</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="sa">f</span><span class="s2">"&gt; Step count: </span><span class="si">{</span><span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s1">'replans'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="n">is_final_iter</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"is_replan"</span><span class="p">]</span>
            <span class="ow">and</span> <span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"replans"</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_replans</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"contexts"</span><span class="p">])</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">formatted_contexts</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">formatted_contexts</span> <span class="o">=</span> <span class="n">format_contexts</span><span class="p">(</span><span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"contexts"</span><span class="p">])</span>
        <span class="n">llm_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">arun_llm</span><span class="p">(</span>
            <span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
            <span class="n">previous_context</span><span class="o">=</span><span class="n">formatted_contexts</span><span class="p">,</span>
            <span class="n">is_replan</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="p">[</span><span class="s2">"is_replan"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Plan: </span><span class="si">{</span><span class="n">llm_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>

        <span class="c1"># return task dict (will generate plan, parse into dictionary)</span>
        <span class="n">task_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">cast</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">llm_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>

        <span class="c1"># execute via task executor</span>
        <span class="n">task_fetching_unit</span> <span class="o">=</span> <span class="n">TaskFetchingUnit</span><span class="o">.</span><span class="n">from_tasks</span><span class="p">(</span>
            <span class="n">task_dict</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span>
        <span class="p">)</span>
        <span class="k">await</span> <span class="n">task_fetching_unit</span><span class="o">.</span><span class="n">schedule</span><span class="p">()</span>

        <span class="c1">## join tasks - get response</span>
        <span class="n">tasks</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">LLMCompilerTask</span><span class="p">],</span> <span class="n">task_fetching_unit</span><span class="o">.</span><span class="n">tasks</span><span class="p">)</span>
        <span class="n">joiner_output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">ajoin</span><span class="p">(</span>
            <span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
            <span class="n">tasks</span><span class="p">,</span>
            <span class="n">is_final</span><span class="o">=</span><span class="n">is_final_iter</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># get task step response (with new steps planned)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_task_step_response</span><span class="p">(</span>
            <span class="n">task</span><span class="p">,</span>
            <span class="n">llmc_tasks</span><span class="o">=</span><span class="n">tasks</span><span class="p">,</span>
            <span class="n">answer</span><span class="o">=</span><span class="n">joiner_output</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
            <span class="n">joiner_thought</span><span class="o">=</span><span class="n">joiner_output</span><span class="o">.</span><span class="n">thought</span><span class="p">,</span>
            <span class="n">step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span>
            <span class="n">is_replan</span><span class="o">=</span><span class="n">joiner_output</span><span class="o">.</span><span class="n">is_replan</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">arun_step</span><span class="p">(</span><span class="n">step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (async)."""</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (stream)."""</span>
        <span class="c1"># # TODO: figure out if we need a different type for TaskStepOutput</span>
        <span class="c1"># return self._run_step_stream(step, task)</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
        <span class="c1"># """Run step (async stream)."""</span>
        <span class="c1"># return await self._arun_step_stream(step, task)</span>

    <span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
        <span class="c1"># add new messages to memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">())</span>
        <span class="c1"># reset new memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.from_tools "Permanent link")

```
from_tools(tools: Optional[Sequence[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, tool_retriever: Optional[[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, verbose: bool = False, **kwargs: Any) -> [LLMCompilerAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker "llama_index.agent.llm_compiler.step.LLMCompilerAgentWorker")
```

Convenience constructor method from set of of BaseTools (Optional).

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `LLMCompilerAgentWorker` | `[LLMCompilerAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker "llama_index.agent.llm_compiler.step.LLMCompilerAgentWorker")` | 
the LLMCompilerAgentWorker instance



 |

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">189</span>
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
<span class="normal">214</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LLMCompilerAgentWorker"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convenience constructor method from set of of BaseTools (Optional).</span>

<span class="sd">    Returns:</span>
<span class="sd">        LLMCompilerAgentWorker: the LLMCompilerAgentWorker instance</span>

<span class="sd">    """</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">DEFAULT_MODEL_NAME</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
        <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### initialize\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.initialize_step "Permanent link")

```
initialize_step(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep")
```

Initialize step from task.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">216</span>
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
<span class="normal">237</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize step from task."""</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># temporary memory for new messages</span>
    <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

    <span class="c1"># put user message in memory</span>
    <span class="n">new_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">))</span>

    <span class="c1"># initialize task state</span>
    <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
        <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
        <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
        <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
        <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
        <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"is_replan"</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span> <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"replans"</span><span class="p">:</span> <span class="mi">0</span><span class="p">},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_tools [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.get_tools "Permanent link")

```
get_tools(input: str) -> List[[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")]
```

Get tools.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get tools."""</span>
    <span class="c1"># return [adapt_to_async_tool(t) for t in self._get_tools(input)]</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### arun\_llm `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.arun_llm "Permanent link")

```
arun_llm(input: str, previous_context: Optional[str] = None, is_replan: bool = False) -> ChatResponse
```

Run LLM.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
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
<span class="normal">264</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">arun_llm</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">previous_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">is_replan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run LLM."""</span>
    <span class="k">if</span> <span class="n">is_replan</span><span class="p">:</span>
        <span class="n">system_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt_replan</span>
        <span class="k">assert</span> <span class="n">previous_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s2">"previous_context cannot be None"</span>
        <span class="n">human_prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Question: </span><span class="si">{</span><span class="nb">input</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">previous_context</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">system_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_prompt</span>
        <span class="n">human_prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Question: </span><span class="si">{</span><span class="nb">input</span><span class="si">}</span><span class="s2">"</span>

    <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">),</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">human_prompt</span><span class="p">),</span>
    <span class="p">]</span>

    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### ajoin `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.ajoin "Permanent link")

```
ajoin(input: str, tasks: Dict[int, LLMCompilerTask], is_final: bool = False) -> JoinerOutput
```

Join answer using LLM/agent.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">266</span>
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
<span class="normal">295</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">ajoin</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">tasks</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">LLMCompilerTask</span><span class="p">],</span>
    <span class="n">is_final</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">JoinerOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Join answer using LLM/agent."""</span>
    <span class="n">agent_scratchpad</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span>
    <span class="n">agent_scratchpad</span> <span class="o">+=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
        <span class="p">[</span>
            <span class="n">task</span><span class="o">.</span><span class="n">get_thought_action_observation</span><span class="p">(</span>
                <span class="n">include_action</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_thought</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">task</span> <span class="ow">in</span> <span class="n">tasks</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">task</span><span class="o">.</span><span class="n">is_join</span>
        <span class="p">]</span>
    <span class="p">)</span>
    <span class="n">agent_scratchpad</span> <span class="o">=</span> <span class="n">agent_scratchpad</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">joiner_program</span><span class="p">(</span>
        <span class="n">query_str</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span>
        <span class="n">context_str</span><span class="o">=</span><span class="n">agent_scratchpad</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">output</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">JoinerOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
        <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Thought: </span><span class="si">{</span><span class="n">output</span><span class="o">.</span><span class="n">thought</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Answer: </span><span class="si">{</span><span class="n">output</span><span class="o">.</span><span class="n">answer</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">is_final</span><span class="p">:</span>
        <span class="n">output</span><span class="o">.</span><span class="n">is_replan</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### run\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.run_step "Permanent link")

```
run_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step."""</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">arun_step</span><span class="p">(</span><span class="n">step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### arun\_step `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.arun_step "Permanent link")

```
arun_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (async).

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (async)."""</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### stream\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.stream_step "Permanent link")

```
stream_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (stream).

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (stream)."""</span>
    <span class="c1"># # TODO: figure out if we need a different type for TaskStepOutput</span>
    <span class="c1"># return self._run_step_stream(step, task)</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### finalize\_task [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/#llama_index.agent.llm_compiler.LLMCompilerAgentWorker.finalize_task "Permanent link")

```
finalize_task(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> None
```

Finalize task, after all the steps are completed.

Source code in `llama-index-integrations/agent/llama-index-agent-llm-compiler/llama_index/agent/llm_compiler/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
    <span class="c1"># add new messages to memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">())</span>
    <span class="c1"># reset new memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Lats](https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/)[Next Openai](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/)
