Title: Tool retriever router - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/

Markdown Content:
Tool retriever router - LlamaIndex


ToolRetrieverRouterQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/#llama_index.core.query_engine.ToolRetrieverRouterQueryEngine "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Tool Retriever router query engine.

Selects a set of candidate query engines to execute a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")` | 
A retriever that retrieves a set of query engine tools.



 | _required_ |
| `service_context` | `Optional[ServiceContext]` | 

A service context.



 | `None` |
| `summarizer` | `Optional[[TreeSummarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/#llama_index.core.response_synthesizers.TreeSummarize "llama_index.core.response_synthesizers.TreeSummarize")]` | 

Tree summarizer to summarize sub-results.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/router_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">320</span>
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
<span class="normal">404</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ToolRetrieverRouterQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tool Retriever router query engine.</span>

<span class="sd">    Selects a set of candidate query engines to execute a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (ObjectRetriever): A retriever that retrieves a set of</span>
<span class="sd">            query engine tools.</span>
<span class="sd">        service_context (Optional[ServiceContext]): A service context.</span>
<span class="sd">        summarizer (Optional[TreeSummarize]): Tree summarizer to summarize sub-results.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summarizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TreeSummarize</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span> <span class="o">=</span> <span class="n">summarizer</span> <span class="ow">or</span> <span class="n">TreeSummarize</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">summary_template</span><span class="o">=</span><span class="n">DEFAULT_TREE_SUMMARIZE_PROMPT_SEL</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="c1"># NOTE: don't include tools for now</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"summarizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">query_engine_tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="n">responses</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">query_engine_tool</span> <span class="ow">in</span> <span class="n">query_engine_tools</span><span class="p">:</span>
                <span class="n">query_engine</span> <span class="o">=</span> <span class="n">query_engine_tool</span><span class="o">.</span><span class="n">query_engine</span>
                <span class="n">responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">responses</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">final_response</span> <span class="o">=</span> <span class="n">combine_responses</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">query_bundle</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">final_response</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

            <span class="c1"># add selected result</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"retrieved_tools"</span><span class="p">]</span> <span class="o">=</span> <span class="n">query_engine_tools</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">query_engine_tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">query_engine_tool</span> <span class="ow">in</span> <span class="n">query_engine_tools</span><span class="p">:</span>
                <span class="n">query_engine</span> <span class="o">=</span> <span class="n">query_engine_tool</span><span class="o">.</span><span class="n">query_engine</span>
                <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>
            <span class="n">responses</span> <span class="o">=</span> <span class="n">run_async_tasks</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">responses</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">final_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">acombine_responses</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">query_bundle</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">final_response</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

            <span class="c1"># add selected result</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"retrieved_tools"</span><span class="p">]</span> <span class="o">=</span> <span class="n">query_engine_tools</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sub question](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/)[Next Transform](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/)
