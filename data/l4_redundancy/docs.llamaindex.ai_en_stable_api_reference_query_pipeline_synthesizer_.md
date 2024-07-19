Title: Synthesizer - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/

Markdown Content:
Synthesizer - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Synthesizer component.

Source code in `llama-index-core/llama_index/core/response_synthesizers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">334</span>
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
<span class="normal">383</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SynthesizerComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Synthesizer component."""</span>

    <span class="n">synthesizer</span><span class="p">:</span> <span class="n">BaseSynthesizer</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Synthesizer"</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># make sure both query_str and nodes are there</span>
        <span class="k">if</span> <span class="s2">"query_str"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'query_str'"</span><span class="p">)</span>
        <span class="nb">input</span><span class="p">[</span><span class="s2">"query_str"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"query_str"</span><span class="p">])</span>

        <span class="k">if</span> <span class="s2">"nodes"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'nodes'"</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="nb">input</span><span class="p">[</span><span class="s2">"nodes"</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input nodes must be a list"</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">NodeWithScore</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input nodes must be a list of NodeWithScore"</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s2">"query_str"</span><span class="p">],</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"nodes"</span><span class="p">])</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query_str"</span><span class="p">],</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"nodes"</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"query_str"</span><span class="p">,</span> <span class="s2">"nodes"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/#llama_index.core.response_synthesizers.base.SynthesizerComponent.input_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/#llama_index.core.response_synthesizers.base.SynthesizerComponent.output_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/#llama_index.core.response_synthesizers.base.SynthesizerComponent.set_callback_manager "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/response_synthesizers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Router](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/)[Next Tool runner](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/tool_runner/)
