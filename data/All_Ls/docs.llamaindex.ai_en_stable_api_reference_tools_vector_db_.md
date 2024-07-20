Title: Vector db - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/

Markdown Content:
Vector db - LlamaIndex


VectorDBToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/#llama_index.tools.vector_db.VectorDBToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Vector DB tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-vector-db/llama_index/tools/vector_db/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorDBToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vector DB tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"auto_retrieve_fn"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseIndex</span><span class="p">,</span>  <span class="c1"># TODO typing</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>

    <span class="k">def</span> <span class="nf">auto_retrieve_fn</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">filter_key_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">filter_value_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Auto retrieval function.</span>

<span class="sd">        Performs auto-retrieval from a vector database, and then applies a set of filters.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to search</span>
<span class="sd">            top_k (int): The number of results to retrieve</span>
<span class="sd">            filter_key_list (List[str]): The list of filter keys</span>
<span class="sd">            filter_value_list (List[str]): The list of filter values</span>
<span class="sd">        """</span>
        <span class="n">exact_match_filters</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ExactMatchFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="n">v</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">filter_key_list</span><span class="p">,</span> <span class="n">filter_value_list</span><span class="p">)</span>
        <span class="p">]</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">MetadataFilters</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="n">exact_match_filters</span><span class="p">),</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="n">retriever</span><span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### auto\_retrieve\_fn [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/#llama_index.tools.vector_db.VectorDBToolSpec.auto_retrieve_fn "Permanent link")

```
auto_retrieve_fn(query: str, top_k: int, filter_key_list: List[str], filter_value_list: List[str]) -> str
```

Auto retrieval function.

Performs auto-retrieval from a vector database, and then applies a set of filters.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to search



 | _required_ |
| `top_k` | `int` | 

The number of results to retrieve



 | _required_ |
| `filter_key_list` | `List[str]` | 

The list of filter keys



 | _required_ |
| `filter_value_list` | `List[str]` | 

The list of filter values



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-vector-db/llama_index/tools/vector_db/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">auto_retrieve_fn</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="n">filter_key_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">filter_value_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Auto retrieval function.</span>

<span class="sd">    Performs auto-retrieval from a vector database, and then applies a set of filters.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to search</span>
<span class="sd">        top_k (int): The number of results to retrieve</span>
<span class="sd">        filter_key_list (List[str]): The list of filter keys</span>
<span class="sd">        filter_value_list (List[str]): The list of filter values</span>
<span class="sd">    """</span>
    <span class="n">exact_match_filters</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">ExactMatchFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="n">v</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">filter_key_list</span><span class="p">,</span> <span class="n">filter_value_list</span><span class="p">)</span>
    <span class="p">]</span>
    <span class="n">retriever</span> <span class="o">=</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="n">MetadataFilters</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="n">exact_match_filters</span><span class="p">),</span>
        <span class="n">top_k</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="n">retriever</span><span class="p">)</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tool spec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/)[Next Waii](https://docs.llamaindex.ai/en/stable/api_reference/tools/waii/)
