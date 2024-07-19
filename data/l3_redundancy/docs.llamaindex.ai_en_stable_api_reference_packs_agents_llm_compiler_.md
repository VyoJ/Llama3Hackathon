Title: Agents llm compiler - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/

Markdown Content:
Agents llm compiler - LlamaIndex


LLMCompilerAgentPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/#llama_index.packs.agents_llm_compiler.LLMCompilerAgentPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

LLMCompilerAgent pack.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tools` | `List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")]` | 
List of tools to use.



 | _required_ |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

LLM to use.



 | `None` |

Source code in `llama-index-packs/llama-index-packs-agents-llm-compiler/llama_index/packs/agents_llm_compiler/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
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
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMCompilerAgentPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMCompilerAgent pack.</span>

<span class="sd">    Args:</span>
<span class="sd">        tools (List[BaseTool]): List of tools to use.</span>
<span class="sd">        llm (Optional[LLM]): LLM to use.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">agent_worker_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">agent_runner_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span> <span class="o">=</span> <span class="n">LLMCompilerAgentWorker</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="o">**</span><span class="p">(</span><span class="n">agent_worker_kwargs</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">AgentRunner</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="o">**</span><span class="p">(</span><span class="n">agent_runner_kwargs</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"callback_manager"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
            <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/#llama_index.packs.agents_llm_compiler.LLMCompilerAgentPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-agents-llm-compiler/llama_index/packs/agents_llm_compiler/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"callback_manager"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
        <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/#llama_index.packs.agents_llm_compiler.LLMCompilerAgentPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-agents-llm-compiler/llama_index/packs/agents_llm_compiler/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Agents lats](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/)[Next Amazon product extraction](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/)
