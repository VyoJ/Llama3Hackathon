Title: Property graph - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/

Markdown Content:
Property graph - LlamaIndex


LlamaIndex data structures.

PropertyGraphIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexLPG]`

An index for a property graph.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `Optional[Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]]` | 
A list of nodes to insert into the index.



 | `None` |
| `llm` | `Optional[BaseLLM]` | 

The language model to use for extracting triplets. Defaults to `Settings.llm`.



 | `None` |
| `kg_extractors` | `Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]]` | 

A list of transformations to apply to the nodes to extract triplets. Defaults to `[SimpleLLMPathExtractor(llm=llm), ImplicitEdgeExtractor()]`.



 | `None` |
| `property_graph_store` | `Optional[PropertyGraphStore]` | 

The property graph store to use. If not provided, a new `SimplePropertyGraphStore` will be created.



 | `None` |
| `vector_store` | `Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")]` | 

The vector store index to use, if the graph store does not support vector queries.



 | `None` |
| `use_async` | `bool` | 

Whether to use async for transformations. Defaults to `True`.



 | `True` |
| `embed_model` | `Optional[EmbedType]` | 

The embedding model to use for embedding nodes. If not provided, `Settings.embed_model` will be used if `embed_kg_nodes=True`.



 | `None` |
| `embed_kg_nodes` | `bool` | 

Whether to embed the KG nodes. Defaults to `True`.



 | `True` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

The callback manager to use.



 | `None` |
| `transformations` | `Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]]` | 

A list of transformations to apply to the nodes before inserting them into the index. These are applied prior to the `kg_extractors`.



 | `None` |
| `storage_context` | `Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")]` | 

The storage context to use.



 | `None` |
| `show_progress` | `bool` | 

Whether to show progress bars for transformations. Defaults to `False`.



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/property_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 43</span>
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
<span class="normal">398</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PropertyGraphIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexLPG</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""An index for a property graph.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (Optional[Sequence[BaseNode]]):</span>
<span class="sd">            A list of nodes to insert into the index.</span>
<span class="sd">        llm (Optional[BaseLLM]):</span>
<span class="sd">            The language model to use for extracting triplets. Defaults to `Settings.llm`.</span>
<span class="sd">        kg_extractors (Optional[List[TransformComponent]]):</span>
<span class="sd">            A list of transformations to apply to the nodes to extract triplets.</span>
<span class="sd">            Defaults to `[SimpleLLMPathExtractor(llm=llm), ImplicitEdgeExtractor()]`.</span>
<span class="sd">        property_graph_store (Optional[PropertyGraphStore]):</span>
<span class="sd">            The property graph store to use. If not provided, a new `SimplePropertyGraphStore` will be created.</span>
<span class="sd">        vector_store (Optional[BasePydanticVectorStore]):</span>
<span class="sd">            The vector store index to use, if the graph store does not support vector queries.</span>
<span class="sd">        use_async (bool):</span>
<span class="sd">            Whether to use async for transformations. Defaults to `True`.</span>
<span class="sd">        embed_model (Optional[EmbedType]):</span>
<span class="sd">            The embedding model to use for embedding nodes.</span>
<span class="sd">            If not provided, `Settings.embed_model` will be used if `embed_kg_nodes=True`.</span>
<span class="sd">        embed_kg_nodes (bool):</span>
<span class="sd">            Whether to embed the KG nodes. Defaults to `True`.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]):</span>
<span class="sd">            The callback manager to use.</span>
<span class="sd">        transformations (Optional[List[TransformComponent]]):</span>
<span class="sd">            A list of transformations to apply to the nodes before inserting them into the index.</span>
<span class="sd">            These are applied prior to the `kg_extractors`.</span>
<span class="sd">        storage_context (Optional[StorageContext]):</span>
<span class="sd">            The storage context to use.</span>
<span class="sd">        show_progress (bool):</span>
<span class="sd">            Whether to show progress bars for transformations. Defaults to `False`.</span>
<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">IndexLPG</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">kg_extractors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PropertyGraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># vector related params</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_kg_nodes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="c1"># parent class params</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">storage_context</span> <span class="o">=</span> <span class="n">storage_context</span> <span class="ow">or</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span>
        <span class="p">)</span>

        <span class="c1"># lazily initialize the graph store on the storage context</span>
        <span class="k">if</span> <span class="n">property_graph_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span> <span class="o">=</span> <span class="n">property_graph_store</span>
        <span class="k">elif</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span> <span class="o">=</span> <span class="n">SimplePropertyGraphStore</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">storage_context</span><span class="o">.</span><span class="n">vector_stores</span><span class="p">[</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">]</span> <span class="o">=</span> <span class="n">vector_store</span>

        <span class="k">if</span> <span class="n">embed_kg_nodes</span> <span class="ow">and</span> <span class="p">(</span>
            <span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">supports_vector_queries</span>
            <span class="ow">or</span> <span class="n">embed_kg_nodes</span>
        <span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">resolve_embed_model</span><span class="p">(</span><span class="n">embed_model</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">embed_model</span>
                <span class="k">else</span> <span class="n">Settings</span><span class="o">.</span><span class="n">embed_model</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_kg_extractors</span> <span class="o">=</span> <span class="n">kg_extractors</span> <span class="ow">or</span> <span class="p">[</span>
            <span class="n">SimpleLLMPathExtractor</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span><span class="p">),</span>
            <span class="n">ImplicitPathExtractor</span><span class="p">(),</span>
        <span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span> <span class="o">=</span> <span class="n">use_async</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_kg_nodes</span> <span class="o">=</span> <span class="n">embed_kg_nodes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_override_vector_store</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="ow">not</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">supports_vector_queries</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_existing</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="s2">"PropertyGraphIndex"</span><span class="p">,</span>
        <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">PropertyGraphStore</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># general params</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">kg_extractors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># vector related params</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_kg_nodes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="c1"># parent class params</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PropertyGraphIndex"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create an index from an existing property graph store (and optional vector store)."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="p">[],</span>  <span class="c1"># no nodes to insert</span>
            <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="n">vector_store</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">kg_extractors</span><span class="o">=</span><span class="n">kg_extractors</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">embed_kg_nodes</span><span class="o">=</span><span class="n">embed_kg_nodes</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">property_graph_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PropertyGraphStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the labelled property graph store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">storage_context</span><span class="o">.</span><span class="n">property_graph_store</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">vector_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_kg_nodes</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_vector_store</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">storage_context</span><span class="o">.</span><span class="n">vector_store</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_insert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Insert nodes to the index struct."""</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">nodes</span>

        <span class="c1"># run transformations on nodes to extract triplets</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="n">arun_transformations</span><span class="p">(</span>
                    <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_extractors</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kg_extractors</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
            <span class="p">)</span>

        <span class="c1"># ensure all nodes have nodes and/or relations in metadata</span>
        <span class="k">assert</span> <span class="nb">all</span><span class="p">(</span>
            <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">KG_NODES_KEY</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="ow">or</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">KG_RELATIONS_KEY</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
        <span class="p">)</span>

        <span class="n">kg_nodes_to_insert</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">kg_rels_to_insert</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Relation</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="c1"># remove nodes and relations from metadata</span>
            <span class="n">kg_nodes</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">KG_NODES_KEY</span><span class="p">,</span> <span class="p">[])</span>
            <span class="n">kg_rels</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">KG_RELATIONS_KEY</span><span class="p">,</span> <span class="p">[])</span>

            <span class="c1"># add source id to properties</span>
            <span class="k">for</span> <span class="n">kg_node</span> <span class="ow">in</span> <span class="n">kg_nodes</span><span class="p">:</span>
                <span class="n">kg_node</span><span class="o">.</span><span class="n">properties</span><span class="p">[</span><span class="n">TRIPLET_SOURCE_KEY</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">id_</span>
            <span class="k">for</span> <span class="n">kg_rel</span> <span class="ow">in</span> <span class="n">kg_rels</span><span class="p">:</span>
                <span class="n">kg_rel</span><span class="o">.</span><span class="n">properties</span><span class="p">[</span><span class="n">TRIPLET_SOURCE_KEY</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">id_</span>

            <span class="c1"># add nodes and relations to insert lists</span>
            <span class="n">kg_nodes_to_insert</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">kg_nodes</span><span class="p">)</span>
            <span class="n">kg_rels_to_insert</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">kg_rels</span><span class="p">)</span>

        <span class="c1"># filter out duplicate kg nodes</span>
        <span class="n">kg_node_ids</span> <span class="o">=</span> <span class="p">{</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">kg_nodes_to_insert</span><span class="p">}</span>
        <span class="n">existing_kg_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">kg_node_ids</span><span class="p">))</span>
        <span class="n">existing_kg_node_ids</span> <span class="o">=</span> <span class="p">{</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">existing_kg_nodes</span><span class="p">}</span>
        <span class="n">kg_nodes_to_insert</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">kg_nodes_to_insert</span> <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">existing_kg_node_ids</span>
        <span class="p">]</span>

        <span class="c1"># filter out duplicate llama nodes</span>
        <span class="n">existing_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">get_llama_nodes</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">existing_node_hashes</span> <span class="o">=</span> <span class="p">{</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">existing_nodes</span><span class="p">}</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span> <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">existing_node_hashes</span><span class="p">]</span>

        <span class="c1"># embed nodes (if needed)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_kg_nodes</span><span class="p">:</span>
            <span class="c1"># embed llama-index nodes</span>
            <span class="n">node_texts</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
            <span class="p">]</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">:</span>
                <span class="n">embeddings</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">aget_text_embedding_batch</span><span class="p">(</span>
                        <span class="n">node_texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
                    <span class="n">node_texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
                <span class="p">)</span>

            <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">embeddings</span><span class="p">):</span>
                <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>

            <span class="c1"># embed kg nodes</span>
            <span class="n">kg_node_texts</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">kg_node</span><span class="p">)</span> <span class="k">for</span> <span class="n">kg_node</span> <span class="ow">in</span> <span class="n">kg_nodes_to_insert</span><span class="p">]</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">:</span>
                <span class="n">kg_embeddings</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">aget_text_embedding_batch</span><span class="p">(</span>
                        <span class="n">kg_node_texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">kg_embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
                    <span class="n">kg_node_texts</span><span class="p">,</span>
                    <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="k">for</span> <span class="n">kg_node</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">kg_nodes_to_insert</span><span class="p">,</span> <span class="n">kg_embeddings</span><span class="p">):</span>
                <span class="n">kg_node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>

        <span class="c1"># if graph store doesn't support vectors, or the vector index was provided, use it</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">kg_nodes_to_insert</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_insert_nodes_to_vector_index</span><span class="p">(</span><span class="n">kg_nodes_to_insert</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">upsert_llama_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">kg_nodes_to_insert</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">upsert_nodes</span><span class="p">(</span><span class="n">kg_nodes_to_insert</span><span class="p">)</span>

        <span class="c1"># important: upsert relations after nodes</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">kg_rels_to_insert</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">upsert_relations</span><span class="p">(</span><span class="n">kg_rels_to_insert</span><span class="p">)</span>

        <span class="c1"># refresh schema if needed</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">supports_structured_queries</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">get_schema</span><span class="p">(</span><span class="n">refresh</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">_insert_nodes_to_vector_index</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert vector nodes."""</span>
        <span class="n">llama_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">llama_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">TextNode</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">node</span><span class="p">),</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="n">VECTOR_SOURCE_KEY</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="o">**</span><span class="n">node</span><span class="o">.</span><span class="n">properties</span><span class="p">},</span>
                        <span class="n">embedding</span><span class="o">=</span><span class="p">[</span><span class="o">*</span><span class="n">node</span><span class="o">.</span><span class="n">embedding</span><span class="p">],</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">stores_text</span><span class="p">:</span>
                    <span class="n">llama_nodes</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">id</span>

            <span class="c1"># clear the embedding to save memory, its not used now</span>
            <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">llama_nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">IndexLPG</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build index from nodes."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_insert_nodes</span><span class="p">(</span><span class="n">nodes</span> <span class="ow">or</span> <span class="p">[])</span>

        <span class="c1"># this isn't really used or needed</span>
        <span class="k">return</span> <span class="n">IndexLPG</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sub_retrievers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="s2">"BasePGRetriever"</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a retriever for the index.</span>

<span class="sd">        Args:</span>
<span class="sd">            sub_retrievers (Optional[List[BasePGRetriever]]):</span>
<span class="sd">                A list of sub-retrievers to use. If not provided, a default list will be used:</span>
<span class="sd">                `[LLMSynonymRetriever, VectorContextRetriever]` if the graph store supports vector queries.</span>
<span class="sd">            include_text (bool):</span>
<span class="sd">                Whether to include source-text in the retriever results.</span>
<span class="sd">            **kwargs:</span>
<span class="sd">                Additional kwargs to pass to the retriever.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">PGRetriever</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.sub_retrievers.vector</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">VectorContextRetriever</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.sub_retrievers.llm_synonym</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">LLMSynonymRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">sub_retrievers</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">sub_retrievers</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">LLMSynonymRetriever</span><span class="p">(</span>
                    <span class="n">graph_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span>
                    <span class="n">include_text</span><span class="o">=</span><span class="n">include_text</span><span class="p">,</span>
                    <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">]</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="ow">and</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">supports_vector_queries</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span>
            <span class="p">):</span>
                <span class="n">sub_retrievers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">VectorContextRetriever</span><span class="p">(</span>
                        <span class="n">graph_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span>
                        <span class="n">vector_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="p">,</span>
                        <span class="n">include_text</span><span class="o">=</span><span class="n">include_text</span><span class="p">,</span>
                        <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span>
                        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">PGRetriever</span><span class="p">(</span><span class="n">sub_retrievers</span><span class="p">,</span> <span class="n">use_async</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a node."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">node_id</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Index-specific logic for inserting nodes to the index struct."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Ref doc info not implemented for PropertyGraphIndex. "</span>
            <span class="s2">"All inserts are already upserts."</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### property\_graph\_store `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex.property_graph_store "Permanent link")

```
property_graph_store: PropertyGraphStore
```

Get the labelled property graph store.

### from\_existing `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex.from_existing "Permanent link")

```
from_existing(property_graph_store: PropertyGraphStore, vector_store: Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")] = None, llm: Optional[BaseLLM] = None, kg_extractors: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, use_async: bool = True, embed_model: Optional[EmbedType] = None, embed_kg_nodes: bool = True, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, transformations: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, storage_context: Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")] = None, show_progress: bool = False, **kwargs: Any) -> [PropertyGraphIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex "llama_index.core.indices.property_graph.base.PropertyGraphIndex")
```

Create an index from an existing property graph store (and optional vector store).

Source code in `llama-index-core/llama_index/core/indices/property_graph/base.py`

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
<span class="normal">177</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_existing</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="s2">"PropertyGraphIndex"</span><span class="p">,</span>
    <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">PropertyGraphStore</span><span class="p">,</span>
    <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># general params</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">kg_extractors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># vector related params</span>
    <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">embed_kg_nodes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="c1"># parent class params</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PropertyGraphIndex"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create an index from an existing property graph store (and optional vector store)."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="p">[],</span>  <span class="c1"># no nodes to insert</span>
        <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="o">=</span><span class="n">vector_store</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">kg_extractors</span><span class="o">=</span><span class="n">kg_extractors</span><span class="p">,</span>
        <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="n">embed_kg_nodes</span><span class="o">=</span><span class="n">embed_kg_nodes</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex.as_retriever "Permanent link")

```
as_retriever(sub_retrievers: Optional[List[BasePGRetriever]] = None, include_text: bool = True, **kwargs: Any) -> [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Return a retriever for the index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sub_retrievers` | `Optional[List[BasePGRetriever]]` | 
A list of sub-retrievers to use. If not provided, a default list will be used: `[LLMSynonymRetriever, VectorContextRetriever]` if the graph store supports vector queries.



 | `None` |
| `include_text` | `bool` | 

Whether to include source-text in the retriever results.



 | `True` |
| `**kwargs` | `Any` | 

Additional kwargs to pass to the retriever.



 | `{}` |

Source code in `llama-index-core/llama_index/core/indices/property_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">333</span>
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
<span class="normal">383</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">sub_retrievers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="s2">"BasePGRetriever"</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a retriever for the index.</span>

<span class="sd">    Args:</span>
<span class="sd">        sub_retrievers (Optional[List[BasePGRetriever]]):</span>
<span class="sd">            A list of sub-retrievers to use. If not provided, a default list will be used:</span>
<span class="sd">            `[LLMSynonymRetriever, VectorContextRetriever]` if the graph store supports vector queries.</span>
<span class="sd">        include_text (bool):</span>
<span class="sd">            Whether to include source-text in the retriever results.</span>
<span class="sd">        **kwargs:</span>
<span class="sd">            Additional kwargs to pass to the retriever.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.retriever</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">PGRetriever</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.sub_retrievers.vector</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">VectorContextRetriever</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.indices.property_graph.sub_retrievers.llm_synonym</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">LLMSynonymRetriever</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="n">sub_retrievers</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">sub_retrievers</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">LLMSynonymRetriever</span><span class="p">(</span>
                <span class="n">graph_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span>
                <span class="n">include_text</span><span class="o">=</span><span class="n">include_text</span><span class="p">,</span>
                <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="ow">and</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">supports_vector_queries</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span>
        <span class="p">):</span>
            <span class="n">sub_retrievers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">VectorContextRetriever</span><span class="p">(</span>
                    <span class="n">graph_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span>
                    <span class="n">vector_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="p">,</span>
                    <span class="n">include_text</span><span class="o">=</span><span class="n">include_text</span><span class="p">,</span>
                    <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="n">PGRetriever</span><span class="p">(</span><span class="n">sub_retrievers</span><span class="p">,</span> <span class="n">use_async</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### ref\_doc\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/#llama_index.core.indices.PropertyGraphIndex.ref_doc_info "Permanent link")

```
ref_doc_info() -> Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Retrieve a dict mapping of ingested documents and their nodes+metadata.

Source code in `llama-index-core/llama_index/core/indices/property_graph/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
        <span class="s2">"Ref doc info not implemented for PropertyGraphIndex. "</span>
        <span class="s2">"All inserts are already upserts."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Postgresml](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/)[Next Summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/)
