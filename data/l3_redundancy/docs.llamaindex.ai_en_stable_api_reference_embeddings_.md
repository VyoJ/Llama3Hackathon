Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/embeddings/

Markdown Content:
Index - LlamaIndex


BaseEmbedding [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")`, `DispatcherSpanMixin`

Base class for embeddings.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 63</span>
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
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseEmbedding</span><span class="p">(</span><span class="n">TransformComponent</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base class for embeddings."""</span>

    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"unknown"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The name of the embedding model."</span>
    <span class="p">)</span>
    <span class="n">embed_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_EMBED_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The batch size for embedding calls."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">lte</span><span class="o">=</span><span class="mi">2048</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">([]),</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>
    <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of workers to use for async embedding calls."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"callback_manager"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_validate_callback_manager</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CallbackManager</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_get_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input query synchronously.</span>

<span class="sd">        Subclasses should implement this method. Reference get_query_embedding's</span>
<span class="sd">        docstring for more information.</span>
<span class="sd">        """</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input query asynchronously.</span>

<span class="sd">        Subclasses should implement this method. Reference get_query_embedding's</span>
<span class="sd">        docstring for more information.</span>
<span class="sd">        """</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">get_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input query.</span>

<span class="sd">        When embedding a query, depending on the model, a special instruction</span>
<span class="sd">        can be prepended to the raw query string. For example, "Represent the</span>
<span class="sd">        question for retrieving supporting documents: ". If you're curious,</span>
<span class="sd">        other examples of predefined instructions can be found in</span>
<span class="sd">        embeddings/huggingface_utils.py.</span>
<span class="sd">        """</span>
        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">query</span><span class="p">],</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">query_embedding</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get query embedding."""</span>
        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">query</span><span class="p">],</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">query_embedding</span>

    <span class="k">def</span> <span class="nf">get_agg_embedding_from_queries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">agg_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get aggregated embedding from multiple queries."""</span>
        <span class="n">query_embeddings</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">get_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
        <span class="n">agg_fn</span> <span class="o">=</span> <span class="n">agg_fn</span> <span class="ow">or</span> <span class="n">mean_agg</span>
        <span class="k">return</span> <span class="n">agg_fn</span><span class="p">(</span><span class="n">query_embeddings</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_agg_embedding_from_queries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">agg_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async get aggregated embedding from multiple queries."""</span>
        <span class="n">query_embeddings</span> <span class="o">=</span> <span class="p">[</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
        <span class="n">agg_fn</span> <span class="o">=</span> <span class="n">agg_fn</span> <span class="ow">or</span> <span class="n">mean_agg</span>
        <span class="k">return</span> <span class="n">agg_fn</span><span class="p">(</span><span class="n">query_embeddings</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_get_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input text synchronously.</span>

<span class="sd">        Subclasses should implement this method. Reference get_text_embedding's</span>
<span class="sd">        docstring for more information.</span>
<span class="sd">        """</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input text asynchronously.</span>

<span class="sd">        Subclasses can implement this method if there is a true async</span>
<span class="sd">        implementation. Reference get_text_embedding's docstring for more</span>
<span class="sd">        information.</span>
<span class="sd">        """</span>
        <span class="c1"># Default implementation just falls back on _get_text_embedding</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_text_embeddings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input sequence of text synchronously.</span>

<span class="sd">        Subclasses can implement this method if batch queries are supported.</span>
<span class="sd">        """</span>
        <span class="c1"># Default implementation just loops over _get_text_embedding</span>
        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">texts</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_text_embeddings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input sequence of text asynchronously.</span>

<span class="sd">        Subclasses can implement this method if batch queries are supported.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="o">*</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">texts</span><span class="p">]</span>
        <span class="p">)</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">get_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Embed the input text.</span>

<span class="sd">        When embedding text, depending on the model, a special instruction</span>
<span class="sd">        can be prepended to the raw text string. For example, "Represent the</span>
<span class="sd">        document for retrieval: ". If you're curious, other examples of</span>
<span class="sd">        predefined instructions can be found in embeddings/huggingface_utils.py.</span>
<span class="sd">        """</span>
        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">text_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">],</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
                <span class="p">}</span>
            <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text</span><span class="p">],</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">text_embedding</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async get text embedding."""</span>
        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">text_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">],</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
                <span class="p">}</span>
            <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text</span><span class="p">],</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">text_embedding</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">get_text_embedding_batch</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a list of text embeddings, with batching."""</span>
        <span class="n">cur_batch</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">result_embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">queue_with_progress</span> <span class="o">=</span> <span class="nb">enumerate</span><span class="p">(</span>
            <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Generating embeddings"</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">queue_with_progress</span><span class="p">:</span>
            <span class="n">cur_batch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">idx</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_batch_size</span><span class="p">:</span>
                <span class="c1"># flush</span>
                <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                        <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()},</span>
                <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                    <span class="n">embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embeddings</span><span class="p">(</span><span class="n">cur_batch</span><span class="p">)</span>
                    <span class="n">result_embeddings</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">embeddings</span><span class="p">)</span>
                    <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                        <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                            <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">cur_batch</span><span class="p">,</span>
                            <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="n">embeddings</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">)</span>
                <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                        <span class="n">chunks</span><span class="o">=</span><span class="n">cur_batch</span><span class="p">,</span>
                        <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="n">cur_batch</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="n">result_embeddings</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_text_embedding_batch</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Asynchronously get a list of text embeddings, with batching."""</span>
        <span class="n">num_workers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>

        <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="n">cur_batch</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">callback_payloads</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">result_embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">embeddings_coroutines</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Coroutine</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">texts</span><span class="p">):</span>
            <span class="n">cur_batch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">idx</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_batch_size</span><span class="p">:</span>
                <span class="c1"># flush</span>
                <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                        <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="n">event_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">on_event_start</span><span class="p">(</span>
                    <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()},</span>
                <span class="p">)</span>
                <span class="n">callback_payloads</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">event_id</span><span class="p">,</span> <span class="n">cur_batch</span><span class="p">))</span>
                <span class="n">embeddings_coroutines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_text_embeddings</span><span class="p">(</span><span class="n">cur_batch</span><span class="p">))</span>
                <span class="n">cur_batch</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># flatten the results of asyncio.gather, which is a list of embeddings lists</span>
        <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                <span class="n">embeddings_coroutines</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
                <span class="n">desc</span><span class="o">=</span><span class="s2">"Generating embeddings"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="kn">from</span> <span class="nn">tqdm.asyncio</span> <span class="kn">import</span> <span class="n">tqdm_asyncio</span>

                    <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">tqdm_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
                        <span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">,</span>
                        <span class="n">total</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">embeddings_coroutines</span><span class="p">),</span>
                        <span class="n">desc</span><span class="o">=</span><span class="s2">"Generating embeddings"</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                    <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">)</span>

        <span class="n">result_embeddings</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">embedding</span> <span class="k">for</span> <span class="n">embeddings</span> <span class="ow">in</span> <span class="n">nested_embeddings</span> <span class="k">for</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="n">embeddings</span>
        <span class="p">]</span>

        <span class="k">for</span> <span class="p">(</span><span class="n">event_id</span><span class="p">,</span> <span class="n">text_batch</span><span class="p">),</span> <span class="n">embeddings</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">callback_payloads</span><span class="p">,</span> <span class="n">nested_embeddings</span>
        <span class="p">):</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                    <span class="n">chunks</span><span class="o">=</span><span class="n">text_batch</span><span class="p">,</span>
                    <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">on_event_end</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">text_batch</span><span class="p">,</span>
                    <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="n">embeddings</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">result_embeddings</span>

    <span class="k">def</span> <span class="nf">similarity</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding1</span><span class="p">:</span> <span class="n">Embedding</span><span class="p">,</span>
        <span class="n">embedding2</span><span class="p">:</span> <span class="n">Embedding</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">SimilarityMode</span> <span class="o">=</span> <span class="n">SimilarityMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get embedding similarity."""</span>
        <span class="k">return</span> <span class="n">similarity</span><span class="p">(</span><span class="n">embedding1</span><span class="o">=</span><span class="n">embedding1</span><span class="p">,</span> <span class="n">embedding2</span><span class="o">=</span><span class="n">embedding2</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">],</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">embeddings</span><span class="p">):</span>
            <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_text_embedding_batch</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">],</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">embeddings</span><span class="p">):</span>
            <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">embedding</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### get\_query\_embedding [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.get_query_embedding "Permanent link")

```
get_query_embedding(query: str) -> Embedding
```

Embed the input query.

When embedding a query, depending on the model, a special instruction can be prepended to the raw query string. For example, "Represent the question for retrieving supporting documents: ". If you're curious, other examples of predefined instructions can be found in embeddings/huggingface\_utils.py.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
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
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">get_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Embed the input query.</span>

<span class="sd">    When embedding a query, depending on the model, a special instruction</span>
<span class="sd">    can be prepended to the raw query string. For example, "Represent the</span>
<span class="sd">    question for retrieving supporting documents: ". If you're curious,</span>
<span class="sd">    other examples of predefined instructions can be found in</span>
<span class="sd">    embeddings/huggingface_utils.py.</span>
<span class="sd">    """</span>
    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
            <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">query</span><span class="p">],</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
            <span class="p">},</span>
        <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
            <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">query_embedding</span>
</code></pre></div></td></tr></tbody></table>

### aget\_query\_embedding `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.aget_query_embedding "Permanent link")

```
aget_query_embedding(query: str) -> Embedding
```

Get query embedding.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">149</span>
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
<span class="normal">176</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get query embedding."""</span>
    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
            <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">query</span><span class="p">],</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
            <span class="p">},</span>
        <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
            <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">query_embedding</span><span class="p">],</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">query_embedding</span>
</code></pre></div></td></tr></tbody></table>

### get\_agg\_embedding\_from\_queries [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.get_agg_embedding_from_queries "Permanent link")

```
get_agg_embedding_from_queries(queries: List[str], agg_fn: Optional[Callable[..., Embedding]] = None) -> Embedding
```

Get aggregated embedding from multiple queries.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_agg_embedding_from_queries</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">agg_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get aggregated embedding from multiple queries."""</span>
    <span class="n">query_embeddings</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">get_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
    <span class="n">agg_fn</span> <span class="o">=</span> <span class="n">agg_fn</span> <span class="ow">or</span> <span class="n">mean_agg</span>
    <span class="k">return</span> <span class="n">agg_fn</span><span class="p">(</span><span class="n">query_embeddings</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget\_agg\_embedding\_from\_queries `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.aget_agg_embedding_from_queries "Permanent link")

```
aget_agg_embedding_from_queries(queries: List[str], agg_fn: Optional[Callable[..., Embedding]] = None) -> Embedding
```

Async get aggregated embedding from multiple queries.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_agg_embedding_from_queries</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">agg_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async get aggregated embedding from multiple queries."""</span>
    <span class="n">query_embeddings</span> <span class="o">=</span> <span class="p">[</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
    <span class="n">agg_fn</span> <span class="o">=</span> <span class="n">agg_fn</span> <span class="ow">or</span> <span class="n">mean_agg</span>
    <span class="k">return</span> <span class="n">agg_fn</span><span class="p">(</span><span class="n">query_embeddings</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_text\_embedding [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.get_text_embedding "Permanent link")

```
get_text_embedding(text: str) -> Embedding
```

Embed the input text.

When embedding text, depending on the model, a special instruction can be prepended to the raw text string. For example, "Represent the document for retrieval: ". If you're curious, other examples of predefined instructions can be found in embeddings/huggingface\_utils.py.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
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
<span class="normal">271</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">get_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Embed the input text.</span>

<span class="sd">    When embedding text, depending on the model, a special instruction</span>
<span class="sd">    can be prepended to the raw text string. For example, "Represent the</span>
<span class="sd">    document for retrieval: ". If you're curious, other examples of</span>
<span class="sd">    predefined instructions can be found in embeddings/huggingface_utils.py.</span>
<span class="sd">    """</span>
    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
            <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">text_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">],</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
            <span class="p">}</span>
        <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
            <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text</span><span class="p">],</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">text_embedding</span>
</code></pre></div></td></tr></tbody></table>

### aget\_text\_embedding `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.aget_text_embedding "Permanent link")

```
aget_text_embedding(text: str) -> Embedding
```

Async get text embedding.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">273</span>
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
<span class="normal">300</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async get text embedding."""</span>
    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
            <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">text_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">],</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
            <span class="p">}</span>
        <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
            <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">text</span><span class="p">],</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="p">[</span><span class="n">text_embedding</span><span class="p">],</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">text_embedding</span>
</code></pre></div></td></tr></tbody></table>

### get\_text\_embedding\_batch [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.get_text_embedding_batch "Permanent link")

```
get_text_embedding_batch(texts: List[str], show_progress: bool = False, **kwargs: Any) -> List[Embedding]
```

Get a list of text embeddings, with batching.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">302</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">get_text_embedding_batch</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a list of text embeddings, with batching."""</span>
    <span class="n">cur_batch</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">result_embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">queue_with_progress</span> <span class="o">=</span> <span class="nb">enumerate</span><span class="p">(</span>
        <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">texts</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Generating embeddings"</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">queue_with_progress</span><span class="p">:</span>
        <span class="n">cur_batch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_batch_size</span><span class="p">:</span>
            <span class="c1"># flush</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                    <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                <span class="n">embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text_embeddings</span><span class="p">(</span><span class="n">cur_batch</span><span class="p">)</span>
                <span class="n">result_embeddings</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">embeddings</span><span class="p">)</span>
                <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">cur_batch</span><span class="p">,</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="n">embeddings</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                    <span class="n">chunks</span><span class="o">=</span><span class="n">cur_batch</span><span class="p">,</span>
                    <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="n">cur_batch</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="n">result_embeddings</span>
</code></pre></div></td></tr></tbody></table>

### aget\_text\_embedding\_batch `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.aget_text_embedding_batch "Permanent link")

```
aget_text_embedding_batch(texts: List[str], show_progress: bool = False) -> List[Embedding]
```

Asynchronously get a list of text embeddings, with batching.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">350</span>
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
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_text_embedding_batch</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Asynchronously get a list of text embeddings, with batching."""</span>
    <span class="n">num_workers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>

    <span class="n">model_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="n">model_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

    <span class="n">cur_batch</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">callback_payloads</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">result_embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">embeddings_coroutines</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Coroutine</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">texts</span><span class="p">):</span>
        <span class="n">cur_batch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_batch_size</span><span class="p">:</span>
            <span class="c1"># flush</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">EmbeddingStartEvent</span><span class="p">(</span>
                    <span class="n">model_dict</span><span class="o">=</span><span class="n">model_dict</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="n">event_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">on_event_start</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()},</span>
            <span class="p">)</span>
            <span class="n">callback_payloads</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">event_id</span><span class="p">,</span> <span class="n">cur_batch</span><span class="p">))</span>
            <span class="n">embeddings_coroutines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_text_embeddings</span><span class="p">(</span><span class="n">cur_batch</span><span class="p">))</span>
            <span class="n">cur_batch</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># flatten the results of asyncio.gather, which is a list of embeddings lists</span>
    <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">embeddings_coroutines</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
            <span class="n">desc</span><span class="o">=</span><span class="s2">"Generating embeddings"</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">tqdm.asyncio</span> <span class="kn">import</span> <span class="n">tqdm_asyncio</span>

                <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">tqdm_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
                    <span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">,</span>
                    <span class="n">total</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">embeddings_coroutines</span><span class="p">),</span>
                    <span class="n">desc</span><span class="o">=</span><span class="s2">"Generating embeddings"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nested_embeddings</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">embeddings_coroutines</span><span class="p">)</span>

    <span class="n">result_embeddings</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">embedding</span> <span class="k">for</span> <span class="n">embeddings</span> <span class="ow">in</span> <span class="n">nested_embeddings</span> <span class="k">for</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="n">embeddings</span>
    <span class="p">]</span>

    <span class="k">for</span> <span class="p">(</span><span class="n">event_id</span><span class="p">,</span> <span class="n">text_batch</span><span class="p">),</span> <span class="n">embeddings</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
        <span class="n">callback_payloads</span><span class="p">,</span> <span class="n">nested_embeddings</span>
    <span class="p">):</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">EmbeddingEndEvent</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="n">text_batch</span><span class="p">,</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">on_event_end</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">text_batch</span><span class="p">,</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span><span class="p">:</span> <span class="n">embeddings</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">result_embeddings</span>
</code></pre></div></td></tr></tbody></table>

### similarity [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding.similarity "Permanent link")

```
similarity(embedding1: Embedding, embedding2: Embedding, mode: SimilarityMode = SimilarityMode.DEFAULT) -> float
```

Get embedding similarity.

Source code in `llama-index-core/llama_index/core/base/embeddings/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">similarity</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">embedding1</span><span class="p">:</span> <span class="n">Embedding</span><span class="p">,</span>
    <span class="n">embedding2</span><span class="p">:</span> <span class="n">Embedding</span><span class="p">,</span>
    <span class="n">mode</span><span class="p">:</span> <span class="n">SimilarityMode</span> <span class="o">=</span> <span class="n">SimilarityMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get embedding similarity."""</span>
    <span class="k">return</span> <span class="n">similarity</span><span class="p">(</span><span class="n">embedding1</span><span class="o">=</span><span class="n">embedding1</span><span class="p">,</span> <span class="n">embedding2</span><span class="o">=</span><span class="n">embedding2</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

resolve\_embed\_model [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.resolve_embed_model "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

```
resolve_embed_model(embed_model: Optional[EmbedType] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None) -> [BaseEmbedding](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "llama_index.core.base.embeddings.base.BaseEmbedding")
```

Resolve embed model.

Source code in `llama-index-core/llama_index/core/embeddings/utils.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">resolve_embed_model</span><span class="p">(</span>
    <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseEmbedding</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Resolve embed model."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.settings</span> <span class="kn">import</span> <span class="n">Settings</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Embeddings</span> <span class="k">as</span> <span class="n">LCEmbeddings</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="n">LCEmbeddings</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: ignore</span>

    <span class="k">if</span> <span class="n">embed_model</span> <span class="o">==</span> <span class="s2">"default"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"IS_TESTING"</span><span class="p">):</span>
            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">MockEmbedding</span><span class="p">(</span><span class="n">embed_dim</span><span class="o">=</span><span class="mi">8</span><span class="p">)</span>
            <span class="n">embed_model</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span>
            <span class="k">return</span> <span class="n">embed_model</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.embeddings.openai</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">OpenAIEmbedding</span><span class="p">,</span>
            <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

            <span class="kn">from</span> <span class="nn">llama_index.embeddings.openai.utils</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">validate_openai_api_key</span><span class="p">,</span>
            <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">OpenAIEmbedding</span><span class="p">()</span>
            <span class="n">validate_openai_api_key</span><span class="p">(</span><span class="n">embed_model</span><span class="o">.</span><span class="n">api_key</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`llama-index-embeddings-openai` package not found, "</span>
                <span class="s2">"please run `pip install llama-index-embeddings-openai`"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">******</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"Could not load OpenAI embedding model. "</span>
                <span class="s2">"If you intended to use OpenAI, please check your OPENAI_API_KEY.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"Original error:</span><span class="se">\n</span><span class="s2">"</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">Consider using embed_model='local'.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"Visit our documentation for more embedding options: "</span>
                <span class="s2">"https://docs.llamaindex.ai/en/stable/module_guides/models/"</span>
                <span class="s2">"embeddings.html#modules"</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">******"</span>
            <span class="p">)</span>
    <span class="c1"># for image multi-modal embeddings</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">embed_model</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="n">embed_model</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"clip"</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.embeddings.clip</span> <span class="kn">import</span> <span class="n">ClipEmbedding</span>  <span class="c1"># pants: no-infer-dep</span>

            <span class="n">clip_model_name</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">embed_model</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">":"</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span> <span class="k">if</span> <span class="s2">":"</span> <span class="ow">in</span> <span class="n">embed_model</span> <span class="k">else</span> <span class="s2">"ViT-B/32"</span>
            <span class="p">)</span>
            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">ClipEmbedding</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">clip_model_name</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`llama-index-embeddings-clip` package not found, "</span>
                <span class="s2">"please run `pip install llama-index-embeddings-clip` and `pip install git+https://github.com/openai/CLIP.git`"</span>
            <span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">embed_model</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.embeddings.huggingface</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">HuggingFaceEmbedding</span><span class="p">,</span>
            <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

            <span class="n">splits</span> <span class="o">=</span> <span class="n">embed_model</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">":"</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
            <span class="n">is_local</span> <span class="o">=</span> <span class="n">splits</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">model_name</span> <span class="o">=</span> <span class="n">splits</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splits</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="kc">None</span>
            <span class="k">if</span> <span class="n">is_local</span> <span class="o">!=</span> <span class="s2">"local"</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"embed_model must start with str 'local' or of type BaseEmbedding"</span>
                <span class="p">)</span>

            <span class="n">cache_folder</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">get_cache_dir</span><span class="p">(),</span> <span class="s2">"models"</span><span class="p">)</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">cache_folder</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">HuggingFaceEmbedding</span><span class="p">(</span>
                <span class="n">model_name</span><span class="o">=</span><span class="n">model_name</span><span class="p">,</span> <span class="n">cache_folder</span><span class="o">=</span><span class="n">cache_folder</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`llama-index-embeddings-huggingface` package not found, "</span>
                <span class="s2">"please run `pip install llama-index-embeddings-huggingface`"</span>
            <span class="p">)</span>

    <span class="k">if</span> <span class="n">LCEmbeddings</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">embed_model</span><span class="p">,</span> <span class="n">LCEmbeddings</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.embeddings.langchain</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">LangchainEmbedding</span><span class="p">,</span>
            <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">LangchainEmbedding</span><span class="p">(</span><span class="n">embed_model</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`llama-index-embeddings-langchain` package not found, "</span>
                <span class="s2">"please run `pip install llama-index-embeddings-langchain`"</span>
            <span class="p">)</span>

    <span class="k">if</span> <span class="n">embed_model</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Embeddings have been explicitly disabled. Using MockEmbedding."</span><span class="p">)</span>
        <span class="n">embed_model</span> <span class="o">=</span> <span class="n">MockEmbedding</span><span class="p">(</span><span class="n">embed_dim</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

    <span class="n">embed_model</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span>

    <span class="k">return</span> <span class="n">embed_model</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Ibm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ibm/)[Next Instructor](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/instructor/)
