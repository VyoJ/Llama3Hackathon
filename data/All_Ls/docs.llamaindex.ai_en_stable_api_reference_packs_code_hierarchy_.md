Title: Code hierarchy - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/

Markdown Content:
Code hierarchy - LlamaIndex


CodeHierarchyAgentPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/#llama_index.packs.code_hierarchy.CodeHierarchyAgentPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.BaseLlamaPack")`

Code hierarchy agent pack.

Source code in `llama-index-packs/llama-index-packs-code-hierarchy/llama_index/packs/code_hierarchy/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
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
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CodeHierarchyAgentPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Code hierarchy agent pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">split_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">llm</span><span class="p">:</span> <span class="n">OpenAI</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize the code hierarchy agent pack."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.packs.code_hierarchy</span> <span class="kn">import</span> <span class="n">CodeHierarchyKeywordQueryEngine</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">CodeHierarchyKeywordQueryEngine</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">split_nodes</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"code_search"</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">"Search the code hierarchy for a specific code element, using keywords or IDs."</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">OpenAIAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">tool</span><span class="p">],</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">system_prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">get_tool_instructions</span><span class="p">(),</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"tool"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool</span><span class="p">,</span>
            <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user_message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the agent on the user message."""</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">user_message</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/#llama_index.packs.code_hierarchy.CodeHierarchyAgentPack.run "Permanent link")

```
run(user_message: str) -> str
```

Run the agent on the user message.

Source code in `llama-index-packs/llama-index-packs-code-hierarchy/llama_index/packs/code_hierarchy/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user_message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the agent on the user message."""</span>
    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">user_message</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chroma autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/chroma_autoretrieval/)[Next Cogniswitch agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/)
