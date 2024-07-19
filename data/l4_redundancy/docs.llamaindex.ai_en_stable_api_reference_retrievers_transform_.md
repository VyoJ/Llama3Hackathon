Title: Transform - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/

Markdown Content:
Transform - LlamaIndex


TransformRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/#llama_index.core.retrievers.TransformRetriever "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Transform Retriever.

Takes in an existing retriever and a query transform and runs the query transform before running the retriever.

Source code in `llama-index-core/llama_index/core/retrievers/transform_retriever.py`

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
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TransformRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Transform Retriever.</span>

<span class="sd">    Takes in an existing retriever and a query transform and runs the query transform</span>
<span class="sd">    before running the retriever.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">query_transform</span><span class="p">:</span> <span class="n">BaseQueryTransform</span><span class="p">,</span>
        <span class="n">transform_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span> <span class="o">=</span> <span class="n">query_transform</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span> <span class="o">=</span> <span class="n">transform_metadata</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="c1"># NOTE: don't include tools for now</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"query_transform"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Summary](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/)[Next Tree](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/)
