Title: Postgres - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/

Markdown Content:
Postgres - LlamaIndex


PostgresKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

Postgres Key-Value store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `connection_string` | `str` | 
psycopg2 connection string



 | _required_ |
| `async_connection_string` | `str` | 

asyncpg connection string



 | _required_ |
| `table_name` | `str` | 

table name



 | _required_ |
| `schema_name` | `Optional[str]` | 

schema name



 | `'public'` |
| `perform_setup` | `Optional[bool]` | 

perform table setup



 | `True` |
| `debug` | `Optional[bool]` | 

debug mode



 | `False` |
| `use_jsonb` | `Optional[bool]` | 

use JSONB data type for storage



 | `False` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
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
<span class="normal">449</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PostgresKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Postgres Key-Value store.</span>

<span class="sd">    Args:</span>
<span class="sd">        connection_string (str): psycopg2 connection string</span>
<span class="sd">        async_connection_string (str): asyncpg connection string</span>
<span class="sd">        table_name (str): table name</span>
<span class="sd">        schema_name (Optional[str]): schema name</span>
<span class="sd">        perform_setup (Optional[bool]): perform table setup</span>
<span class="sd">        debug (Optional[bool]): debug mode</span>
<span class="sd">        use_jsonb (Optional[bool]): use JSONB data type for storage</span>
<span class="sd">    """</span>

    <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">async_connection_string</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">async_connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">asyncpg</span>  <span class="c1"># noqa</span>
            <span class="kn">import</span> <span class="nn">psycopg2</span>  <span class="c1"># noqa</span>
            <span class="kn">import</span> <span class="nn">sqlalchemy</span>
            <span class="kn">import</span> <span class="nn">sqlalchemy.ext.asyncio</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`sqlalchemy[asyncio]`, `psycopg2-binary` and `asyncpg` "</span>
                <span class="s2">"packages should be pre installed"</span>
            <span class="p">)</span>

        <span class="n">table_name</span> <span class="o">=</span> <span class="n">table_name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="n">schema_name</span> <span class="o">=</span> <span class="n">schema_name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">connection_string</span> <span class="o">=</span> <span class="n">connection_string</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">async_connection_string</span> <span class="o">=</span> <span class="n">async_connection_string</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">table_name</span> <span class="o">=</span> <span class="n">table_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span> <span class="o">=</span> <span class="n">schema_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">perform_setup</span> <span class="o">=</span> <span class="n">perform_setup</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">debug</span> <span class="o">=</span> <span class="n">debug</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_jsonb</span> <span class="o">=</span> <span class="n">use_jsonb</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="kn">from</span> <span class="nn">sqlalchemy.orm</span> <span class="kn">import</span> <span class="n">declarative_base</span>

        <span class="c1"># sqlalchemy model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base</span> <span class="o">=</span> <span class="n">declarative_base</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span> <span class="o">=</span> <span class="n">get_data_model</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base</span><span class="p">,</span>
            <span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"kvstore"</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return connection string from database parameters."""</span>
        <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">connection_string</span>
            <span class="ow">or</span> <span class="sa">f</span><span class="s2">"postgresql+psycopg2://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="n">async_conn_str</span> <span class="o">=</span> <span class="n">async_connection_string</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"postgresql+asyncpg://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="o">=</span><span class="n">conn_str</span><span class="p">,</span>
            <span class="n">async_connection_string</span><span class="o">=</span><span class="n">async_conn_str</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"kvstore"</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return connection string from database parameters."""</span>
        <span class="n">params</span> <span class="o">=</span> <span class="n">params_from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_params</span><span class="p">(</span>
            <span class="o">**</span><span class="n">params</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">create_engine</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.ext.asyncio</span> <span class="kn">import</span> <span class="n">AsyncSession</span><span class="p">,</span> <span class="n">create_async_engine</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.orm</span> <span class="kn">import</span> <span class="n">sessionmaker</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">connection_string</span><span class="p">,</span> <span class="n">echo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span> <span class="o">=</span> <span class="n">sessionmaker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_engine</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_async_engine</span> <span class="o">=</span> <span class="n">create_async_engine</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_connection_string</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span> <span class="o">=</span> <span class="n">sessionmaker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_async_engine</span><span class="p">,</span> <span class="n">class_</span><span class="o">=</span><span class="n">AsyncSession</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_schema_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">text</span>

            <span class="c1"># Check if the specified schema exists with "CREATE" statement</span>
            <span class="n">check_schema_statement</span> <span class="o">=</span> <span class="n">text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">'"</span>
            <span class="p">)</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">check_schema_statement</span><span class="p">)</span><span class="o">.</span><span class="n">fetchone</span><span class="p">()</span>

            <span class="c1"># If the schema does not exist, then create it</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
                <span class="n">create_schema_statement</span> <span class="o">=</span> <span class="n">text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"CREATE SCHEMA IF NOT EXISTS </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">create_schema_statement</span><span class="p">)</span>

            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_create_tables_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">create_all</span><span class="p">(</span><span class="n">session</span><span class="o">.</span><span class="n">connection</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">_initialize</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_connect</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">perform_setup</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_schema_if_not_exists</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_tables_if_not_exists</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span> <span class="o">=</span> <span class="kc">True</span>

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
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">text</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">kv_pairs</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">):</span>
                <span class="n">batch</span> <span class="o">=</span> <span class="n">kv_pairs</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span>

                <span class="c1"># Prepare the VALUES part of the SQL statement</span>
                <span class="n">values_clause</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"(:key_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">, :namespace_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">, :value_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">)"</span>
                    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">batch</span><span class="p">)</span>
                <span class="p">)</span>

                <span class="c1"># Prepare the raw SQL for bulk upsert</span>
                <span class="c1"># Note: This SQL is PostgreSQL-specific. Adjust for other databases.</span>
                <span class="n">stmt</span> <span class="o">=</span> <span class="n">text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">                INSERT INTO </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">__tablename__</span><span class="si">}</span><span class="s2"> (key, namespace, value)</span>
<span class="s2">                VALUES </span><span class="si">{</span><span class="n">values_clause</span><span class="si">}</span>
<span class="s2">                ON CONFLICT (key, namespace)</span>
<span class="s2">                DO UPDATE SET</span>
<span class="s2">                value = EXCLUDED.value;</span>
<span class="s2">                """</span>
                <span class="p">)</span>

                <span class="c1"># Flatten the list of tuples for execute parameters</span>
                <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">batch</span><span class="p">):</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"key_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">key</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"namespace_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">collection</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"value_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>

                <span class="c1"># Execute the bulk upsert</span>
                <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">text</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">kv_pairs</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">):</span>
                <span class="n">batch</span> <span class="o">=</span> <span class="n">kv_pairs</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span>

                <span class="c1"># Prepare the VALUES part of the SQL statement</span>
                <span class="n">values_clause</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"(:key_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">, :namespace_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">, :value_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">)"</span>
                    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">batch</span><span class="p">)</span>
                <span class="p">)</span>

                <span class="c1"># Prepare the raw SQL for bulk upsert</span>
                <span class="c1"># Note: This SQL is PostgreSQL-specific. Adjust for other databases.</span>
                <span class="n">stmt</span> <span class="o">=</span> <span class="n">text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">                INSERT INTO </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">__tablename__</span><span class="si">}</span><span class="s2"> (key, namespace, value)</span>
<span class="s2">                VALUES </span><span class="si">{</span><span class="n">values_clause</span><span class="si">}</span>
<span class="s2">                ON CONFLICT (key, namespace)</span>
<span class="s2">                DO UPDATE SET</span>
<span class="s2">                value = EXCLUDED.value;</span>
<span class="s2">                """</span>
                <span class="p">)</span>

                <span class="c1"># Flatten the list of tuples for execute parameters</span>
                <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">batch</span><span class="p">):</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"key_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">key</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"namespace_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">collection</span>
                    <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"value_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>

                <span class="c1"># Execute the bulk upsert</span>
                <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
                <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span><span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">results</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">result</span><span class="o">.</span><span class="n">key</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">}</span> <span class="k">if</span> <span class="n">results</span> <span class="k">else</span> <span class="p">{}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span><span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">results</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">result</span><span class="o">.</span><span class="n">key</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">}</span> <span class="k">if</span> <span class="n">results</span> <span class="k">else</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">delete</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">rowcount</span> <span class="o">&gt;</span> <span class="mi">0</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">delete</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
                    <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
                    <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">rowcount</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

### from\_params `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.from_params "Permanent link")

```
from_params(host: Optional[str] = None, port: Optional[str] = None, database: Optional[str] = None, user: Optional[str] = None, password: Optional[str] = None, table_name: str = 'kvstore', schema_name: str = 'public', connection_string: Optional[str] = None, async_connection_string: Optional[str] = None, perform_setup: bool = True, debug: bool = False, use_jsonb: bool = False) -> [PostgresKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore "llama_index.storage.kvstore.postgres.base.PostgresKVStore")
```

Return connection string from database parameters.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"kvstore"</span><span class="p">,</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return connection string from database parameters."""</span>
    <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">connection_string</span>
        <span class="ow">or</span> <span class="sa">f</span><span class="s2">"postgresql+psycopg2://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s2">"</span>
    <span class="p">)</span>
    <span class="n">async_conn_str</span> <span class="o">=</span> <span class="n">async_connection_string</span> <span class="ow">or</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">"postgresql+asyncpg://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s2">"</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">connection_string</span><span class="o">=</span><span class="n">conn_str</span><span class="p">,</span>
        <span class="n">async_connection_string</span><span class="o">=</span><span class="n">async_conn_str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
        <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_uri `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.from_uri "Permanent link")

```
from_uri(uri: str, table_name: str = 'kvstore', schema_name: str = 'public', perform_setup: bool = True, debug: bool = False, use_jsonb: bool = False) -> [PostgresKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore "llama_index.storage.kvstore.postgres.base.PostgresKVStore")
```

Return connection string from database parameters.

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
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
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"kvstore"</span><span class="p">,</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return connection string from database parameters."""</span>
    <span class="n">params</span> <span class="o">=</span> <span class="n">params_from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_params</span><span class="p">(</span>
        <span class="o">**</span><span class="n">params</span><span class="p">,</span>
        <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
        <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.put "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">215</span>
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
<span class="normal">229</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
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

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.aput "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">231</span>
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
<span class="normal">245</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
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

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.get "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">331</span>
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
<span class="normal">351</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.aget "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">353</span>
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
<span class="normal">375</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.get_all "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">377</span>
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
<span class="normal">392</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span><span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">results</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">{</span><span class="n">result</span><span class="o">.</span><span class="n">key</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">}</span> <span class="k">if</span> <span class="n">results</span> <span class="k">else</span> <span class="p">{}</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.aget_all "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">394</span>
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
<span class="normal">409</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span><span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">results</span><span class="o">.</span><span class="n">scalars</span><span class="p">()</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">{</span><span class="n">result</span><span class="o">.</span><span class="n">key</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">}</span> <span class="k">if</span> <span class="n">results</span> <span class="k">else</span> <span class="p">{}</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.delete "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">411</span>
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
<span class="normal">429</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">delete</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
            <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">rowcount</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore.adelete "Permanent link")

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

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-postgres/llama_index/storage/kvstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">431</span>
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
<span class="normal">449</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">delete</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>
                <span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">)</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">rowcount</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/)[Next Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/redis/)
