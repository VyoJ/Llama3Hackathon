Title: Document summary - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/

Markdown Content:
Document summary - LlamaIndex


LlamaIndex data structures.

DocumentSummaryIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/#llama_index.core.indices.DocumentSummaryIndex "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexDocumentSummary]`

Document Summary Index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `response_synthesizer` | `[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")` | 
A response synthesizer for generating summaries.



 | `None` |
| `summary_query` | `str` | 

The query to use to generate the summary for each document.



 | `DEFAULT_SUMMARY_QUERY` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `embed_summaries` | `bool` | 

Whether to embed the summaries. This is required for running the default embedding-based retriever. Defaults to True.



 | `True` |

Source code in `llama-index-core/llama_index/core/indices/document_summary/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 62</span>
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
<span class="normal">315</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DocumentSummaryIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexDocumentSummary</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Document Summary Index.</span>

<span class="sd">    Args:</span>
<span class="sd">        response_synthesizer (BaseSynthesizer): A response synthesizer for generating</span>
<span class="sd">            summaries.</span>
<span class="sd">        summary_query (str): The query to use to generate the summary for each document.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars.</span>
<span class="sd">            Defaults to False.</span>
<span class="sd">        embed_summaries (bool): Whether to embed the summaries.</span>
<span class="sd">            This is required for running the default embedding-based retriever.</span>
<span class="sd">            Defaults to True.</span>

<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">IndexDocumentSummary</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexDocumentSummary</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summary_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_SUMMARY_QUERY</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">embed_summaries</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="n">response_mode</span><span class="o">=</span><span class="n">ResponseMode</span><span class="o">.</span><span class="n">TREE_SUMMARIZE</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_summary_query</span> <span class="o">=</span> <span class="n">summary_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_summaries</span> <span class="o">=</span> <span class="n">embed_summaries</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">vector_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePydanticVectorStore</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_RetrieverMode</span><span class="p">]</span> <span class="o">=</span> <span class="n">_RetrieverMode</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get retriever.</span>

<span class="sd">        Args:</span>
<span class="sd">            retriever_mode (Union[str, DocumentSummaryRetrieverMode]): A retriever mode.</span>
<span class="sd">                Defaults to DocumentSummaryRetrieverMode.EMBEDDING.</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.document_summary.retrievers</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">DocumentSummaryIndexEmbeddingRetriever</span><span class="p">,</span>
            <span class="n">DocumentSummaryIndexLLMRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">LLMRetriever</span> <span class="o">=</span> <span class="n">DocumentSummaryIndexLLMRetriever</span>
        <span class="n">EmbeddingRetriever</span> <span class="o">=</span> <span class="n">DocumentSummaryIndexEmbeddingRetriever</span>

        <span class="k">if</span> <span class="n">retriever_mode</span> <span class="o"></span> <span class="n">_RetrieverMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">LLMRetriever</span><span class="p">(</span>
                <span class="bp">self</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown retriever mode: </span><span class="si">{</span><span class="n">retriever_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_document_summary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get document summary by doc id.</span>

<span class="sd">        Args:</span>
<span class="sd">            doc_id (str): A document id.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">doc_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">doc_id_to_summary_id</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"doc_id </span><span class="si">{</span><span class="n">doc_id</span><span class="si">}</span><span class="s2"> not in index"</span><span class="p">)</span>
        <span class="n">summary_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">doc_id_to_summary_id</span><span class="p">[</span><span class="n">doc_id</span><span class="p">]</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">summary_id</span><span class="p">)</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_add_nodes_to_index</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">IndexDocumentSummary</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index."""</span>
        <span class="n">doc_id_to_nodes</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"ref_doc_id of node cannot be None when building a document "</span>
                    <span class="s2">"summary index"</span>
                <span class="p">)</span>
            <span class="n">doc_id_to_nodes</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="n">summary_node_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">doc_id_to_nodes</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="n">iterable_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">items</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Summarizing documents"</span>
        <span class="p">)</span>

        <span class="k">for</span> <span class="n">doc_id</span><span class="p">,</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">iterable_with_progress</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"current doc id: </span><span class="si">{</span><span class="n">doc_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">nodes_with_scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">n</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
            <span class="c1"># get the summary for each doc_id</span>
            <span class="n">summary_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_summary_query</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes_with_scores</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">summary_response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Response</span><span class="p">,</span> <span class="n">summary_response</span><span class="p">)</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">doc_id_to_nodes</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">doc_id</span><span class="p">,</span> <span class="p">[</span><span class="n">TextNode</span><span class="p">()])[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">metadata</span>
            <span class="n">summary_node_dict</span><span class="p">[</span><span class="n">doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">summary_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span>
                <span class="n">relationships</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">:</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span><span class="n">node_id</span><span class="o">=</span><span class="n">doc_id</span><span class="p">)</span>
                <span class="p">},</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">([</span><span class="n">summary_node_dict</span><span class="p">[</span><span class="n">doc_id</span><span class="p">]])</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; Generated summary for doc </span><span class="si">{</span><span class="n">doc_id</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">summary_response</span><span class="o">.</span><span class="n">response</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">doc_id</span><span class="p">,</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">doc_id_to_nodes</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">index_struct</span><span class="o">.</span><span class="n">add_summary_and_nodes</span><span class="p">(</span><span class="n">summary_node_dict</span><span class="p">[</span><span class="n">doc_id</span><span class="p">],</span> <span class="n">nodes</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_summaries</span><span class="p">:</span>
            <span class="n">summary_nodes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">summary_node_dict</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
            <span class="n">id_to_embed_map</span> <span class="o">=</span> <span class="n">embed_nodes</span><span class="p">(</span>
                <span class="n">summary_nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span>
            <span class="p">)</span>

            <span class="n">summary_nodes_with_embedding</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">summary_nodes</span><span class="p">:</span>
                <span class="n">node_with_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                <span class="n">node_with_embedding</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">id_to_embed_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span>
                <span class="n">summary_nodes_with_embedding</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_embedding</span><span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">summary_nodes_with_embedding</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexDocumentSummary</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build index from nodes."""</span>
        <span class="c1"># first get doc_id to nodes_dict, generate a summary for each doc_id,</span>
        <span class="c1"># then build the index struct</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="n">IndexDocumentSummary</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_add_nodes_to_index</span><span class="p">(</span><span class="n">index_struct</span><span class="p">,</span> <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">index_struct</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_add_nodes_to_index</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a list of nodes from the index.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_ids (List[str]): A list of node_ids from the nodes to delete</span>

<span class="sd">        """</span>
        <span class="n">index_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">node_id_to_summary_id</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">index_nodes</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"node_id </span><span class="si">{</span><span class="n">node</span><span class="si">}</span><span class="s2"> not found, will not be deleted."</span><span class="p">)</span>
                <span class="n">node_ids</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">)</span>

        <span class="n">remove_summary_ids</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">summary_id</span>
            <span class="k">for</span> <span class="n">summary_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">summary_id_to_node_ids</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">summary_id_to_node_ids</span><span class="p">[</span><span class="n">summary_id</span><span class="p">])</span> <span class="o"></span> <span class="n">_RetrieverMode</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_summaries</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot use embedding retriever if embed_summaries is False"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">EmbeddingRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">if</span> <span class="n">retriever_mode</span> <span class="o"></span> <span class="mi">0</span>
    <span class="p">]</span>

    <span class="n">remove_docs</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">doc_id</span>
        <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">doc_id_to_summary_id</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">doc_id_to_summary_id</span><span class="p">[</span><span class="n">doc_id</span><span class="p">]</span> <span class="ow">in</span> <span class="n">remove_summary_ids</span>
    <span class="p">]</span>

    <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">remove_docs</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">doc_id</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/#llama_index.core.indices.DocumentSummaryIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a document from the index. All nodes in the index related to the document will be deleted.

Source code in `llama-index-core/llama_index/core/indices/document_summary/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">285</span>
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
<span class="normal">301</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document from the index.</span>
<span class="sd">    All nodes in the index related to the document will be deleted.</span>
<span class="sd">    """</span>
    <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">ref_doc_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"ref_doc_id </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2"> not found, nothing deleted."</span><span class="p">)</span>
        <span class="k">return</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/)[Next Google](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/)
