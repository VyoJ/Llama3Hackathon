Title: Pairwise comparison - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/

Markdown Content:
Pairwise comparison - LlamaIndex


Evaluation modules.

PairwiseComparisonEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/#llama_index.core.evaluation.PairwiseComparisonEvaluator "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Pairwise comparison evaluator.

Evaluates the quality of a response vs. a "reference" response given a question by having an LLM judge which response is better.

Outputs whether the `response` given is better than the `reference` response.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context` | `Optional[ServiceContext]` | 
The service context to use for evaluation.



 | `None` |
| `eval_template` | `Optional[Union[str, [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]]` | 

The template to use for evaluation.



 | `None` |
| `enforce_consensus` | `bool` | 

Whether to enforce consensus (consistency if we flip the order of the answers). Defaults to True.



 | `True` |

Source code in `llama-index-core/llama_index/core/evaluation/pairwise.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 93</span>
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
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PairwiseComparisonEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pairwise comparison evaluator.</span>

<span class="sd">    Evaluates the quality of a response vs. a "reference" response given a question by</span>
<span class="sd">    having an LLM judge which response is better.</span>

<span class="sd">    Outputs whether the `response` given is better than the `reference` response.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context (Optional[ServiceContext]):</span>
<span class="sd">            The service context to use for evaluation.</span>
<span class="sd">        eval_template (Optional[Union[str, BasePromptTemplate]]):</span>
<span class="sd">            The template to use for evaluation.</span>
<span class="sd">        enforce_consensus (bool): Whether to enforce consensus (consistency if we</span>
<span class="sd">            flip the order of the answers). Defaults to True.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">eval_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parser_function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span>
            <span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">_default_parser_function</span><span class="p">,</span>
        <span class="n">enforce_consensus</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_template</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">eval_template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">eval_template</span> <span class="ow">or</span> <span class="n">DEFAULT_EVAL_TEMPLATE</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_enforce_consensus</span> <span class="o">=</span> <span class="n">enforce_consensus</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_function</span> <span class="o">=</span> <span class="n">parser_function</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"eval_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"eval_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"eval_template"</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_get_eval_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">second_response</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">reference</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get evaluation result."""</span>
        <span class="n">eval_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">answer_1</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">answer_2</span><span class="o">=</span><span class="n">second_response</span><span class="p">,</span>
            <span class="n">reference</span><span class="o">=</span><span class="n">reference</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Extract from response</span>
        <span class="n">passing</span><span class="p">,</span> <span class="n">score</span><span class="p">,</span> <span class="n">feedback</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_function</span><span class="p">(</span><span class="n">eval_response</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">passing</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">score</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">feedback</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">invalid_result</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">invalid_reason</span><span class="o">=</span><span class="s2">"Output cannot be parsed"</span><span class="p">,</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_response</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">eval_response</span><span class="p">,</span>
                <span class="n">passing</span><span class="o">=</span><span class="n">passing</span><span class="p">,</span>
                <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">,</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_response</span><span class="p">,</span>
                <span class="n">pairwise_source</span><span class="o">=</span><span class="n">EvaluationSource</span><span class="o">.</span><span class="n">ORIGINAL</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_resolve_results</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span><span class="p">,</span>
        <span class="n">flipped_eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Resolve eval results from evaluation + flipped evaluation.</span>

<span class="sd">        Args:</span>
<span class="sd">            eval_result (EvaluationResult): Result when answer_1 is shown first</span>
<span class="sd">            flipped_eval_result (EvaluationResult): Result when answer_2 is shown first</span>

<span class="sd">        Returns:</span>
<span class="sd">            EvaluationResult: The final evaluation result</span>
<span class="sd">        """</span>
        <span class="c1"># add pairwise_source to eval_result and flipped_eval_result</span>
        <span class="n">eval_result</span><span class="o">.</span><span class="n">pairwise_source</span> <span class="o">=</span> <span class="n">EvaluationSource</span><span class="o">.</span><span class="n">ORIGINAL</span>
        <span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">pairwise_source</span> <span class="o">=</span> <span class="n">EvaluationSource</span><span class="o">.</span><span class="n">FLIPPED</span>

        <span class="c1"># count the votes for each of the 2 answers</span>
        <span class="n">votes_1</span> <span class="o">=</span> <span class="mf">0.0</span>
        <span class="n">votes_2</span> <span class="o">=</span> <span class="mf">0.0</span>
        <span class="k">if</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">votes_1</span> <span class="o">=</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">score</span> <span class="o">+</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>
            <span class="n">votes_2</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">score</span><span class="p">)</span> <span class="o">+</span> <span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">score</span>

        <span class="k">if</span> <span class="n">votes_1</span> <span class="o">+</span> <span class="n">votes_2</span> <span class="o">!=</span> <span class="mi">2</span><span class="p">:</span>  <span class="c1"># each round, the judge can give a total of 1 vote</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Impossible score results. Total amount of votes is 2."</span><span class="p">)</span>

        <span class="c1"># get the judges (original and flipped) who voted for answer_1</span>
        <span class="n">voters_1</span> <span class="o">=</span> <span class="p">[</span><span class="n">eval_result</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span> <span class="o"></span> <span class="mf">0.0</span><span class="p">)</span>

        <span class="c1"># get the judges (original and flipped) who voted for answer_2</span>
        <span class="n">voters_2</span> <span class="o">=</span> <span class="p">[</span><span class="n">eval_result</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span> <span class="o"></span> <span class="mf">1.0</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">votes_1</span> <span class="o">&gt;</span> <span class="n">votes_2</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">voters_1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># return any voter for answer_1</span>
        <span class="k">elif</span> <span class="n">votes_2</span> <span class="o">&gt;</span> <span class="n">votes_1</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">voters_2</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># return any vote for answer_2</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="n">eval_result</span><span class="o">.</span><span class="n">score</span> <span class="o"> votes_2 can only happen if both are 1.0 (so actual tie)</span>
                <span class="c1"># doesn't matter which one we return here</span>
                <span class="k">return</span> <span class="n">eval_result</span>
            <span class="k">else</span><span class="p">:</span>  <span class="c1"># Inconclusive case!</span>
                <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                    <span class="n">response</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                    <span class="n">passing</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
                    <span class="n">score</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span>
                    <span class="n">feedback</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                    <span class="n">pairwise_source</span><span class="o">=</span><span class="n">EvaluationSource</span><span class="o">.</span><span class="n">NEITHER</span><span class="p">,</span>
                <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">second_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reference</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>
        <span class="k">del</span> <span class="n">contexts</span>  <span class="c1"># Unused</span>

        <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">second_response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"query, response, second_response, and reference must be provided"</span>
            <span class="p">)</span>

        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="n">eval_result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_result</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="p">,</span> <span class="n">second_response</span><span class="p">,</span> <span class="n">reference</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enforce_consensus</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
            <span class="c1"># Flip the order of the answers and see if the answer is consistent</span>
            <span class="c1"># (which means that the score should flip from 0 to 1 and vice-versa)</span>
            <span class="c1"># if not, then we return a tie</span>
            <span class="n">flipped_eval_result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_result</span><span class="p">(</span>
                <span class="n">query</span><span class="p">,</span> <span class="n">second_response</span><span class="p">,</span> <span class="n">response</span><span class="p">,</span> <span class="n">reference</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
                <span class="n">resolved_eval_result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_resolve_results</span><span class="p">(</span>
                    <span class="n">eval_result</span><span class="p">,</span> <span class="n">flipped_eval_result</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">resolved_eval_result</span> <span class="o">=</span> <span class="n">EvaluationResult</span><span class="p">(</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                    <span class="n">response</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">feedback</span><span class="o">=</span><span class="n">flipped_eval_result</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">invalid_result</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">invalid_reason</span><span class="o">=</span><span class="s2">"Output cannot be parsed."</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">resolved_eval_result</span> <span class="o">=</span> <span class="n">eval_result</span>

        <span class="k">return</span> <span class="n">resolved_eval_result</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/)[Next Query response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/query_response/)
