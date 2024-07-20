Title: Knowledge graph - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/

Markdown Content:
Knowledge graph - LlamaIndex


LlamaIndex data structures.

KnowledgeGraphIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[KG]`

Knowledge Graph Index.

Build a KG by extracting triplets, and leveraging the KG during query-time.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `kg_triplet_extract_template` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 
The prompt to use for extracting triplets.



 | `None` |
| `max_triplets_per_chunk` | `int` | 

The maximum number of triplets to extract.



 | `10` |
| `service_context` | `Optional[ServiceContext]` | 

The service context to use.



 | `None` |
| `storage_context` | `Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")]` | 

The storage context to use.



 | `None` |
| `graph_store` | `Optional[[GraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "llama_index.core.graph_stores.types.GraphStore")]` | 

The graph store to use.



 | _required_ |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `include_embeddings` | `bool` | 

Whether to include embeddings in the index. Defaults to False.



 | `False` |
| `max_object_length` | `int` | 

The maximum length of the object in a triplet. Defaults to 128.



 | `128` |
| `kg_triplet_extract_fn` | `Optional[Callable]` | 

The function to use for extracting triplets. Defaults to None.



 | `None` |

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
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
<span class="normal">384</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="o">.</span><span class="n">deprecated</span><span class="p">(</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">"0.10.53"</span><span class="p">,</span>
    <span class="n">reason</span><span class="o">=</span><span class="p">(</span>
        <span class="s2">"The KnowledgeGraphIndex class has been deprecated. "</span>
        <span class="s2">"Please use the new PropertyGraphIndex class instead. "</span>
        <span class="s2">"If a certain graph store integration is missing in the new class, "</span>
        <span class="s2">"please open an issue on the GitHub repository or contribute it!"</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="k">class</span> <span class="nc">KnowledgeGraphIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">KG</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Knowledge Graph Index.</span>

<span class="sd">    Build a KG by extracting triplets, and leveraging the KG during query-time.</span>

<span class="sd">    Args:</span>
<span class="sd">        kg_triplet_extract_template (BasePromptTemplate): The prompt to use for</span>
<span class="sd">            extracting triplets.</span>
<span class="sd">        max_triplets_per_chunk (int): The maximum number of triplets to extract.</span>
<span class="sd">        service_context (Optional[ServiceContext]): The service context to use.</span>
<span class="sd">        storage_context (Optional[StorageContext]): The storage context to use.</span>
<span class="sd">        graph_store (Optional[GraphStore]): The graph store to use.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">        include_embeddings (bool): Whether to include embeddings in the index.</span>
<span class="sd">            Defaults to False.</span>
<span class="sd">        max_object_length (int): The maximum length of the object in a triplet.</span>
<span class="sd">            Defaults to 128.</span>
<span class="sd">        kg_triplet_extract_fn (Optional[Callable]): The function to use for</span>
<span class="sd">            extracting triplets. Defaults to None.</span>

<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">KG</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">KG</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">kg_triplet_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_triplets_per_chunk</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">include_embeddings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_object_length</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">128</span><span class="p">,</span>
        <span class="n">kg_triplet_extract_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="c1"># need to set parameters before building index in base class.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">include_embeddings</span> <span class="o">=</span> <span class="n">include_embeddings</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_triplets_per_chunk</span> <span class="o">=</span> <span class="n">max_triplets_per_chunk</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">kg_triplet_extract_template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">kg_triplet_extract_template</span> <span class="ow">or</span> <span class="n">DEFAULT_KG_TRIPLET_EXTRACT_PROMPT</span>
        <span class="p">)</span>
        <span class="c1"># NOTE: Partially format keyword extract template here.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">kg_triplet_extract_template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">kg_triplet_extract_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                <span class="n">max_knowledge_triplets</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_triplets_per_chunk</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_object_length</span> <span class="o">=</span> <span class="n">max_object_length</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kg_triplet_extract_fn</span> <span class="o">=</span> <span class="n">kg_triplet_extract_fn</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># TODO: legacy conversion - remove in next release</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">table</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
            <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="p">,</span> <span class="n">SimpleGraphStore</span><span class="p">)</span>
            <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">graph_dict</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span>
        <span class="p">):</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Upgrading previously saved KG index to new storage format."</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">graph_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">rel_map</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">graph_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphStore</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.knowledge_graph.retrievers</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">KGRetrieverMode</span><span class="p">,</span>
            <span class="n">KGTableRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">embedding_dict</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">retriever_mode</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">retriever_mode</span> <span class="o">=</span> <span class="n">KGRetrieverMode</span><span class="o">.</span><span class="n">HYBRID</span>

        <span class="k">return</span> <span class="n">KGTableRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span>
            <span class="n">retriever_mode</span><span class="o">=</span><span class="n">retriever_mode</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_extract_triplets</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_triplet_extract_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_triplet_extract_fn</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm_extract_triplets</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_llm_extract_triplets</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from text."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">kg_triplet_extract_template</span><span class="p">,</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_triplet_response</span><span class="p">(</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_object_length</span>
        <span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_parse_triplet_response</span><span class="p">(</span>
        <span class="n">response</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">max_length</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">128</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]:</span>
        <span class="n">knowledge_strs</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">knowledge_strs</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"("</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">text</span> <span class="ow">or</span> <span class="s2">")"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">text</span> <span class="ow">or</span> <span class="n">text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">")"</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"("</span><span class="p">):</span>
                <span class="c1"># skip empty lines and non-triplets</span>
                <span class="k">continue</span>
            <span class="n">triplet_part</span> <span class="o">=</span> <span class="n">text</span><span class="p">[</span><span class="n">text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"("</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span> <span class="p">:</span> <span class="n">text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">")"</span><span class="p">)]</span>
            <span class="n">tokens</span> <span class="o">=</span> <span class="n">triplet_part</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">","</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tokens</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">3</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span> <span class="o">&gt;</span> <span class="n">max_length</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">tokens</span><span class="p">):</span>
                <span class="c1"># We count byte-length instead of len() for UTF-8 chars,</span>
                <span class="c1"># will skip if any of the tokens are too long.</span>
                <span class="c1"># This is normally due to a poorly formatted triplet</span>
                <span class="c1"># extraction, in more serious KG building cases</span>
                <span class="c1"># we'll need NLP models to better extract triplets.</span>
                <span class="k">continue</span>

            <span class="n">subj</span><span class="p">,</span> <span class="n">pred</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="o">.</span><span class="n">strip</span><span class="p">,</span> <span class="n">tokens</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">subj</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">pred</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">obj</span><span class="p">:</span>
                <span class="c1"># skip partial triplets</span>
                <span class="k">continue</span>

            <span class="c1"># Strip double quotes and Capitalize triplets for disambiguation</span>
            <span class="n">subj</span><span class="p">,</span> <span class="n">pred</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">entity</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">'"'</span><span class="p">)</span><span class="o">.</span><span class="n">capitalize</span><span class="p">()</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="p">[</span><span class="n">subj</span><span class="p">,</span> <span class="n">pred</span><span class="p">,</span> <span class="n">obj</span><span class="p">]</span>
            <span class="p">)</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">subj</span><span class="p">,</span> <span class="n">pred</span><span class="p">,</span> <span class="n">obj</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">KG</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes."""</span>
        <span class="c1"># do simple concatenation</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_struct_cls</span><span class="p">()</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span> <span class="s2">"Processing nodes"</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">triplets</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_triplets</span><span class="p">(</span>
                <span class="n">n</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Extracted triplets: </span><span class="si">{</span><span class="n">triplets</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">triplet</span> <span class="ow">in</span> <span class="n">triplets</span><span class="p">:</span>
                <span class="n">subj</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">triplet</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
                <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">([</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">],</span> <span class="n">n</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_embeddings</span><span class="p">:</span>
                <span class="n">triplet_texts</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">triplets</span><span class="p">]</span>

                <span class="n">embed_outputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
                    <span class="n">triplet_texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">rel_text</span><span class="p">,</span> <span class="n">rel_embed</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">triplet_texts</span><span class="p">,</span> <span class="n">embed_outputs</span><span class="p">):</span>
                    <span class="n">index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="n">rel_text</span><span class="p">,</span> <span class="n">rel_embed</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">index_struct</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">triplets</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_triplets</span><span class="p">(</span>
                <span class="n">n</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted triplets: </span><span class="si">{</span><span class="n">triplets</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">triplet</span> <span class="ow">in</span> <span class="n">triplets</span><span class="p">:</span>
                <span class="n">subj</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">triplet</span>
                <span class="n">triplet_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">([</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">],</span> <span class="n">n</span><span class="p">)</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">include_embeddings</span>
                    <span class="ow">and</span> <span class="n">triplet_str</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">embedding_dict</span>
                <span class="p">):</span>
                    <span class="n">rel_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">,</span> <span class="n">rel_embedding</span><span class="p">)</span>

        <span class="c1"># Update the storage context's index_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">triplet</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">include_embeddings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert triplets and optionally embeddings.</span>

<span class="sd">        Used for manual insertion of KG triplets (in the form</span>
<span class="sd">        of (subject, relationship, object)).</span>

<span class="sd">        Args:</span>
<span class="sd">            triplet (tuple): Knowledge triplet</span>
<span class="sd">            embedding (Any, optional): Embedding option for the triplet. Defaults to None.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="o">*</span><span class="n">triplet</span><span class="p">)</span>
        <span class="n">triplet_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">include_embeddings</span><span class="p">:</span>
            <span class="n">set_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">),</span> <span class="n">set_embedding</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add node.</span>

<span class="sd">        Used for manual insertion of nodes (keyed by keywords).</span>

<span class="sd">        Args:</span>
<span class="sd">            keywords (List[str]): Keywords to index the node.</span>
<span class="sd">            node (Node): Node to be indexed.</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">keywords</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">([</span><span class="n">node</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">upsert_triplet_and_node</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">triplet</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">,</span>
        <span class="n">include_embeddings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Upsert KG triplet and node.</span>

<span class="sd">        Calls both upsert_triplet and add_node.</span>
<span class="sd">        Behavior is idempotent; if Node already exists,</span>
<span class="sd">        only triplet will be added.</span>

<span class="sd">        Args:</span>
<span class="sd">            keywords (List[str]): Keywords to index the node.</span>
<span class="sd">            node (Node): Node to be indexed.</span>
<span class="sd">            include_embeddings (bool): Option to add embeddings for triplets. Defaults to False</span>

<span class="sd">        """</span>
        <span class="n">subj</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">triplet</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_node</span><span class="p">([</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">],</span> <span class="n">node</span><span class="p">)</span>
        <span class="n">triplet_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">include_embeddings</span><span class="p">:</span>
            <span class="n">set_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">),</span> <span class="n">set_embedding</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a node."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Delete is not supported for KG index yet."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
        <span class="n">node_doc_ids_sets</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="n">node_doc_ids</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">()</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="o">*</span><span class="n">node_doc_ids_sets</span><span class="p">))</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_doc_ids</span><span class="p">)</span>

        <span class="n">all_ref_doc_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">ref_node</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">ref_node</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">ref_doc_info</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">all_ref_doc_info</span><span class="p">[</span><span class="n">ref_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc_info</span>
        <span class="k">return</span> <span class="n">all_ref_doc_info</span>

    <span class="k">def</span> <span class="nf">get_networkx_graph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get networkx representation of the graph structure.</span>

<span class="sd">        Args:</span>
<span class="sd">            limit (int): Number of starting nodes to be included in the graph.</span>

<span class="sd">        NOTE: This function requires networkx to be installed.</span>
<span class="sd">        NOTE: This is a beta feature.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">networkx</span> <span class="k">as</span> <span class="nn">nx</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install networkx to visualize the graph: `pip install networkx`"</span>
            <span class="p">)</span>

        <span class="n">g</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
        <span class="n">subjs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

        <span class="c1"># add edges</span>
        <span class="n">rel_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">get_rel_map</span><span class="p">(</span><span class="n">subjs</span><span class="o">=</span><span class="n">subjs</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">)</span>

        <span class="n">added_nodes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">keyword</span> <span class="ow">in</span> <span class="n">rel_map</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">rel_map</span><span class="p">[</span><span class="n">keyword</span><span class="p">]:</span>
                <span class="n">subj</span> <span class="o">=</span> <span class="n">keyword</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">path</span><span class="p">),</span> <span class="mi">2</span><span class="p">):</span>
                    <span class="k">if</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
                        <span class="k">break</span>

                    <span class="k">if</span> <span class="n">subj</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">added_nodes</span><span class="p">:</span>
                        <span class="n">g</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>
                        <span class="n">added_nodes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>

                    <span class="n">rel</span> <span class="o">=</span> <span class="n">path</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span>
                    <span class="n">obj</span> <span class="o">=</span> <span class="n">path</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">2</span><span class="p">]</span>

                    <span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="n">rel</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">rel</span><span class="p">)</span>
                    <span class="n">subj</span> <span class="o">=</span> <span class="n">obj</span>
        <span class="k">return</span> <span class="n">g</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">query_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">GRAPH_STORE_KEY</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### ref\_doc\_info `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex.ref_doc_info "Permanent link")

```
ref_doc_info: Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Retrieve a dict mapping of ingested documents and their nodes+metadata.

### upsert\_triplet [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex.upsert_triplet "Permanent link")

```
upsert_triplet(triplet: Tuple[str, str, str], include_embeddings: bool = False) -> None
```

Insert triplets and optionally embeddings.

Used for manual insertion of KG triplets (in the form of (subject, relationship, object)).

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `triplet` | `tuple` | 
Knowledge triplet



 | _required_ |
| `embedding` | `Any` | 

Embedding option for the triplet. Defaults to None.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">257</span>
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
<span class="normal">274</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">triplet</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">include_embeddings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert triplets and optionally embeddings.</span>

<span class="sd">    Used for manual insertion of KG triplets (in the form</span>
<span class="sd">    of (subject, relationship, object)).</span>

<span class="sd">    Args:</span>
<span class="sd">        triplet (tuple): Knowledge triplet</span>
<span class="sd">        embedding (Any, optional): Embedding option for the triplet. Defaults to None.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="o">*</span><span class="n">triplet</span><span class="p">)</span>
    <span class="n">triplet_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">include_embeddings</span><span class="p">:</span>
        <span class="n">set_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">),</span> <span class="n">set_embedding</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex.add_node "Permanent link")

```
add_node(keywords: List[str], node: [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")) -> None
```

Add node.

Used for manual insertion of nodes (keyed by keywords).

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `keywords` | `List[str]` | 
Keywords to index the node.



 | _required_ |
| `node` | `Node` | 

Node to be indexed.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">276</span>
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
<span class="normal">287</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add node.</span>

<span class="sd">    Used for manual insertion of nodes (keyed by keywords).</span>

<span class="sd">    Args:</span>
<span class="sd">        keywords (List[str]): Keywords to index the node.</span>
<span class="sd">        node (Node): Node to be indexed.</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">keywords</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">([</span><span class="n">node</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_triplet\_and\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex.upsert_triplet_and_node "Permanent link")

```
upsert_triplet_and_node(triplet: Tuple[str, str, str], node: [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode"), include_embeddings: bool = False) -> None
```

Upsert KG triplet and node.

Calls both upsert\_triplet and add\_node. Behavior is idempotent; if Node already exists, only triplet will be added.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `keywords` | `List[str]` | 
Keywords to index the node.



 | _required_ |
| `node` | `Node` | 

Node to be indexed.



 | _required_ |
| `include_embeddings` | `bool` | 

Option to add embeddings for triplets. Defaults to False



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">289</span>
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
<span class="normal">314</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_triplet_and_node</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">triplet</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">,</span>
    <span class="n">include_embeddings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Upsert KG triplet and node.</span>

<span class="sd">    Calls both upsert_triplet and add_node.</span>
<span class="sd">    Behavior is idempotent; if Node already exists,</span>
<span class="sd">    only triplet will be added.</span>

<span class="sd">    Args:</span>
<span class="sd">        keywords (List[str]): Keywords to index the node.</span>
<span class="sd">        node (Node): Node to be indexed.</span>
<span class="sd">        include_embeddings (bool): Option to add embeddings for triplets. Defaults to False</span>

<span class="sd">    """</span>
    <span class="n">subj</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">triplet</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">upsert_triplet</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">add_node</span><span class="p">([</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">],</span> <span class="n">node</span><span class="p">)</span>
    <span class="n">triplet_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">include_embeddings</span><span class="p">:</span>
        <span class="n">set_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span><span class="n">triplet_str</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_to_embedding_dict</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">triplet</span><span class="p">),</span> <span class="n">set_embedding</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_networkx\_graph [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/#llama_index.core.indices.KnowledgeGraphIndex.get_networkx_graph "Permanent link")

```
get_networkx_graph(limit: int = 100) -> Any
```

Get networkx representation of the graph structure.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `limit` | `int` | 
Number of starting nodes to be included in the graph.



 | `100` |

NOTE: This function requires networkx to be installed. NOTE: This is a beta feature.

Source code in `llama-index-core/llama_index/core/indices/knowledge_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">340</span>
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
<span class="normal">380</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_networkx_graph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get networkx representation of the graph structure.</span>

<span class="sd">    Args:</span>
<span class="sd">        limit (int): Number of starting nodes to be included in the graph.</span>

<span class="sd">    NOTE: This function requires networkx to be installed.</span>
<span class="sd">    NOTE: This is a beta feature.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">networkx</span> <span class="k">as</span> <span class="nn">nx</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install networkx to visualize the graph: `pip install networkx`"</span>
        <span class="p">)</span>

    <span class="n">g</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
    <span class="n">subjs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

    <span class="c1"># add edges</span>
    <span class="n">rel_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_store</span><span class="o">.</span><span class="n">get_rel_map</span><span class="p">(</span><span class="n">subjs</span><span class="o">=</span><span class="n">subjs</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">)</span>

    <span class="n">added_nodes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">keyword</span> <span class="ow">in</span> <span class="n">rel_map</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">rel_map</span><span class="p">[</span><span class="n">keyword</span><span class="p">]:</span>
            <span class="n">subj</span> <span class="o">=</span> <span class="n">keyword</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">path</span><span class="p">),</span> <span class="mi">2</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
                    <span class="k">break</span>

                <span class="k">if</span> <span class="n">subj</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">added_nodes</span><span class="p">:</span>
                    <span class="n">g</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>
                    <span class="n">added_nodes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>

                <span class="n">rel</span> <span class="o">=</span> <span class="n">path</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span>
                <span class="n">obj</span> <span class="o">=</span> <span class="n">path</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">2</span><span class="p">]</span>

                <span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="n">rel</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">rel</span><span class="p">)</span>
                <span class="n">subj</span> <span class="o">=</span> <span class="n">obj</span>
    <span class="k">return</span> <span class="n">g</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Keyword](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/)[Next Llama cloud](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/)
