Title: Cogniswitch agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/

Markdown Content:
Cogniswitch agent - LlamaIndex


CogniswitchAgentPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/#llama_index.packs.cogniswitch_agent.CogniswitchAgentPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-cogniswitch-agent/llama_index/packs/cogniswitch_agent/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
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
<span class="normal">24</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CogniswitchAgentPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cogniswitch_tool_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.tools.cogniswitch</span> <span class="kn">import</span> <span class="n">CogniswitchToolSpec</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"llama_hub not installed."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">tool_spec</span> <span class="o">=</span> <span class="n">CogniswitchToolSpec</span><span class="p">(</span><span class="o">**</span><span class="n">cogniswitch_tool_kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">ReActAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_spec</span><span class="o">.</span><span class="n">to_tool_list</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"cogniswitch_tool"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_spec</span><span class="p">,</span> <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/#llama_index.packs.cogniswitch_agent.CogniswitchAgentPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-cogniswitch-agent/llama_index/packs/cogniswitch_agent/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"cogniswitch_tool"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_spec</span><span class="p">,</span> <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/#llama_index.packs.cogniswitch_agent.CogniswitchAgentPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-cogniswitch-agent/llama_index/packs/cogniswitch_agent/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Code hierarchy](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/)[Next Cohere citation chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/)
