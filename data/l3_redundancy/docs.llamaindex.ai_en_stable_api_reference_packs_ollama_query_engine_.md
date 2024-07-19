Title: Ollama query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/

Markdown Content:
Ollama query engine - LlamaIndex


OllamaQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/#llama_index.packs.ollama_query_engine.OllamaQueryEnginePack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-ollama-query-engine/llama_index/packs/ollama_query_engine/base.py`

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
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OllamaQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_OLLAMA_BASE_URL</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="n">model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="n">base_url</span>

        <span class="n">llm</span> <span class="o">=</span> <span class="n">Ollama</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span><span class="p">)</span>

        <span class="n">embed_model</span> <span class="o">=</span> <span class="n">OllamaEmbedding</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span><span class="p">)</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/#llama_index.packs.ollama_query_engine.OllamaQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-ollama-query-engine/llama_index/packs/ollama_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/#llama_index.packs.ollama_query_engine.OllamaQueryEnginePack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-ollama-query-engine/llama_index/packs/ollama_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Node parser semantic chunking](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/)[Next Panel chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/)
