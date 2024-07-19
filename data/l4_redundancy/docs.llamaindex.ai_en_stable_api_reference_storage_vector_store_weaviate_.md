Title: Weaviate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/

Markdown Content:
Weaviate - LlamaIndex


WeaviateVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Weaviate vector store.

In this vector store, embeddings and docs are stored within a Weaviate collection.

During query time, the index uses Weaviate to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `weaviate_client` | `Client` | 
WeaviateClient instance from `weaviate-client` package



 | `None` |
| `index_name` | `Optional[str]` | 

name for Weaviate classes



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-weaviate`

```
import weaviate

resource_owner_config = weaviate.AuthClientPassword(
    username="<username>",
    password="<password>",
)
client = weaviate.Client(
    "https://llama-test-ezjahb4m.weaviate.network",
    auth_client_secret=resource_owner_config,
)

vector_store = WeaviateVectorStore(
    weaviate_client=client, index_name="LlamaIndex"
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 94</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WeaviateVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Weaviate vector store.</span>

<span class="sd">    In this vector store, embeddings and docs are stored within a</span>
<span class="sd">    Weaviate collection.</span>

<span class="sd">    During query time, the index uses Weaviate to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        weaviate_client (weaviate.Client): WeaviateClient</span>
<span class="sd">            instance from `weaviate-client` package</span>
<span class="sd">        index_name (Optional[str]): name for Weaviate classes</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-weaviate`</span>

<span class="sd">        ```python</span>
<span class="sd">        import weaviate</span>

<span class="sd">        resource_owner_config = weaviate.AuthClientPassword(</span>
<span class="sd">            username="&lt;username&gt;",</span>
<span class="sd">            password="&lt;password&gt;",</span>
<span class="sd">        )</span>
<span class="sd">        client = weaviate.Client(</span>
<span class="sd">            "https://llama-test-ezjahb4m.weaviate.network",</span>
<span class="sd">            auth_client_secret=resource_owner_config,</span>
<span class="sd">        )</span>

<span class="sd">        vector_store = WeaviateVectorStore(</span>
<span class="sd">            weaviate_client=client, index_name="LlamaIndex"</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">auth_config</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>
    <span class="n">client_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="n">_client</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">weaviate_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">class_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
        <span class="n">auth_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">client_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="k">if</span> <span class="n">weaviate_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">auth_config</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="n">auth_config</span> <span class="o">=</span> <span class="n">weaviate</span><span class="o">.</span><span class="n">auth</span><span class="o">.</span><span class="n">AuthApiKey</span><span class="p">(</span><span class="n">auth_config</span><span class="p">)</span>

            <span class="n">client_kwargs</span> <span class="o">=</span> <span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">weaviate</span><span class="o">.</span><span class="n">WeaviateClient</span><span class="p">(</span>
                <span class="n">auth_client_secret</span><span class="o">=</span><span class="n">auth_config</span><span class="p">,</span> <span class="o">**</span><span class="n">client_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">weaviate</span><span class="o">.</span><span class="n">WeaviateClient</span><span class="p">,</span> <span class="n">weaviate_client</span><span class="p">)</span>

        <span class="c1"># validate class prefix starts with a capital letter</span>
        <span class="k">if</span> <span class="n">class_prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"class_prefix is deprecated, please use index_name"</span><span class="p">)</span>
            <span class="c1"># legacy, kept for backward compatibility</span>
            <span class="n">index_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">class_prefix</span><span class="si">}</span><span class="s2">_Node"</span>

        <span class="n">index_name</span> <span class="o">=</span> <span class="n">index_name</span> <span class="ow">or</span> <span class="sa">f</span><span class="s2">"LlamaIndex_</span><span class="si">{</span><span class="n">uuid4</span><span class="p">()</span><span class="o">.</span><span class="n">hex</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">index_name</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">isupper</span><span class="p">():</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Index name must start with a capital letter, e.g. 'LlamaIndex'"</span>
            <span class="p">)</span>

        <span class="c1"># create default schema if does not exist</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">class_schema_exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="n">index_name</span><span class="p">):</span>
            <span class="n">create_default_schema</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="n">index_name</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="n">auth_config</span><span class="o">=</span><span class="n">auth_config</span><span class="o">.</span><span class="vm">__dict__</span> <span class="k">if</span> <span class="n">auth_config</span> <span class="k">else</span> <span class="p">{},</span>
            <span class="n">client_kwargs</span><span class="o">=</span><span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">auth_config</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
        <span class="n">client_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"WeaviateVectorStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create WeaviateVectorStore from config."""</span>
        <span class="n">client_kwargs</span> <span class="o">=</span> <span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">weaviate_client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">auth_client_secret</span><span class="o">=</span><span class="n">auth_config</span><span class="p">,</span> <span class="o">**</span><span class="n">client_kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">weaviate_client</span><span class="o">=</span><span class="n">weaviate_client</span><span class="p">,</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span>
            <span class="n">auth_config</span><span class="o">=</span><span class="n">auth_config</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">,</span>
            <span class="n">client_kwargs</span><span class="o">=</span><span class="n">client_kwargs</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"WeaviateVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        """</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">dynamic</span><span class="p">()</span> <span class="k">as</span> <span class="n">batch</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
                <span class="n">add_node</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span>
                    <span class="n">node</span><span class="p">,</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
                    <span class="n">batch</span><span class="o">=</span><span class="n">batch</span><span class="p">,</span>
                    <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>

        <span class="n">where_filter</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"ref_doc_id"</span><span class="p">)</span><span class="o">.</span><span class="n">equal</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">delete_kwargs</span> <span class="ow">and</span> <span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">where_filter</span> <span class="o">=</span> <span class="n">where_filter</span> <span class="o">&amp;</span> <span class="n">_to_weaviate_filter</span><span class="p">(</span><span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">])</span>

        <span class="n">collection</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">delete_many</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="n">where_filter</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete the index associated with the client.</span>

<span class="sd">        Raises:</span>
<span class="sd">        - Exception: If the deletion fails, for some reason.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">class_schema_exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">):</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">' does not exist. No action taken."</span>
            <span class="p">)</span>
            <span class="k">return</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Successfully deleted index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">'."</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to delete index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">': </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to delete index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">': </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes."""</span>
        <span class="n">all_properties</span> <span class="o">=</span> <span class="n">get_all_properties</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
        <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="c1"># list of documents to constrain search</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">)</span><span class="o">.</span><span class="n">contains_any</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span><span class="o">.</span><span class="n">contains_any</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">)</span>

        <span class="n">return_metatada</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">MetadataQuery</span><span class="p">(</span><span class="n">distance</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="n">vector</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
        <span class="n">similarity_key</span> <span class="o">=</span> <span class="s2">"distance"</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Using hybrid search with alpha </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">similarity_key</span> <span class="o">=</span> <span class="s2">"score"</span>
            <span class="k">if</span> <span class="n">vector</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">:</span>
                <span class="n">alpha</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">_to_weaviate_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">elif</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span>

        <span class="n">limit</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Using limit of </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># execute query</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">query_result</span> <span class="o">=</span> <span class="n">collection</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">vector</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span>
                <span class="n">alpha</span><span class="o">=</span><span class="n">alpha</span><span class="p">,</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
                <span class="n">return_metadata</span><span class="o">=</span><span class="n">return_metatada</span><span class="p">,</span>
                <span class="n">return_properties</span><span class="o">=</span><span class="n">all_properties</span><span class="p">,</span>
                <span class="n">include_vector</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">weaviate</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">WeaviateQueryError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query, got errors: </span><span class="si">{</span><span class="n">e</span><span class="o">.</span><span class="n">message</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># parse results</span>

        <span class="n">entries</span> <span class="o">=</span> <span class="n">query_result</span><span class="o">.</span><span class="n">objects</span>

        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">entry</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">entries</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">:</span>
                <span class="n">entry_as_dict</span> <span class="o">=</span> <span class="n">entry</span><span class="o">.</span><span class="vm">__dict__</span>
                <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">get_node_similarity</span><span class="p">(</span><span class="n">entry_as_dict</span><span class="p">,</span> <span class="n">similarity_key</span><span class="p">))</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">to_node</span><span class="p">(</span><span class="n">entry_as_dict</span><span class="p">,</span> <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">))</span>
                <span class="n">node_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### from\_params `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.from_params "Permanent link")

```
from_params(url: str, auth_config: Any, index_name: Optional[str] = None, text_key: str = DEFAULT_TEXT_KEY, client_kwargs: Optional[Dict[str, Any]] = None, **kwargs: Any) -> [WeaviateVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore "llama_index.vector_stores.weaviate.base.WeaviateVectorStore")
```

Create WeaviateVectorStore from config.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
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
<span class="normal">209</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">auth_config</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
    <span class="n">client_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"WeaviateVectorStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create WeaviateVectorStore from config."""</span>
    <span class="n">client_kwargs</span> <span class="o">=</span> <span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">weaviate_client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span>
        <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">auth_client_secret</span><span class="o">=</span><span class="n">auth_config</span><span class="p">,</span> <span class="o">**</span><span class="n">client_kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">weaviate_client</span><span class="o">=</span><span class="n">weaviate_client</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span>
        <span class="n">auth_config</span><span class="o">=</span><span class="n">auth_config</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">,</span>
        <span class="n">client_kwargs</span><span class="o">=</span><span class="n">client_kwargs</span><span class="p">,</span>
        <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
        <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">220</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">dynamic</span><span class="p">()</span> <span class="k">as</span> <span class="n">batch</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">add_node</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
                <span class="n">batch</span><span class="o">=</span><span class="n">batch</span><span class="p">,</span>
                <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">,</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document to delete.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
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
<span class="normal">259</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>

    <span class="n">where_filter</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"ref_doc_id"</span><span class="p">)</span><span class="o">.</span><span class="n">equal</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

    <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">delete_kwargs</span> <span class="ow">and</span> <span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">where_filter</span> <span class="o">=</span> <span class="n">where_filter</span> <span class="o">&amp;</span> <span class="n">_to_weaviate_filter</span><span class="p">(</span><span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">])</span>

    <span class="n">collection</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">delete_many</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="n">where_filter</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.delete_index "Permanent link")

```
delete_index() -> None
```

Delete the index associated with the client.

Raises: - Exception: If the deletion fails, for some reason.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">261</span>
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
<span class="normal">277</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete the index associated with the client.</span>

<span class="sd">    Raises:</span>
<span class="sd">    - Exception: If the deletion fails, for some reason.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">class_schema_exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">):</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">' does not exist. No action taken."</span>
        <span class="p">)</span>
        <span class="k">return</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Successfully deleted index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">'."</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to delete index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">': </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to delete index '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="si">}</span><span class="s2">': </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/#llama_index.vector_stores.weaviate.WeaviateVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-weaviate/llama_index/vector_stores/weaviate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">279</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes."""</span>
    <span class="n">all_properties</span> <span class="o">=</span> <span class="n">get_all_properties</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
    <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collections</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="c1"># list of documents to constrain search</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">)</span><span class="o">.</span><span class="n">contains_any</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">:</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">Filter</span><span class="o">.</span><span class="n">by_property</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span><span class="o">.</span><span class="n">contains_any</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">node_ids</span><span class="p">)</span>

    <span class="n">return_metatada</span> <span class="o">=</span> <span class="n">wvc</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">MetadataQuery</span><span class="p">(</span><span class="n">distance</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="n">vector</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
    <span class="n">similarity_key</span> <span class="o">=</span> <span class="s2">"distance"</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Using hybrid search with alpha </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">similarity_key</span> <span class="o">=</span> <span class="s2">"score"</span>
        <span class="k">if</span> <span class="n">vector</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">:</span>
            <span class="n">alpha</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="n">_to_weaviate_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">elif</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span>

    <span class="n">limit</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Using limit of </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># execute query</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">query_result</span> <span class="o">=</span> <span class="n">collection</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">vector</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span>
            <span class="n">alpha</span><span class="o">=</span><span class="n">alpha</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
            <span class="n">return_metadata</span><span class="o">=</span><span class="n">return_metatada</span><span class="p">,</span>
            <span class="n">return_properties</span><span class="o">=</span><span class="n">all_properties</span><span class="p">,</span>
            <span class="n">include_vector</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">except</span> <span class="n">weaviate</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">WeaviateQueryError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query, got errors: </span><span class="si">{</span><span class="n">e</span><span class="o">.</span><span class="n">message</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># parse results</span>

    <span class="n">entries</span> <span class="o">=</span> <span class="n">query_result</span><span class="o">.</span><span class="n">objects</span>

    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">entry</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">entries</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">:</span>
            <span class="n">entry_as_dict</span> <span class="o">=</span> <span class="n">entry</span><span class="o">.</span><span class="vm">__dict__</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">get_node_similarity</span><span class="p">(</span><span class="n">entry_as_dict</span><span class="p">,</span> <span class="n">similarity_key</span><span class="p">))</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">to_node</span><span class="p">(</span><span class="n">entry_as_dict</span><span class="p">,</span> <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">))</span>
            <span class="n">node_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">break</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vespa](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vespa/)[Next Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/wordlift/)
