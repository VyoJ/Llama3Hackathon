Title: Correctness - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/

Markdown Content:
Correctness - LlamaIndex


Evaluation modules.

CorrectnessEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/#llama_index.core.evaluation.CorrectnessEvaluator "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Correctness evaluator.

Evaluates the correctness of a question answering system. This evaluator depends on `reference` answer to be provided, in addition to the query string and response string.

It outputs a score between 1 and 5, where 1 is the worst and 5 is the best, along with a reasoning for the score. Passing is defined as a score greater than or equal to the given threshold.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context` | `Optional[ServiceContext]` | 
Service context.



 | `None` |
| `eval_template` | `Optional[Union[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate"), str]]` | 

Template for the evaluation prompt.



 | `None` |
| `score_threshold` | `float` | 

Numerical threshold for passing the evaluation, defaults to 4.0.



 | `4.0` |

Source code in `llama-index-core/llama_index/core/evaluation/correctness.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 69</span>
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
<span class="normal">154</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CorrectnessEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Correctness evaluator.</span>

<span class="sd">    Evaluates the correctness of a question answering system.</span>
<span class="sd">    This evaluator depends on `reference` answer to be provided, in addition to the</span>
<span class="sd">    query string and response string.</span>

<span class="sd">    It outputs a score between 1 and 5, where 1 is the worst and 5 is the best,</span>
<span class="sd">    along with a reasoning for the score.</span>
<span class="sd">    Passing is defined as a score greater than or equal to the given threshold.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context (Optional[ServiceContext]): Service context.</span>
<span class="sd">        eval_template (Optional[Union[BasePromptTemplate, str]]):</span>
<span class="sd">            Template for the evaluation prompt.</span>
<span class="sd">        score_threshold (float): Numerical threshold for passing the evaluation,</span>
<span class="sd">            defaults to 4.0.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">eval_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">score_threshold</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">4.0</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parser_function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span>
            <span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">default_parser</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_template</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">eval_template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">eval_template</span> <span class="ow">or</span> <span class="n">DEFAULT_EVAL_TEMPLATE</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_score_threshold</span> <span class="o">=</span> <span class="n">score_threshold</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">parser_function</span> <span class="o">=</span> <span class="n">parser_function</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"eval_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"eval_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"eval_template"</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reference</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>
        <span class="k">del</span> <span class="n">contexts</span>  <span class="c1"># Unused</span>

        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query, and response must be provided"</span><span class="p">)</span>

        <span class="n">eval_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">generated_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">reference_answer</span><span class="o">=</span><span class="n">reference</span> <span class="ow">or</span> <span class="s2">"(NO REFERENCE ANSWER SUPPLIED)"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Use the parser function</span>
        <span class="n">score</span><span class="p">,</span> <span class="n">reasoning</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_function</span><span class="p">(</span><span class="n">eval_response</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">passing</span><span class="o">=</span><span class="n">score</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_score_threshold</span> <span class="k">if</span> <span class="n">score</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">,</span>
            <span class="n">feedback</span><span class="o">=</span><span class="n">reasoning</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Context relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/context_relevancy/)[Next Dataset generation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/)
