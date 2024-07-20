Title: Router - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/

Markdown Content:
Router - LlamaIndex


RouterQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/#llama_index.core.query_engine.RouterQueryEngine "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Router query engine.

Selects one out of several candidate query engines to execute a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `selector` | `BaseSelector` | 
A selector that chooses one out of many options based on each candidate's metadata and query.



 | _required_ |
| `query_engine_tools` | `Sequence[[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")]` | 

A sequence of candidate query engines. They must be wrapped as tools to expose metadata to the selector.



 | _required_ |
| `service_context` | `Optional[ServiceContext]` | 

A service context.



 | `None` |
| `summarizer` | `Optional[[TreeSummarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/#llama_index.core.response_synthesizers.TreeSummarize "llama_index.core.response_synthesizers.TreeSummarize")]` | 

Tree summarizer to summarize sub-results.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/router_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">254</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RouterQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Router query engine.</span>

<span class="sd">    Selects one out of several candidate query engines to execute a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        selector (BaseSelector): A selector that chooses one out of many options based</span>
<span class="sd">            on each candidate's metadata and query.</span>
<span class="sd">        query_engine_tools (Sequence[QueryEngineTool]): A sequence of candidate</span>
<span class="sd">            query engines. They must be wrapped as tools to expose metadata to</span>
<span class="sd">            the selector.</span>
<span class="sd">        service_context (Optional[ServiceContext]): A service context.</span>
<span class="sd">        summarizer (Optional[TreeSummarize]): Tree summarizer to summarize sub-results.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">BaseSelector</span><span class="p">,</span>
        <span class="n">query_engine_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summarizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TreeSummarize</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">llm</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span> <span class="o">=</span> <span class="n">selector</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">query_engine</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">query_engine_tools</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">query_engine_tools</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span> <span class="o">=</span> <span class="n">summarizer</span> <span class="ow">or</span> <span class="n">TreeSummarize</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">summary_template</span><span class="o">=</span><span class="n">DEFAULT_TREE_SUMMARIZE_PROMPT_SEL</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="c1"># NOTE: don't include tools for now</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"summarizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">,</span> <span class="s2">"selector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">query_engine_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSelector</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summarizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TreeSummarize</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select_multi</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RouterQueryEngine"</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">llm</span><span class="p">)</span>

        <span class="n">selector</span> <span class="o">=</span> <span class="n">selector</span> <span class="ow">or</span> <span class="n">get_selector_from_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">is_multi</span><span class="o">=</span><span class="n">select_multi</span><span class="p">)</span>

        <span class="k">assert</span> <span class="n">selector</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">selector</span><span class="p">,</span>
            <span class="n">query_engine_tools</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">summarizer</span><span class="o">=</span><span class="n">summarizer</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">responses</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">engine_ind</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">):</span>
                    <span class="n">log_str</span> <span class="o">=</span> <span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Selecting query engine </span><span class="si">{</span><span class="n">engine_ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reasons</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s2">."</span>
                    <span class="p">)</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>

                    <span class="n">selected_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">engine_ind</span><span class="p">]</span>
                    <span class="n">responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">selected_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">responses</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                    <span class="n">final_response</span> <span class="o">=</span> <span class="n">combine_responses</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">query_bundle</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">final_response</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">selected_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
                    <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Selecting query engine </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Failed to select query engine"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

                <span class="n">final_response</span> <span class="o">=</span> <span class="n">selected_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="c1"># add selected result</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"selector_result"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="o">.</span><span class="n">aselect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">engine_ind</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">):</span>
                    <span class="n">log_str</span> <span class="o">=</span> <span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Selecting query engine </span><span class="si">{</span><span class="n">engine_ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reasons</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s2">."</span>
                    <span class="p">)</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
                    <span class="n">selected_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">engine_ind</span><span class="p">]</span>
                    <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">selected_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

                <span class="n">responses</span> <span class="o">=</span> <span class="n">run_async_tasks</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">responses</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                    <span class="n">final_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">acombine_responses</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_summarizer</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">query_bundle</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">final_response</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">selected_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
                    <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Selecting query engine </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Failed to select query engine"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

                <span class="n">final_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">selected_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="c1"># add selected result</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="n">final_response</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"selector_result"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">final_response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">final_response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retry](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/)[Next Simple multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/)
