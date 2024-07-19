Title: Openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/openai/

Markdown Content:
Openai - LlamaIndex


OpenAIPydanticProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/#llama_index.program.openai.OpenAIPydanticProgram "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseLLMFunctionProgram[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]`

An OpenAI-based function that returns a pydantic model.

Note: this interface is not yet stable.

Source code in `llama-index-integrations/program/llama-index-program-openai/llama_index/program/openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 83</span>
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
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIPydanticProgram</span><span class="p">(</span><span class="n">BaseLLMFunctionProgram</span><span class="p">[</span><span class="n">LLM</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    An OpenAI-based function that returns a pydantic model.</span>

<span class="sd">    Note: this interface is not yet stable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">,</span>
        <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
        <span class="n">allow_multiple</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_allow_multiple</span> <span class="o">=</span> <span class="n">allow_multiple</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tool_choice</span> <span class="o">=</span> <span class="n">tool_choice</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">],</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">allow_multiple</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIPydanticProgram"</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">OpenAI</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"OpenAIPydanticProgram only supports OpenAI LLMs. "</span> <span class="sa">f</span><span class="s2">"Got: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">llm</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">is_function_calling_model</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Model name </span><span class="si">{</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">model_name</span><span class="si">}</span><span class="s2"> does not support "</span>
                <span class="s2">"function calling API. "</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">prompt_template_str</span><span class="p">)</span>

        <span class="n">tool_choice</span> <span class="o">=</span> <span class="n">tool_choice</span> <span class="ow">or</span> <span class="n">_default_tool_choice</span><span class="p">(</span><span class="n">output_cls</span><span class="p">,</span> <span class="n">allow_multiple</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">PromptTemplate</span><span class="p">,</span> <span class="n">prompt</span><span class="p">),</span>
            <span class="n">tool_choice</span><span class="o">=</span><span class="n">tool_choice</span><span class="p">,</span>
            <span class="n">allow_multiple</span><span class="o">=</span><span class="n">allow_multiple</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePromptTemplate</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span>

    <span class="nd">@prompt</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">Model</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Model</span><span class="p">]]:</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_description_eval</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">openai_fn_spec</span> <span class="o">=</span> <span class="n">to_openai_tool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">)</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">openai_fn_spec</span><span class="p">],</span>
            <span class="n">tool_choice</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_tool_choice</span><span class="p">,</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="k">if</span> <span class="s2">"tool_calls"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Expected tool_calls in ai_message.additional_kwargs, "</span>
                <span class="s2">"but none found."</span>
            <span class="p">)</span>

        <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">_parse_tool_calls</span><span class="p">(</span>
            <span class="n">tool_calls</span><span class="p">,</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">allow_multiple</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_allow_multiple</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">Model</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Model</span><span class="p">]]:</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_description_eval</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">openai_fn_spec</span> <span class="o">=</span> <span class="n">to_openai_tool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">)</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">openai_fn_spec</span><span class="p">],</span>
            <span class="n">tool_choice</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_tool_choice</span><span class="p">,</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="k">if</span> <span class="s2">"tool_calls"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Expected function call in ai_message.additional_kwargs, "</span>
                <span class="s2">"but none found."</span>
            <span class="p">)</span>

        <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">_parse_tool_calls</span><span class="p">(</span>
            <span class="n">tool_calls</span><span class="p">,</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">allow_multiple</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_allow_multiple</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_list</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Model</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Streams a list of objects."""</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_description_eval</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">list_output_cls</span> <span class="o">=</span> <span class="n">create_list_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">)</span>
        <span class="n">openai_fn_spec</span> <span class="o">=</span> <span class="n">to_openai_tool</span><span class="p">(</span><span class="n">list_output_cls</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">)</span>

        <span class="n">chat_response_gen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">openai_fn_spec</span><span class="p">],</span>
            <span class="n">tool_choice</span><span class="o">=</span><span class="n">_default_tool_choice</span><span class="p">(</span><span class="n">list_output_cls</span><span class="p">),</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="c1"># extract function call arguments</span>
        <span class="c1"># obj_start_idx finds start position (before a new "{" in JSON)</span>
        <span class="n">obj_start_idx</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>  <span class="c1"># NOTE: uninitialized</span>
        <span class="k">for</span> <span class="n">stream_resp</span> <span class="ow">in</span> <span class="n">chat_response_gen</span><span class="p">:</span>
            <span class="n">kwargs</span> <span class="o">=</span> <span class="n">stream_resp</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span>
            <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tool_calls</span><span class="p">)</span> <span class="o"></span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
                    <span class="n">obj_start_idx</span> <span class="o">=</span> <span class="n">fn_args</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"["</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># keep going until we find the start position</span>
                <span class="k">continue</span>

            <span class="n">new_obj_json_str</span><span class="p">,</span> <span class="n">obj_start_idx</span> <span class="o">=</span> <span class="n">_get_json_str</span><span class="p">(</span><span class="n">fn_args</span><span class="p">,</span> <span class="n">obj_start_idx</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">new_obj_json_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">obj_json_str</span> <span class="o">=</span> <span class="n">new_obj_json_str</span>
                <span class="n">obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">obj_json_str</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted object: </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">json</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="k">yield</span> <span class="n">obj</span>

    <span class="k">def</span> <span class="nf">stream_partial_objects</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Model</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Streams the intermediate partial object."""</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_description_eval</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">openai_fn_spec</span> <span class="o">=</span> <span class="n">to_openai_tool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">)</span>
        <span class="n">chat_response_gen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">openai_fn_spec</span><span class="p">],</span>
            <span class="n">tool_choice</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_tool_choice</span><span class="p">,</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">partial_resp</span> <span class="ow">in</span> <span class="n">chat_response_gen</span><span class="p">:</span>
            <span class="n">kwargs</span> <span class="o">=</span> <span class="n">partial_resp</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span>
            <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tool_calls</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">continue</span>

        <span class="c1"># NOTE: right now assume only one tool call</span>
        <span class="c1"># TODO: handle parallel tool calls in streaming setting</span>
        <span class="n">fn_args</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="n">arguments</span>

        <span class="c1"># this is inspired by `get_object` from `MultiTaskBase` in</span>
        <span class="c1"># the openai_function_call repo</span>

        <span class="k">if</span> <span class="n">fn_args</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"["</span><span class="p">)</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">obj_start_idx</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">fn_args</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="n">arguments</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">partial_object</span> <span class="o">=</span> <span class="n">parse_partial_json</span><span class="p">(</span><span class="n">fn_args</span><span class="p">)</span>
            <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">partial_object</span><span class="p">)</span>
        <span class="k">except</span> <span class="p">(</span><span class="n">ValidationError</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">):</span>
            <span class="k">continue</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/prompts/)
