Title: Knowledge graph - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/

Markdown Content:
Knowledge graph - LlamaIndex


KGTableRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/#llama_index.core.retrievers.KGTableRetriever "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

KG Table Retriever.

Arguments are shared among subclasses.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_keyword_extract_template` | `Optional[QueryKGExtractPrompt]` | 
A Query KG Extraction Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `refine_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A Refinement Prompt (see :ref:`Prompt-Templates`).



 | _required_ |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A Question Answering Prompt (see :ref:`Prompt-Templates`).



 | _required_ |
| `max_keywords_per_query` | `int` | 

Maximum number of keywords to extract from query.



 | `10` |
| `num_chunks_per_query` | `int` | 

Maximum number of text chunks to query.



 | `10` |
| `include_text` | `bool` | 

Use the document text source from each relevant triplet during queries.



 | `True` |
| `retriever_mode` | `KGRetrieverMode` | 

Specifies whether to use keywords, embeddings, or both to find relevant triplets. Should be one of "keyword", "embedding", or "hybrid".



 | `KEYWORD` |
| `similarity_top_k` | `int` | 

The number of top embeddings to use (if embeddings are used).



 | `2` |
| `graph_store_query_depth` | `int` | 

The depth of the graph store query.



 | `2` |
| `use_global_node_triplets` | `bool` | 

Whether to get more keywords(entities) from text chunks matched by keywords. This helps introduce more global knowledge. While it's more expensive, thus to be turned off by default.



 | `False` |
| `max_knowledge_sequence` | `int` | 

The maximum number of knowledge sequence to include in the response. By default, it's 30.



 | `REL_TEXT_LIMIT` |

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 65</span>
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
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="o">.</span><span class="n">deprecated</span><span class="p">(</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">"0.10.53"</span><span class="p">,</span>
    <span class="n">reason</span><span class="o">=</span><span class="p">(</span>
        <span class="s2">"KGTableRetriever is deprecated, it is recommended to use "</span>
        <span class="s2">"PropertyGraphIndex and associated retrievers instead."</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="k">class</span> <span class="nc">KGTableRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""KG Table Retriever.</span>

<span class="sd">    Arguments are shared among subclasses.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_keyword_extract_template (Optional[QueryKGExtractPrompt]): A Query</span>
<span class="sd">            KG Extraction</span>
<span class="sd">            Prompt (see :ref:`Prompt-Templates`).</span>
<span class="sd">        refine_template (Optional[BasePromptTemplate]): A Refinement Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): A Question Answering Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        max_keywords_per_query (int): Maximum number of keywords to extract from query.</span>
<span class="sd">        num_chunks_per_query (int): Maximum number of text chunks to query.</span>
<span class="sd">        include_text (bool): Use the document text source from each relevant triplet</span>
<span class="sd">            during queries.</span>
<span class="sd">        retriever_mode (KGRetrieverMode): Specifies whether to use keywords,</span>
<span class="sd">            embeddings, or both to find relevant triplets. Should be one of "keyword",</span>
<span class="sd">            "embedding", or "hybrid".</span>
<span class="sd">        similarity_top_k (int): The number of top embeddings to use</span>
<span class="sd">            (if embeddings are used).</span>
<span class="sd">        graph_store_query_depth (int): The depth of the graph store query.</span>
<span class="sd">        use_global_node_triplets (bool): Whether to get more keywords(entities) from</span>
<span class="sd">            text chunks matched by keywords. This helps introduce more global knowledge.</span>
<span class="sd">            While it's more expensive, thus to be turned off by default.</span>
<span class="sd">        max_knowledge_sequence (int): The maximum number of knowledge sequence to</span>
<span class="sd">            include in the response. By default, it's 30.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">KnowledgeGraphIndex</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_keyword_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_keywords_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">num_chunks_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">include_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">KGRetrieverMode</span><span class="p">]</span> <span class="o">=</span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">KEYWORD</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">graph_store_query_depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">use_global_node_triplets</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_knowledge_sequence</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">REL_TEXT_LIMIT</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">KnowledgeGraphIndex</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">index_struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">docstore</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span> <span class="o">=</span> <span class="n">max_keywords_per_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_chunks_per_query</span> <span class="o">=</span> <span class="n">num_chunks_per_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_keyword_extract_template</span> <span class="o">=</span> <span class="n">query_keyword_extract_template</span> <span class="ow">or</span> <span class="n">DQKET</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_include_text</span> <span class="o">=</span> <span class="n">include_text</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">KGRetrieverMode</span><span class="p">(</span><span class="n">retriever_mode</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">retriever_mode</span>
            <span class="k">else</span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">KEYWORD</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">graph_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graph_store_query_depth</span> <span class="o">=</span> <span class="n">graph_store_query_depth</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_global_node_triplets</span> <span class="o">=</span> <span class="n">use_global_node_triplets</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_knowledge_sequence</span> <span class="o">=</span> <span class="n">max_knowledge_sequence</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"verbose"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
        <span class="n">refresh_schema</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"refresh_schema"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">get_schema</span><span class="p">(</span><span class="n">refresh</span><span class="o">=</span><span class="n">refresh_schema</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to get graph schema: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
            <span class="p">),</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_keyword_extract_template</span><span class="p">,</span>
            <span class="n">max_keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span><span class="p">,</span>
            <span class="n">question</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="n">extract_keywords_given_response</span><span class="p">(</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">start_token</span><span class="o">=</span><span class="s2">"KEYWORDS:"</span><span class="p">,</span> <span class="n">lowercase</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">keywords</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_extract_rel_text_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rel_texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Find the keywords for given rel text triplets."""</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">rel_text</span> <span class="ow">in</span> <span class="n">rel_texts</span><span class="p">:</span>
            <span class="n">splited_texts</span> <span class="o">=</span> <span class="n">rel_text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">","</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splited_texts</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">keyword</span> <span class="o">=</span> <span class="n">splited_texts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">keyword</span><span class="p">:</span>
                <span class="n">keywords</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">keyword</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">"(</span><span class="se">\"</span><span class="s2">'"</span><span class="p">))</span>

            <span class="c1"># Return the Object as well</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splited_texts</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">2</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">keyword</span> <span class="o">=</span> <span class="n">splited_texts</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">keyword</span><span class="p">:</span>
                <span class="n">keywords</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">keyword</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">" ()</span><span class="se">\"</span><span class="s2">'"</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">keywords</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">node_visited</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keywords</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted keywords: </span><span class="si">{</span><span class="n">keywords</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>
        <span class="n">rel_texts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">cur_rel_map</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">chunk_indices_count</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="o">!=</span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">keyword</span> <span class="ow">in</span> <span class="n">keywords</span><span class="p">:</span>
                <span class="n">subjs</span> <span class="o">=</span> <span class="p">{</span><span class="n">keyword</span><span class="p">}</span>
                <span class="n">node_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">search_node_by_keyword</span><span class="p">(</span><span class="n">keyword</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">[:</span><span class="n">GLOBAL_EXPLORE_NODE_LIMIT</span><span class="p">]:</span>
                    <span class="k">if</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_visited</span><span class="p">:</span>
                        <span class="k">continue</span>

                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_include_text</span><span class="p">:</span>
                        <span class="n">chunk_indices_count</span><span class="p">[</span><span class="n">node_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>

                    <span class="n">node_visited</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_global_node_triplets</span><span class="p">:</span>
                        <span class="c1"># Get nodes from keyword search, and add them to the subjs</span>
                        <span class="c1"># set. This helps introduce more global knowledge into the</span>
                        <span class="c1"># query. While it's more expensive, thus to be turned off</span>
                        <span class="c1"># by default, it can be useful for some applications.</span>

                        <span class="c1"># TODO: we should a keyword-node_id map in IndexStruct, so that</span>
                        <span class="c1"># node-keywords extraction with LLM will be called only once</span>
                        <span class="c1"># during indexing.</span>
                        <span class="n">extended_subjs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keywords</span><span class="p">(</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span>
                                <span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span>
                            <span class="p">)</span>
                        <span class="p">)</span>
                        <span class="n">subjs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extended_subjs</span><span class="p">)</span>

                <span class="n">rel_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">get_rel_map</span><span class="p">(</span>
                    <span class="nb">list</span><span class="p">(</span><span class="n">subjs</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store_query_depth</span>
                <span class="p">)</span>

                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"rel_map: </span><span class="si">{</span><span class="n">rel_map</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

                <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_map</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="n">rel_texts</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="nb">str</span><span class="p">(</span><span class="n">rel_obj</span><span class="p">)</span>
                        <span class="k">for</span> <span class="n">rel_objs</span> <span class="ow">in</span> <span class="n">rel_map</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
                        <span class="k">for</span> <span class="n">rel_obj</span> <span class="ow">in</span> <span class="n">rel_objs</span>
                    <span class="p">]</span>
                <span class="p">)</span>
                <span class="n">cur_rel_map</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">rel_map</span><span class="p">)</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="o">!=</span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">KEYWORD</span>
            <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">embedding_dict</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
        <span class="p">):</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
            <span class="p">)</span>
            <span class="n">all_rel_texts</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">embedding_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

            <span class="n">rel_text_embeddings</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">embedding_dict</span><span class="p">[</span><span class="n">_id</span><span class="p">]</span> <span class="k">for</span> <span class="n">_id</span> <span class="ow">in</span> <span class="n">all_rel_texts</span>
            <span class="p">]</span>
            <span class="n">similarities</span><span class="p">,</span> <span class="n">top_rel_texts</span> <span class="o">=</span> <span class="n">get_top_k_embeddings</span><span class="p">(</span>
                <span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">rel_text_embeddings</span><span class="p">,</span>
                <span class="n">similarity_top_k</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">embedding_ids</span><span class="o">=</span><span class="n">all_rel_texts</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Found the following rel_texts+query similarites: </span><span class="si">{</span><span class="n">similarities</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Found the following top_k rel_texts: </span><span class="si">{</span><span class="n">rel_texts</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">rel_texts</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">top_rel_texts</span><span class="p">)</span>

        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">embedding_dict</span><span class="p">)</span> <span class="o"></span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
            <span class="n">rel_texts</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">rel_texts</span><span class="p">))</span>

            <span class="c1"># remove shorter rel_texts that are substrings of longer rel_texts</span>
            <span class="n">rel_texts</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="nb">len</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">rel_texts</span><span class="p">)):</span>
                <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">rel_texts</span><span class="p">)):</span>
                    <span class="k">if</span> <span class="n">rel_texts</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="ow">in</span> <span class="n">rel_texts</span><span class="p">[</span><span class="n">i</span><span class="p">]:</span>
                        <span class="n">rel_texts</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">rel_texts</span> <span class="o">=</span> <span class="p">[</span><span class="n">rel_text</span> <span class="k">for</span> <span class="n">rel_text</span> <span class="ow">in</span> <span class="n">rel_texts</span> <span class="k">if</span> <span class="n">rel_text</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">]</span>

            <span class="c1"># truncate rel_texts</span>
            <span class="n">rel_texts</span> <span class="o">=</span> <span class="n">rel_texts</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_knowledge_sequence</span><span class="p">]</span>

        <span class="c1"># When include_text = True just get the actual content of all the nodes</span>
        <span class="c1"># (Nodes with actual keyword match, Nodes which are found from the depth search and Nodes founnd from top_k similarity)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_include_text</span><span class="p">:</span>
            <span class="n">keywords</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_rel_text_keywords</span><span class="p">(</span>
                <span class="n">rel_texts</span>
            <span class="p">)</span>  <span class="c1"># rel_texts will have all the Triplets retrieved with respect to the Query</span>
            <span class="n">nested_node_ids</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">search_node_by_keyword</span><span class="p">(</span><span class="n">keyword</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">keyword</span> <span class="ow">in</span> <span class="n">keywords</span>
            <span class="p">]</span>
            <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">_id</span> <span class="k">for</span> <span class="n">ids</span> <span class="ow">in</span> <span class="n">nested_node_ids</span> <span class="k">for</span> <span class="n">_id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
                <span class="n">chunk_indices_count</span><span class="p">[</span><span class="n">node_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="n">sorted_chunk_indices</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span>
            <span class="n">chunk_indices_count</span><span class="o">.</span><span class="n">keys</span><span class="p">(),</span>
            <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">chunk_indices_count</span><span class="p">[</span><span class="n">x</span><span class="p">],</span>
            <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">sorted_chunk_indices</span> <span class="o">=</span> <span class="n">sorted_chunk_indices</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_chunks_per_query</span><span class="p">]</span>
        <span class="n">sorted_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">sorted_chunk_indices</span><span class="p">)</span>

        <span class="c1"># TMP/TODO: also filter rel_texts as nodes until we figure out better</span>
        <span class="c1"># abstraction</span>
        <span class="c1"># TODO(suo): figure out what this does</span>
        <span class="c1"># rel_text_nodes = [Node(text=rel_text) for rel_text in rel_texts]</span>
        <span class="c1"># for node_processor in self._node_postprocessors:</span>
        <span class="c1">#     rel_text_nodes = node_processor.postprocess_nodes(rel_text_nodes)</span>
        <span class="c1"># rel_texts = [node.get_content() for node in rel_text_nodes]</span>

        <span class="n">sorted_nodes_with_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">chunk_idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">sorted_chunk_indices</span><span class="p">,</span> <span class="n">sorted_nodes</span><span class="p">):</span>
            <span class="c1"># nodes are found with keyword mapping, give high conf to avoid cutoff</span>
            <span class="n">sorted_nodes_with_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">DEFAULT_NODE_SCORE</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; Querying with idx: </span><span class="si">{</span><span class="n">chunk_idx</span><span class="si">}</span><span class="s2">: "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">truncate_text</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span><span class="w"> </span><span class="mi">80</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="c1"># if no relationship is found, return the nodes found by keywords</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_texts</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"&gt; No relationships found, returning nodes found by keywords."</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sorted_nodes_with_scores</span><span class="p">)</span> <span class="o"></span> <span class="s2">"intersection"</span><span class="p">:</span>
            <span class="k">assert</span> <span class="nb">all</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="n">handle_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span>
                    <span class="n">handle_llm_prompt_template</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span>
                <span class="p">]</span>
            <span class="p">),</span> <span class="s2">"Must provide entity extract function and template."</span>
        <span class="k">assert</span> <span class="nb">any</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="n">handle_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span>
                <span class="n">handle_llm_prompt_template</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span>
            <span class="p">]</span>
        <span class="p">),</span> <span class="s2">"Must provide either entity extract function or template."</span>
        <span class="n">enitities_fn</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">enitities_llm</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">handle_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">enitities_fn</span> <span class="o">=</span> <span class="n">handle_fn</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">handle_llm_prompt_template</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="n">handle_llm_prompt_template</span><span class="p">,</span>
                <span class="n">max_keywords</span><span class="o">=</span><span class="n">max_items</span><span class="p">,</span>
                <span class="n">question</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">enitities_llm</span> <span class="o">=</span> <span class="n">extract_keywords_given_response</span><span class="p">(</span>
                <span class="n">response</span><span class="p">,</span> <span class="n">start_token</span><span class="o">=</span><span class="n">result_start_token</span><span class="p">,</span> <span class="n">lowercase</span><span class="o">=</span><span class="kc">False</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">cross_handle_policy</span> <span class="o"></span> <span class="s2">"intersection"</span><span class="p">:</span>
            <span class="n">entities</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">enitities_fn</span><span class="p">)</span><span class="o">.</span><span class="n">intersection</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">enitities_llm</span><span class="p">)))</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Entities processed: </span><span class="si">{</span><span class="n">entities</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">entities</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aprocess_entities</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">handle_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span>
        <span class="n">handle_llm_prompt_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">],</span>
        <span class="n">cross_handle_policy</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"union"</span><span class="p">,</span>
        <span class="n">max_items</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">result_start_token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"KEYWORDS:"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get entities from query string."""</span>
        <span class="k">assert</span> <span class="n">cross_handle_policy</span> <span class="ow">in</span> <span class="p">[</span>
            <span class="s2">"union"</span><span class="p">,</span>
            <span class="s2">"intersection"</span><span class="p">,</span>
        <span class="p">],</span> <span class="s2">"Invalid entity extraction policy."</span>
        <span class="k">if</span> <span class="n">cross_handle_policy</span> <span class="o"></span> <span class="s2">"union"</span><span class="p">:</span>
            <span class="n">entities</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">enitities_fn</span><span class="p">)</span> <span class="o">|</span> <span class="n">enitities_llm</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">cross_handle_policy</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"&gt; No knowledge sequence extracted from entities."</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="n">_new_line_char</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="n">context_string</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"The following are knowledge sequence in max depth"</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_graph_traversal_depth</span><span class="si">}</span><span class="s2"> "</span>
            <span class="sa">f</span><span class="s2">"in the form of directed graph like:</span><span class="se">\n</span><span class="s2">"</span>
            <span class="sa">f</span><span class="s2">"`subject -[predicate]-&gt;, object, &lt;-[predicate_next_hop]-,"</span>
            <span class="sa">f</span><span class="s2">" object_next_hop ...`"</span>
            <span class="sa">f</span><span class="s2">" extracted based on key entities as subject:</span><span class="se">\n</span><span class="s2">"</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">_new_line_char</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">knowledge_sequence</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph RAG context:</span><span class="se">\n</span><span class="si">{</span><span class="n">context_string</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>

        <span class="n">rel_node_info</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"kg_rel_map"</span><span class="p">:</span> <span class="n">rel_map</span><span class="p">,</span>
            <span class="s2">"kg_rel_text"</span><span class="p">:</span> <span class="n">knowledge_sequence</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">metadata_keys</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"kg_rel_map"</span><span class="p">,</span> <span class="s2">"kg_rel_text"</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">:</span>
            <span class="n">rel_node_info</span><span class="p">[</span><span class="s2">"kg_schema"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"schema"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">}</span>
            <span class="n">metadata_keys</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">"kg_schema"</span><span class="p">)</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
            <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">context_string</span><span class="p">,</span>
                <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">rel_node_info</span><span class="p">,</span>
                <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">metadata_keys</span><span class="p">,</span>
                <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">metadata_keys</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_retrieve_keyword</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve in keyword mode."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"keyword"</span><span class="p">,</span> <span class="s2">"keyword_embedding"</span><span class="p">]:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="c1"># Get entities</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_entities</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="c1"># Before we enable embedding/semantic search, we need to make sure</span>
        <span class="c1"># we don't miss any entities that's synoynm of the entities we extracted</span>
        <span class="c1"># in string matching based retrieval in following steps, thus we expand</span>
        <span class="c1"># synonyms here.</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"&gt; No entities extracted from query string."</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="c1"># Get SubGraph from Graph Store as Knowledge Sequence</span>
        <span class="n">knowledge_sequence</span><span class="p">,</span> <span class="n">rel_map</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_knowledge_sequence</span><span class="p">(</span><span class="n">entities</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_nodes</span><span class="p">(</span><span class="n">knowledge_sequence</span><span class="p">,</span> <span class="n">rel_map</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve in embedding mode."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"embedding"</span><span class="p">,</span> <span class="s2">"keyword_embedding"</span><span class="p">]:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="c1"># TBD: will implement this later with vector store.</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve_embedding</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve in embedding mode."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"embedding"</span><span class="p">,</span> <span class="s2">"keyword_embedding"</span><span class="p">]:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="c1"># TBD: will implement this later with vector store.</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Build nodes for response."""</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_with_nl2graphquery</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">nodes_nl2graphquery</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_query_engine</span><span class="o">.</span><span class="n">_retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes_nl2graphquery</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error in retrieving from nl2graphquery: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_keyword</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_embedding</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Build nodes for response."""</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_with_nl2graphquery</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">nodes_nl2graphquery</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_query_engine</span><span class="o">.</span><span class="n">_aretrieve</span><span class="p">(</span>
                    <span class="n">query_bundle</span>
                <span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes_nl2graphquery</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error in retrieving from nl2graphquery: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve_keyword</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve_embedding</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Keyword](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/)[Next Mongodb atlas bm25 retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/)
