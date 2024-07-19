Title: FLARE - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/

Markdown Content:
FLARE - LlamaIndex


FLAREInstructQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/#llama_index.core.query_engine.FLAREInstructQueryEngine "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

FLARE Instruct query engine.

This is the version of FLARE that uses retrieval-encouraging instructions.

NOTE: this is a beta feature. Interfaces might change, and it might not always give correct answers.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
query engine to use



 | _required_ |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

LLM model. Defaults to None.



 | `None` |
| `service_context` | `Optional[ServiceContext]` | 

service context. Defaults to None.



 | `None` |
| `instruct_prompt` | `Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.base.PromptTemplate")]` | 

instruct prompt. Defaults to None.



 | `None` |
| `lookahead_answer_inserter` | `Optional[BaseLookaheadAnswerInserter]` | 

lookahead answer inserter. Defaults to None.



 | `None` |
| `done_output_parser` | `Optional[IsDoneOutputParser]` | 

done output parser. Defaults to None.



 | `None` |
| `query_task_output_parser` | `Optional[QueryTaskOutputParser]` | 

query task output parser. Defaults to None.



 | `None` |
| `max_iterations` | `int` | 

max iterations. Defaults to 10.



 | `10` |
| `max_lookahead_query_tasks` | `int` | 

max lookahead query tasks. Defaults to 1.



 | `1` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

callback manager. Defaults to None.



 | `None` |
| `verbose` | `bool` | 

give verbose outputs. Defaults to False.



 | `False` |

Source code in `llama-index-core/llama_index/core/query_engine/flare/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 98</span>
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
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FLAREInstructQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""FLARE Instruct query engine.</span>

<span class="sd">    This is the version of FLARE that uses retrieval-encouraging instructions.</span>

<span class="sd">    NOTE: this is a beta feature. Interfaces might change, and it might not</span>
<span class="sd">    always give correct answers.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): query engine to use</span>
<span class="sd">        llm (Optional[LLM]): LLM model. Defaults to None.</span>
<span class="sd">        service_context (Optional[ServiceContext]): service context.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        instruct_prompt (Optional[PromptTemplate]): instruct prompt. Defaults to None.</span>
<span class="sd">        lookahead_answer_inserter (Optional[BaseLookaheadAnswerInserter]):</span>
<span class="sd">            lookahead answer inserter. Defaults to None.</span>
<span class="sd">        done_output_parser (Optional[IsDoneOutputParser]): done output parser.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        query_task_output_parser (Optional[QueryTaskOutputParser]):</span>
<span class="sd">            query task output parser. Defaults to None.</span>
<span class="sd">        max_iterations (int): max iterations. Defaults to 10.</span>
<span class="sd">        max_lookahead_query_tasks (int): max lookahead query tasks. Defaults to 1.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): callback manager.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        verbose (bool): give verbose outputs. Defaults to False.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">instruct_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">lookahead_answer_inserter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLookaheadAnswerInserter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">done_output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IsDoneOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_task_output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryTaskOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">max_lookahead_query_tasks</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_instruct_prompt</span> <span class="o">=</span> <span class="n">instruct_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_INSTRUCT_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_lookahead_answer_inserter</span> <span class="o">=</span> <span class="n">lookahead_answer_inserter</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="n">LLMLookaheadAnswerInserter</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_done_output_parser</span> <span class="o">=</span> <span class="n">done_output_parser</span> <span class="ow">or</span> <span class="n">IsDoneOutputParser</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_task_output_parser</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">query_task_output_parser</span> <span class="ow">or</span> <span class="n">QueryTaskOutputParser</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_iterations</span> <span class="o">=</span> <span class="n">max_iterations</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_lookahead_query_tasks</span> <span class="o">=</span> <span class="n">max_lookahead_query_tasks</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"instruct_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instruct_prompt</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"instruct_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_instruct_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"instruct_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
            <span class="s2">"lookahead_answer_inserter"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lookahead_answer_inserter</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_relevant_lookahead_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">updated_lookahead_resp</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get relevant lookahead response."""</span>
        <span class="c1"># if there's remaining query tasks, then truncate the response</span>
        <span class="c1"># until the start position of the first tag</span>
        <span class="c1"># there may be remaining query tasks because the _max_lookahead_query_tasks</span>
        <span class="c1"># is less than the total number of generated [Search(query)] tags</span>
        <span class="n">remaining_query_tasks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_task_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span>
            <span class="n">updated_lookahead_resp</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">remaining_query_tasks</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">relevant_lookahead_resp</span> <span class="o">=</span> <span class="n">updated_lookahead_resp</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">first_task</span> <span class="o">=</span> <span class="n">remaining_query_tasks</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">relevant_lookahead_resp</span> <span class="o">=</span> <span class="n">updated_lookahead_resp</span><span class="p">[:</span> <span class="n">first_task</span><span class="o">.</span><span class="n">start_idx</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">relevant_lookahead_resp</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query and get response."""</span>
        <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query: </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>
        <span class="n">cur_response</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">source_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="nb">iter</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_iterations</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Current response: </span><span class="si">{</span><span class="n">cur_response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
            <span class="c1"># generate "lookahead response" that contains "[Search(query)]" tags</span>
            <span class="c1"># e.g.</span>
            <span class="c1"># The colors on the flag of Ghana have the following meanings. Red is</span>
            <span class="c1"># for [Search(Ghana flag meaning)],...</span>
            <span class="n">lookahead_resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_instruct_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">existing_answer</span><span class="o">=</span><span class="n">cur_response</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">lookahead_resp</span> <span class="o">=</span> <span class="n">lookahead_resp</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Lookahead response: </span><span class="si">{</span><span class="n">lookahead_resp</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>

            <span class="n">is_done</span><span class="p">,</span> <span class="n">fmt_lookahead</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_done_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lookahead_resp</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="n">cur_response</span> <span class="o">=</span> <span class="n">cur_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">fmt_lookahead</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
                <span class="k">break</span>

            <span class="c1"># parse lookahead response into query tasks</span>
            <span class="n">query_tasks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_task_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lookahead_resp</span><span class="p">)</span>

            <span class="c1"># get answers for each query task</span>
            <span class="n">query_tasks</span> <span class="o">=</span> <span class="n">query_tasks</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_max_lookahead_query_tasks</span><span class="p">]</span>
            <span class="n">query_answers</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">query_task</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">query_tasks</span><span class="p">):</span>
                <span class="n">answer_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_task</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">answer_obj</span><span class="p">,</span> <span class="n">Response</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Expected Response object, got </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">answer_obj</span><span class="p">)</span><span class="si">}</span><span class="s2"> instead."</span>
                    <span class="p">)</span>
                <span class="n">query_answer</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">answer_obj</span><span class="p">)</span>
                <span class="n">query_answers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">query_answer</span><span class="p">)</span>
                <span class="n">source_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">answer_obj</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">)</span>

            <span class="c1"># fill in the lookahead response template with the query answers</span>
            <span class="c1"># from the query engine</span>
            <span class="n">updated_lookahead_resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lookahead_answer_inserter</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span>
                <span class="n">lookahead_resp</span><span class="p">,</span> <span class="n">query_tasks</span><span class="p">,</span> <span class="n">query_answers</span><span class="p">,</span> <span class="n">prev_response</span><span class="o">=</span><span class="n">cur_response</span>
            <span class="p">)</span>

            <span class="c1"># get "relevant" lookahead response by truncating the updated</span>
            <span class="c1"># lookahead response until the start position of the first tag</span>
            <span class="c1"># also remove the prefix from the lookahead response, so that</span>
            <span class="c1"># we can concatenate it with the existing response</span>
            <span class="n">relevant_lookahead_resp_wo_prefix</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_relevant_lookahead_response</span><span class="p">(</span>
                <span class="n">updated_lookahead_resp</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="s2">"Updated lookahead response: "</span>
                    <span class="o">+</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">relevant_lookahead_resp_wo_prefix</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="c1"># append the relevant lookahead response to the final response</span>
            <span class="n">cur_response</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">cur_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">relevant_lookahead_resp_wo_prefix</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="p">)</span>

        <span class="c1"># NOTE: at the moment, does not support streaming</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">cur_response</span><span class="p">,</span> <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="c1"># if the query engine is a retriever, then use the retrieve method</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                <span class="s2">"This query engine does not support retrieve, use query directly"</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="c1"># if the query engine is a retriever, then use the retrieve method</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                <span class="s2">"This query engine does not support retrieve, use query directly"</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/prompts/)[Next JSONalayze](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/)
