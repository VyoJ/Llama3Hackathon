Title: Retry - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/

Markdown Content:
Retry - LlamaIndex


RetryGuidelineQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/#llama_index.core.query_engine.RetryGuidelineQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Does retry with evaluator feedback if query engine fails evaluation.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
A query engine object



 | _required_ |
| `guideline_evaluator` | `[GuidelineEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/#llama_index.core.evaluation.GuidelineEvaluator "llama_index.core.evaluation.guideline.GuidelineEvaluator")` | 

A guideline evaluator object



 | _required_ |
| `resynthesize_query` | `bool` | 

Whether to resynthesize query



 | `False` |
| `max_retries` | `int` | 

Maximum number of retries



 | `3` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager object



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/retry_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 71</span>
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
<span class="normal">136</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetryGuidelineQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Does retry with evaluator feedback</span>
<span class="sd">    if query engine fails evaluation.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): A query engine object</span>
<span class="sd">        guideline_evaluator (GuidelineEvaluator): A guideline evaluator object</span>
<span class="sd">        resynthesize_query (bool): Whether to resynthesize query</span>
<span class="sd">        max_retries (int): Maximum number of retries</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager object</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">guideline_evaluator</span><span class="p">:</span> <span class="n">GuidelineEvaluator</span><span class="p">,</span>
        <span class="n">resynthesize_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_transformer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FeedbackQueryTransformation</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_guideline_evaluator</span> <span class="o">=</span> <span class="n">guideline_evaluator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">=</span> <span class="n">max_retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">resynthesize_query</span> <span class="o">=</span> <span class="n">resynthesize_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_transformer</span> <span class="o">=</span> <span class="n">query_transformer</span> <span class="ow">or</span> <span class="n">FeedbackQueryTransformation</span><span class="p">(</span>
            <span class="n">resynthesize_query</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">resynthesize_query</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
            <span class="s2">"guideline_evalator"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_guideline_evaluator</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="n">typed_response</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">response</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Response</span><span class="p">)</span> <span class="k">else</span> <span class="n">response</span><span class="o">.</span><span class="n">get_response</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="nb">eval</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_guideline_evaluator</span><span class="o">.</span><span class="n">evaluate_response</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">typed_response</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">eval</span><span class="o">.</span><span class="n">passing</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned True."</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned False."</span><span class="p">)</span>
            <span class="n">new_query_engine</span> <span class="o">=</span> <span class="n">RetryGuidelineQueryEngine</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_guideline_evaluator</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">resynthesize_query</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">new_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_transformer</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="p">{</span><span class="s2">"evaluation"</span><span class="p">:</span> <span class="nb">eval</span><span class="p">})</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"New query: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">new_query</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">new_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">new_query</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Not supported."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RetryQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/#llama_index.core.query_engine.RetryQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Does retry on query engine if it fails evaluation.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
A query engine object



 | _required_ |
| `evaluator` | `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")` | 

An evaluator object



 | _required_ |
| `max_retries` | `int` | 

Maximum number of retries



 | `3` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager object



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/retry_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
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
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetryQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Does retry on query engine if it fails evaluation.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): A query engine object</span>
<span class="sd">        evaluator (BaseEvaluator): An evaluator object</span>
<span class="sd">        max_retries (int): Maximum number of retries</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager object</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">evaluator</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span> <span class="o">=</span> <span class="n">evaluator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">=</span> <span class="n">max_retries</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="s2">"evaluator"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="n">typed_response</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">response</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Response</span><span class="p">)</span> <span class="k">else</span> <span class="n">response</span><span class="o">.</span><span class="n">get_response</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="nb">eval</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="o">.</span><span class="n">evaluate_response</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">typed_response</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">eval</span><span class="o">.</span><span class="n">passing</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned True."</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned False."</span><span class="p">)</span>
            <span class="n">new_query_engine</span> <span class="o">=</span> <span class="n">RetryQueryEngine</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">-</span> <span class="mi">1</span>
            <span class="p">)</span>
            <span class="n">query_transformer</span> <span class="o">=</span> <span class="n">FeedbackQueryTransformation</span><span class="p">()</span>
            <span class="n">new_query</span> <span class="o">=</span> <span class="n">query_transformer</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="p">{</span><span class="s2">"evaluation"</span><span class="p">:</span> <span class="nb">eval</span><span class="p">})</span>
            <span class="k">return</span> <span class="n">new_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">new_query</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Not supported."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RetrySourceQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/#llama_index.core.query_engine.RetrySourceQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Retry with different source nodes.

Source code in `llama-index-core/llama_index/core/query_engine/retry_source_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
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
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrySourceQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retry with different source nodes."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="n">evaluator</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run a BaseQueryEngine with retries."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span> <span class="o">=</span> <span class="n">evaluator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">=</span> <span class="n">max_retries</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="s2">"evaluator"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="n">typed_response</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">response</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Response</span><span class="p">)</span> <span class="k">else</span> <span class="n">response</span><span class="o">.</span><span class="n">get_response</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="nb">eval</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="o">.</span><span class="n">evaluate_response</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">typed_response</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">eval</span><span class="o">.</span><span class="n">passing</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned True."</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Evaluation returned False."</span><span class="p">)</span>
            <span class="c1"># Test source nodes</span>
            <span class="n">source_evals</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="n">response</span><span class="o">=</span><span class="n">typed_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">contexts</span><span class="o">=</span><span class="p">[</span><span class="n">source_node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()],</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">source_node</span> <span class="ow">in</span> <span class="n">typed_response</span><span class="o">.</span><span class="n">source_nodes</span>
            <span class="p">]</span>
            <span class="n">orig_nodes</span> <span class="o">=</span> <span class="n">typed_response</span><span class="o">.</span><span class="n">source_nodes</span>
            <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">source_evals</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No source nodes passed evaluation."</span><span class="p">)</span>
            <span class="n">new_index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
                <span class="n">new_docs</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">new_retriever_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="p">(</span><span class="n">new_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">())</span>
            <span class="n">new_query_engine</span> <span class="o">=</span> <span class="n">RetrySourceQueryEngine</span><span class="p">(</span>
                <span class="n">new_retriever_engine</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_evaluator</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">new_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Not supported."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/)[Next Router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/)
