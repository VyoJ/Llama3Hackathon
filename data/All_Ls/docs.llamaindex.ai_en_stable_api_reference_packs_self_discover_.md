Title: Self discover - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/

Markdown Content:
Self discover - LlamaIndex


SelfDiscoverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/#llama_index.packs.self_discover.SelfDiscoverPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Self-Discover Pack.

Source code in `llama-index-packs/llama-index-packs-self-discover/llama_index/packs/self_discover/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">144</span>
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
<span class="normal">167</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SelfDiscoverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Self-Discover Pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span> <span class="o">=</span> <span class="n">_REASONING_MODULES</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"reasoning_modules"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Runs the configured pipeline for a specified task and reasoning modules."""</span>
        <span class="n">configurator</span> <span class="o">=</span> <span class="n">PipelineConfigurator</span><span class="p">(</span>
            <span class="n">task</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span>
        <span class="p">)</span>
        <span class="n">pipeline</span> <span class="o">=</span> <span class="n">configurator</span><span class="o">.</span><span class="n">configure</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="n">reasoning_modules</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/#llama_index.packs.self_discover.SelfDiscoverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-self-discover/llama_index/packs/self_discover/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"reasoning_modules"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/#llama_index.packs.self_discover.SelfDiscoverPack.run "Permanent link")

```
run(task)
```

Runs the configured pipeline for a specified task and reasoning modules.

Source code in `llama-index-packs/llama-index-packs-self-discover/llama_index/packs/self_discover/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Runs the configured pipeline for a specified task and reasoning modules."""</span>
    <span class="n">configurator</span> <span class="o">=</span> <span class="n">PipelineConfigurator</span><span class="p">(</span>
        <span class="n">task</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span>
    <span class="p">)</span>
    <span class="n">pipeline</span> <span class="o">=</span> <span class="n">configurator</span><span class="o">.</span><span class="n">configure</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="n">reasoning_modules</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reasoning_modules</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Secgpt](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/)[Next Self rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_rag/)
