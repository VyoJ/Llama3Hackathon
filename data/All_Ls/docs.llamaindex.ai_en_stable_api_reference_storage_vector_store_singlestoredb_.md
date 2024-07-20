Title: Singlestoredb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/

Markdown Content:
Singlestoredb - LlamaIndex


SingleStoreVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/#llama_index.vector_stores.singlestoredb.SingleStoreVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

SingleStore vector store.

This vector store stores embeddings within a SingleStore database table.

During query time, the index uses SingleStore to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `table_name` | `str` | 
Specifies the name of the table in use. Defaults to "embeddings".



 | `'embeddings'` |
| `content_field` | `str` | 

Specifies the field to store the content. Defaults to "content".



 | `'content'` |
| `metadata_field` | `str` | 

Specifies the field to store metadata. Defaults to "metadata".



 | `'metadata'` |
| `vector_field` | `str` | 

Specifies the field to store the vector. Defaults to "vector".



 | `'vector'` |
| `Following` | `arguments pertain to the connection pool` | 

 | _required_ |
| `pool_size` | `int` | 

Determines the number of active connections in the pool. Defaults to 5.



 | `5` |
| `max_overflow` | `int` | 

Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.



 | `10` |
| `timeout` | `float` | 

Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.



 | `30` |
| `Following` | `arguments pertain to the connection` | 

 | _required_ |
| `host` | `str` | 

Specifies the hostname, IP address, or URL for the database connection. The default scheme is "mysql".



 | _required_ |
| `user` | `str` | 

Database username.



 | _required_ |
| `password` | `str` | 

Database password.



 | _required_ |
| `port` | `int` | 

Database port. Defaults to 3306 for non-HTTP connections, 80 for HTTP connections, and 443 for HTTPS connections.



 | _required_ |
| `database` | `str` | 

Database name.



 | _required_ |

**Examples:**

`pip install llama-index-vector-stores-singlestoredb`

```
from llama_index.vector_stores.singlestoredb import SingleStoreVectorStore
import os

# can set the singlestore db url in env
# or pass it in as an argument to the SingleStoreVectorStore constructor
os.environ["SINGLESTOREDB_URL"] = "PLACEHOLDER URL"
vector_store = SingleStoreVectorStore(
    table_name="embeddings",
    content_field="content",
    metadata_field="metadata",
    vector_field="vector",
    timeout=30,
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-singlestoredb/llama_index/vector_stores/singlestoredb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
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
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SingleStoreVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SingleStore vector store.</span>

<span class="sd">    This vector store stores embeddings within a SingleStore database table.</span>

<span class="sd">    During query time, the index uses SingleStore to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        table_name (str, optional): Specifies the name of the table in use.</span>
<span class="sd">                Defaults to "embeddings".</span>
<span class="sd">        content_field (str, optional): Specifies the field to store the content.</span>
<span class="sd">            Defaults to "content".</span>
<span class="sd">        metadata_field (str, optional): Specifies the field to store metadata.</span>
<span class="sd">            Defaults to "metadata".</span>
<span class="sd">        vector_field (str, optional): Specifies the field to store the vector.</span>
<span class="sd">            Defaults to "vector".</span>

<span class="sd">        Following arguments pertain to the connection pool:</span>

<span class="sd">        pool_size (int, optional): Determines the number of active connections in</span>
<span class="sd">            the pool. Defaults to 5.</span>
<span class="sd">        max_overflow (int, optional): Determines the maximum number of connections</span>
<span class="sd">            allowed beyond the pool_size. Defaults to 10.</span>
<span class="sd">        timeout (float, optional): Specifies the maximum wait time in seconds for</span>
<span class="sd">            establishing a connection. Defaults to 30.</span>

<span class="sd">        Following arguments pertain to the connection:</span>

<span class="sd">        host (str, optional): Specifies the hostname, IP address, or URL for the</span>
<span class="sd">                database connection. The default scheme is "mysql".</span>
<span class="sd">        user (str, optional): Database username.</span>
<span class="sd">        password (str, optional): Database password.</span>
<span class="sd">        port (int, optional): Database port. Defaults to 3306 for non-HTTP</span>
<span class="sd">            connections, 80 for HTTP connections, and 443 for HTTPS connections.</span>
<span class="sd">        database (str, optional): Database name.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-singlestoredb`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.singlestoredb import SingleStoreVectorStore</span>
<span class="sd">        import os</span>

<span class="sd">        # can set the singlestore db url in env</span>
<span class="sd">        # or pass it in as an argument to the SingleStoreVectorStore constructor</span>
<span class="sd">        os.environ["SINGLESTOREDB_URL"] = "PLACEHOLDER URL"</span>
<span class="sd">        vector_store = SingleStoreVectorStore(</span>
<span class="sd">            table_name="embeddings",</span>
<span class="sd">            content_field="content",</span>
<span class="sd">            metadata_field="metadata",</span>
<span class="sd">            vector_field="vector",</span>
<span class="sd">            timeout=30,</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">content_field</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">metadata_field</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">vector_field</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">pool_size</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">max_overflow</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">connection_kwargs</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="n">connection_pool</span><span class="p">:</span> <span class="n">QueuePool</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embeddings"</span><span class="p">,</span>
        <span class="n">content_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"content"</span><span class="p">,</span>
        <span class="n">metadata_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">vector_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"vector"</span><span class="p">,</span>
        <span class="n">pool_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">max_overflow</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">content_field</span><span class="o">=</span><span class="n">content_field</span><span class="p">,</span>
            <span class="n">metadata_field</span><span class="o">=</span><span class="n">metadata_field</span><span class="p">,</span>
            <span class="n">vector_field</span><span class="o">=</span><span class="n">vector_field</span><span class="p">,</span>
            <span class="n">pool_size</span><span class="o">=</span><span class="n">pool_size</span><span class="p">,</span>
            <span class="n">max_overflow</span><span class="o">=</span><span class="n">max_overflow</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="n">connection_kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="n">connection_pool</span><span class="o">=</span><span class="n">QueuePool</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_get_connection</span><span class="p">,</span>
                <span class="n">pool_size</span><span class="o">=</span><span class="n">pool_size</span><span class="p">,</span>
                <span class="n">max_overflow</span><span class="o">=</span><span class="n">max_overflow</span><span class="p">,</span>
                <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_create_table</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return SingleStoreDB client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_connection</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SingleStoreVectorStore"</span>

    <span class="k">def</span> <span class="nf">_get_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">s2</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">connection_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_table</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"""CREATE TABLE IF NOT EXISTS </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span>
<span class="s2">                    (</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content_field</span><span class="si">}</span><span class="s2"> TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,</span>
<span class="s2">                    </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span><span class="si">}</span><span class="s2"> BLOB, </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_field</span><span class="si">}</span><span class="s2"> JSON);"""</span>
                <span class="p">)</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="n">cur</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        """</span>
        <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
        <span class="n">cursor</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
                <span class="n">embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                    <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
                <span class="p">)</span>
                <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="s2">"INSERT INTO </span><span class="si">{}</span><span class="s2"> VALUES (</span><span class="si">%s</span><span class="s2">, JSON_ARRAY_PACK(</span><span class="si">%s</span><span class="s2">), </span><span class="si">%s</span><span class="s2">)"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">table_name</span>
                    <span class="p">),</span>
                    <span class="p">(</span>
                        <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
                        <span class="s2">"[</span><span class="si">{}</span><span class="s2">]"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">embedding</span><span class="p">))),</span>
                        <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">metadata</span><span class="p">),</span>
                    <span class="p">),</span>
                <span class="p">)</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="n">cursor</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
            <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
        <span class="n">cursor</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"DELETE FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2"> WHERE JSON_EXTRACT_JSON(metadata, 'ref_doc_id') = %s"</span><span class="p">,</span>
                <span class="p">(</span><span class="s1">'"'</span> <span class="o">+</span> <span class="n">ref_doc_id</span> <span class="o">+</span> <span class="s1">'"'</span><span class="p">,),</span>
            <span class="p">)</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="n">cursor</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
            <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="nb">filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): Contains query_embedding and similarity_top_k attributes.</span>
<span class="sd">            filter (Optional[dict]): A dictionary of metadata fields and values to filter by. Defaults to None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            VectorStoreQueryResult: Contains nodes, similarities, and ids attributes.</span>
<span class="sd">        """</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
        <span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
        <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
        <span class="n">where_clause</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">where_clause_values</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="nb">filter</span><span class="p">:</span>
            <span class="n">where_clause</span> <span class="o">=</span> <span class="s2">"WHERE "</span>
            <span class="n">arguments</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">def</span> <span class="nf">build_where_clause</span><span class="p">(</span>
                <span class="n">where_clause_values</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
                <span class="n">sub_filter</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
                <span class="n">prefix_args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">prefix_args</span> <span class="o">=</span> <span class="n">prefix_args</span> <span class="ow">or</span> <span class="p">[]</span>
                <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">sub_filter</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
                        <span class="n">build_where_clause</span><span class="p">(</span>
                            <span class="n">where_clause_values</span><span class="p">,</span> <span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="p">[</span><span class="o">*</span><span class="n">prefix_args</span><span class="p">,</span> <span class="n">key</span><span class="p">]</span>
                        <span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">arguments</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="s2">"JSON_EXTRACT(</span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">) = </span><span class="si">%s</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                                <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_field</span><span class="p">},</span>
                                <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s2">"</span><span class="si">%s</span><span class="s2">"</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">prefix_args</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)),</span>
                            <span class="p">)</span>
                        <span class="p">)</span>
                        <span class="n">where_clause_values</span> <span class="o">+=</span> <span class="p">[</span><span class="o">*</span><span class="n">prefix_args</span><span class="p">,</span> <span class="n">key</span><span class="p">]</span>
                        <span class="n">where_clause_values</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">]))</span>

            <span class="n">build_where_clause</span><span class="p">(</span><span class="n">where_clause_values</span><span class="p">,</span> <span class="nb">filter</span><span class="p">)</span>
            <span class="n">where_clause</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>

        <span class="n">results</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">query_embedding</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
                <span class="n">formatted_vector</span> <span class="o">=</span> <span class="s2">"[</span><span class="si">{}</span><span class="s2">]"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">query_embedding</span><span class="p">)))</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"vector field: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">formatted_vector</span><span class="p">)</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"similarity_top_k: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="p">)</span>
                    <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"SELECT </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content_field</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_field</span><span class="si">}</span><span class="s2">, "</span>
                        <span class="sa">f</span><span class="s2">"DOT_PRODUCT(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span><span class="si">}</span><span class="s2">, "</span>
                        <span class="s2">"JSON_ARRAY_PACK(</span><span class="si">%s</span><span class="s2">)) as similarity_score "</span>
                        <span class="sa">f</span><span class="s2">"FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">where_clause</span><span class="si">}</span><span class="s2"> "</span>
                        <span class="sa">f</span><span class="s2">"ORDER BY similarity_score DESC LIMIT </span><span class="si">{</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="p">(</span><span class="n">formatted_vector</span><span class="p">,</span> <span class="o">*</span><span class="nb">tuple</span><span class="p">(</span><span class="n">where_clause_values</span><span class="p">)),</span>
                    <span class="p">)</span>
                    <span class="n">results</span> <span class="o">=</span> <span class="n">cur</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
                <span class="k">finally</span><span class="p">:</span>
                    <span class="n">cur</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="p">,</span> <span class="n">similarity_score</span> <span class="o">=</span> <span class="n">result</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
            <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">similarity_score</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/#llama_index.vector_stores.singlestoredb.SingleStoreVectorStore.client "Permanent link")

```
client: Any
```

Return SingleStoreDB client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/#llama_index.vector_stores.singlestoredb.SingleStoreVectorStore.add "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-singlestoredb/llama_index/vector_stores/singlestoredb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">151</span>
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
<span class="normal">179</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
    <span class="n">cursor</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>
            <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="s2">"INSERT INTO </span><span class="si">{}</span><span class="s2"> VALUES (</span><span class="si">%s</span><span class="s2">, JSON_ARRAY_PACK(</span><span class="si">%s</span><span class="s2">), </span><span class="si">%s</span><span class="s2">)"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">table_name</span>
                <span class="p">),</span>
                <span class="p">(</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
                    <span class="s2">"[</span><span class="si">{}</span><span class="s2">]"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">embedding</span><span class="p">))),</span>
                    <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">metadata</span><span class="p">),</span>
                <span class="p">),</span>
            <span class="p">)</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="n">cursor</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/#llama_index.vector_stores.singlestoredb.SingleStoreVectorStore.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-singlestoredb/llama_index/vector_stores/singlestoredb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">181</span>
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
<span class="normal">198</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
    <span class="n">cursor</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"DELETE FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2"> WHERE JSON_EXTRACT_JSON(metadata, 'ref_doc_id') = %s"</span><span class="p">,</span>
            <span class="p">(</span><span class="s1">'"'</span> <span class="o">+</span> <span class="n">ref_doc_id</span> <span class="o">+</span> <span class="s1">'"'</span><span class="p">,),</span>
        <span class="p">)</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="n">cursor</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/#llama_index.vector_stores.singlestoredb.SingleStoreVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), filter: Optional[dict] = None, **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Contains query\_embedding and similarity\_top\_k attributes.



 | _required_ |
| `filter` | `Optional[dict]` | 

A dictionary of metadata fields and values to filter by. Defaults to None.



 | `None` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `VectorStoreQueryResult` | `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
Contains nodes, similarities, and ids attributes.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-singlestoredb/llama_index/vector_stores/singlestoredb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
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
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="nb">filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): Contains query_embedding and similarity_top_k attributes.</span>
<span class="sd">        filter (Optional[dict]): A dictionary of metadata fields and values to filter by. Defaults to None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        VectorStoreQueryResult: Contains nodes, similarities, and ids attributes.</span>
<span class="sd">    """</span>
    <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span>
    <span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>
    <span class="n">conn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_pool</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
    <span class="n">where_clause</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">where_clause_values</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="nb">filter</span><span class="p">:</span>
        <span class="n">where_clause</span> <span class="o">=</span> <span class="s2">"WHERE "</span>
        <span class="n">arguments</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">def</span> <span class="nf">build_where_clause</span><span class="p">(</span>
            <span class="n">where_clause_values</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
            <span class="n">sub_filter</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
            <span class="n">prefix_args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prefix_args</span> <span class="o">=</span> <span class="n">prefix_args</span> <span class="ow">or</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">sub_filter</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
                    <span class="n">build_where_clause</span><span class="p">(</span>
                        <span class="n">where_clause_values</span><span class="p">,</span> <span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="p">[</span><span class="o">*</span><span class="n">prefix_args</span><span class="p">,</span> <span class="n">key</span><span class="p">]</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">arguments</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="s2">"JSON_EXTRACT(</span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">) = </span><span class="si">%s</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                            <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_field</span><span class="p">},</span>
                            <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s2">"</span><span class="si">%s</span><span class="s2">"</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">prefix_args</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)),</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                    <span class="n">where_clause_values</span> <span class="o">+=</span> <span class="p">[</span><span class="o">*</span><span class="n">prefix_args</span><span class="p">,</span> <span class="n">key</span><span class="p">]</span>
                    <span class="n">where_clause_values</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">sub_filter</span><span class="p">[</span><span class="n">key</span><span class="p">]))</span>

        <span class="n">build_where_clause</span><span class="p">(</span><span class="n">where_clause_values</span><span class="p">,</span> <span class="nb">filter</span><span class="p">)</span>
        <span class="n">where_clause</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>

    <span class="n">results</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">query_embedding</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
            <span class="n">formatted_vector</span> <span class="o">=</span> <span class="s2">"[</span><span class="si">{}</span><span class="s2">]"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">query_embedding</span><span class="p">)))</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"vector field: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">formatted_vector</span><span class="p">)</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"similarity_top_k: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="p">)</span>
                <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"SELECT </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content_field</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_field</span><span class="si">}</span><span class="s2">, "</span>
                    <span class="sa">f</span><span class="s2">"DOT_PRODUCT(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span><span class="si">}</span><span class="s2">, "</span>
                    <span class="s2">"JSON_ARRAY_PACK(</span><span class="si">%s</span><span class="s2">)) as similarity_score "</span>
                    <span class="sa">f</span><span class="s2">"FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">where_clause</span><span class="si">}</span><span class="s2"> "</span>
                    <span class="sa">f</span><span class="s2">"ORDER BY similarity_score DESC LIMIT </span><span class="si">{</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="p">(</span><span class="n">formatted_vector</span><span class="p">,</span> <span class="o">*</span><span class="nb">tuple</span><span class="p">(</span><span class="n">where_clause_values</span><span class="p">)),</span>
                <span class="p">)</span>
                <span class="n">results</span> <span class="o">=</span> <span class="n">cur</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="n">cur</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
        <span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="p">,</span> <span class="n">similarity_score</span> <span class="o">=</span> <span class="n">result</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
        <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">similarity_score</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/simple/)[Next Supabase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/)
