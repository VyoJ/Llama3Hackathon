Title: Multi modal - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/

Markdown Content:
Multi modal - LlamaIndex


Evaluation modules.

MultiModalRetrieverEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/#llama_index.core.evaluation.MultiModalRetrieverEvaluator "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetrievalEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator "llama_index.core.evaluation.retrieval.base.BaseRetrievalEvaluator")`

Retriever evaluator.

This module will evaluate a retriever using a set of metrics.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metrics` | `List[BaseRetrievalMetric]` | 
Sequence of metrics to evaluate



 | _required_ |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.indices.base_retriever.BaseRetriever")` | 

Retriever to evaluate.



 | _required_ |
| `node_postprocessors` | `Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]]` | 

Post-processor to apply after retrieval.



 | `None` |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/evaluator.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 70</span>
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
<span class="normal">134</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiModalRetrieverEvaluator</span><span class="p">(</span><span class="n">BaseRetrievalEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retriever evaluator.</span>

<span class="sd">    This module will evaluate a retriever using a set of metrics.</span>

<span class="sd">    Args:</span>
<span class="sd">        metrics (List[BaseRetrievalMetric]): Sequence of metrics to evaluate</span>
<span class="sd">        retriever: Retriever to evaluate.</span>
<span class="sd">        node_postprocessors (Optional[List[BaseNodePostprocessor]]): Post-processor to apply after retrieval.</span>

<span class="sd">    """</span>

    <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Retriever to evaluate"</span><span class="p">)</span>
    <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Optional post-processor"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">metrics</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseRetrievalMetric</span><span class="p">],</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">metrics</span><span class="o">=</span><span class="n">metrics</span><span class="p">,</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_retrieved_ids_and_texts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get retrieved ids."""</span>
        <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="n">image_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ImageNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">text_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_postprocessors</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_postprocessors</span><span class="p">:</span>
                <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                    <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query</span>
                <span class="p">)</span>

        <span class="k">for</span> <span class="n">scored_node</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">scored_node</span><span class="o">.</span><span class="n">node</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">ImageNode</span><span class="p">):</span>
                <span class="n">image_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="p">:</span>
                <span class="n">text_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">mode</span> <span class="o"></span> <span class="s2">"image"</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">image_nodes</span><span class="p">],</span>
                <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">image_nodes</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Unsupported mode."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Metrics](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/)[Next Pairwise comparison](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/)
