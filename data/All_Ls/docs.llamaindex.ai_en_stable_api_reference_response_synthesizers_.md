Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/

Markdown Content:
Index - LlamaIndex


Response builder class.

This class provides general functions for taking in a set of text and generating a response.

Will support different modes, from 1) stuffing chunks into prompt, 2) create and refine separately over each chunk, 3) tree summarization.

BaseSynthesizer [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[ChainableMixin](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "llama_index.core.base.query_pipeline.query.ChainableMixin")`, `PromptMixin`, `DispatcherSpanMixin`

Response builder class.

Source code in `llama-index-core/llama_index/core/response_synthesizers/base.py`

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
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseSynthesizer</span><span class="p">(</span><span class="n">ChainableMixin</span><span class="p">,</span> <span class="n">PromptMixin</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Response builder class."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_helper</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptHelper</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">BaseModel</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">callback_manager</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">prompt_helper</span>
            <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">_prompt_helper</span>
            <span class="ow">or</span> <span class="n">PromptHelper</span><span class="o">.</span><span class="n">from_llm_metadata</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">streaming</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="c1"># TODO: keep this for now since response synthesizers don't generally have sub-modules</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CallbackManager</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span>

    <span class="nd">@callback_manager</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="c1"># TODO: please fix this later</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get response."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get response."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">_log_prompt_and_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">formatted_prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">,</span>
        <span class="n">log_prefix</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Log prompt and response from LLM."""</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; </span><span class="si">{</span><span class="n">log_prefix</span><span class="si">}</span><span class="s2"> prompt template: </span><span class="si">{</span><span class="n">formatted_prompt</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; </span><span class="si">{</span><span class="n">log_prefix</span><span class="si">}</span><span class="s2"> response: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_metadata_for_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get metadata for response."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_prepare_response_output</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">response_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RESPONSE_TEXT_TYPE</span><span class="p">],</span>
        <span class="n">source_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Prepare response object from response string."""</span>
        <span class="n">response_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_metadata_for_response</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">source_nodes</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_str</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span>
                <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_str</span><span class="p">,</span> <span class="n">Generator</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">StreamingResponse</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span>
                <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_str</span><span class="p">,</span> <span class="n">AsyncGenerator</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">AsyncStreamingResponse</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span>
                <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_str</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">PydanticResponse</span><span class="p">(</span>
                <span class="n">response_str</span><span class="p">,</span> <span class="n">source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span>
            <span class="p">)</span>

        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Response must be a string or a generator. Found </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">response_str</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">QueryTextType</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">SynthesizeStartEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
                <span class="n">empty_response</span> <span class="o">=</span> <span class="n">AsyncStreamingResponse</span><span class="p">(</span>
                    <span class="n">response_gen</span><span class="o">=</span><span class="n">empty_response_agenerator</span><span class="p">()</span>
                <span class="p">)</span>
                <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">SynthesizeEndEvent</span><span class="p">(</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                        <span class="n">response</span><span class="o">=</span><span class="n">empty_response</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">empty_response</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">empty_response</span> <span class="o">=</span> <span class="n">Response</span><span class="p">(</span><span class="s2">"Empty Response"</span><span class="p">)</span>
                <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">SynthesizeEndEvent</span><span class="p">(</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                        <span class="n">response</span><span class="o">=</span><span class="n">empty_response</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">empty_response</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">SYNTHESIZE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_response</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">text_chunks</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span>
                <span class="p">],</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">additional_source_nodes</span> <span class="o">=</span> <span class="n">additional_source_nodes</span> <span class="ow">or</span> <span class="p">[]</span>
            <span class="n">source_nodes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">additional_source_nodes</span><span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_response_output</span><span class="p">(</span><span class="n">response_str</span><span class="p">,</span> <span class="n">source_nodes</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">SynthesizeEndEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""As query component."""</span>
        <span class="k">return</span> <span class="n">SynthesizerComponent</span><span class="p">(</span><span class="n">synthesizer</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_response `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer.get_response "Permanent link")

```
get_response(query_str: str, text_chunks: Sequence[str], **response_kwargs: Any) -> RESPONSE_TEXT_TYPE
```

Get response.

Source code in `llama-index-core/llama_index/core/response_synthesizers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get response."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### aget\_response `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer.aget_response "Permanent link")

```
aget_response(query_str: str, text_chunks: Sequence[str], **response_kwargs: Any) -> RESPONSE_TEXT_TYPE
```

Get response.

Source code in `llama-index-core/llama_index/core/response_synthesizers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get response."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

get\_response\_synthesizer [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.factory.get_response_synthesizer "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
get_response_synthesizer(llm: Optional[LLMPredictorType] = None, prompt_helper: Optional[PromptHelper] = None, service_context: Optional[ServiceContext] = None, text_qa_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, refine_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, summary_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, simple_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, response_mode: [ResponseMode](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "llama_index.core.response_synthesizers.type.ResponseMode") = ResponseMode.COMPACT, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, use_async: bool = False, streaming: bool = False, structured_answer_filtering: bool = False, output_cls: Optional[BaseModel] = None, program_factory: Optional[Callable[[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.prompts.PromptTemplate")], [BasePydanticProgram](https://docs.llamaindex.ai/en/stable/api_reference/program/#llama_index.core.types.BasePydanticProgram "llama_index.core.types.BasePydanticProgram")]] = None, verbose: bool = False) -> [BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.base.BaseSynthesizer")
```

Get a response synthesizer.

Source code in `llama-index-core/llama_index/core/response_synthesizers/factory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 38</span>
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
<span class="normal">174</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_response_synthesizer</span><span class="p">(</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prompt_helper</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptHelper</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">summary_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">simple_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">structured_answer_filtering</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">output_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">program_factory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">PromptTemplate</span><span class="p">],</span> <span class="n">BasePydanticProgram</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseSynthesizer</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get a response synthesizer."""</span>
    <span class="n">text_qa_template</span> <span class="o">=</span> <span class="n">text_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT_SEL</span>
    <span class="n">refine_template</span> <span class="o">=</span> <span class="n">refine_template</span> <span class="ow">or</span> <span class="n">DEFAULT_REFINE_PROMPT_SEL</span>
    <span class="n">simple_template</span> <span class="o">=</span> <span class="n">simple_template</span> <span class="ow">or</span> <span class="n">DEFAULT_SIMPLE_INPUT_PROMPT</span>
    <span class="n">summary_template</span> <span class="o">=</span> <span class="n">summary_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TREE_SUMMARIZE_PROMPT_SEL</span>

    <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
        <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
    <span class="p">)</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">prompt_helper</span> <span class="o">=</span> <span class="n">service_context</span><span class="o">.</span><span class="n">prompt_helper</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">prompt_helper</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">prompt_helper</span>
            <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">_prompt_helper</span>
            <span class="ow">or</span> <span class="n">PromptHelper</span><span class="o">.</span><span class="n">from_llm_metadata</span><span class="p">(</span>
                <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">response_mode</span> <span class="o"></span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">CompactAndRefine</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">refine_template</span><span class="o">=</span><span class="n">refine_template</span><span class="p">,</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
            <span class="n">structured_answer_filtering</span><span class="o">=</span><span class="n">structured_answer_filtering</span><span class="p">,</span>
            <span class="n">program_factory</span><span class="o">=</span><span class="n">program_factory</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="c1"># deprecated</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">response_mode</span> <span class="o"></span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">SIMPLE_SUMMARIZE</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">SimpleSummarize</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
            <span class="c1"># deprecated</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">response_mode</span> <span class="o"></span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">ACCUMULATE</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Accumulate</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
            <span class="c1"># deprecated</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">response_mode</span> <span class="o"></span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">NO_TEXT</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">NoText</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="c1"># deprecated</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown mode: </span><span class="si">{</span><span class="n">response_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ResponseMode [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Response modes of the response builder (and synthesizer).

Source code in `llama-index-core/llama_index/core/response_synthesizers/type.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 4</span>
<span class="normal"> 5</span>
<span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
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
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ResponseMode</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Response modes of the response builder (and synthesizer)."""</span>

    <span class="n">REFINE</span> <span class="o">=</span> <span class="s2">"refine"</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Refine is an iterative way of generating a response.</span>
<span class="sd">    We first use the context in the first node, along with the query, to generate an \</span>
<span class="sd">    initial answer.</span>
<span class="sd">    We then pass this answer, the query, and the context of the second node as input \</span>
<span class="sd">    into a “refine prompt” to generate a refined answer. We refine through N-1 nodes, \</span>
<span class="sd">    where N is the total number of nodes.</span>
<span class="sd">    """</span>

    <span class="n">COMPACT</span> <span class="o">=</span> <span class="s2">"compact"</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Compact and refine mode first combine text chunks into larger consolidated chunks \</span>
<span class="sd">    that more fully utilize the available context window, then refine answers \</span>
<span class="sd">    across them.</span>
<span class="sd">    This mode is faster than refine since we make fewer calls to the LLM.</span>
<span class="sd">    """</span>

    <span class="n">SIMPLE_SUMMARIZE</span> <span class="o">=</span> <span class="s2">"simple_summarize"</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Merge all text chunks into one, and make a LLM call.</span>
<span class="sd">    This will fail if the merged text chunk exceeds the context window size.</span>
<span class="sd">    """</span>

    <span class="n">TREE_SUMMARIZE</span> <span class="o">=</span> <span class="s2">"tree_summarize"</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Build a tree index over the set of candidate nodes, with a summary prompt seeded \</span>
<span class="sd">    with the query.</span>
<span class="sd">    The tree is built in a bottoms-up fashion, and in the end the root node is \</span>
<span class="sd">    returned as the response</span>
<span class="sd">    """</span>

    <span class="n">GENERATION</span> <span class="o">=</span> <span class="s2">"generation"</span>
<span class="w">    </span><span class="sd">"""Ignore context, just use LLM to generate a response."""</span>

    <span class="n">NO_TEXT</span> <span class="o">=</span> <span class="s2">"no_text"</span>
<span class="w">    </span><span class="sd">"""Return the retrieved context nodes, without synthesizing a final response."""</span>

    <span class="n">ACCUMULATE</span> <span class="o">=</span> <span class="s2">"accumulate"</span>
<span class="w">    </span><span class="sd">"""Synthesize a response for each text chunk, and then return the concatenation."""</span>

    <span class="n">COMPACT_ACCUMULATE</span> <span class="o">=</span> <span class="s2">"compact_accumulate"</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Compact and accumulate mode first combine text chunks into larger consolidated \</span>
<span class="sd">    chunks that more fully utilize the available context window, then accumulate \</span>
<span class="sd">    answers for each of them and finally return the concatenation.</span>
<span class="sd">    This mode is faster than accumulate since we make fewer calls to the LLM.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

### REFINE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.REFINE "Permanent link")

```
REFINE = 'refine'
```

Refine is an iterative way of generating a response. We first use the context in the first node, along with the query, to generate an initial answer. We then pass this answer, the query, and the context of the second node as input into a “refine prompt” to generate a refined answer. We refine through N-1 nodes, where N is the total number of nodes.

### COMPACT `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.COMPACT "Permanent link")

```
COMPACT = 'compact'
```

Compact and refine mode first combine text chunks into larger consolidated chunks that more fully utilize the available context window, then refine answers across them. This mode is faster than refine since we make fewer calls to the LLM.

### SIMPLE\_SUMMARIZE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.SIMPLE_SUMMARIZE "Permanent link")

```
SIMPLE_SUMMARIZE = 'simple_summarize'
```

Merge all text chunks into one, and make a LLM call. This will fail if the merged text chunk exceeds the context window size.

### TREE\_SUMMARIZE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.TREE_SUMMARIZE "Permanent link")

```
TREE_SUMMARIZE = 'tree_summarize'
```

Build a tree index over the set of candidate nodes, with a summary prompt seeded with the query. The tree is built in a bottoms-up fashion, and in the end the root node is returned as the response

### GENERATION `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.GENERATION "Permanent link")

```
GENERATION = 'generation'
```

Ignore context, just use LLM to generate a response.

### NO\_TEXT `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.NO_TEXT "Permanent link")

```
NO_TEXT = 'no_text'
```

Return the retrieved context nodes, without synthesizing a final response.

### ACCUMULATE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.ACCUMULATE "Permanent link")

```
ACCUMULATE = 'accumulate'
```

Synthesize a response for each text chunk, and then return the concatenation.

### COMPACT\_ACCUMULATE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.COMPACT_ACCUMULATE "Permanent link")

```
COMPACT_ACCUMULATE = 'compact_accumulate'
```

Compact and accumulate mode first combine text chunks into larger consolidated chunks that more fully utilize the available context window, then accumulate answers for each of them and finally return the concatenation. This mode is faster than accumulate since we make fewer calls to the LLM.

Back to top

[Previous Google](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/)[Next Refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/)
