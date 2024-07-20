Title: Azure - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/

Markdown Content:
Azure - LlamaIndex


AzureChatStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/#llama_index.storage.chat_store.azure.AzureChatStore "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore "llama_index.core.storage.chat_store.base.BaseChatStore")`

Azure chat store leveraging Azure Table Storage or Cosmos DB.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-azure/llama_index/storage/chat_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 32</span>
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
<span class="normal">382</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureChatStore</span><span class="p">(</span><span class="n">BaseChatStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure chat store leveraging Azure Table Storage or Cosmos DB."""</span>

    <span class="n">_table_service_client</span><span class="p">:</span> <span class="n">TableServiceClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_atable_service_client</span><span class="p">:</span> <span class="n">AsyncTableServiceClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHAT_TABLE</span><span class="p">)</span>
    <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_METADATA_TABLE</span><span class="p">)</span>
    <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">table_service_client</span><span class="p">:</span> <span class="n">TableServiceClient</span><span class="p">,</span>
        <span class="n">atable_service_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncTableServiceClient</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_TABLE</span><span class="p">,</span>
        <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_METADATA_TABLE</span><span class="p">,</span>
        <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">sanitized_chat_table_name</span> <span class="o">=</span> <span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">chat_table_name</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">chat_table_name</span><span class="o">=</span><span class="n">sanitized_chat_table_name</span><span class="p">,</span>
            <span class="n">metadata_table_name</span><span class="o">=</span><span class="n">sanitize_table_name</span><span class="p">(</span><span class="n">metadata_table_name</span><span class="p">),</span>
            <span class="n">metadata_partition_key</span><span class="o">=</span><span class="p">(</span>
                <span class="n">sanitized_chat_table_name</span>
                <span class="k">if</span> <span class="n">metadata_partition_key</span> <span class="ow">is</span> <span class="kc">None</span>
                <span class="k">else</span> <span class="n">metadata_partition_key</span>
            <span class="p">),</span>
            <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span> <span class="o">=</span> <span class="n">table_service_client</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_atable_service_client</span> <span class="o">=</span> <span class="n">atable_service_client</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_TABLE</span><span class="p">,</span>
        <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_METADATA_TABLE</span><span class="p">,</span>
        <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Creates an instance of AzureChatStore using a connection string."""</span>
        <span class="n">table_service_client</span> <span class="o">=</span> <span class="n">TableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span>
        <span class="p">)</span>
        <span class="n">atable_service_client</span> <span class="o">=</span> <span class="n">AsyncTableServiceClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">table_service_client</span><span class="p">,</span>
            <span class="n">atable_service_client</span><span class="p">,</span>
            <span class="n">chat_table_name</span><span class="p">,</span>
            <span class="n">metadata_table_name</span><span class="p">,</span>
            <span class="n">metadata_partition_key</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_TABLE</span><span class="p">,</span>
        <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_METADATA_TABLE</span><span class="p">,</span>
        <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureChatStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initializes AzureChatStore from an account name and key."""</span>
        <span class="k">if</span> <span class="n">endpoint</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://</span><span class="si">{</span><span class="n">account_name</span><span class="si">}</span><span class="s2">.table.core.windows.net"</span>
        <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureNamedKeyCredential</span><span class="p">(</span><span class="n">account_name</span><span class="p">,</span> <span class="n">account_key</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">credential</span><span class="p">,</span>
            <span class="n">chat_table_name</span><span class="p">,</span>
            <span class="n">metadata_table_name</span><span class="p">,</span>
            <span class="n">metadata_partition_key</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_TABLE</span><span class="p">,</span>
        <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_METADATA_TABLE</span><span class="p">,</span>
        <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureChatStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an AzureChatStore instance using a SAS token."""</span>
        <span class="n">credential</span> <span class="o">=</span> <span class="n">AzureSasCredential</span><span class="p">(</span><span class="n">sas_token</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">credential</span><span class="p">,</span>
            <span class="n">chat_table_name</span><span class="p">,</span>
            <span class="n">metadata_table_name</span><span class="p">,</span>
            <span class="n">metadata_partition_key</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_TABLE</span><span class="p">,</span>
        <span class="n">metadata_table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_METADATA_TABLE</span><span class="p">,</span>
        <span class="n">metadata_partition_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureChatStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an AzureChatStore using an Azure Active Directory token."""</span>
        <span class="kn">from</span> <span class="nn">azure.identity</span> <span class="kn">import</span> <span class="n">DefaultAzureCredential</span>

        <span class="n">credential</span> <span class="o">=</span> <span class="n">DefaultAzureCredential</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_from_clients</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">credential</span><span class="p">,</span>
            <span class="n">chat_table_name</span><span class="p">,</span>
            <span class="n">metadata_table_name</span><span class="p">,</span>
            <span class="n">metadata_partition_key</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set messages for a key."""</span>
        <span class="c1"># Delete existing messages and insert new messages in one transaction</span>
        <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
        <span class="p">)</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">chat_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
        <span class="n">delete_operations</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">DELETE</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
        <span class="p">)</span>
        <span class="n">create_operations</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">(</span>
                <span class="n">TransactionOperation</span><span class="o">.</span><span class="n">CREATE</span><span class="p">,</span>
                <span class="n">serialize</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span>
                    <span class="p">{</span>
                        <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                        <span class="s2">"RowKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">idx</span><span class="p">),</span>
                        <span class="o">**</span><span class="n">message</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span>
                    <span class="p">},</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">message</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">chat_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="n">delete_operations</span><span class="p">,</span> <span class="n">create_operations</span><span class="p">))</span>

        <span class="c1"># Update metadata</span>
        <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
        <span class="p">)</span>
        <span class="n">messages_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="n">metadata_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata_partition_key</span><span class="p">,</span>
                <span class="s2">"RowKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="s2">"LastMessageRowKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">messages_len</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span>
                <span class="s2">"MessageCount"</span><span class="p">:</span> <span class="n">messages_len</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get messages for a key."""</span>
        <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
        <span class="p">)</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">chat_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">deserialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span> <span class="n">entity</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Add a message for a key."""</span>
        <span class="c1"># Fetch current metadata to find the next index</span>
        <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
        <span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_or_default_metadata</span><span class="p">(</span><span class="n">metadata_client</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span>
        <span class="n">next_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">])</span>

        <span class="k">if</span> <span class="n">idx</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">idx</span> <span class="o">&gt;</span> <span class="n">next_index</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Index out of bounds: </span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">idx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">idx</span> <span class="o">=</span> <span class="n">next_index</span>

        <span class="c1"># Insert the new message</span>
        <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
        <span class="p">)</span>
        <span class="n">chat_client</span><span class="o">.</span><span class="n">create_entity</span><span class="p">(</span>
            <span class="n">serialize</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">service_mode</span><span class="p">,</span>
                <span class="p">{</span>
                    <span class="s2">"PartitionKey"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                    <span class="s2">"RowKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">idx</span><span class="p">),</span>
                    <span class="o">**</span><span class="n">message</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span>
                <span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">metadata</span><span class="p">[</span><span class="s2">"LastMessageRowKey"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">]</span> <span class="o">=</span> <span class="n">next_index</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="c1"># Update medatada</span>
        <span class="n">metadata_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span><span class="n">metadata</span><span class="p">,</span> <span class="n">UpdateMode</span><span class="o">.</span><span class="n">MERGE</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
        <span class="c1"># Delete all messages for the key</span>
        <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
        <span class="p">)</span>
        <span class="n">entities</span> <span class="o">=</span> <span class="n">chat_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span><span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
        <span class="n">chat_client</span><span class="o">.</span><span class="n">submit_transaction</span><span class="p">(</span>
            <span class="p">(</span><span class="n">TransactionOperation</span><span class="o">.</span><span class="n">DELETE</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span>
        <span class="p">)</span>

        <span class="c1"># Reset metadata</span>
        <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
        <span class="p">)</span>
        <span class="n">metadata_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_metadata</span><span class="p">(</span><span class="n">key</span><span class="p">),</span> <span class="n">UpdateMode</span><span class="o">.</span><span class="n">REPLACE</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Delete specific message for a key."""</span>
        <span class="c1"># Fetch metadata to get the message count</span>
        <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
        <span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span>
        <span class="p">)</span>

        <span class="c1"># Index out of bounds</span>
        <span class="n">message_count</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">])</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="o">&gt;=</span> <span class="n">message_count</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="c1"># Delete the message</span>
        <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
        <span class="p">)</span>
        <span class="n">chat_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">idx</span><span class="p">))</span>

        <span class="c1"># Update metadata if last message was deleted</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="o"></span> <span class="n">message_count</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"LastMessageRowKey"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span><span class="n">idx</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">]</span> <span class="o">=</span> <span class="n">message_count</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="n">metadata_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span><span class="n">metadata</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">UpdateMode</span><span class="o">.</span><span class="n">MERGE</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_last\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/#llama_index.storage.chat_store.azure.AzureChatStore.delete_last_message "Permanent link")

```
delete_last_message(key: str) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete last message for a key.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-azure/llama_index/storage/chat_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">292</span>
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
<span class="normal">315</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete last message for a key."""</span>
    <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
    <span class="p">)</span>
    <span class="c1"># Retrieve metadata to get the last message row key</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata_client</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span>
        <span class="n">partition_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_partition_key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">key</span>
    <span class="p">)</span>
    <span class="n">last_row_key</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"LastMessageRowKey"</span><span class="p">]</span>

    <span class="n">chat_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chat_table_name</span>
    <span class="p">)</span>
    <span class="c1"># Delete the last message</span>
    <span class="n">chat_client</span><span class="o">.</span><span class="n">delete_entity</span><span class="p">(</span><span class="n">partition_key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">row_key</span><span class="o">=</span><span class="n">last_row_key</span><span class="p">)</span>

    <span class="c1"># Update metadata</span>
    <span class="n">last_row_key_num</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">last_row_key</span><span class="p">)</span>
    <span class="n">metadata</span><span class="p">[</span><span class="s2">"LastMessageRowKey"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_row_key</span><span class="p">(</span>
        <span class="n">last_row_key_num</span> <span class="o">-</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">last_row_key_num</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="p">)</span>
    <span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"MessageCount"</span><span class="p">])</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">metadata_client</span><span class="o">.</span><span class="n">upsert_entity</span><span class="p">(</span><span class="n">metadata</span><span class="p">,</span> <span class="n">UpdateMode</span><span class="o">.</span><span class="n">MERGE</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_keys [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/#llama_index.storage.chat_store.azure.AzureChatStore.get_keys "Permanent link")

```
get_keys() -> List[str]
```

Get all keys.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-azure/llama_index/storage/chat_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all keys."""</span>
    <span class="n">metadata_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_service_client</span><span class="o">.</span><span class="n">create_table_if_not_exists</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metadata_table_name</span>
    <span class="p">)</span>
    <span class="n">entities</span> <span class="o">=</span> <span class="n">metadata_client</span><span class="o">.</span><span class="n">query_entities</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_partition_key</span><span class="si">}</span><span class="s2">'"</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">entity</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]</span> <span class="k">for</span> <span class="n">entity</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/#llama_index.storage.chat_store.azure.AzureChatStore.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-azure/llama_index/storage/chat_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"AzureChatStore"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/schema/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/)
