Title: Summary - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/

Markdown Content:
Summary - LlamaIndex


SummaryIndexRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/#llama_index.core.retrievers.SummaryIndexRetriever "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Simple retriever for SummaryIndex that returns all nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `[SummaryIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/#llama_index.core.indices.SummaryIndex "llama_index.core.indices.list.base.SummaryIndex")` | 
The index to retrieve from.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/list/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
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
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SummaryIndexRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple retriever for SummaryIndex that returns all nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (SummaryIndex): The index to retrieve from.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">SummaryIndex</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes."""</span>
        <span class="k">del</span> <span class="n">query_bundle</span>

        <span class="n">node_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">nodes</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sql](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/)[Next Transform](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/)
