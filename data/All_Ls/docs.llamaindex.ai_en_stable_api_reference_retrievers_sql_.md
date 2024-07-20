Title: Sql - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/

Markdown Content:
Sql - LlamaIndex


NLSQLRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`, `PromptMixin`

Text-to-SQL Retriever.

Retrieves via text.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_database` | `SQLDatabase` | 
SQL database.



 | _required_ |
| `text_to_sql_prompt` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 

Prompt template for text-to-sql. Defaults to DEFAULT\_TEXT\_TO\_SQL\_PROMPT.



 | `None` |
| `context_query_kwargs` | `dict` | 

Mapping from table name to context query. Defaults to None.



 | `None` |
| `tables` | `Union[List[str], List[Table]]` | 

List of table names or Table objects.



 | `None` |
| `table_retriever` | `[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[SQLTableSchema](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableSchema "llama_index.core.objects.table_node_mapping.SQLTableSchema")]` | 

Object retriever for SQLTableSchema objects. Defaults to None.



 | `None` |
| `context_str_prefix` | `str` | 

Prefix for context string. Defaults to None.



 | `None` |
| `service_context` | `ServiceContext` | 

Service context. Defaults to None.



 | `None` |
| `return_raw` | `bool` | 

Whether to return plain-text dump of SQL results, or parsed into Nodes.



 | `True` |
| `handle_sql_errors` | `bool` | 

Whether to handle SQL errors. Defaults to True.



 | `True` |
| `sql_only` | `bool) ` | 

Whether to get only sql and not the sql query result. Default to False.



 | `False` |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

Language model to use.



 | `None` |

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">184</span>
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
<span class="normal">426</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NLSQLRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">,</span> <span class="n">PromptMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Text-to-SQL Retriever.</span>

<span class="sd">    Retrieves via text.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_database (SQLDatabase): SQL database.</span>
<span class="sd">        text_to_sql_prompt (BasePromptTemplate): Prompt template for text-to-sql.</span>
<span class="sd">            Defaults to DEFAULT_TEXT_TO_SQL_PROMPT.</span>
<span class="sd">        context_query_kwargs (dict): Mapping from table name to context query.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        tables (Union[List[str], List[Table]]): List of table names or Table objects.</span>
<span class="sd">        table_retriever (ObjectRetriever[SQLTableSchema]): Object retriever for</span>
<span class="sd">            SQLTableSchema objects. Defaults to None.</span>
<span class="sd">        context_str_prefix (str): Prefix for context string. Defaults to None.</span>
<span class="sd">        service_context (ServiceContext): Service context. Defaults to None.</span>
<span class="sd">        return_raw (bool): Whether to return plain-text dump of SQL results, or parsed into Nodes.</span>
<span class="sd">        handle_sql_errors (bool): Whether to handle SQL errors. Defaults to True.</span>
<span class="sd">        sql_only (bool) : Whether to get only sql and not the sql query result.</span>
<span class="sd">            Default to False.</span>
<span class="sd">        llm (Optional[LLM]): Language model to use.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">,</span>
        <span class="n">text_to_sql_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_query_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Table</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_str_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_parser_mode</span><span class="p">:</span> <span class="n">SQLParserMode</span> <span class="o">=</span> <span class="n">SQLParserMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">return_raw</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">handle_sql_errors</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">sql_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span> <span class="o">=</span> <span class="n">SQLRetriever</span><span class="p">(</span><span class="n">sql_database</span><span class="p">,</span> <span class="n">return_raw</span><span class="o">=</span><span class="n">return_raw</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span> <span class="o">=</span> <span class="n">sql_database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_get_tables</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_get_tables_fn</span><span class="p">(</span>
            <span class="n">sql_database</span><span class="p">,</span> <span class="n">tables</span><span class="p">,</span> <span class="n">context_query_kwargs</span><span class="p">,</span> <span class="n">table_retriever</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_context_str_prefix</span> <span class="o">=</span> <span class="n">context_str_prefix</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span> <span class="o">=</span> <span class="n">text_to_sql_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_TO_SQL_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser_mode</span> <span class="o">=</span> <span class="n">sql_parser_mode</span>

        <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sql_parser</span><span class="p">(</span><span class="n">sql_parser_mode</span><span class="p">,</span> <span class="n">embed_model</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_handle_sql_errors</span> <span class="o">=</span> <span class="n">handle_sql_errors</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_only</span> <span class="o">=</span> <span class="n">sql_only</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"text_to_sql_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"text_to_sql_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"text_to_sql_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_load_sql_parser</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sql_parser_mode</span><span class="p">:</span> <span class="n">SQLParserMode</span><span class="p">,</span> <span class="n">embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseSQLParser</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load SQL parser."""</span>
        <span class="k">if</span> <span class="n">sql_parser_mode</span> <span class="o"></span> <span class="n">SQLParserMode</span><span class="o">.</span><span class="n">PGVECTOR</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PGVectorSQLParser</span><span class="p">(</span><span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown SQL parser mode: </span><span class="si">{</span><span class="n">sql_parser_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_get_tables_fn</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">,</span>
        <span class="n">tables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Table</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_query_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Load get_tables function."""</span>
        <span class="n">context_query_kwargs</span> <span class="o">=</span> <span class="n">context_query_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">table_retriever</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="k">lambda</span> <span class="n">query_str</span><span class="p">:</span> <span class="n">cast</span><span class="p">(</span><span class="n">Any</span><span class="p">,</span> <span class="n">table_retriever</span><span class="p">)</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">tables</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">table_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">t</span><span class="o">.</span><span class="n">name</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">Table</span><span class="p">)</span> <span class="k">else</span> <span class="n">t</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tables</span>
                <span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">table_names</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">sql_database</span><span class="o">.</span><span class="n">get_usable_table_names</span><span class="p">())</span>
            <span class="n">context_strs</span> <span class="o">=</span> <span class="p">[</span><span class="n">context_query_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">table_names</span><span class="p">]</span>
            <span class="n">table_schemas</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">SQLTableSchema</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">t</span><span class="p">,</span> <span class="n">context_str</span><span class="o">=</span><span class="n">c</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">t</span><span class="p">,</span> <span class="n">c</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">table_names</span><span class="p">,</span> <span class="n">context_strs</span><span class="p">)</span>
            <span class="p">]</span>
            <span class="k">return</span> <span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="n">table_schemas</span>

    <span class="k">def</span> <span class="nf">retrieve_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve with metadata."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
        <span class="n">table_desc_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_table_context</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">table_desc_str</span><span class="p">,</span>
            <span class="n">dialect</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">dialect</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">sql_query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span><span class="o">.</span><span class="n">parse_response_to_sql</span><span class="p">(</span>
            <span class="n">response_str</span><span class="p">,</span> <span class="n">query_bundle</span>
        <span class="p">)</span>
        <span class="c1"># assume that it's a valid SQL query</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_only</span><span class="p">:</span>
            <span class="n">sql_only_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">sql_only_node</span><span class="p">)]</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"result"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span><span class="o">.</span><span class="n">retrieve_with_metadata</span><span class="p">(</span>
                    <span class="n">sql_query_str</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">BaseException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="c1"># if handle_sql_errors is True, then return error message</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_sql_errors</span><span class="p">:</span>
                    <span class="n">err_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
                    <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">err_node</span><span class="p">)]</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span>

        <span class="k">return</span> <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">,</span> <span class="o">**</span><span class="n">metadata</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Async retrieve with metadata."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
        <span class="n">table_desc_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_table_context</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">response_str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">table_desc_str</span><span class="p">,</span>
            <span class="n">dialect</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">dialect</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">sql_query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span><span class="o">.</span><span class="n">parse_response_to_sql</span><span class="p">(</span>
            <span class="n">response_str</span><span class="p">,</span> <span class="n">query_bundle</span>
        <span class="p">)</span>
        <span class="c1"># assume that it's a valid SQL query</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_only</span><span class="p">:</span>
            <span class="n">sql_only_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">sql_only_node</span><span class="p">)]</span>
            <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="p">(</span>
                    <span class="n">retrieved_nodes</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="p">,</span>
                <span class="p">)</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span><span class="o">.</span><span class="n">aretrieve_with_metadata</span><span class="p">(</span><span class="n">sql_query_str</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">BaseException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="c1"># if handle_sql_errors is True, then return error message</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_sql_errors</span><span class="p">:</span>
                    <span class="n">err_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
                    <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">err_node</span><span class="p">)]</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span>
        <span class="k">return</span> <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">,</span> <span class="o">**</span><span class="n">metadata</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query."""</span>
        <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_with_metadata</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retrieved_nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Async retrieve nodes given query."""</span>
        <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aretrieve_with_metadata</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retrieved_nodes</span>

    <span class="k">def</span> <span class="nf">_get_table_context</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get table context.</span>

<span class="sd">        Get tables schema + optional context as a single string.</span>

<span class="sd">        """</span>
        <span class="n">table_schema_objs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tables</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">context_strs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_str_prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">context_strs</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_context_str_prefix</span><span class="p">]</span>

        <span class="k">for</span> <span class="n">table_schema_obj</span> <span class="ow">in</span> <span class="n">table_schema_objs</span><span class="p">:</span>
            <span class="n">table_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">get_single_table_info</span><span class="p">(</span>
                <span class="n">table_schema_obj</span><span class="o">.</span><span class="n">table_name</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="n">table_schema_obj</span><span class="o">.</span><span class="n">context_str</span><span class="p">:</span>
                <span class="n">table_opt_context</span> <span class="o">=</span> <span class="s2">" The table description is: "</span>
                <span class="n">table_opt_context</span> <span class="o">+=</span> <span class="n">table_schema_obj</span><span class="o">.</span><span class="n">context_str</span>
                <span class="n">table_info</span> <span class="o">+=</span> <span class="n">table_opt_context</span>

            <span class="n">context_strs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">table_info</span><span class="p">)</span>

        <span class="k">return</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">context_strs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_with\_metadata [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever.retrieve_with_metadata "Permanent link")

```
retrieve_with_metadata(str_or_query_bundle: QueryType) -> Tuple[List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")], Dict]
```

Retrieve with metadata.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">301</span>
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
<span class="normal">347</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_with_metadata</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve with metadata."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
    <span class="n">table_desc_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_table_context</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span><span class="p">,</span>
        <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">schema</span><span class="o">=</span><span class="n">table_desc_str</span><span class="p">,</span>
        <span class="n">dialect</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">dialect</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">sql_query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span><span class="o">.</span><span class="n">parse_response_to_sql</span><span class="p">(</span>
        <span class="n">response_str</span><span class="p">,</span> <span class="n">query_bundle</span>
    <span class="p">)</span>
    <span class="c1"># assume that it's a valid SQL query</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_only</span><span class="p">:</span>
        <span class="n">sql_only_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">sql_only_node</span><span class="p">)]</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"result"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">}</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span><span class="o">.</span><span class="n">retrieve_with_metadata</span><span class="p">(</span>
                <span class="n">sql_query_str</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">BaseException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># if handle_sql_errors is True, then return error message</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_sql_errors</span><span class="p">:</span>
                <span class="n">err_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">err_node</span><span class="p">)]</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>

    <span class="k">return</span> <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">,</span> <span class="o">**</span><span class="n">metadata</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### aretrieve\_with\_metadata `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever.aretrieve_with_metadata "Permanent link")

```
aretrieve_with_metadata(str_or_query_bundle: QueryType) -> Tuple[List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")], Dict]
```

Async retrieve with metadata.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">349</span>
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
<span class="normal">391</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve_with_metadata</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Async retrieve with metadata."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
    <span class="n">table_desc_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_table_context</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Table desc str: </span><span class="si">{</span><span class="n">table_desc_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">response_str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_sql_prompt</span><span class="p">,</span>
        <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">schema</span><span class="o">=</span><span class="n">table_desc_str</span><span class="p">,</span>
        <span class="n">dialect</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">dialect</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">sql_query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_parser</span><span class="o">.</span><span class="n">parse_response_to_sql</span><span class="p">(</span>
        <span class="n">response_str</span><span class="p">,</span> <span class="n">query_bundle</span>
    <span class="p">)</span>
    <span class="c1"># assume that it's a valid SQL query</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Predicted SQL query: </span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_only</span><span class="p">:</span>
        <span class="n">sql_only_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sql_query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">sql_only_node</span><span class="p">)]</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="p">(</span>
                <span class="n">retrieved_nodes</span><span class="p">,</span>
                <span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span><span class="o">.</span><span class="n">aretrieve_with_metadata</span><span class="p">(</span><span class="n">sql_query_str</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">BaseException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># if handle_sql_errors is True, then return error message</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_sql_errors</span><span class="p">:</span>
                <span class="n">err_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">err_node</span><span class="p">)]</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>
    <span class="k">return</span> <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">sql_query_str</span><span class="p">,</span> <span class="o">**</span><span class="n">metadata</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

SQLParserMode [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.SQLParserMode "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

SQL Parser Mode.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLParserMode</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SQL Parser Mode."""</span>

    <span class="n">DEFAULT</span> <span class="o">=</span> <span class="s2">"default"</span>
    <span class="n">PGVECTOR</span> <span class="o">=</span> <span class="s2">"pgvector"</span>
</code></pre></div></td></tr></tbody></table>

SQLRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.SQLRetriever "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

SQL Retriever.

Retrieves via raw SQL statements.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_database` | `SQLDatabase` | 
SQL database.



 | _required_ |
| `return_raw` | `bool` | 

Whether to return raw results or format results. Defaults to True.



 | `True` |

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 38</span>
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
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SQL Retriever.</span>

<span class="sd">    Retrieves via raw SQL statements.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_database (SQLDatabase): SQL database.</span>
<span class="sd">        return_raw (bool): Whether to return raw results or format results.</span>
<span class="sd">            Defaults to True.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">,</span>
        <span class="n">return_raw</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span> <span class="o">=</span> <span class="n">sql_database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_return_raw</span> <span class="o">=</span> <span class="n">return_raw</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_format_node_results</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]],</span> <span class="n">col_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format node results."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="c1"># associate column keys with result tuple</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">col_keys</span><span class="p">,</span> <span class="n">result</span><span class="p">))</span>
            <span class="c1"># NOTE: leave text field blank for now</span>
            <span class="n">text_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">text_node</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">retrieve_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve with metadata."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
        <span class="n">raw_response_str</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">run_sql</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_return_raw</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">raw_response_str</span><span class="p">,</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                            <span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                            <span class="s2">"result"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"result"</span><span class="p">],</span>
                            <span class="s2">"col_keys"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"col_keys"</span><span class="p">],</span>
                        <span class="p">},</span>
                        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="p">[</span>
                            <span class="s2">"sql_query"</span><span class="p">,</span>
                            <span class="s2">"result"</span><span class="p">,</span>
                            <span class="s2">"col_keys"</span><span class="p">,</span>
                        <span class="p">],</span>
                        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"sql_query"</span><span class="p">,</span> <span class="s2">"result"</span><span class="p">,</span> <span class="s2">"col_keys"</span><span class="p">],</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="p">],</span> <span class="n">metadata</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># return formatted</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"result"</span><span class="p">]</span>
            <span class="n">col_keys</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"col_keys"</span><span class="p">]</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_node_results</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="n">col_keys</span><span class="p">),</span> <span class="n">metadata</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_with_metadata</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query."""</span>
        <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_with_metadata</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retrieved_nodes</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_with\_metadata [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.SQLRetriever.retrieve_with_metadata "Permanent link")

```
retrieve_with_metadata(str_or_query_bundle: QueryType) -> Tuple[List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")], Dict]
```

Retrieve with metadata.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 78</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_with_metadata</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve with metadata."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
    <span class="n">raw_response_str</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">run_sql</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_return_raw</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">NodeWithScore</span><span class="p">(</span>
                <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">raw_response_str</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"sql_query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                        <span class="s2">"result"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"result"</span><span class="p">],</span>
                        <span class="s2">"col_keys"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"col_keys"</span><span class="p">],</span>
                    <span class="p">},</span>
                    <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="p">[</span>
                        <span class="s2">"sql_query"</span><span class="p">,</span>
                        <span class="s2">"result"</span><span class="p">,</span>
                        <span class="s2">"col_keys"</span><span class="p">,</span>
                    <span class="p">],</span>
                    <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"sql_query"</span><span class="p">,</span> <span class="s2">"result"</span><span class="p">,</span> <span class="s2">"col_keys"</span><span class="p">],</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="p">],</span> <span class="n">metadata</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># return formatted</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"result"</span><span class="p">]</span>
        <span class="n">col_keys</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"col_keys"</span><span class="p">]</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_node_results</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="n">col_keys</span><span class="p">),</span> <span class="n">metadata</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Router](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)[Next Summary](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/)
