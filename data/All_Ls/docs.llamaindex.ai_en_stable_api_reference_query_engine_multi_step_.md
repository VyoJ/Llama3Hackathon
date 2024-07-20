Title: Multi step - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/

Markdown Content:
Multi step - LlamaIndex


MultiStepQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/#llama_index.core.query_engine.MultiStepQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Multi-step query engine.

This query engine can operate over an existing base query engine, along with the multi-step query transform.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
A BaseQueryEngine object.



 | _required_ |
| `query_transform` | `StepDecomposeQueryTransform` | 

A StepDecomposeQueryTransform object.



 | _required_ |
| `response_synthesizer` | `Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")]` | 

A BaseSynthesizer object.



 | `None` |
| `num_steps` | `Optional[int]` | 

Number of steps to run the multi-step query.



 | `3` |
| `early_stopping` | `bool` | 

Whether to stop early if the stop function returns True.



 | `True` |
| `index_summary` | `str` | 

A string summary of the index.



 | `'None'` |
| `stop_fn` | `Optional[Callable[[Dict], bool]]` | 

A stop function that takes in a dictionary of information and returns a boolean.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/multistep_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 26</span>
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
<span class="normal">177</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiStepQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Multi-step query engine.</span>

<span class="sd">    This query engine can operate over an existing base query engine,</span>
<span class="sd">    along with the multi-step query transform.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): A BaseQueryEngine object.</span>
<span class="sd">        query_transform (StepDecomposeQueryTransform): A StepDecomposeQueryTransform</span>
<span class="sd">            object.</span>
<span class="sd">        response_synthesizer (Optional[BaseSynthesizer]): A BaseSynthesizer</span>
<span class="sd">            object.</span>
<span class="sd">        num_steps (Optional[int]): Number of steps to run the multi-step query.</span>
<span class="sd">        early_stopping (bool): Whether to stop early if the stop function returns True.</span>
<span class="sd">        index_summary (str): A string summary of the index.</span>
<span class="sd">        stop_fn (Optional[Callable[[Dict], bool]]): A stop function that takes in a</span>
<span class="sd">            dictionary of information and returns a boolean.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">query_transform</span><span class="p">:</span> <span class="n">StepDecomposeQueryTransform</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_steps</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">early_stopping</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">index_summary</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"None"</span><span class="p">,</span>
        <span class="n">stop_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Dict</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span> <span class="o">=</span> <span class="n">query_transform</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_index_summary</span> <span class="o">=</span> <span class="n">index_summary</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_num_steps</span> <span class="o">=</span> <span class="n">num_steps</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_early_stopping</span> <span class="o">=</span> <span class="n">early_stopping</span>
        <span class="c1"># TODO: make interface to stop function better</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_stop_fn</span> <span class="o">=</span> <span class="n">stop_fn</span> <span class="ow">or</span> <span class="n">default_stop_fn</span>
        <span class="c1"># num_steps must be provided if early_stopping is False</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_early_stopping</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_steps</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify num_steps if early_stopping is False."</span><span class="p">)</span>

        <span class="n">callback_manager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"response_synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">,</span>
            <span class="s2">"query_transform"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">source_nodes</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_multistep</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="n">final_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">source_nodes</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_multistep</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="n">final_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">def</span> <span class="nf">_combine_queries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span> <span class="n">prev_reasoning</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryBundle</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Combine queries."""</span>
        <span class="n">transform_metadata</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"prev_reasoning"</span><span class="p">:</span> <span class="n">prev_reasoning</span><span class="p">,</span>
            <span class="s2">"index_summary"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_summary</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_transform</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">transform_metadata</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query_multistep</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Run query combiner."""</span>
        <span class="n">prev_reasoning</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">cur_response</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">should_stop</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="n">cur_steps</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="c1"># use response</span>
        <span class="n">final_response_metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"sub_qa"</span><span class="p">:</span> <span class="p">[]}</span>

        <span class="n">text_chunks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">source_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="n">should_stop</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_steps</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">cur_steps</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_num_steps</span><span class="p">:</span>
                <span class="n">should_stop</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">break</span>
            <span class="k">elif</span> <span class="n">should_stop</span><span class="p">:</span>
                <span class="k">break</span>

            <span class="n">updated_query_bundle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_combine_queries</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">prev_reasoning</span><span class="p">)</span>

            <span class="c1"># TODO: make stop logic better</span>
            <span class="n">stop_dict</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query_bundle"</span><span class="p">:</span> <span class="n">updated_query_bundle</span><span class="p">}</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stop_fn</span><span class="p">(</span><span class="n">stop_dict</span><span class="p">):</span>
                <span class="n">should_stop</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">break</span>

            <span class="n">cur_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">updated_query_bundle</span><span class="p">)</span>

            <span class="c1"># append to response builder</span>
            <span class="n">cur_qa_text</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Question: </span><span class="si">{</span><span class="n">updated_query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
                <span class="sa">f</span><span class="s2">"Answer: </span><span class="si">{</span><span class="n">cur_response</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">text_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">cur_qa_text</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">source_node</span> <span class="ow">in</span> <span class="n">cur_response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">:</span>
                <span class="n">source_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">source_node</span><span class="p">)</span>
            <span class="c1"># update metadata</span>
            <span class="n">final_response_metadata</span><span class="p">[</span><span class="s2">"sub_qa"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">(</span><span class="n">updated_query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">cur_response</span><span class="p">)</span>
            <span class="p">)</span>

            <span class="n">prev_reasoning</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"- </span><span class="si">{</span><span class="n">updated_query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"- </span><span class="si">{</span><span class="n">cur_response</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">cur_steps</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text_chunk</span><span class="p">))</span> <span class="k">for</span> <span class="n">text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="n">nodes</span><span class="p">,</span> <span class="n">source_nodes</span><span class="p">,</span> <span class="n">final_response_metadata</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/)[Next Pandas](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/)
