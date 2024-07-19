Title: Agents lats - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/

Markdown Content:
Agents lats - LlamaIndex


LATSPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/#llama_index.packs.agents_lats.LATSPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.BaseLlamaPack")`

Pack for running the LATS agent.

Source code in `llama-index-packs/llama-index-packs-agents-lats/llama_index/packs/agents_lats/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LATSPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pack for running the LATS agent."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span> <span class="o">=</span> <span class="n">LATSAgentWorker</span><span class="p">(</span><span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">AgentRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
            <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/#llama_index.packs.agents_lats.LATSPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-agents-lats/llama_index/packs/agents_lats/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
        <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/#llama_index.packs.agents_lats.LATSPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run.

Source code in `llama-index-packs/llama-index-packs-agents-lats/llama_index/packs/agents_lats/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Agents coa](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/)[Next Agents llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/)
