Title: Metrics - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/

Markdown Content:
Metrics - LlamaIndex


Evaluation modules.

MRR [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.MRR "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseRetrievalMetric`

MRR (Mean Reciprocal Rank) metric with two calculation options.

*   The default method calculates the reciprocal rank of the first relevant retrieved document.
*   The more granular method sums the reciprocal ranks of all relevant retrieved documents and divides by the count of relevant documents.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `metric_name` | `str` | 
The name of the metric.



 |
| `use_granular_mrr` | `bool` | 

Determines whether to use the granular method for calculation.



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 75</span>
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
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MRR</span><span class="p">(</span><span class="n">BaseRetrievalMetric</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""MRR (Mean Reciprocal Rank) metric with two calculation options.</span>

<span class="sd">    - The default method calculates the reciprocal rank of the first relevant retrieved document.</span>
<span class="sd">    - The more granular method sums the reciprocal ranks of all relevant retrieved documents and divides by the count of relevant documents.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        metric_name (str): The name of the metric.</span>
<span class="sd">        use_granular_mrr (bool): Determines whether to use the granular method for calculation.</span>
<span class="sd">    """</span>

    <span class="n">metric_name</span><span class="p">:</span> <span class="n">ClassVar</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"mrr"</span>
    <span class="n">use_granular_mrr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">compute</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retrieved_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retrieved_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalMetricResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Compute MRR based on the provided inputs and selected method.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            query (Optional[str]): The query string (not used in the current implementation).</span>
<span class="sd">            expected_ids (Optional[List[str]]): Expected document IDs.</span>
<span class="sd">            retrieved_ids (Optional[List[str]]): Retrieved document IDs.</span>
<span class="sd">            expected_texts (Optional[List[str]]): Expected texts (not used in the current implementation).</span>
<span class="sd">            retrieved_texts (Optional[List[str]]): Retrieved texts (not used in the current implementation).</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If the necessary IDs are not provided.</span>

<span class="sd">        Returns:</span>
<span class="sd">            RetrievalMetricResult: The result with the computed MRR score.</span>
<span class="sd">        """</span>
        <span class="c1"># Checking for the required arguments</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">retrieved_ids</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="n">expected_ids</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="ow">not</span> <span class="n">retrieved_ids</span>
            <span class="ow">or</span> <span class="ow">not</span> <span class="n">expected_ids</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retrieved ids and expected ids must be provided"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_granular_mrr</span><span class="p">:</span>
            <span class="c1"># Granular MRR calculation: All relevant retrieved docs have their reciprocal ranks summed and averaged</span>
            <span class="n">expected_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span>
            <span class="n">reciprocal_rank_sum</span> <span class="o">=</span> <span class="mf">0.0</span>
            <span class="n">relevant_docs_count</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">retrieved_ids</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">expected_set</span><span class="p">:</span>
                    <span class="n">relevant_docs_count</span> <span class="o">+=</span> <span class="mi">1</span>
                    <span class="n">reciprocal_rank_sum</span> <span class="o">+=</span> <span class="mf">1.0</span> <span class="o">/</span> <span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
            <span class="n">mrr_score</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">reciprocal_rank_sum</span> <span class="o">/</span> <span class="n">relevant_docs_count</span>
                <span class="k">if</span> <span class="n">relevant_docs_count</span> <span class="o">&gt;</span> <span class="mi">0</span>
                <span class="k">else</span> <span class="mf">0.0</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Default MRR calculation: Reciprocal rank of the first relevant document retrieved</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="nb">id</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">retrieved_ids</span><span class="p">):</span>
                <span class="k">if</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">expected_ids</span><span class="p">:</span>
                    <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="o">/</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
            <span class="n">mrr_score</span> <span class="o">=</span> <span class="mf">0.0</span>

        <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="n">mrr_score</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### compute [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.MRR.compute "Permanent link")

```
compute(query: Optional[str] = None, expected_ids: Optional[List[str]] = None, retrieved_ids: Optional[List[str]] = None, expected_texts: Optional[List[str]] = None, retrieved_texts: Optional[List[str]] = None) -> [RetrievalMetricResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.RetrievalMetricResult "llama_index.core.evaluation.retrieval.metrics_base.RetrievalMetricResult")
```

Compute MRR based on the provided inputs and selected method.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `Optional[str]` | 
The query string (not used in the current implementation).



 | `None` |
| `expected_ids` | `Optional[List[str]]` | 

Expected document IDs.



 | `None` |
| `retrieved_ids` | `Optional[List[str]]` | 

Retrieved document IDs.



 | `None` |
| `expected_texts` | `Optional[List[str]]` | 

Expected texts (not used in the current implementation).



 | `None` |
| `retrieved_texts` | `Optional[List[str]]` | 

Retrieved texts (not used in the current implementation).



 | `None` |

**Raises:**

| Type | Description |
| --- | --- |
| `ValueError` | 
If the necessary IDs are not provided.



 |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `RetrievalMetricResult` | `[RetrievalMetricResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.RetrievalMetricResult "llama_index.core.evaluation.retrieval.metrics_base.RetrievalMetricResult")` | 
The result with the computed MRR score.



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 89</span>
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
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">compute</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retrieved_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retrieved_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalMetricResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Compute MRR based on the provided inputs and selected method.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        query (Optional[str]): The query string (not used in the current implementation).</span>
<span class="sd">        expected_ids (Optional[List[str]]): Expected document IDs.</span>
<span class="sd">        retrieved_ids (Optional[List[str]]): Retrieved document IDs.</span>
<span class="sd">        expected_texts (Optional[List[str]]): Expected texts (not used in the current implementation).</span>
<span class="sd">        retrieved_texts (Optional[List[str]]): Retrieved texts (not used in the current implementation).</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If the necessary IDs are not provided.</span>

<span class="sd">    Returns:</span>
<span class="sd">        RetrievalMetricResult: The result with the computed MRR score.</span>
<span class="sd">    """</span>
    <span class="c1"># Checking for the required arguments</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">retrieved_ids</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="ow">or</span> <span class="n">expected_ids</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="ow">or</span> <span class="ow">not</span> <span class="n">retrieved_ids</span>
        <span class="ow">or</span> <span class="ow">not</span> <span class="n">expected_ids</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retrieved ids and expected ids must be provided"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_granular_mrr</span><span class="p">:</span>
        <span class="c1"># Granular MRR calculation: All relevant retrieved docs have their reciprocal ranks summed and averaged</span>
        <span class="n">expected_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span>
        <span class="n">reciprocal_rank_sum</span> <span class="o">=</span> <span class="mf">0.0</span>
        <span class="n">relevant_docs_count</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">retrieved_ids</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">expected_set</span><span class="p">:</span>
                <span class="n">relevant_docs_count</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">reciprocal_rank_sum</span> <span class="o">+=</span> <span class="mf">1.0</span> <span class="o">/</span> <span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
        <span class="n">mrr_score</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">reciprocal_rank_sum</span> <span class="o">/</span> <span class="n">relevant_docs_count</span>
            <span class="k">if</span> <span class="n">relevant_docs_count</span> <span class="o">&gt;</span> <span class="mi">0</span>
            <span class="k">else</span> <span class="mf">0.0</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># Default MRR calculation: Reciprocal rank of the first relevant document retrieved</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="nb">id</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">retrieved_ids</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">expected_ids</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="o">/</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
        <span class="n">mrr_score</span> <span class="o">=</span> <span class="mf">0.0</span>

    <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="n">mrr_score</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

HitRate [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.HitRate "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseRetrievalMetric`

Hit rate metric: Compute hit rate with two calculation options.

*   The default method checks for a single match between any of the retrieved docs and expected docs.
*   The more granular method checks for all potential matches between retrieved docs and expected docs.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `metric_name` | `str` | 
The name of the metric.



 |
| `use_granular_hit_rate` | `bool` | 

Determines whether to use the granular method for calculation.



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
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
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HitRate</span><span class="p">(</span><span class="n">BaseRetrievalMetric</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hit rate metric: Compute hit rate with two calculation options.</span>

<span class="sd">    - The default method checks for a single match between any of the retrieved docs and expected docs.</span>
<span class="sd">    - The more granular method checks for all potential matches between retrieved docs and expected docs.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        metric_name (str): The name of the metric.</span>
<span class="sd">        use_granular_hit_rate (bool): Determines whether to use the granular method for calculation.</span>
<span class="sd">    """</span>

    <span class="n">metric_name</span><span class="p">:</span> <span class="n">ClassVar</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"hit_rate"</span>
    <span class="n">use_granular_hit_rate</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">compute</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retrieved_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retrieved_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalMetricResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Compute metric based on the provided inputs.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            query (Optional[str]): The query string (not used in the current implementation).</span>
<span class="sd">            expected_ids (Optional[List[str]]): Expected document IDs.</span>
<span class="sd">            retrieved_ids (Optional[List[str]]): Retrieved document IDs.</span>
<span class="sd">            expected_texts (Optional[List[str]]): Expected texts (not used in the current implementation).</span>
<span class="sd">            retrieved_texts (Optional[List[str]]): Retrieved texts (not used in the current implementation).</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If the necessary IDs are not provided.</span>

<span class="sd">        Returns:</span>
<span class="sd">            RetrievalMetricResult: The result with the computed hit rate score.</span>
<span class="sd">        """</span>
        <span class="c1"># Checking for the required arguments</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">retrieved_ids</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="n">expected_ids</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="ow">not</span> <span class="n">retrieved_ids</span>
            <span class="ow">or</span> <span class="ow">not</span> <span class="n">expected_ids</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retrieved ids and expected ids must be provided"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_granular_hit_rate</span><span class="p">:</span>
            <span class="c1"># Granular HitRate calculation: Calculate all hits and divide by the number of expected docs</span>
            <span class="n">expected_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span>
            <span class="n">hits</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="mi">1</span> <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">retrieved_ids</span> <span class="k">if</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">expected_set</span><span class="p">)</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">hits</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span> <span class="k">if</span> <span class="n">expected_ids</span> <span class="k">else</span> <span class="mf">0.0</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Default HitRate calculation: Check if there is a single hit</span>
            <span class="n">is_hit</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="nb">id</span> <span class="ow">in</span> <span class="n">expected_ids</span> <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">retrieved_ids</span><span class="p">)</span>
            <span class="n">score</span> <span class="o">=</span> <span class="mf">1.0</span> <span class="k">if</span> <span class="n">is_hit</span> <span class="k">else</span> <span class="mf">0.0</span>

        <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### compute [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.HitRate.compute "Permanent link")

```
compute(query: Optional[str] = None, expected_ids: Optional[List[str]] = None, retrieved_ids: Optional[List[str]] = None, expected_texts: Optional[List[str]] = None, retrieved_texts: Optional[List[str]] = None) -> [RetrievalMetricResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.RetrievalMetricResult "llama_index.core.evaluation.retrieval.metrics_base.RetrievalMetricResult")
```

Compute metric based on the provided inputs.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `Optional[str]` | 
The query string (not used in the current implementation).



 | `None` |
| `expected_ids` | `Optional[List[str]]` | 

Expected document IDs.



 | `None` |
| `retrieved_ids` | `Optional[List[str]]` | 

Retrieved document IDs.



 | `None` |
| `expected_texts` | `Optional[List[str]]` | 

Expected texts (not used in the current implementation).



 | `None` |
| `retrieved_texts` | `Optional[List[str]]` | 

Retrieved texts (not used in the current implementation).



 | `None` |

**Raises:**

| Type | Description |
| --- | --- |
| `ValueError` | 
If the necessary IDs are not provided.



 |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `RetrievalMetricResult` | `[RetrievalMetricResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.RetrievalMetricResult "llama_index.core.evaluation.retrieval.metrics_base.RetrievalMetricResult")` | 
The result with the computed hit rate score.



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">30</span>
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
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">compute</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retrieved_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retrieved_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalMetricResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Compute metric based on the provided inputs.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        query (Optional[str]): The query string (not used in the current implementation).</span>
<span class="sd">        expected_ids (Optional[List[str]]): Expected document IDs.</span>
<span class="sd">        retrieved_ids (Optional[List[str]]): Retrieved document IDs.</span>
<span class="sd">        expected_texts (Optional[List[str]]): Expected texts (not used in the current implementation).</span>
<span class="sd">        retrieved_texts (Optional[List[str]]): Retrieved texts (not used in the current implementation).</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If the necessary IDs are not provided.</span>

<span class="sd">    Returns:</span>
<span class="sd">        RetrievalMetricResult: The result with the computed hit rate score.</span>
<span class="sd">    """</span>
    <span class="c1"># Checking for the required arguments</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">retrieved_ids</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="ow">or</span> <span class="n">expected_ids</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="ow">or</span> <span class="ow">not</span> <span class="n">retrieved_ids</span>
        <span class="ow">or</span> <span class="ow">not</span> <span class="n">expected_ids</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retrieved ids and expected ids must be provided"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_granular_hit_rate</span><span class="p">:</span>
        <span class="c1"># Granular HitRate calculation: Calculate all hits and divide by the number of expected docs</span>
        <span class="n">expected_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span>
        <span class="n">hits</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="mi">1</span> <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">retrieved_ids</span> <span class="k">if</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">expected_set</span><span class="p">)</span>
        <span class="n">score</span> <span class="o">=</span> <span class="n">hits</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">expected_ids</span><span class="p">)</span> <span class="k">if</span> <span class="n">expected_ids</span> <span class="k">else</span> <span class="mf">0.0</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># Default HitRate calculation: Check if there is a single hit</span>
        <span class="n">is_hit</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="nb">id</span> <span class="ow">in</span> <span class="n">expected_ids</span> <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">retrieved_ids</span><span class="p">)</span>
        <span class="n">score</span> <span class="o">=</span> <span class="mf">1.0</span> <span class="k">if</span> <span class="n">is_hit</span> <span class="k">else</span> <span class="mf">0.0</span>

    <span class="k">return</span> <span class="n">RetrievalMetricResult</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RetrievalMetricResult [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.RetrievalMetricResult "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Metric result.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `score` | `float` | 
Score for the metric



 |
| `metadata` | `Dict[str, Any]` | 

Metadata for the metric result



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics_base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">27</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrievalMetricResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Metric result.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        score (float): Score for the metric</span>
<span class="sd">        metadata (Dict[str, Any]): Metadata for the metric result</span>

<span class="sd">    """</span>

    <span class="n">score</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Score for the metric"</span><span class="p">)</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Metadata for the metric result"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""String representation."""</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"Score: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">score</span><span class="si">}</span><span class="se">\n</span><span class="s2">Metadata: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="fm">__float__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Float representation."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span>
</code></pre></div></td></tr></tbody></table>

resolve\_metrics [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/#llama_index.core.evaluation.resolve_metrics "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

```
resolve_metrics(metrics: List[str]) -> List[Type[BaseRetrievalMetric]]
```

Resolve metrics from list of metric names.

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/metrics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">resolve_metrics</span><span class="p">(</span><span class="n">metrics</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseRetrievalMetric</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Resolve metrics from list of metric names."""</span>
    <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="n">metrics</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">metric</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">METRIC_REGISTRY</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid metric name: </span><span class="si">{</span><span class="n">metric</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">METRIC_REGISTRY</span><span class="p">[</span><span class="n">metric</span><span class="p">]</span> <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="n">metrics</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/)[Next Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/)
