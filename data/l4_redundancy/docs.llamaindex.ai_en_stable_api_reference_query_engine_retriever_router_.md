Title: Retriever router - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/

Markdown Content:
Retriever router - LlamaIndex


RetrieverRouterQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/#llama_index.core.query_engine.RetrieverRouterQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Retriever-based router query engine.

NOTE: this is deprecated, please use our new ToolRetrieverRouterQueryEngine

Use a retriever to select a set of Nodes. Each node will be converted into a ToolMetadata object, and also used to retrieve a query engine, to form a QueryEngineTool.

NOTE: this is a beta feature. We are figuring out the right interface between the retriever and query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `selector` | `BaseSelector` | 
A selector that chooses one out of many options based on each candidate's metadata and query.



 | _required_ |
| `query_engine_tools` | `Sequence[[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")]` | 

A sequence of candidate query engines. They must be wrapped as tools to expose metadata to the selector.



 | _required_ |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/router_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">269</span>
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
<span class="normal">317</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrieverRouterQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retriever-based router query engine.</span>

<span class="sd">    NOTE: this is deprecated, please use our new ToolRetrieverRouterQueryEngine</span>

<span class="sd">    Use a retriever to select a set of Nodes. Each node will be converted</span>
<span class="sd">    into a ToolMetadata object, and also used to retrieve a query engine, to form</span>
<span class="sd">    a QueryEngineTool.</span>

<span class="sd">    NOTE: this is a beta feature. We are figuring out the right interface</span>
<span class="sd">    between the retriever and query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        selector (BaseSelector): A selector that chooses one out of many options based</span>
<span class="sd">            on each candidate's metadata and query.</span>
<span class="sd">        query_engine_tools (Sequence[QueryEngineTool]): A sequence of candidate</span>
<span class="sd">            query engines. They must be wrapped as tools to expose metadata to</span>
<span class="sd">            the selector.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">node_to_query_engine_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_to_query_engine_fn</span> <span class="o">=</span> <span class="n">node_to_query_engine_fn</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="c1"># NOTE: don't include tools for now</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">nodes_with_score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="c1"># TODO: for now we only support retrieving one node</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes_with_score</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retrieved more than one node."</span><span class="p">)</span>

        <span class="n">node</span> <span class="o">=</span> <span class="n">nodes_with_score</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">node</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_to_query_engine_fn</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/)[Next Retry](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/)
