Title: Elasticsearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/

Markdown Content:
Elasticsearch - LlamaIndex


ElasticsearchKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/#llama_index.storage.kvstore.elasticsearch.ElasticsearchKVStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

Elasticsearch Key-Value store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index_name` | `str` | 
Name of the Elasticsearch index.



 | _required_ |
| `es_client` | `Optional[Any]` | 

Optional. Pre-existing AsyncElasticsearch client.



 | _required_ |
| `es_url` | `Optional[str]` | 

Optional. Elasticsearch URL.



 | `None` |
| `es_cloud_id` | `Optional[str]` | 

Optional. Elasticsearch cloud ID.



 | `None` |
| `es_api_key` | `Optional[str]` | 

Optional. Elasticsearch API key.



 | `None` |
| `es_user` | `Optional[str]` | 

Optional. Elasticsearch username.



 | `None` |
| `es_password` | `Optional[str]` | 

Optional. Elasticsearch password.



 | `None` |

**Raises:**

| Type | Description |
| --- | --- |
| `ConnectionError` | 
If AsyncElasticsearch client cannot connect to Elasticsearch.



 |
| `ValueError` | 

If neither es\_client nor es\_url nor es\_cloud\_id is provided.



 |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-elasticsearch/llama_index/storage/kvstore/elasticsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 78</span>
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
<span class="normal">318</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ElasticsearchKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Elasticsearch Key-Value store.</span>

<span class="sd">    Args:</span>
<span class="sd">        index_name: Name of the Elasticsearch index.</span>
<span class="sd">        es_client: Optional. Pre-existing AsyncElasticsearch client.</span>
<span class="sd">        es_url: Optional. Elasticsearch URL.</span>
<span class="sd">        es_cloud_id: Optional. Elasticsearch cloud ID.</span>
<span class="sd">        es_api_key: Optional. Elasticsearch API key.</span>
<span class="sd">        es_user: Optional. Elasticsearch username.</span>
<span class="sd">        es_password: Optional. Elasticsearch password.</span>


<span class="sd">    Raises:</span>
<span class="sd">        ConnectionError: If AsyncElasticsearch client cannot connect to Elasticsearch.</span>
<span class="sd">        ValueError: If neither es_client nor es_url nor es_cloud_id is provided.</span>

<span class="sd">    """</span>

    <span class="n">es_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span>
    <span class="n">es_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">es_cloud_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">es_api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">es_user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">es_password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">es_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="n">es_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">es_cloud_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">es_api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">es_user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">es_password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">nest_asyncio</span><span class="o">.</span><span class="n">apply</span><span class="p">()</span>

<span class="w">        </span><span class="sd">"""Init a ElasticsearchKVStore."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">elasticsearch</span> <span class="kn">import</span> <span class="n">AsyncElasticsearch</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">es_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">es_client</span><span class="o">.</span><span class="n">options</span><span class="p">(</span>
                <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"user-agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_user_agent</span><span class="p">()}</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">es_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">es_cloud_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">:</span> <span class="n">AsyncElasticsearch</span> <span class="o">=</span> <span class="n">_get_elasticsearch_client</span><span class="p">(</span>
                <span class="n">es_url</span><span class="o">=</span><span class="n">es_url</span><span class="p">,</span>
                <span class="n">username</span><span class="o">=</span><span class="n">es_user</span><span class="p">,</span>
                <span class="n">password</span><span class="o">=</span><span class="n">es_password</span><span class="p">,</span>
                <span class="n">cloud_id</span><span class="o">=</span><span class="n">es_cloud_id</span><span class="p">,</span>
                <span class="n">api_key</span><span class="o">=</span><span class="n">es_api_key</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""Either provide a pre-existing AsyncElasticsearch or valid \</span>
<span class="sd">                credentials for creating a new connection."""</span>
            <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get async elasticsearch client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">get_user_agent</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get user agent for elasticsearch client."""</span>
        <span class="k">return</span> <span class="s2">"llama_index-py-vs"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_create_index_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create the AsyncElasticsearch index if it doesn't already exist.</span>

<span class="sd">        Args:</span>
<span class="sd">            index_name: Name of the AsyncElasticsearch index to create.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">indices</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">index_name</span><span class="p">):</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="n">index_name</span><span class="si">}</span><span class="s2"> already exists. Skipping creation."</span><span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">index_settings</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"mappings"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"_source"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"enabled"</span><span class="p">:</span> <span class="kc">True</span><span class="p">}}}</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Creating index </span><span class="si">{</span><span class="n">index_name</span><span class="si">}</span><span class="s2"> with mappings </span><span class="si">{</span><span class="n">index_settings</span><span class="p">[</span><span class="s1">'mappings'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">indices</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span> <span class="o">**</span><span class="n">index_settings</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">put_all</span><span class="p">([(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)],</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aput_all</span><span class="p">([(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)],</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">put_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span><span class="n">kv_pairs</span><span class="p">,</span> <span class="n">collection</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_not_exists</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>

        <span class="c1"># Prepare documents with '_id' set to the key for batch insertion</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span> <span class="o">**</span><span class="n">value</span><span class="p">}</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kv_pairs</span><span class="p">]</span>

        <span class="c1"># Insert documents in batches</span>
        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="n">docs</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">)</span>
        <span class="p">):</span>
            <span class="n">requests</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                <span class="n">doc_id</span> <span class="o">=</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
                <span class="n">request</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="s2">"_op_type"</span><span class="p">:</span> <span class="s2">"index"</span><span class="p">,</span>
                    <span class="s2">"_index"</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">doc</span><span class="p">,</span>
                    <span class="s2">"_id"</span><span class="p">:</span> <span class="n">doc_id</span><span class="p">,</span>
                <span class="p">}</span>
                <span class="n">requests</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
            <span class="k">await</span> <span class="n">async_bulk</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">,</span> <span class="n">requests</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">refresh</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aget</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_not_exists</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">collection</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">source</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">body</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span>
        <span class="k">except</span> <span class="n">elasticsearch</span><span class="o">.</span><span class="n">NotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aget_all</span><span class="p">(</span><span class="n">collection</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_not_exists</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>

        <span class="n">q</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"match_all"</span><span class="p">:</span> <span class="p">{}}}</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">collection</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">q</span><span class="p">,</span> <span class="n">source</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">][</span><span class="s2">"hits"</span><span class="p">]:</span>
            <span class="n">doc_id</span> <span class="o">=</span> <span class="n">r</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">r</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span>
            <span class="n">result</span><span class="p">[</span><span class="n">doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">content</span>
        <span class="k">return</span> <span class="n">result</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">adelete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_index_if_not_exists</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">collection</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">body</span><span class="p">[</span><span class="s2">"result"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"deleted"</span>
    <span class="k">except</span> <span class="n">elasticsearch</span><span class="o">.</span><span class="n">NotFoundError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/)[Next Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/)
