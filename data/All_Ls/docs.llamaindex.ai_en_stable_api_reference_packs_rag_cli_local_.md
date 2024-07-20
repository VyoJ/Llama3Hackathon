Title: Rag cli local - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/

Markdown Content:
Rag cli local - LlamaIndex


LocalRAGCLIPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/#llama_index.packs.rag_cli_local.LocalRAGCLIPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Local RAG CLI Pack.

Source code in `llama-index-packs/llama-index-packs-rag-cli-local/llama_index/packs/rag_cli_local/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 82</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LocalRAGCLIPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Local RAG CLI Pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm_model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"mistral"</span><span class="p">,</span>
        <span class="n">embed_model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"BAAI/bge-m3"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">persist_dir</span> <span class="o">=</span> <span class="n">persist_dir</span> <span class="ow">or</span> <span class="n">default_ragcli_persist_dir</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm_model_name</span> <span class="o">=</span> <span class="n">llm_model_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model_name</span> <span class="o">=</span> <span class="n">embed_model_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">rag_cli</span> <span class="o">=</span> <span class="n">init_local_rag_cli</span><span class="p">(</span>
            <span class="n">persist_dir</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">persist_dir</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">llm_model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm_model_name</span><span class="p">,</span>
            <span class="n">embed_model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model_name</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"rag_cli"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">rag_cli</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rag_cli</span><span class="o">.</span><span class="n">cli</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/#llama_index.packs.rag_cli_local.LocalRAGCLIPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-rag-cli-local/llama_index/packs/rag_cli_local/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"rag_cli"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">rag_cli</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/#llama_index.packs.rag_cli_local.LocalRAGCLIPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-rag-cli-local/llama_index/packs/rag_cli_local/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rag_cli</span><span class="o">.</span><span class="n">cli</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Raft dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/)[Next Rag evaluator](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/)
