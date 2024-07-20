Title: Langchain - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/

Markdown Content:
Langchain - LlamaIndex


Node parsers.

LangchainNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/#llama_index.core.node_parser.LangchainNodeParser "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `TextSplitter`

Basic wrapper around langchain's text splitter.

TODO: Figure out how to make this metadata aware.

Source code in `llama-index-core/llama_index/core/node_parser/text/langchain.py`

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
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LangchainNodeParser</span><span class="p">(</span><span class="n">TextSplitter</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Basic wrapper around langchain's text splitter.</span>

<span class="sd">    TODO: Figure out how to make this metadata aware.</span>
<span class="sd">    """</span>

    <span class="n">_lc_splitter</span><span class="p">:</span> <span class="s2">"LC_TextSplitter"</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">lc_splitter</span><span class="p">:</span> <span class="s2">"LC_TextSplitter"</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">(),</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_lc_splitter</span> <span class="o">=</span> <span class="n">lc_splitter</span>

    <span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Split text into sentences."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lc_splitter</span><span class="o">.</span><span class="n">split_text</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### split\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/#llama_index.core.node_parser.LangchainNodeParser.split_text "Permanent link")

```
split_text(text: str) -> List[str]
```

Split text into sentences.

Source code in `llama-index-core/llama_index/core/node_parser/text/langchain.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Split text into sentences."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lc_splitter</span><span class="o">.</span><span class="n">split_text</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Json](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/)[Next Markdown](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown/)
