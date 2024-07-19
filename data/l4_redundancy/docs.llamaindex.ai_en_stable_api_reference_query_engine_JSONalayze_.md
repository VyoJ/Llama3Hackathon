Title: JSONalayze - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/

Markdown Content:
JSONalayze - LlamaIndex


JSONalyzeQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/#llama_index.core.query_engine.JSONalyzeQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

JSON List Shape Data Analysis Query Engine.

Converts natural language statasical queries to SQL within in-mem SQLite queries.

list\_of\_dict(List\[Dict\[str, Any\]\]): List of dictionaries to query. service\_context (ServiceContext): ServiceContext jsonalyze\_prompt (BasePromptTemplate): The JSONalyze prompt to use. use\_async (bool): Whether to use async. analyzer (Callable): The analyzer that executes the query. sql\_parser (BaseSQLParser): The SQL parser that ensures valid SQL being parsed from llm output. synthesize\_response (bool): Whether to synthesize a response. response\_synthesis\_prompt (BasePromptTemplate): The response synthesis prompt to use. table\_name (str): The table name to use. verbose (bool): Whether to print verbose output.

Source code in `llama-index-core/llama_index/core/query_engine/jsonalyze_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">209</span>
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
<span class="normal">356</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JSONalyzeQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""JSON List Shape Data Analysis Query Engine.</span>

<span class="sd">    Converts natural language statasical queries to SQL within in-mem SQLite queries.</span>

<span class="sd">    list_of_dict(List[Dict[str, Any]]): List of dictionaries to query.</span>
<span class="sd">    service_context (ServiceContext): ServiceContext</span>
<span class="sd">    jsonalyze_prompt (BasePromptTemplate): The JSONalyze prompt to use.</span>
<span class="sd">    use_async (bool): Whether to use async.</span>
<span class="sd">    analyzer (Callable): The analyzer that executes the query.</span>
<span class="sd">    sql_parser (BaseSQLParser): The SQL parser that ensures valid SQL being parsed</span>
<span class="sd">        from llm output.</span>
<span class="sd">    synthesize_response (bool): Whether to synthesize a response.</span>
<span class="sd">    response_synthesis_prompt (BasePromptTemplate): The response synthesis prompt</span>
<span class="sd">        to use.</span>
<span class="sd">    table_name (str): The table name to use.</span>
<span class="sd">    verbose (bool): Whether to print verbose output.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">list_of_dict</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">jsonalyze_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">analyzer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSQLParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">synthesize_response</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">response_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TABLE_NAME</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_list_of_dict</span> <span class="o">=</span> <span class="n">list_of_dict</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_jsonalyze_prompt</span> <span class="o">=</span> <span class="n">jsonalyze_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_JSONALYZE_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span> <span class="o">=</span> <span class="n">use_async</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_analyzer</span> <span class="o">=</span> <span class="n">load_jsonalyzer</span><span class="p">(</span><span class="n">use_async</span><span class="p">,</span> <span class="n">analyzer</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span> <span class="o">=</span> <span class="n">sql_parser</span> <span class="ow">or</span> <span class="n">DefaultSQLParser</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_synthesize_response</span> <span class="o">=</span> <span class="n">synthesize_response</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">response_synthesis_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_RESPONSE_SYNTHESIS_PROMPT</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table_name</span> <span class="o">=</span> <span class="n">table_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"jsonalyze_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jsonalyze_prompt</span><span class="p">,</span>
            <span class="s2">"response_synthesis_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"jsonalyze_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_jsonalyze_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"jsonalyze_prompt"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"response_synthesis_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"response_synthesis_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer an analytical query on the JSON List."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

        <span class="c1"># Perform the analysis</span>
        <span class="n">sql_query</span><span class="p">,</span> <span class="n">table_schema</span><span class="p">,</span> <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_analyzer</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_list_of_dict</span><span class="p">,</span>
            <span class="n">query_bundle</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_name</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_jsonalyze_prompt</span><span class="p">,</span>
            <span class="n">sql_parser</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL Query: </span><span class="si">{</span><span class="n">sql_query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Table Schema: </span><span class="si">{</span><span class="n">table_schema</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"cyan"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL Response: </span><span class="si">{</span><span class="n">results</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_synthesize_response</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span><span class="p">,</span>
                <span class="n">sql_query</span><span class="o">=</span><span class="n">sql_query</span><span class="p">,</span>
                <span class="n">table_schema</span><span class="o">=</span><span class="n">table_schema</span><span class="p">,</span>
                <span class="n">sql_response</span><span class="o">=</span><span class="n">results</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Response: </span><span class="si">{</span><span class="n">response_str</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"magenta"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
        <span class="n">response_metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query</span><span class="p">,</span> <span class="s2">"table_schema"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">table_schema</span><span class="p">)}</span>

        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer an analytical query on the JSON List."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

        <span class="c1"># Perform the analysis</span>
        <span class="n">sql_query</span><span class="p">,</span> <span class="n">table_schema</span><span class="p">,</span> <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_analyzer</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_list_of_dict</span><span class="p">,</span>
            <span class="n">query</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_name</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_jsonalyze_prompt</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL Query: </span><span class="si">{</span><span class="n">sql_query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Table Schema: </span><span class="si">{</span><span class="n">table_schema</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"cyan"</span><span class="p">)</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SQL Response: </span><span class="si">{</span><span class="n">results</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_synthesize_response</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span><span class="p">,</span>
                <span class="n">sql_query</span><span class="o">=</span><span class="n">sql_query</span><span class="p">,</span>
                <span class="n">table_schema</span><span class="o">=</span><span class="n">table_schema</span><span class="p">,</span>
                <span class="n">sql_response</span><span class="o">=</span><span class="n">results</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Response: </span><span class="si">{</span><span class="n">response_str</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"magenta"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query</span><span class="p">,</span>
                    <span class="s2">"table_schema"</span><span class="p">:</span> <span class="n">table_schema</span><span class="p">,</span>
                    <span class="s2">"sql_response"</span><span class="p">:</span> <span class="n">results</span><span class="p">,</span>
                <span class="p">}</span>
            <span class="p">)</span>
        <span class="n">response_metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query</span><span class="p">,</span> <span class="s2">"table_schema"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">table_schema</span><span class="p">)}</span>

        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous FLARE](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/)[Next NL SQL table](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/)
