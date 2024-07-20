Title: Mongodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/

Markdown Content:
Mongodb - LlamaIndex


MongoDBKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

MongoDB Key-Value store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mongo_client` | `Any` | 
MongoDB client



 | _required_ |
| `uri` | `Optional[str]` | 

MongoDB URI



 | `None` |
| `host` | `Optional[str]` | 

MongoDB host



 | `None` |
| `port` | `Optional[int]` | 

MongoDB port



 | `None` |
| `db_name` | `Optional[str]` | 

MongoDB database name



 | `None` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
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
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MongoDBKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""MongoDB Key-Value store.</span>

<span class="sd">    Args:</span>
<span class="sd">        mongo_client (Any): MongoDB client</span>
<span class="sd">        uri (Optional[str]): MongoDB URI</span>
<span class="sd">        host (Optional[str]): MongoDB host</span>
<span class="sd">        port (Optional[int]): MongoDB port</span>
<span class="sd">        db_name (Optional[str]): MongoDB database name</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">mongo_client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">mongo_aclient</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a MongoDBKVStore."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">motor.motor_asyncio</span> <span class="kn">import</span> <span class="n">AsyncIOMotorClient</span>
            <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">MongoClient</span><span class="p">,</span> <span class="n">mongo_client</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">cast</span><span class="p">(</span><span class="n">AsyncIOMotorClient</span><span class="p">,</span> <span class="n">mongo_aclient</span><span class="p">)</span> <span class="k">if</span> <span class="n">mongo_aclient</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_uri</span> <span class="o">=</span> <span class="n">uri</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_host</span> <span class="o">=</span> <span class="n">host</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_port</span> <span class="o">=</span> <span class="n">port</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_db_name</span> <span class="o">=</span> <span class="n">db_name</span> <span class="ow">or</span> <span class="s2">"db_docstore"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_db_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_db_name</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="k">else</span> <span class="kc">None</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoDBKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a MongoDBKVStore from a MongoDB URI.</span>

<span class="sd">        Args:</span>
<span class="sd">            uri (str): MongoDB URI</span>
<span class="sd">            db_name (Optional[str]): MongoDB database name</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">motor.motor_asyncio</span> <span class="kn">import</span> <span class="n">AsyncIOMotorClient</span>
            <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">mongo_client</span><span class="p">:</span> <span class="n">MongoClient</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
        <span class="n">mongo_aclient</span><span class="p">:</span> <span class="n">AsyncIOMotorClient</span> <span class="o">=</span> <span class="n">AsyncIOMotorClient</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">mongo_client</span><span class="o">=</span><span class="n">mongo_client</span><span class="p">,</span>
            <span class="n">mongo_aclient</span><span class="o">=</span><span class="n">mongo_aclient</span><span class="p">,</span>
            <span class="n">db_name</span><span class="o">=</span><span class="n">db_name</span><span class="p">,</span>
            <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_host_and_port</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoDBKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a MongoDBKVStore from a MongoDB host and port.</span>

<span class="sd">        Args:</span>
<span class="sd">            host (str): MongoDB host</span>
<span class="sd">            port (int): MongoDB port</span>
<span class="sd">            db_name (Optional[str]): MongoDB database name</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">motor.motor_asyncio</span> <span class="kn">import</span> <span class="n">AsyncIOMotorClient</span>
            <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">mongo_client</span><span class="p">:</span> <span class="n">MongoClient</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
        <span class="n">mongo_aclient</span><span class="p">:</span> <span class="n">AsyncIOMotorClient</span> <span class="o">=</span> <span class="n">AsyncIOMotorClient</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">mongo_client</span><span class="o">=</span><span class="n">mongo_client</span><span class="p">,</span>
            <span class="n">mongo_aclient</span><span class="o">=</span><span class="n">mongo_aclient</span><span class="p">,</span>
            <span class="n">db_name</span><span class="o">=</span><span class="n">db_name</span><span class="p">,</span>
            <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_check_async_client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"MongoDBKVStore was not initialized with an async client"</span><span class="p">)</span>

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
        <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">UpdateOne</span>

        <span class="c1"># Prepare documents with '_id' set to the key for batch insertion</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span> <span class="o">**</span><span class="n">value</span><span class="p">}</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kv_pairs</span><span class="p">]</span>

        <span class="c1"># Insert documents in batches</span>
        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="n">docs</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">)</span>
        <span class="p">):</span>
            <span class="n">new_docs</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                <span class="n">new_docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">UpdateOne</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]},</span> <span class="p">{</span><span class="s2">"$set"</span><span class="p">:</span> <span class="n">doc</span><span class="p">},</span> <span class="n">upsert</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
                <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">bulk_write</span><span class="p">(</span><span class="n">new_docs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">UpdateOne</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

        <span class="c1"># Prepare documents with '_id' set to the key for batch insertion</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span> <span class="o">**</span><span class="n">value</span><span class="p">}</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kv_pairs</span><span class="p">]</span>

        <span class="c1"># Insert documents in batches</span>
        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="n">docs</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">)</span>
        <span class="p">):</span>
            <span class="n">new_docs</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                <span class="n">new_docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">UpdateOne</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]},</span> <span class="p">{</span><span class="s2">"$set"</span><span class="p">:</span> <span class="n">doc</span><span class="p">},</span> <span class="n">upsert</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
                <span class="p">)</span>

            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">bulk_write</span><span class="p">(</span><span class="n">new_docs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">result</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">result</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find</span><span class="p">()</span>
        <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
            <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find</span><span class="p">()</span>
        <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="k">await</span> <span class="n">results</span><span class="o">.</span><span class="n">to_list</span><span class="p">(</span><span class="n">length</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
            <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">deleted_count</span> <span class="o">&gt;</span> <span class="mi">0</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">deleted_count</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

### from\_uri `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.from_uri "Permanent link")

```
from_uri(uri: str, db_name: Optional[str] = None) -> [MongoDBKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore "llama_index.storage.kvstore.mongodb.base.MongoDBKVStore")
```

Load a MongoDBKVStore from a MongoDB URI.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `uri` | `str` | 
MongoDB URI



 | _required_ |
| `db_name` | `Optional[str]` | 

MongoDB database name



 | `None` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoDBKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a MongoDBKVStore from a MongoDB URI.</span>

<span class="sd">    Args:</span>
<span class="sd">        uri (str): MongoDB URI</span>
<span class="sd">        db_name (Optional[str]): MongoDB database name</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">motor.motor_asyncio</span> <span class="kn">import</span> <span class="n">AsyncIOMotorClient</span>
        <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">mongo_client</span><span class="p">:</span> <span class="n">MongoClient</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
    <span class="n">mongo_aclient</span><span class="p">:</span> <span class="n">AsyncIOMotorClient</span> <span class="o">=</span> <span class="n">AsyncIOMotorClient</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">mongo_client</span><span class="o">=</span><span class="n">mongo_client</span><span class="p">,</span>
        <span class="n">mongo_aclient</span><span class="o">=</span><span class="n">mongo_aclient</span><span class="p">,</span>
        <span class="n">db_name</span><span class="o">=</span><span class="n">db_name</span><span class="p">,</span>
        <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_host\_and\_port `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.from_host_and_port "Permanent link")

```
from_host_and_port(host: str, port: int, db_name: Optional[str] = None) -> [MongoDBKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore "llama_index.storage.kvstore.mongodb.base.MongoDBKVStore")
```

Load a MongoDBKVStore from a MongoDB host and port.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `host` | `str` | 
MongoDB host



 | _required_ |
| `port` | `int` | 

MongoDB port



 | _required_ |
| `db_name` | `Optional[str]` | 

MongoDB database name



 | `None` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 83</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_host_and_port</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoDBKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a MongoDBKVStore from a MongoDB host and port.</span>

<span class="sd">    Args:</span>
<span class="sd">        host (str): MongoDB host</span>
<span class="sd">        port (int): MongoDB port</span>
<span class="sd">        db_name (Optional[str]): MongoDB database name</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">motor.motor_asyncio</span> <span class="kn">import</span> <span class="n">AsyncIOMotorClient</span>
        <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

    <span class="n">mongo_client</span><span class="p">:</span> <span class="n">MongoClient</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
    <span class="n">mongo_aclient</span><span class="p">:</span> <span class="n">AsyncIOMotorClient</span> <span class="o">=</span> <span class="n">AsyncIOMotorClient</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">mongo_client</span><span class="o">=</span><span class="n">mongo_client</span><span class="p">,</span>
        <span class="n">mongo_aclient</span><span class="o">=</span><span class="n">mongo_aclient</span><span class="p">,</span>
        <span class="n">db_name</span><span class="o">=</span><span class="n">db_name</span><span class="p">,</span>
        <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
        <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.put "Permanent link")

```
put(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">118</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">put_all</span><span class="p">([(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)],</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.aput "Permanent link")

```
aput(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
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
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aput_all</span><span class="p">([(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)],</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.get "Permanent link")

```
get(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
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
<span class="normal">210</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.aget "Permanent link")

```
aget(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">212</span>
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
<span class="normal">228</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.get_all "Permanent link")

```
get_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">230</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find</span><span class="p">()</span>
    <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
        <span class="n">key</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
        <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.aget_all "Permanent link")

```
aget_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

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
<span class="normal">258</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">find</span><span class="p">()</span>
    <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="k">await</span> <span class="n">results</span><span class="o">.</span><span class="n">to_list</span><span class="p">(</span><span class="n">length</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="n">key</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"_id"</span><span class="p">)</span>
        <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.delete "Permanent link")

```
delete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">deleted_count</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore.adelete "Permanent link")

```
adelete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-mongodb/llama_index/storage/kvstore/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">271</span>
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
<span class="normal">282</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_check_async_client</span><span class="p">()</span>

    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">})</span>
    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">deleted_count</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/)[Next Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/)
