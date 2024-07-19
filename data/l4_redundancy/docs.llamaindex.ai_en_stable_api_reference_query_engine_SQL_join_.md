Title: SQL join - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/

Markdown Content:
SQL join - LlamaIndex


SQLJoinQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/#llama_index.core.query_engine.SQLJoinQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

SQL Join Query Engine.

This query engine can "Join" a SQL database results with another query engine. It can decide it needs to query the SQL database or the other query engine. If it decides to query the SQL database, it will first query the SQL database, whether to augment information with retrieved results from the other query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_query_tool` | `[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")` | 
Query engine tool for SQL database. other\_query\_tool (QueryEngineTool): Other query engine tool.



 | _required_ |
| `selector` | `Optional[Union[LLMSingleSelector, PydanticSingleSelector]]` | 

Selector to use.



 | `None` |
| `service_context` | `Optional[ServiceContext]` | 

Service context to use.



 | `None` |
| `sql_join_synthesis_prompt` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")]` | 

PromptTemplate to use for SQL join synthesis.



 | `None` |
| `sql_augment_query_transform` | `Optional[SQLAugmentQueryTransform]` | 

Query transform to use for SQL augmentation.



 | `None` |
| `use_sql_join_synthesis` | `bool` | 

Whether to use SQL join synthesis.



 | `True` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

Callback manager to use.



 | `None` |
| `verbose` | `bool` | 

Whether to print intermediate results.



 | `True` |

Source code in `llama-index-core/llama_index/core/query_engine/sql_join_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">169</span>
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
<span class="normal">355</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLJoinQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SQL Join Query Engine.</span>

<span class="sd">    This query engine can "Join" a SQL database results</span>
<span class="sd">    with another query engine.</span>
<span class="sd">    It can decide it needs to query the SQL database or the other query engine.</span>
<span class="sd">    If it decides to query the SQL database, it will first query the SQL database,</span>
<span class="sd">    whether to augment information with retrieved results from the other query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_query_tool (QueryEngineTool): Query engine tool for SQL database.</span>
<span class="sd">            other_query_tool (QueryEngineTool): Other query engine tool.</span>
<span class="sd">        selector (Optional[Union[LLMSingleSelector, PydanticSingleSelector]]):</span>
<span class="sd">            Selector to use.</span>
<span class="sd">        service_context (Optional[ServiceContext]): Service context to use.</span>
<span class="sd">        sql_join_synthesis_prompt (Optional[BasePromptTemplate]):</span>
<span class="sd">            PromptTemplate to use for SQL join synthesis.</span>
<span class="sd">        sql_augment_query_transform (Optional[SQLAugmentQueryTransform]): Query</span>
<span class="sd">            transform to use for SQL augmentation.</span>
<span class="sd">        use_sql_join_synthesis (bool): Whether to use SQL join synthesis.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): Callback manager to use.</span>
<span class="sd">        verbose (bool): Whether to print intermediate results.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_query_tool</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">,</span>
        <span class="n">other_query_tool</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">LLMSingleSelector</span><span class="p">,</span> <span class="n">PydanticSingleSelector</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_join_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_augment_query_transform</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SQLAugmentQueryTransform</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_sql_join_synthesis</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>
        <span class="c1"># validate that the query engines are of the right type</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="n">sql_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="p">(</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">,</span> <span class="n">NLSQLTableQueryEngine</span><span class="p">),</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"sql_query_tool.query_engine must be an instance of "</span>
                <span class="s2">"BaseSQLTableQueryEngine or NLSQLTableQueryEngine"</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_query_tool</span> <span class="o">=</span> <span class="n">sql_query_tool</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_other_query_tool</span> <span class="o">=</span> <span class="n">other_query_tool</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span> <span class="o">=</span> <span class="n">selector</span> <span class="ow">or</span> <span class="n">get_selector_from_llm</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="n">is_multi</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="p">,</span> <span class="p">(</span><span class="n">LLMSingleSelector</span><span class="p">,</span> <span class="n">PydanticSingleSelector</span><span class="p">))</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sql_join_synthesis_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_SQL_JOIN_SYNTHESIS_PROMPT</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_augment_query_transform</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sql_augment_query_transform</span> <span class="ow">or</span> <span class="n">SQLAugmentQueryTransform</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_sql_join_synthesis</span> <span class="o">=</span> <span class="n">use_sql_join_synthesis</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">streaming</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"selector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="p">,</span>
            <span class="s2">"sql_augment_query_transform"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_augment_query_transform</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"sql_join_synthesis_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"sql_join_synthesis_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"sql_join_synthesis_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_query_sql_other</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query SQL database + other query engine in sequence."""</span>
        <span class="c1"># first query SQL database</span>
        <span class="n">sql_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_sql_join_synthesis</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">sql_response</span>

        <span class="n">sql_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sql_response</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sql_query"</span><span class="p">]</span> <span class="k">if</span> <span class="n">sql_response</span><span class="o">.</span><span class="n">metadata</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL query: </span><span class="si">{</span><span class="n">sql_query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL response: </span><span class="si">{</span><span class="n">sql_response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="c1"># given SQL db, transform query into new query</span>
        <span class="n">new_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_augment_query_transform</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">_format_sql_query</span><span class="p">(</span><span class="n">sql_query</span><span class="p">),</span>
                <span class="s2">"sql_query_response"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">sql_response</span><span class="p">),</span>
            <span class="p">},</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Transformed query given SQL response: </span><span class="si">{</span><span class="n">new_query</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Transformed query given SQL response: </span><span class="si">{</span><span class="n">new_query</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_augment_query_transform</span><span class="o">.</span><span class="n">check_stop</span><span class="p">(</span><span class="n">new_query</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">sql_response</span>

        <span class="n">other_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_other_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">new_query</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query engine response: </span><span class="si">{</span><span class="n">other_response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; query engine response: </span><span class="si">{</span><span class="n">other_response</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">sql_query_str</span><span class="o">=</span><span class="n">sql_query</span><span class="p">,</span>
                <span class="n">sql_response_str</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">sql_response</span><span class="p">),</span>
                <span class="n">query_engine_query_str</span><span class="o">=</span><span class="n">new_query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">query_engine_response_str</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">other_response</span><span class="p">),</span>
            <span class="p">)</span>

            <span class="n">response_metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="o">**</span><span class="p">(</span><span class="n">sql_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}),</span>
                <span class="o">**</span><span class="p">(</span><span class="n">other_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}),</span>
            <span class="p">}</span>
            <span class="n">source_nodes</span> <span class="o">=</span> <span class="n">other_response</span><span class="o">.</span><span class="n">source_nodes</span>
            <span class="k">return</span> <span class="n">StreamingResponse</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">,</span>
                <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">sql_query_str</span><span class="o">=</span><span class="n">sql_query</span><span class="p">,</span>
                <span class="n">sql_response_str</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">sql_response</span><span class="p">),</span>
                <span class="n">query_engine_query_str</span><span class="o">=</span><span class="n">new_query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">query_engine_response_str</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">other_response</span><span class="p">),</span>
            <span class="p">)</span>

            <span class="n">response_metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="o">**</span><span class="p">(</span><span class="n">sql_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}),</span>
                <span class="o">**</span><span class="p">(</span><span class="n">other_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}),</span>
            <span class="p">}</span>
            <span class="n">source_nodes</span> <span class="o">=</span> <span class="n">other_response</span><span class="o">.</span><span class="n">source_nodes</span>
            <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">,</span>
                <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query and get response."""</span>
        <span class="c1"># TODO: see if this can be consolidated with logic in RouterQueryEngine</span>
        <span class="n">metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_query_tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_other_query_tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">]</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>
        <span class="c1"># pick sql query</span>
        <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">ind</span> <span class="o"></span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Querying other query engine: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span>
                <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Querying other query engine: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_other_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid result.ind: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="c1"># TODO: make async</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

SQLAutoVectorQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/#llama_index.core.query_engine.SQLAutoVectorQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[SQLJoinQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/#llama_index.core.query_engine.SQLJoinQueryEngine "llama_index.core.query_engine.sql_join_query_engine.SQLJoinQueryEngine")`

SQL + Vector Index Auto Retriever Query Engine.

This query engine can query both a SQL database as well as a vector database. It will first decide whether it needs to query the SQL database or vector store. If it decides to query the SQL database, it will also decide whether to augment information with retrieved results from the vector store. We use the VectorIndexAutoRetriever to retrieve results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_query_tool` | `[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")` | 
Query engine tool for SQL database.



 | _required_ |
| `vector_query_tool` | `[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")` | 

Query engine tool for vector database.



 | _required_ |
| `selector` | `Optional[Union[LLMSingleSelector, PydanticSingleSelector]]` | 

Selector to use.



 | `None` |
| `service_context` | `Optional[ServiceContext]` | 

Service context to use.



 | `None` |
| `sql_vector_synthesis_prompt` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")]` | 

Prompt to use for SQL vector synthesis.



 | `None` |
| `sql_augment_query_transform` | `Optional[SQLAugmentQueryTransform]` | 

Query transform to use for SQL augmentation.



 | `None` |
| `use_sql_vector_synthesis` | `bool` | 

Whether to use SQL vector synthesis.



 | `True` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

Callback manager to use.



 | `None` |
| `verbose` | `bool` | 

Whether to print intermediate results.



 | `True` |

Source code in `llama-index-core/llama_index/core/query_engine/sql_vector_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
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
<span class="normal">177</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLAutoVectorQueryEngine</span><span class="p">(</span><span class="n">SQLJoinQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SQL + Vector Index Auto Retriever Query Engine.</span>

<span class="sd">    This query engine can query both a SQL database</span>
<span class="sd">    as well as a vector database. It will first decide</span>
<span class="sd">    whether it needs to query the SQL database or vector store.</span>
<span class="sd">    If it decides to query the SQL database, it will also decide</span>
<span class="sd">    whether to augment information with retrieved results from the vector store.</span>
<span class="sd">    We use the VectorIndexAutoRetriever to retrieve results.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_query_tool (QueryEngineTool): Query engine tool for SQL database.</span>
<span class="sd">        vector_query_tool (QueryEngineTool): Query engine tool for vector database.</span>
<span class="sd">        selector (Optional[Union[LLMSingleSelector, PydanticSingleSelector]]):</span>
<span class="sd">            Selector to use.</span>
<span class="sd">        service_context (Optional[ServiceContext]): Service context to use.</span>
<span class="sd">        sql_vector_synthesis_prompt (Optional[BasePromptTemplate]):</span>
<span class="sd">            Prompt to use for SQL vector synthesis.</span>
<span class="sd">        sql_augment_query_transform (Optional[SQLAugmentQueryTransform]): Query</span>
<span class="sd">            transform to use for SQL augmentation.</span>
<span class="sd">        use_sql_vector_synthesis (bool): Whether to use SQL vector synthesis.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): Callback manager to use.</span>
<span class="sd">        verbose (bool): Whether to print intermediate results.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_query_tool</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">,</span>
        <span class="n">vector_query_tool</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">LLMSingleSelector</span><span class="p">,</span> <span class="n">PydanticSingleSelector</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_vector_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_augment_query_transform</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SQLAugmentQueryTransform</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_sql_vector_synthesis</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="c1"># validate that the query engines are of the right type</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="n">sql_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="p">(</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">,</span> <span class="n">NLSQLTableQueryEngine</span><span class="p">),</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"sql_query_tool.query_engine must be an instance of "</span>
                <span class="s2">"BaseSQLTableQueryEngine or NLSQLTableQueryEngine"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">vector_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"vector_query_tool.query_engine must be an instance of "</span>
                <span class="s2">"RetrieverQueryEngine"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="n">vector_query_tool</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span> <span class="n">VectorIndexAutoRetriever</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"vector_query_tool.query_engine.retriever must be an instance "</span>
                <span class="s2">"of VectorIndexAutoRetriever"</span>
            <span class="p">)</span>

        <span class="n">sql_vector_synthesis_prompt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sql_vector_synthesis_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_SQL_VECTOR_SYNTHESIS_PROMPT</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">sql_query_tool</span><span class="p">,</span>
            <span class="n">vector_query_tool</span><span class="p">,</span>
            <span class="n">selector</span><span class="o">=</span><span class="n">selector</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">sql_join_synthesis_prompt</span><span class="o">=</span><span class="n">sql_vector_synthesis_prompt</span><span class="p">,</span>
            <span class="n">sql_augment_query_transform</span><span class="o">=</span><span class="n">sql_augment_query_transform</span><span class="p">,</span>
            <span class="n">use_sql_join_synthesis</span><span class="o">=</span><span class="n">use_sql_vector_synthesis</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"selector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="p">,</span>
            <span class="s2">"sql_augment_query_transform"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_augment_query_transform</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"sql_join_synthesis_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"sql_join_synthesis_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_sql_join_synthesis_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"sql_join_synthesis_prompt"</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_sql_and_vector_query_engines</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">sql_query_engine</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">,</span> <span class="n">NLSQLTableQueryEngine</span><span class="p">],</span>
        <span class="n">sql_tool_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sql_tool_description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_auto_retriever</span><span class="p">:</span> <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="n">vector_tool_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_tool_description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">LLMSingleSelector</span><span class="p">,</span> <span class="n">PydanticSingleSelector</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SQLAutoVectorQueryEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From SQL and vector query engines.</span>

<span class="sd">        Args:</span>
<span class="sd">            sql_query_engine (BaseSQLTableQueryEngine): SQL query engine.</span>
<span class="sd">            vector_query_engine (VectorIndexAutoRetriever): Vector retriever.</span>
<span class="sd">            selector (Optional[Union[LLMSingleSelector, PydanticSingleSelector]]):</span>
<span class="sd">                Selector to use.</span>

<span class="sd">        """</span>
        <span class="n">sql_query_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">sql_query_engine</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">sql_tool_name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">sql_tool_description</span>
        <span class="p">)</span>
        <span class="n">vector_query_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">vector_auto_retriever</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="n">vector_tool_name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="n">vector_tool_description</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">sql_query_tool</span><span class="p">,</span> <span class="n">vector_query_tool</span><span class="p">,</span> <span class="n">selector</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_sql\_and\_vector\_query\_engines `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/#llama_index.core.query_engine.SQLAutoVectorQueryEngine.from_sql_and_vector_query_engines "Permanent link")

```
from_sql_and_vector_query_engines(sql_query_engine: Union[BaseSQLTableQueryEngine, [NLSQLTableQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/#llama_index.core.query_engine.NLSQLTableQueryEngine "llama_index.core.indices.struct_store.sql_query.NLSQLTableQueryEngine")], sql_tool_name: str, sql_tool_description: str, vector_auto_retriever: [RetrieverQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/#llama_index.core.query_engine.RetrieverQueryEngine "llama_index.core.query_engine.retriever_query_engine.RetrieverQueryEngine"), vector_tool_name: str, vector_tool_description: str, selector: Optional[Union[LLMSingleSelector, PydanticSingleSelector]] = None, **kwargs: Any) -> [SQLAutoVectorQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/#llama_index.core.query_engine.SQLAutoVectorQueryEngine "llama_index.core.query_engine.sql_vector_query_engine.SQLAutoVectorQueryEngine")
```

From SQL and vector query engines.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_query_engine` | `BaseSQLTableQueryEngine` | 
SQL query engine.



 | _required_ |
| `vector_query_engine` | `[VectorIndexAutoRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/#llama_index.core.retrievers.VectorIndexAutoRetriever "llama_index.core.indices.vector_store.retrievers.auto_retriever.VectorIndexAutoRetriever")` | 

Vector retriever.



 | _required_ |
| `selector` | `Optional[Union[LLMSingleSelector, PydanticSingleSelector]]` | 

Selector to use.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/sql_vector_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
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
<span class="normal">177</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_sql_and_vector_query_engines</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">sql_query_engine</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">,</span> <span class="n">NLSQLTableQueryEngine</span><span class="p">],</span>
    <span class="n">sql_tool_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">sql_tool_description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">vector_auto_retriever</span><span class="p">:</span> <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
    <span class="n">vector_tool_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">vector_tool_description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">LLMSingleSelector</span><span class="p">,</span> <span class="n">PydanticSingleSelector</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SQLAutoVectorQueryEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From SQL and vector query engines.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_query_engine (BaseSQLTableQueryEngine): SQL query engine.</span>
<span class="sd">        vector_query_engine (VectorIndexAutoRetriever): Vector retriever.</span>
<span class="sd">        selector (Optional[Union[LLMSingleSelector, PydanticSingleSelector]]):</span>
<span class="sd">            Selector to use.</span>

<span class="sd">    """</span>
    <span class="n">sql_query_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">sql_query_engine</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">sql_tool_name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">sql_tool_description</span>
    <span class="p">)</span>
    <span class="n">vector_query_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">vector_auto_retriever</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="n">vector_tool_name</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="n">vector_tool_description</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">sql_query_tool</span><span class="p">,</span> <span class="n">vector_query_tool</span><span class="p">,</span> <span class="n">selector</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous PGVector SQL](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/)[Next SQL table retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/)
