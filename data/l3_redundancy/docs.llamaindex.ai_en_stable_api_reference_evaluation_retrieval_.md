Title: Retrieval - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/

Markdown Content:
Retrieval - LlamaIndex


Evaluation modules.

BaseRetrievalEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base Retrieval Evaluator class.

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 78</span>
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
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseRetrievalEvaluator</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base Retrieval Evaluator class."""</span>

    <span class="n">metrics</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseRetrievalMetric</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"List of metrics to evaluate"</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_metric_names</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">metric_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseRetrievalEvaluator"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create evaluator from metric names.</span>

<span class="sd">        Args:</span>
<span class="sd">            metric_names (List[str]): List of metric names</span>
<span class="sd">            **kwargs: Additional arguments for the evaluator</span>

<span class="sd">        """</span>
        <span class="n">metric_types</span> <span class="o">=</span> <span class="n">resolve_metrics</span><span class="p">(</span><span class="n">metric_names</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="n">metric</span><span class="p">()</span> <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="n">metric_types</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_retrieved_ids_and_texts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get retrieved ids and texts."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation results with query string and expected ids.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): Query string</span>
<span class="sd">            expected_ids (List[str]): Expected ids</span>

<span class="sd">        Returns:</span>
<span class="sd">            RetrievalEvalResult: Evaluation result</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span>
                <span class="n">expected_texts</span><span class="o">=</span><span class="n">expected_texts</span><span class="p">,</span>
                <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="c1"># @abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">        and generated response string.</span>

<span class="sd">        Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">        take in additional arguments.</span>
<span class="sd">        """</span>
        <span class="n">retrieved_ids</span><span class="p">,</span> <span class="n">retrieved_texts</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_retrieved_ids_and_texts</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">mode</span>
        <span class="p">)</span>
        <span class="n">metric_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">metrics</span><span class="p">:</span>
            <span class="n">eval_result</span> <span class="o">=</span> <span class="n">metric</span><span class="o">.</span><span class="n">compute</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">,</span> <span class="n">retrieved_ids</span><span class="p">,</span> <span class="n">expected_texts</span><span class="p">,</span> <span class="n">retrieved_texts</span>
            <span class="p">)</span>
            <span class="n">metric_dict</span><span class="p">[</span><span class="n">metric</span><span class="o">.</span><span class="n">metric_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">eval_result</span>

        <span class="k">return</span> <span class="n">RetrievalEvalResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span>
            <span class="n">expected_texts</span><span class="o">=</span><span class="n">expected_texts</span><span class="p">,</span>
            <span class="n">retrieved_ids</span><span class="o">=</span><span class="n">retrieved_ids</span><span class="p">,</span>
            <span class="n">retrieved_texts</span><span class="o">=</span><span class="n">retrieved_texts</span><span class="p">,</span>
            <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
            <span class="n">metric_dict</span><span class="o">=</span><span class="n">metric_dict</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">dataset</span><span class="p">:</span> <span class="n">EmbeddingQAFinetuneDataset</span><span class="p">,</span>
        <span class="n">workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RetrievalEvalResult</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with dataset."""</span>
        <span class="n">semaphore</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="n">workers</span><span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">eval_worker</span><span class="p">(</span>
            <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span>
        <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">semaphore</span><span class="p">:</span>
                <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">)</span>

        <span class="n">response_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">mode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">dataset</span><span class="o">.</span><span class="n">mode</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">query_id</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">dataset</span><span class="o">.</span><span class="n">queries</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">expected_ids</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">relevant_docs</span><span class="p">[</span><span class="n">query_id</span><span class="p">]</span>
            <span class="n">response_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">eval_worker</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">,</span> <span class="n">mode</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">tqdm.asyncio</span> <span class="kn">import</span> <span class="n">tqdm_asyncio</span>

            <span class="n">eval_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">tqdm_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">eval_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">eval_results</span>
</code></pre></div></td></tr></tbody></table>

### from\_metric\_names `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator.from_metric_names "Permanent link")

```
from_metric_names(metric_names: List[str], **kwargs: Any) -> [BaseRetrievalEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator "llama_index.core.evaluation.retrieval.base.BaseRetrievalEvaluator")
```

Create evaluator from metric names.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metric_names` | `List[str]` | 
List of metric names



 | _required_ |
| `**kwargs` | `Any` | 

Additional arguments for the evaluator



 | `{}` |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 88</span>
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
<span class="normal">100</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_metric_names</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="n">metric_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseRetrievalEvaluator"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create evaluator from metric names.</span>

<span class="sd">    Args:</span>
<span class="sd">        metric_names (List[str]): List of metric names</span>
<span class="sd">        **kwargs: Additional arguments for the evaluator</span>

<span class="sd">    """</span>
    <span class="n">metric_types</span> <span class="o">=</span> <span class="n">resolve_metrics</span><span class="p">(</span><span class="n">metric_names</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="n">metric</span><span class="p">()</span> <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="n">metric_types</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator.evaluate "Permanent link")

```
evaluate(query: str, expected_ids: List[str], expected_texts: Optional[List[str]] = None, mode: RetrievalEvalMode = RetrievalEvalMode.TEXT, **kwargs: Any) -> [RetrievalEvalResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult "llama_index.core.evaluation.retrieval.base.RetrievalEvalResult")
```

Run evaluation results with query string and expected ids.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
Query string



 | _required_ |
| `expected_ids` | `List[str]` | 

Expected ids



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `RetrievalEvalResult` | `[RetrievalEvalResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult "llama_index.core.evaluation.retrieval.base.RetrievalEvalResult")` | 
Evaluation result



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
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
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation results with query string and expected ids.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): Query string</span>
<span class="sd">        expected_ids (List[str]): Expected ids</span>

<span class="sd">    Returns:</span>
<span class="sd">        RetrievalEvalResult: Evaluation result</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span>
            <span class="n">expected_texts</span><span class="o">=</span><span class="n">expected_texts</span><span class="p">,</span>
            <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator.aevaluate "Permanent link")

```
aevaluate(query: str, expected_ids: List[str], expected_texts: Optional[List[str]] = None, mode: RetrievalEvalMode = RetrievalEvalMode.TEXT, **kwargs: Any) -> [RetrievalEvalResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult "llama_index.core.evaluation.retrieval.base.RetrievalEvalResult")
```

Run evaluation with query string, retrieved contexts, and generated response string.

Subclasses can override this method to provide custom evaluation logic and take in additional arguments.

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">    and generated response string.</span>

<span class="sd">    Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">    take in additional arguments.</span>
<span class="sd">    """</span>
    <span class="n">retrieved_ids</span><span class="p">,</span> <span class="n">retrieved_texts</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_retrieved_ids_and_texts</span><span class="p">(</span>
        <span class="n">query</span><span class="p">,</span> <span class="n">mode</span>
    <span class="p">)</span>
    <span class="n">metric_dict</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">metric</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">metrics</span><span class="p">:</span>
        <span class="n">eval_result</span> <span class="o">=</span> <span class="n">metric</span><span class="o">.</span><span class="n">compute</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">,</span> <span class="n">retrieved_ids</span><span class="p">,</span> <span class="n">expected_texts</span><span class="p">,</span> <span class="n">retrieved_texts</span>
        <span class="p">)</span>
        <span class="n">metric_dict</span><span class="p">[</span><span class="n">metric</span><span class="o">.</span><span class="n">metric_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">eval_result</span>

    <span class="k">return</span> <span class="n">RetrievalEvalResult</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span>
        <span class="n">expected_texts</span><span class="o">=</span><span class="n">expected_texts</span><span class="p">,</span>
        <span class="n">retrieved_ids</span><span class="o">=</span><span class="n">retrieved_ids</span><span class="p">,</span>
        <span class="n">retrieved_texts</span><span class="o">=</span><span class="n">retrieved_texts</span><span class="p">,</span>
        <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
        <span class="n">metric_dict</span><span class="o">=</span><span class="n">metric_dict</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_dataset `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.BaseRetrievalEvaluator.aevaluate_dataset "Permanent link")

```
aevaluate_dataset(dataset: EmbeddingQAFinetuneDataset, workers: int = 2, show_progress: bool = False, **kwargs: Any) -> List[[RetrievalEvalResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult "llama_index.core.evaluation.retrieval.base.RetrievalEvalResult")]
```

Run evaluation with dataset.

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_dataset</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">dataset</span><span class="p">:</span> <span class="n">EmbeddingQAFinetuneDataset</span><span class="p">,</span>
    <span class="n">workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RetrievalEvalResult</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with dataset."""</span>
    <span class="n">semaphore</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="n">workers</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">eval_worker</span><span class="p">(</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">mode</span><span class="p">:</span> <span class="n">RetrievalEvalMode</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RetrievalEvalResult</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">semaphore</span><span class="p">:</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="o">=</span><span class="n">expected_ids</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">)</span>

    <span class="n">response_jobs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">mode</span> <span class="o">=</span> <span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">dataset</span><span class="o">.</span><span class="n">mode</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">query_id</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">dataset</span><span class="o">.</span><span class="n">queries</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">expected_ids</span> <span class="o">=</span> <span class="n">dataset</span><span class="o">.</span><span class="n">relevant_docs</span><span class="p">[</span><span class="n">query_id</span><span class="p">]</span>
        <span class="n">response_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">eval_worker</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">expected_ids</span><span class="p">,</span> <span class="n">mode</span><span class="p">))</span>
    <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tqdm.asyncio</span> <span class="kn">import</span> <span class="n">tqdm_asyncio</span>

        <span class="n">eval_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">tqdm_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">eval_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">eval_results</span>
</code></pre></div></td></tr></tbody></table>

RetrieverEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrieverEvaluator "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

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

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
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
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrieverEvaluator</span><span class="p">(</span><span class="n">BaseRetrievalEvaluator</span><span class="p">):</span>
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
<span class="w">        </span><span class="sd">"""Get retrieved ids and texts, potentially applying a post-processor."""</span>
        <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_postprocessors</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_postprocessors</span><span class="p">:</span>
                <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                    <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span><span class="p">],</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span><span class="p">],</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RetrievalEvalResult [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Retrieval eval result.

NOTE: this abstraction might change in the future.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `query` | `str` | 
Query string



 |
| `expected_ids` | `List[str]` | 

Expected ids



 |
| `retrieved_ids` | `List[str]` | 

Retrieved ids



 |
| `metric_dict` | `Dict[str, BaseRetrievalMetric]` | 

Metric dictionary for the evaluation



 |

Source code in `llama-index-core/llama_index/core/evaluation/retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
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
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrievalEvalResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retrieval eval result.</span>

<span class="sd">    NOTE: this abstraction might change in the future.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        query (str): Query string</span>
<span class="sd">        expected_ids (List[str]): Expected ids</span>
<span class="sd">        retrieved_ids (List[str]): Retrieved ids</span>
<span class="sd">        metric_dict (Dict[str, BaseRetrievalMetric]): \</span>
<span class="sd">            Metric dictionary for the evaluation</span>

<span class="sd">    """</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Query string"</span><span class="p">)</span>
    <span class="n">expected_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Expected ids"</span><span class="p">)</span>
    <span class="n">expected_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Expected texts associated with nodes provided in `expected_ids`"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">retrieved_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Retrieved ids"</span><span class="p">)</span>
    <span class="n">retrieved_texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Retrieved texts"</span><span class="p">)</span>
    <span class="n">mode</span><span class="p">:</span> <span class="s2">"RetrievalEvalMode"</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">RetrievalEvalMode</span><span class="o">.</span><span class="n">TEXT</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"text or image"</span>
    <span class="p">)</span>
    <span class="n">metric_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RetrievalMetricResult</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Metric dictionary for the evaluation"</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metric_vals_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Dictionary of metric values."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""String representation."""</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"Query: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"Metrics: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metric_vals_dict</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

### metric\_vals\_dict `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/#llama_index.core.evaluation.RetrievalEvalResult.metric_vals_dict "Permanent link")

```
metric_vals_dict: Dict[str, float]
```

Dictionary of metric values.

Back to top

[Previous Response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/response/)[Next Semantic similarity](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/)
