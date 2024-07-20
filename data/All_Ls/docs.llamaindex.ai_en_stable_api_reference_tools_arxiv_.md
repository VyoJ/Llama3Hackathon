Title: Arxiv - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/

Markdown Content:
Arxiv - LlamaIndex


ArxivToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/#llama_index.tools.arxiv.ArxivToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

arXiv tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-arxiv/llama_index/tools/arxiv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
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
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ArxivToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""arXiv tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"arxiv_query"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_results</span> <span class="o">=</span> <span class="n">max_results</span>

    <span class="k">def</span> <span class="nf">arxiv_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">sort_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"relevance"</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        A tool to query arxiv.org</span>
<span class="sd">        ArXiv contains a variety of papers that are useful for answering</span>
<span class="sd">        mathematic and scientific questions.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to arXiv.</span>
<span class="sd">            sort_by (str): Either 'relevance' (default) or 'recent'</span>

<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">arxiv</span>

        <span class="n">sort</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">Relevance</span>
        <span class="k">if</span> <span class="n">sort_by</span> <span class="o"></span> <span class="s2">"recent"</span><span class="p">:</span>
        <span class="n">sort</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">SubmittedDate</span>
    <span class="n">search</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">max_results</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_results</span><span class="p">,</span> <span class="n">sort_by</span><span class="o">=</span><span class="n">sort</span><span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search</span><span class="o">.</span><span class="n">results</span><span class="p">():</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">pdf_url</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Zep](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/)[Next Azure code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/)
