Title: Zep - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/

Markdown Content:
Zep - LlamaIndex


ZepVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Zep Vector Store for storing and retrieving embeddings.

Zep supports both normalized and non-normalized embeddings. Cosine similarity is used to compute distance and the returned score is normalized to be between 0 and 1.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the Zep collection in which to store embeddings.



 | _required_ |
| `api_url` | `str` | 

URL of the Zep API.



 | _required_ |
| `api_key` | `str` | 

Key for the Zep API. Defaults to None.



 | `None` |
| `collection_description` | `str` | 

Description of the collection. Defaults to None.



 | `None` |
| `collection_metadata` | `dict` | 

Metadata of the collection. Defaults to None.



 | `None` |
| `embedding_dimensions` | `int` | 

Dimensions of the embeddings. Defaults to None.



 | `None` |
| `is_auto_embedded` | `bool` | 

Whether the embeddings are auto-embedded. Defaults to False.



 | `False` |

**Examples:**

`pip install llama-index-vector-stores-zep`

```
from llama_index.vector_stores.zep import ZepVectorStore

vector_store = ZepVectorStore(
    api_url="<api_url>",
    api_key="<api_key>",
    collection_name="<unique_collection_name>",  # Can either be an existing collection or a new one
    embedding_dimensions=1536,  # Optional, required if creating a new collection
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
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
<span class="normal">341</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ZepVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Zep Vector Store for storing and retrieving embeddings.</span>

<span class="sd">    Zep supports both normalized and non-normalized embeddings. Cosine similarity is</span>
<span class="sd">    used to compute distance and the returned score is normalized to be between 0 and 1.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): Name of the Zep collection in which to store embeddings.</span>
<span class="sd">        api_url (str): URL of the Zep API.</span>
<span class="sd">        api_key (str, optional): Key for the Zep API. Defaults to None.</span>
<span class="sd">        collection_description (str, optional): Description of the collection.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        collection_metadata (dict, optional): Metadata of the collection.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        embedding_dimensions (int, optional): Dimensions of the embeddings.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        is_auto_embedded (bool, optional): Whether the embeddings are auto-embedded.</span>
<span class="sd">            Defaults to False.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-zep`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.zep import ZepVectorStore</span>

<span class="sd">        vector_store = ZepVectorStore(</span>
<span class="sd">            api_url="&lt;api_url&gt;",</span>
<span class="sd">            api_key="&lt;api_key&gt;",</span>
<span class="sd">            collection_name="&lt;unique_collection_name&gt;",  # Can either be an existing collection or a new one</span>
<span class="sd">            embedding_dimensions=1536,  # Optional, required if creating a new collection</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">ZepClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">DocumentCollection</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">api_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection_description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embedding_dimensions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">is_auto_embedded</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">ZepClient</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">api_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>
        <span class="n">collection</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">DocumentCollection</span><span class="p">,</span> <span class="kc">None</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">zep_python</span><span class="o">.</span><span class="n">NotFoundError</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">embedding_dimensions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"embedding_dimensions must be specified if collection does not"</span>
                    <span class="s2">" exist"</span>
                <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Collection </span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2"> does not exist, "</span>
                <span class="sa">f</span><span class="s2">"will try creating one with dimensions=</span><span class="si">{</span><span class="n">embedding_dimensions</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

            <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">add_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
                <span class="n">embedding_dimensions</span><span class="o">=</span><span class="n">embedding_dimensions</span><span class="p">,</span>
                <span class="n">is_auto_embedded</span><span class="o">=</span><span class="n">is_auto_embedded</span><span class="p">,</span>
                <span class="n">description</span><span class="o">=</span><span class="n">collection_description</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">collection_metadata</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">assert</span> <span class="n">collection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="n">collection</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ZepVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">_prepare_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="s2">"ZepDocument"</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"ZepDocument"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">metadata_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">())</span> <span class="o"> "</span><span class="si">{</span><span class="n">f</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s1">")'</span><span class="p">})</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"where"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"and"</span><span class="p">:</span> <span class="n">filter_conditions</span><span class="p">}}</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query the index for the top k most similar nodes to the given query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): Query object containing either a query string</span>
<span class="sd">                or a query embedding.</span>

<span class="sd">        Returns:</span>
<span class="sd">            VectorStoreQueryResult: Result of the query, containing the most similar</span>
<span class="sd">                nodes, their similarities, and their IDs.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query must have one of query_str or query_embedding"</span><span class="p">)</span>

        <span class="c1"># If we have an embedding, we shouldn't use the query string</span>
        <span class="c1"># Zep does not allow both to be set</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
            <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="n">metadata_filters</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata_filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_zep_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_filters</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronously query the index for the top k most similar nodes to the</span>
<span class="sd">            given query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): Query object containing either a query string or</span>
<span class="sd">                a query embedding.</span>

<span class="sd">        Returns:</span>
<span class="sd">            VectorStoreQueryResult: Result of the query, containing the most similar</span>
<span class="sd">                nodes, their similarities, and their IDs.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query must have one of query_str or query_embedding"</span><span class="p">)</span>

        <span class="c1"># If we have an embedding, we shouldn't use the query string</span>
        <span class="c1"># Zep does not allow both to be set</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
            <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="n">metadata_filters</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata_filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_zep_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">asearch</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_filters</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to the collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List of nodes with embeddings.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
List\[str\]: List of IDs of the added documents.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
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
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to the collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode]): List of nodes with embeddings.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[str]: List of IDs of the added documents.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">is_auto_embedded</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection is auto embedded, cannot add embeddings"</span><span class="p">)</span>

    <span class="n">docs</span><span class="p">,</span> <span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### async\_add `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.async_add "Permanent link")

```
async_add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Asynchronously add nodes to the collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List of nodes with embeddings.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
List\[str\]: List of IDs of the added documents.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">161</span>
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
<span class="normal">184</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Asynchronously add nodes to the collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode]): List of nodes with embeddings.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[str]: List of IDs of the added documents.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">is_auto_embedded</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection is auto embedded, cannot add embeddings"</span><span class="p">)</span>

    <span class="n">docs</span><span class="p">,</span> <span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">aadd_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.delete "Permanent link")

```
delete(ref_doc_id: Optional[str] = None, **delete_kwargs: Any) -> None
```

Delete a document from the collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `Optional[str]` | 
ID of the document to delete. Not currently supported.



 | `None` |
| `delete_kwargs` | `Any` | 

Must contain "uuid" key with UUID of the document to delete.



 | `{}` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

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
<span class="normal">207</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
<span class="w">    </span><span class="sd">"""Delete a document from the collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (Optional[str]): ID of the document to delete.</span>
<span class="sd">            Not currently supported.</span>
<span class="sd">        delete_kwargs: Must contain "uuid" key with UUID of the document to delete.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Delete by ref_doc_id not yet implemented for Zep."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="s2">"uuid"</span> <span class="ow">in</span> <span class="n">delete_kwargs</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span><span class="n">uuid</span><span class="o">=</span><span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"uuid"</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"uuid must be specified"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.adelete "Permanent link")

```
adelete(ref_doc_id: Optional[str] = None, **delete_kwargs: Any) -> None
```

Asynchronously delete a document from the collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `Optional[str]` | 
ID of the document to delete. Not currently supported.



 | `None` |
| `delete_kwargs` | `Any` | 

Must contain "uuid" key with UUID of the document to delete.



 | `{}` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">209</span>
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
<span class="normal">230</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
<span class="w">    </span><span class="sd">"""Asynchronously delete a document from the collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (Optional[str]): ID of the document to delete.</span>
<span class="sd">            Not currently supported.</span>
<span class="sd">        delete_kwargs: Must contain "uuid" key with UUID of the document to delete.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Delete by ref_doc_id not yet implemented for Zep."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="s2">"uuid"</span> <span class="ow">in</span> <span class="n">delete_kwargs</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">adelete_document</span><span class="p">(</span><span class="n">uuid</span><span class="o">=</span><span class="n">delete_kwargs</span><span class="p">[</span><span class="s2">"uuid"</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"uuid must be specified"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query the index for the top k most similar nodes to the given query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Query object containing either a query string or a query embedding.



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `VectorStoreQueryResult` | `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
Result of the query, containing the most similar nodes, their similarities, and their IDs.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">264</span>
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
<span class="normal">301</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query the index for the top k most similar nodes to the given query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): Query object containing either a query string</span>
<span class="sd">            or a query embedding.</span>

<span class="sd">    Returns:</span>
<span class="sd">        VectorStoreQueryResult: Result of the query, containing the most similar</span>
<span class="sd">            nodes, their similarities, and their IDs.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query must have one of query_str or query_embedding"</span><span class="p">)</span>

    <span class="c1"># If we have an embedding, we shouldn't use the query string</span>
    <span class="c1"># Zep does not allow both to be set</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
        <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">metadata_filters</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata_filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_zep_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">embedding</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_filters</span><span class="p">,</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aquery `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/#llama_index.vector_stores.zep.ZepVectorStore.aquery "Permanent link")

```
aquery(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Asynchronously query the index for the top k most similar nodes to the given query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Query object containing either a query string or a query embedding.



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `VectorStoreQueryResult` | `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
Result of the query, containing the most similar nodes, their similarities, and their IDs.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-zep/llama_index/vector_stores/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">303</span>
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
<span class="normal">341</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Asynchronously query the index for the top k most similar nodes to the</span>
<span class="sd">        given query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): Query object containing either a query string or</span>
<span class="sd">            a query embedding.</span>

<span class="sd">    Returns:</span>
<span class="sd">        VectorStoreQueryResult: Result of the query, containing the most similar</span>
<span class="sd">            nodes, their similarities, and their IDs.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">,</span> <span class="n">DocumentCollection</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query must have one of query_str or query_embedding"</span><span class="p">)</span>

    <span class="c1"># If we have an embedding, we shouldn't use the query string</span>
    <span class="c1"># Zep does not allow both to be set</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
        <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">metadata_filters</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata_filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_zep_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">asearch</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">embedding</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_filters</span><span class="p">,</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/wordlift/)[Next Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/)
