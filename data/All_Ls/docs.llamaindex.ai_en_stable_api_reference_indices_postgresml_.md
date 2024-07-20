Title: Postgresml - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/

Markdown Content:
Postgresml - LlamaIndex


PostgresMLRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/#llama_index.indices.managed.postgresml.PostgresMLRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

PostgresML Retriever.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `PostgresMLIndex` | 
the PostgresML Index



 | _required_ |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-postgresml/llama_index/indices/managed/postgresml/retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
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
<span class="normal">100</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PostgresMLRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PostgresML Retriever.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (PostgresMLIndex): the PostgresML Index</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">PostgresMLIndex</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">pgml_query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">rerank</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pgml_query</span> <span class="o">=</span> <span class="n">pgml_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span> <span class="o">=</span> <span class="n">limit</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span> <span class="o">=</span> <span class="n">rerank</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">run_async_tasks</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)])[</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">async</span> <span class="k">def</span> <span class="nf">do_vector_search</span><span class="p">():</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pgml_query</span><span class="p">:</span>
                <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">vector_search</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_pgml_query</span><span class="p">,</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">pipeline</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">query_bundle</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span>
                        <span class="s2">"Must provide either query or query_bundle to retrieve and aretrieve"</span>
                    <span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span> <span class="o">|</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
                <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">vector_search</span><span class="p">(</span>
                    <span class="p">{</span>
                        <span class="s2">"query"</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">"fields"</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">"content"</span><span class="p">:</span> <span class="p">{</span>
                                    <span class="s2">"query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                                    <span class="s2">"parameters"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"prompt"</span><span class="p">:</span> <span class="s2">"query: "</span><span class="p">},</span>
                                <span class="p">}</span>
                            <span class="p">}</span>
                        <span class="p">},</span>
                        <span class="s2">"rerank"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span><span class="p">,</span>
                        <span class="s2">"limit"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">pipeline</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">do_vector_search</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">NodeWithScore</span><span class="p">(</span>
                <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"id"</span><span class="p">],</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"chunk"</span><span class="p">],</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"metadata"</span><span class="p">],</span>
                <span class="p">),</span>
                <span class="n">score</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"score"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rerank</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="k">else</span> <span class="n">NodeWithScore</span><span class="p">(</span>
                <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"id"</span><span class="p">],</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"chunk"</span><span class="p">],</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"document"</span><span class="p">][</span><span class="s2">"metadata"</span><span class="p">],</span>
                <span class="p">),</span>
                <span class="n">score</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"rerank_score"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">results</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llama cloud](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/)[Next Property graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/)
