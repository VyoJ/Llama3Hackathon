Title: Evaluator benchmarker - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/

Markdown Content:
Evaluator benchmarker - LlamaIndex


EvaluatorBenchmarkerPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/#llama_index.packs.evaluator_benchmarker.EvaluatorBenchmarkerPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

A pack for benchmarking/evaluating your own evaluator.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `evaluator` | `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.BaseEvaluator")` | 
The evaluator to evaluate/benchmark.



 | _required_ |
| `eval_dataset` | `[LabelledEvaluatorDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataset "llama_index.core.llama_dataset.evaluator_evaluation.LabelledEvaluatorDataset") | [LabelledPairwiseEvaluatorDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataset "llama_index.core.llama_dataset.evaluator_evaluation.LabelledPairwiseEvaluatorDataset")` | 

The labelled evaluation dataset to run benchmarks against.



 | _required_ |

Source code in `llama-index-packs/llama-index-packs-evaluator-benchmarker/llama_index/packs/evaluator_benchmarker/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
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
<span class="normal">162</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EvaluatorBenchmarkerPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A pack for benchmarking/evaluating your own evaluator.</span>

<span class="sd">    Args:</span>
<span class="sd">        evaluator (BaseEvaluator): The evaluator to evaluate/benchmark.</span>
<span class="sd">        eval_dataset (LabelledEvaluatorDataset | LabelledPairwiseEvaluatorDataset): The</span>
<span class="sd">            labelled evaluation dataset to run benchmarks against.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">evaluator</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">eval_dataset</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">LabelledEvaluatorDataset</span><span class="p">,</span> <span class="n">LabelledPairwiseEvaluatorDataset</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">evaluator</span> <span class="o">=</span> <span class="n">evaluator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span> <span class="o">=</span> <span class="n">eval_dataset</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_amake_predictions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Async make predictions with evaluator."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
            <span class="n">EvaluatorPredictionDataset</span><span class="p">,</span> <span class="n">PairwiseEvaluatorPredictionDataset</span>
        <span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="o">.</span><span class="n">amake_predictions_with</span><span class="p">(</span>
            <span class="n">predictor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluator</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">make_predictions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Sync make predictions with evaluator."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
            <span class="n">EvaluatorPredictionDataset</span><span class="p">,</span> <span class="n">PairwiseEvaluatorPredictionDataset</span>
        <span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="o">.</span><span class="n">make_predictions_with</span><span class="p">(</span>
            <span class="n">predictor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluator</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_prepare_and_save_benchmark_results_pairwise_grading</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Compute benchmark metrics for pairwise evaluation."""</span>
        <span class="n">inconclusive_counts</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">agreements_with_ties</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">agreements_without_ties</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">ties</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">invalid_counts</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">prediction</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="p">[:],</span> <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">[:]</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="n">prediction</span><span class="o">.</span><span class="n">invalid_prediction</span><span class="p">:</span>
                <span class="n">invalid_counts</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">continue</span>

            <span class="c1"># don't count inconclusive results</span>
            <span class="k">if</span> <span class="n">prediction</span><span class="o">.</span><span class="n">evaluation_source</span> <span class="o"></span> <span class="mf">0.5</span> <span class="ow">or</span> <span class="n">example</span><span class="o">.</span><span class="n">reference_score</span> <span class="o"></span> <span class="n">prediction</span><span class="o">.</span><span class="n">score</span>
                <span class="p">)</span>
            <span class="n">agreements_with_ties</span> <span class="o">+=</span> <span class="nb">int</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">reference_score</span> <span class="o"></span> <span class="n">np_refs</span><span class="p">[</span><span class="n">invalid_mask</span><span class="p">])</span>

        <span class="n">df_data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"number_examples"</span><span class="p">:</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">[:])],</span>
            <span class="s2">"invalid_predictions"</span><span class="p">:</span> <span class="p">[</span><span class="n">invalid_counts</span><span class="p">],</span>
            <span class="s2">"correlation"</span><span class="p">:</span> <span class="p">[</span><span class="n">corr</span><span class="p">],</span>
            <span class="s2">"mae"</span><span class="p">:</span> <span class="p">[</span><span class="n">mae</span><span class="p">],</span>
            <span class="s2">"hamming"</span><span class="p">:</span> <span class="p">[</span><span class="n">hamming</span><span class="p">],</span>
        <span class="p">}</span>
        <span class="n">benchmark_df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">df_data</span><span class="p">)</span>
        <span class="n">benchmark_df</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s2">"benchmark.csv"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">benchmark_df</span>

    <span class="k">def</span> <span class="nf">_make_evaluations</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns benchmark_df."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="p">,</span> <span class="n">LabelledPairwiseEvaluatorDataset</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_and_save_benchmark_results_pairwise_grading</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_and_save_benchmark_results_single_grading</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">batch_size</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"You've set a large batch_size (&gt;10). If using OpenAI GPT-4 as "</span>
                <span class="s2">" `judge_llm` (which is the default judge_llm),"</span>
                <span class="s2">" you may experience a RateLimitError. Previous successful eval "</span>
                <span class="s2">" responses are cached per batch. So hitting a RateLimitError"</span>
                <span class="s2">" would mean you'd lose all of the current batches successful "</span>
                <span class="s2">" GPT-4 calls."</span>
            <span class="p">)</span>

        <span class="c1"># make predictions</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_amake_predictions</span><span class="p">(</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="c1"># produce metrics</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_evaluations</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### make\_predictions [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/#llama_index.packs.evaluator_benchmarker.EvaluatorBenchmarkerPack.make_predictions "Permanent link")

```
make_predictions(batch_size: int = 20, sleep_time_in_seconds: int = 1)
```

Sync make predictions with evaluator.

Source code in `llama-index-packs/llama-index-packs-evaluator-benchmarker/llama_index/packs/evaluator_benchmarker/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">make_predictions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Sync make predictions with evaluator."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">prediction_dataset</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
        <span class="n">EvaluatorPredictionDataset</span><span class="p">,</span> <span class="n">PairwiseEvaluatorPredictionDataset</span>
    <span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eval_dataset</span><span class="o">.</span><span class="n">make_predictions_with</span><span class="p">(</span>
        <span class="n">predictor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluator</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Docugami kg rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/docugami_kg_rag/)[Next Finchat](https://docs.llamaindex.ai/en/stable/api_reference/packs/finchat/)
