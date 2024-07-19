Title: Vector - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/

Markdown Content:
Vector - LlamaIndex


LlamaIndex data structures.

VectorStoreIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexDict]`

Vector Store Index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `use_async` | `bool` | 
Whether to use asynchronous calls. Defaults to False.



 | `False` |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `store_nodes_override` | `bool` | 

set to True to always store Node objects in index store and document store even if vector store keeps text. Defaults to False



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/vector_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorStoreIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexDict</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Vector Store Index.</span>

<span class="sd">    Args:</span>
<span class="sd">        use_async (bool): Whether to use asynchronous calls. Defaults to False.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">        store_nodes_override (bool): set to True to always store Node objects in index</span>
<span class="sd">            store and document store even if vector store keeps text. Defaults to False</span>
<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">IndexDict</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># vector store index params</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">store_nodes_override</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2048</span><span class="p">,</span>
        <span class="c1"># parent class params</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexDict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span> <span class="o">=</span> <span class="n">use_async</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span> <span class="o">=</span> <span class="n">store_nodes_override</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">resolve_embed_model</span><span class="p">(</span><span class="n">embed_model</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">embed_model</span>
            <span class="k">else</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_batch_size</span> <span class="o">=</span> <span class="n">insert_batch_size</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_vector_store</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">BasePydanticVectorStore</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"VectorStoreIndex"</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">vector_store</span><span class="o">.</span><span class="n">stores_text</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot initialize from a vector store that does not store text."</span>
            <span class="p">)</span>

        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"storage_context"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">vector_store</span><span class="o">=</span><span class="n">vector_store</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">vector_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePydanticVectorStore</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="c1"># NOTE: lazy import</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.vector_store.retrievers</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">VectorIndexRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="p">,</span>
            <span class="n">node_ids</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">nodes_dict</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_node_with_embedding</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tuples of id, node, and embedding.</span>

<span class="sd">        Allows us to store these nodes in a vector store.</span>
<span class="sd">        Embeddings are called in batches.</span>

<span class="sd">        """</span>
        <span class="n">id_to_embed_map</span> <span class="o">=</span> <span class="n">embed_nodes</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span>
        <span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">id_to_embed_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">result</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_node_with_embedding</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Asynchronously get tuples of id, node, and embedding.</span>

<span class="sd">        Allows us to store these nodes in a vector store.</span>
<span class="sd">        Embeddings are called in batches.</span>

<span class="sd">        """</span>
        <span class="n">id_to_embed_map</span> <span class="o">=</span> <span class="k">await</span> <span class="n">async_embed_nodes</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">id_to_embed_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">result</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_add_nodes_to_index</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">IndexDict</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronously add nodes to index."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">return</span>

        <span class="k">for</span> <span class="n">nodes_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_insert_batch_size</span><span class="p">):</span>
            <span class="n">nodes_batch</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_node_with_embedding</span><span class="p">(</span>
                <span class="n">nodes_batch</span><span class="p">,</span> <span class="n">show_progress</span>
            <span class="p">)</span>
            <span class="n">new_ids</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">async_add</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>

            <span class="c1"># if the vector store doesn't store text, we need to add the nodes to the</span>
            <span class="c1"># index struct and document store</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">new_id</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="n">new_ids</span><span class="p">):</span>
                    <span class="c1"># NOTE: remove embedding from node to avoid duplication</span>
                    <span class="n">node_without_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                    <span class="n">node_without_embedding</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>

                    <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">node_without_embedding</span><span class="p">,</span> <span class="n">text_id</span><span class="o">=</span><span class="n">new_id</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span>
                        <span class="p">[</span><span class="n">node_without_embedding</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># NOTE: if the vector store keeps text,</span>
                <span class="c1"># we only need to add image and index nodes</span>
                <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">new_id</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="n">new_ids</span><span class="p">):</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="p">(</span><span class="n">ImageNode</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">)):</span>
                        <span class="c1"># NOTE: remove embedding from node to avoid duplication</span>
                        <span class="n">node_without_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                        <span class="n">node_without_embedding</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>

                        <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">node_without_embedding</span><span class="p">,</span> <span class="n">text_id</span><span class="o">=</span><span class="n">new_id</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span>
                            <span class="p">[</span><span class="n">node_without_embedding</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span>
                        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_add_nodes_to_index</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">IndexDict</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add document to index."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">return</span>

        <span class="k">for</span> <span class="n">nodes_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_insert_batch_size</span><span class="p">):</span>
            <span class="n">nodes_batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_node_with_embedding</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">)</span>
            <span class="n">new_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span><span class="p">:</span>
                <span class="c1"># NOTE: if the vector store doesn't store text,</span>
                <span class="c1"># we need to add the nodes to the index struct and document store</span>
                <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">new_id</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="n">new_ids</span><span class="p">):</span>
                    <span class="c1"># NOTE: remove embedding from node to avoid duplication</span>
                    <span class="n">node_without_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                    <span class="n">node_without_embedding</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>

                    <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">node_without_embedding</span><span class="p">,</span> <span class="n">text_id</span><span class="o">=</span><span class="n">new_id</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span>
                        <span class="p">[</span><span class="n">node_without_embedding</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># NOTE: if the vector store keeps text,</span>
                <span class="c1"># we only need to add image and index nodes</span>
                <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">new_id</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">,</span> <span class="n">new_ids</span><span class="p">):</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="p">(</span><span class="n">ImageNode</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">)):</span>
                        <span class="c1"># NOTE: remove embedding from node to avoid duplication</span>
                        <span class="n">node_without_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                        <span class="n">node_without_embedding</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>

                        <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">node_without_embedding</span><span class="p">,</span> <span class="n">text_id</span><span class="o">=</span><span class="n">new_id</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span>
                            <span class="p">[</span><span class="n">node_without_embedding</span><span class="p">],</span> <span class="n">allow_update</span><span class="o">=</span><span class="kc">True</span>
                        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexDict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build index from nodes."""</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_struct_cls</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">:</span>
            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_async_add_nodes_to_index</span><span class="p">(</span>
                    <span class="n">index_struct</span><span class="p">,</span>
                    <span class="n">nodes</span><span class="p">,</span>
                    <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">]</span>
            <span class="n">run_async_tasks</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_add_nodes_to_index</span><span class="p">(</span>
                <span class="n">index_struct</span><span class="p">,</span>
                <span class="n">nodes</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
                <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">index_struct</span>

    <span class="k">def</span> <span class="nf">build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexDict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes.</span>

<span class="sd">        NOTE: Overrides BaseIndex.build_index_from_nodes.</span>
<span class="sd">            VectorStoreIndex only stores nodes in document store</span>
<span class="sd">            if vector store does not store text</span>
<span class="sd">        """</span>
        <span class="c1"># raise an error if even one node has no content</span>
        <span class="k">if</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span> <span class="o"></span> <span class="s2">""</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Cannot build index from nodes with no content. "</span>
            <span class="s2">"Please ensure all nodes have content."</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_index_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex.insert_nodes "Permanent link")

```
insert_nodes(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **insert_kwargs: Any) -> None
```

Insert nodes.

overrides BaseIndex.insert\_nodes.VectorStoreIndex only stores nodes in document store if vector store does not store text

Source code in `llama-index-core/llama_index/core/indices/vector_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">314</span>
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
<span class="normal">331</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">insert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert nodes.</span>

<span class="sd">    NOTE: overrides BaseIndex.insert_nodes.</span>
<span class="sd">        VectorStoreIndex only stores nodes in document store</span>
<span class="sd">        if vector store does not store text</span>
<span class="sd">    """</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">obj</span>
                <span class="n">node</span><span class="o">.</span><span class="n">obj</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"insert_nodes"</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex.delete_nodes "Permanent link")

```
delete_nodes(node_ids: List[str], delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a list of nodes from the index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_ids` | `List[str]` | 
A list of node\_ids from the nodes to delete



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/vector_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">336</span>
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
<span class="normal">356</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a list of nodes from the index.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_ids (List[str]): A list of node_ids from the nodes to delete</span>

<span class="sd">    """</span>
    <span class="c1"># delete nodes from vector store</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>

    <span class="c1"># delete from docstore only if needed</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span>
    <span class="p">)</span> <span class="ow">and</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a document and it's nodes by using ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/indices/vector_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">358</span>
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
<span class="normal">378</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document and it's nodes by using ref_doc_id."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>

    <span class="c1"># delete from index_struct only if needed</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span><span class="p">:</span>
        <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">ref_doc_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">ref_doc_info</span><span class="o">.</span><span class="n">node_ids</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>

    <span class="c1"># delete from docstore only if needed</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store_nodes_override</span>
    <span class="p">)</span> <span class="ow">and</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vectara](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/)[Next Vertexai](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/)
