Title: Faithfullness - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/

Markdown Content:
Faithfullness - LlamaIndex


Evaluation modules.

FaithfulnessEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/#llama_index.core.evaluation.FaithfulnessEvaluator "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Faithfulness evaluator.

Evaluates whether a response is faithful to the contexts (i.e. whether the response is supported by the contexts or hallucinated.)

This evaluator only considers the response string and the list of context strings.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context(Optional[ServiceContext])` |  | 
The service context to use for evaluation.



 | _required_ |
| `raise_error(bool)` |  | 

Whether to raise an error when the response is invalid. Defaults to False.



 | _required_ |
| `eval_template(Optional[Union[str,` | `BasePromptTemplate]]` | 

The template to use for evaluation.



 | _required_ |
| `refine_template(Optional[Union[str,` | `BasePromptTemplate]]` | 

The template to use for refining the evaluation.



 | _required_ |

Source code in `llama-index-core/llama_index/core/evaluation/faithfulness.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
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
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FaithfulnessEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Faithfulness evaluator.</span>

<span class="sd">    Evaluates whether a response is faithful to the contexts</span>
<span class="sd">    (i.e. whether the response is supported by the contexts or hallucinated.)</span>

<span class="sd">    This evaluator only considers the response string and the list of context strings.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context(Optional[ServiceContext]):</span>
<span class="sd">            The service context to use for evaluation.</span>
<span class="sd">        raise_error(bool): Whether to raise an error when the response is invalid.</span>
<span class="sd">            Defaults to False.</span>
<span class="sd">        eval_template(Optional[Union[str, BasePromptTemplate]]):</span>
<span class="sd">            The template to use for evaluation.</span>
<span class="sd">        refine_template(Optional[Union[str, BasePromptTemplate]]):</span>
<span class="sd">            The template to use for refining the evaluation.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">eval_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePromptTemplate</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePromptTemplate</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_raise_error</span> <span class="o">=</span> <span class="n">raise_error</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_template</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">eval_template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">model_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">model_name</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">eval_template</span> <span class="ow">or</span> <span class="n">TEMPLATES_CATALOG</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                <span class="n">model_name</span><span class="p">,</span> <span class="n">DEFAULT_EVAL_TEMPLATE</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">refine_template</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">refine_template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">refine_template</span> <span class="ow">or</span> <span class="n">DEFAULT_REFINE_TEMPLATE</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"eval_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
            <span class="s2">"refine_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"eval_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"eval_template"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"refine_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"refine_template"</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluate whether the response is faithful to the contexts."""</span>
        <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>

        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">contexts</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"contexts and response must be provided"</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">context</span><span class="p">)</span> <span class="k">for</span> <span class="n">context</span> <span class="ow">in</span> <span class="n">contexts</span><span class="p">]</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

        <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
            <span class="n">refine_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

        <span class="n">raw_response_txt</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response_obj</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"yes"</span> <span class="ow">in</span> <span class="n">raw_response_txt</span><span class="o">.</span><span class="n">lower</span><span class="p">():</span>
            <span class="n">passing</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">passing</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_raise_error</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"The response is invalid"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">passing</span><span class="o">=</span><span class="n">passing</span><span class="p">,</span>
            <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="k">if</span> <span class="n">passing</span> <span class="k">else</span> <span class="mf">0.0</span><span class="p">,</span>
            <span class="n">feedback</span><span class="o">=</span><span class="n">raw_response_txt</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/#llama_index.core.evaluation.FaithfulnessEvaluator.aevaluate "Permanent link")

```
aevaluate(query: str | None = None, response: str | None = None, contexts: Sequence[str] | None = None, sleep_time_in_seconds: int = 0, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Evaluate whether the response is faithful to the contexts.

Source code in `llama-index-core/llama_index/core/evaluation/faithfulness.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">161</span>
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
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Evaluate whether the response is faithful to the contexts."""</span>
    <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>

    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">contexts</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"contexts and response must be provided"</span><span class="p">)</span>

    <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">context</span><span class="p">)</span> <span class="k">for</span> <span class="n">context</span> <span class="ow">in</span> <span class="n">contexts</span><span class="p">]</span>
    <span class="n">index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
        <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">response_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

    <span class="n">raw_response_txt</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response_obj</span><span class="p">)</span>

    <span class="k">if</span> <span class="s2">"yes"</span> <span class="ow">in</span> <span class="n">raw_response_txt</span><span class="o">.</span><span class="n">lower</span><span class="p">():</span>
        <span class="n">passing</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">passing</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_raise_error</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"The response is invalid"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
        <span class="n">passing</span><span class="o">=</span><span class="n">passing</span><span class="p">,</span>
        <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="k">if</span> <span class="n">passing</span> <span class="k">else</span> <span class="mf">0.0</span><span class="p">,</span>
        <span class="n">feedback</span><span class="o">=</span><span class="n">raw_response_txt</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dataset generation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/)[Next Guideline](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/)
