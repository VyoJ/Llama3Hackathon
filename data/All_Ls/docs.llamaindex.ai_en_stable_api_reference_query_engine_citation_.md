Title: Citation - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/

Markdown Content:
Citation - LlamaIndex


CitationQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/#llama_index.core.query_engine.CitationQueryEngine "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Citation query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 
A retriever object.



 | _required_ |
| `response_synthesizer` | `Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")]` | 

A BaseSynthesizer object.



 | `None` |
| `citation_chunk_size` | `int` | 

Size of citation chunks, default=512. Useful for controlling granularity of sources.



 | `DEFAULT_CITATION_CHUNK_SIZE` |
| `citation_chunk_overlap` | `int` | 

Overlap of citation nodes, default=20.



 | `DEFAULT_CITATION_CHUNK_OVERLAP` |
| `text_splitter` | `Optional[TextSplitter]` | 

A text splitter for creating citation source nodes. Default is a SentenceSplitter.



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager.



 | `None` |
| `metadata_mode` | `MetadataMode` | 

A MetadataMode object that controls how metadata is included in the citation prompt.



 | `NONE` |

Source code in `llama-index-core/llama_index/core/query_engine/citation_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 87</span>
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
<span class="normal">330</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CitationQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Citation query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (BaseRetriever): A retriever object.</span>
<span class="sd">        response_synthesizer (Optional[BaseSynthesizer]):</span>
<span class="sd">            A BaseSynthesizer object.</span>
<span class="sd">        citation_chunk_size (int):</span>
<span class="sd">            Size of citation chunks, default=512. Useful for controlling</span>
<span class="sd">            granularity of sources.</span>
<span class="sd">        citation_chunk_overlap (int): Overlap of citation nodes, default=20.</span>
<span class="sd">        text_splitter (Optional[TextSplitter]):</span>
<span class="sd">            A text splitter for creating citation source nodes. Default is</span>
<span class="sd">            a SentenceSplitter.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>
<span class="sd">        metadata_mode (MetadataMode): A MetadataMode object that controls how</span>
<span class="sd">            metadata is included in the citation prompt.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">citation_chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">citation_chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">text_splitter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextSplitter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">text_splitter</span> <span class="o">=</span> <span class="n">text_splitter</span> <span class="ow">or</span> <span class="n">SentenceSplitter</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">citation_chunk_size</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">citation_chunk_overlap</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">retriever</span><span class="o">.</span><span class="n">get_service_context</span><span class="p">()</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_mode</span> <span class="o">=</span> <span class="n">metadata_mode</span>

        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_args</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseGPTIndex</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">citation_chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">citation_chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">text_splitter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextSplitter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">citation_qa_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">CITATION_QA_TEMPLATE</span><span class="p">,</span>
        <span class="n">citation_refine_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">CITATION_REFINE_TEMPLATE</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseRetriever</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># response synthesizer args</span>
        <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># class-specific args</span>
        <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CitationQueryEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a CitationQueryEngine object.".</span>

<span class="sd">        Args:</span>
<span class="sd">            index: (BastGPTIndex): index to use for querying</span>
<span class="sd">            llm: (Optional[LLM]): LLM object to use for response generation.</span>
<span class="sd">            citation_chunk_size (int):</span>
<span class="sd">                Size of citation chunks, default=512. Useful for controlling</span>
<span class="sd">                granularity of sources.</span>
<span class="sd">            citation_chunk_overlap (int): Overlap of citation nodes, default=20.</span>
<span class="sd">            text_splitter (Optional[TextSplitter]):</span>
<span class="sd">                A text splitter for creating citation source nodes. Default is</span>
<span class="sd">                a SentenceSplitter.</span>
<span class="sd">            citation_qa_template (BasePromptTemplate): Template for initial citation QA</span>
<span class="sd">            citation_refine_template (BasePromptTemplate):</span>
<span class="sd">                Template for citation refinement.</span>
<span class="sd">            retriever (BaseRetriever): A retriever object.</span>
<span class="sd">            service_context (Optional[ServiceContext]): A ServiceContext object.</span>
<span class="sd">            node_postprocessors (Optional[List[BaseNodePostprocessor]]): A list of</span>
<span class="sd">                node postprocessors.</span>
<span class="sd">            verbose (bool): Whether to print out debug info.</span>
<span class="sd">            response_mode (ResponseMode): A ResponseMode object.</span>
<span class="sd">            use_async (bool): Whether to use async.</span>
<span class="sd">            streaming (bool): Whether to use streaming.</span>
<span class="sd">            optimizer (Optional[BaseTokenUsageOptimizer]): A BaseTokenUsageOptimizer</span>
<span class="sd">                object.</span>

<span class="sd">        """</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="n">retriever</span> <span class="ow">or</span> <span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">index</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">citation_qa_template</span><span class="p">,</span>
            <span class="n">refine_template</span><span class="o">=</span><span class="n">citation_refine_template</span><span class="p">,</span>
            <span class="n">response_mode</span><span class="o">=</span><span class="n">response_mode</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
            <span class="p">),</span>
            <span class="n">citation_chunk_size</span><span class="o">=</span><span class="n">citation_chunk_size</span><span class="p">,</span>
            <span class="n">citation_chunk_overlap</span><span class="o">=</span><span class="n">citation_chunk_overlap</span><span class="p">,</span>
            <span class="n">text_splitter</span><span class="o">=</span><span class="n">text_splitter</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
            <span class="n">metadata_mode</span><span class="o">=</span><span class="n">metadata_mode</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"response_synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_create_citation_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Modify retrieved nodes to be granular sources."""</span>
        <span class="n">new_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">text_chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_splitter</span><span class="o">.</span><span class="n">split_text</span><span class="p">(</span>
                <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_mode</span><span class="p">)</span>
            <span class="p">)</span>

            <span class="k">for</span> <span class="n">text_chunk</span> <span class="ow">in</span> <span class="n">text_chunks</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Source </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">)</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="si">{</span><span class="n">text_chunk</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

                <span class="n">new_node</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="p">),</span> <span class="n">score</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">score</span>
                <span class="p">)</span>
                <span class="n">new_node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text</span>
                <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_node</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_nodes</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the retriever object."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span>

    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_citation_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">asynthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_citation_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_citation_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_citation_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/#llama_index.core.query_engine.CitationQueryEngine.retriever "Permanent link")

```
retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Get the retriever object.

### from\_args `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/#llama_index.core.query_engine.CitationQueryEngine.from_args "Permanent link")

```
from_args(index: BaseGPTIndex, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, response_synthesizer: Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")] = None, citation_chunk_size: int = DEFAULT_CITATION_CHUNK_SIZE, citation_chunk_overlap: int = DEFAULT_CITATION_CHUNK_OVERLAP, text_splitter: Optional[TextSplitter] = None, citation_qa_template: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate") = CITATION_QA_TEMPLATE, citation_refine_template: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate") = CITATION_REFINE_TEMPLATE, retriever: Optional[[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")] = None, node_postprocessors: Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]] = None, response_mode: [ResponseMode](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "llama_index.core.response_synthesizers.ResponseMode") = ResponseMode.COMPACT, use_async: bool = False, streaming: bool = False, metadata_mode: MetadataMode = MetadataMode.NONE, **kwargs: Any) -> [CitationQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/#llama_index.core.query_engine.CitationQueryEngine "llama_index.core.query_engine.citation_query_engine.CitationQueryEngine")
```

Initialize a CitationQueryEngine object.".

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `BaseGPTIndex` | 
(BastGPTIndex): index to use for querying



 | _required_ |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

(Optional\[LLM\]): LLM object to use for response generation.



 | `None` |
| `citation_chunk_size` | `int` | 

Size of citation chunks, default=512. Useful for controlling granularity of sources.



 | `DEFAULT_CITATION_CHUNK_SIZE` |
| `citation_chunk_overlap` | `int` | 

Overlap of citation nodes, default=20.



 | `DEFAULT_CITATION_CHUNK_OVERLAP` |
| `text_splitter` | `Optional[TextSplitter]` | 

A text splitter for creating citation source nodes. Default is a SentenceSplitter.



 | `None` |
| `citation_qa_template` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")` | 

Template for initial citation QA



 | `CITATION_QA_TEMPLATE` |
| `citation_refine_template` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")` | 

Template for citation refinement.



 | `CITATION_REFINE_TEMPLATE` |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 

A retriever object.



 | `None` |
| `service_context` | `Optional[ServiceContext]` | 

A ServiceContext object.



 | _required_ |
| `node_postprocessors` | `Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]]` | 

A list of node postprocessors.



 | `None` |
| `verbose` | `bool` | 

Whether to print out debug info.



 | _required_ |
| `response_mode` | `[ResponseMode](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "llama_index.core.response_synthesizers.ResponseMode")` | 

A ResponseMode object.



 | `[COMPACT](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.COMPACT "llama_index.core.response_synthesizers.ResponseMode.COMPACT")` |
| `use_async` | `bool` | 

Whether to use async.



 | `False` |
| `streaming` | `bool` | 

Whether to use streaming.



 | `False` |
| `optimizer` | `Optional[BaseTokenUsageOptimizer]` | 

A BaseTokenUsageOptimizer object.



 | _required_ |

Source code in `llama-index-core/llama_index/core/query_engine/citation_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
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
<span class="normal">215</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_args</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">index</span><span class="p">:</span> <span class="n">BaseGPTIndex</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">citation_chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_SIZE</span><span class="p">,</span>
    <span class="n">citation_chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CITATION_CHUNK_OVERLAP</span><span class="p">,</span>
    <span class="n">text_splitter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextSplitter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">citation_qa_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">CITATION_QA_TEMPLATE</span><span class="p">,</span>
    <span class="n">citation_refine_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">CITATION_REFINE_TEMPLATE</span><span class="p">,</span>
    <span class="n">retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseRetriever</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># response synthesizer args</span>
    <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
    <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="c1"># class-specific args</span>
    <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CitationQueryEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a CitationQueryEngine object.".</span>

<span class="sd">    Args:</span>
<span class="sd">        index: (BastGPTIndex): index to use for querying</span>
<span class="sd">        llm: (Optional[LLM]): LLM object to use for response generation.</span>
<span class="sd">        citation_chunk_size (int):</span>
<span class="sd">            Size of citation chunks, default=512. Useful for controlling</span>
<span class="sd">            granularity of sources.</span>
<span class="sd">        citation_chunk_overlap (int): Overlap of citation nodes, default=20.</span>
<span class="sd">        text_splitter (Optional[TextSplitter]):</span>
<span class="sd">            A text splitter for creating citation source nodes. Default is</span>
<span class="sd">            a SentenceSplitter.</span>
<span class="sd">        citation_qa_template (BasePromptTemplate): Template for initial citation QA</span>
<span class="sd">        citation_refine_template (BasePromptTemplate):</span>
<span class="sd">            Template for citation refinement.</span>
<span class="sd">        retriever (BaseRetriever): A retriever object.</span>
<span class="sd">        service_context (Optional[ServiceContext]): A ServiceContext object.</span>
<span class="sd">        node_postprocessors (Optional[List[BaseNodePostprocessor]]): A list of</span>
<span class="sd">            node postprocessors.</span>
<span class="sd">        verbose (bool): Whether to print out debug info.</span>
<span class="sd">        response_mode (ResponseMode): A ResponseMode object.</span>
<span class="sd">        use_async (bool): Whether to use async.</span>
<span class="sd">        streaming (bool): Whether to use streaming.</span>
<span class="sd">        optimizer (Optional[BaseTokenUsageOptimizer]): A BaseTokenUsageOptimizer</span>
<span class="sd">            object.</span>

<span class="sd">    """</span>
    <span class="n">retriever</span> <span class="o">=</span> <span class="n">retriever</span> <span class="ow">or</span> <span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">service_context</span><span class="o">=</span><span class="n">index</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="o">=</span><span class="n">citation_qa_template</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="o">=</span><span class="n">citation_refine_template</span><span class="p">,</span>
        <span class="n">response_mode</span><span class="o">=</span><span class="n">response_mode</span><span class="p">,</span>
        <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
        <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="p">),</span>
        <span class="n">citation_chunk_size</span><span class="o">=</span><span class="n">citation_chunk_size</span><span class="p">,</span>
        <span class="n">citation_chunk_overlap</span><span class="o">=</span><span class="n">citation_chunk_overlap</span><span class="p">,</span>
        <span class="n">text_splitter</span><span class="o">=</span><span class="n">text_splitter</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
        <span class="n">metadata_mode</span><span class="o">=</span><span class="n">metadata_mode</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous SQL table retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/)[Next Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/)
