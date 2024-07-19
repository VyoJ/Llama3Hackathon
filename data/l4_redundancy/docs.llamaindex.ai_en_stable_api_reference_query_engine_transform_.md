Title: Transform - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/

Markdown Content:
Transform - LlamaIndex


TransformQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/#llama_index.core.query_engine.TransformQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Transform query engine.

Applies a query transform to a query bundle before passing it to a query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
A query engine object.



 | _required_ |
| `query_transform` | `BaseQueryTransform` | 

A query transform object.



 | _required_ |
| `transform_metadata` | `Optional[dict]` | 

metadata to pass to the query transform.



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/transform_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TransformQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Transform query engine.</span>

<span class="sd">    Applies a query transform to a query bundle before passing</span>
<span class="sd">        it to a query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): A query engine object.</span>
<span class="sd">        query_transform (BaseQueryTransform): A query transform object.</span>
<span class="sd">        transform_metadata (Optional[dict]): metadata to pass to the</span>
<span class="sd">            query transform.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">query_transform</span><span class="p">:</span> <span class="n">BaseQueryTransform</span><span class="p">,</span>
        <span class="n">transform_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span> <span class="o">=</span> <span class="n">query_transform</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span> <span class="o">=</span> <span class="n">transform_metadata</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_transform"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">asynthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_transform_metadata</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tool retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/)[Next Agent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/)
