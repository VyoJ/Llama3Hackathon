Title: Custom - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/

Markdown Content:
Custom - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Custom query component.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">243</span>
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
<span class="normal">297</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CustomQueryComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Custom query component."""</span>

    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Callback manager"</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># NOTE: user can override this method to validate inputs</span>
        <span class="c1"># but we do this by default for convenience</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"This component does not support async run."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Input keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_optional_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Optional input keys dict."""</span>
        <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Output keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>

        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_input_keys</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_optional_input_keys</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.input_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.output_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.set_callback_manager "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Arg pack](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/arg_pack/)[Next Function](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/)
