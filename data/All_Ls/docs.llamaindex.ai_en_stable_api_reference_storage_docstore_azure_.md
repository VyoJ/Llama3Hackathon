Title: Azure - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/

Markdown Content:
Azure - LlamaIndex


AzureDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVDocumentStore`

Azure Document (Node) store. An Azure Table store for Document and Node objects.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 27</span>
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
<span class="normal">365</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureDocumentStore</span><span class="p">(</span><span class="n">KVDocumentStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Azure Document (Node) store.</span>
<span class="sd">    An Azure Table store for Document and Node objects.</span>
<span class="sd">    """</span>

    <span class="n">_kvstore</span><span class="p">:</span> <span class="n">AzureKVStore</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">azure_kvstore</span><span class="p">:</span> <span class="n">AzureKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize an AzureDocumentStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">azure_kvstore</span><span class="p">,</span>
            <span class="n">namespace</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="p">,</span>
            <span class="n">node_collection_suffix</span><span class="p">,</span>
            <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
            <span class="n">metadata_collection_suffix</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize an AzureDocumentStore from an Azure connection string."""</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">azure_kvstore</span><span class="p">,</span>
            <span class="n">namespace</span><span class="p">,</span>
            <span class="n">node_collection_suffix</span><span class="p">,</span>
            <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
            <span class="n">metadata_collection_suffix</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize an AzureDocumentStore from an account name and key."""</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_account_and_key</span><span class="p">(</span>
            <span class="n">account_name</span><span class="p">,</span>
            <span class="n">account_key</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">azure_kvstore</span><span class="p">,</span>
            <span class="n">namespace</span><span class="p">,</span>
            <span class="n">node_collection_suffix</span><span class="p">,</span>
            <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
            <span class="n">metadata_collection_suffix</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize an AzureDocumentStore from a SAS token."""</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_sas_token</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">sas_token</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">azure_kvstore</span><span class="p">,</span>
            <span class="n">namespace</span><span class="p">,</span>
            <span class="n">node_collection_suffix</span><span class="p">,</span>
            <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
            <span class="n">metadata_collection_suffix</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize an AzureDocumentStore from an AAD token."""</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_aad_token</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
            <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">azure_kvstore</span><span class="p">,</span>
            <span class="n">namespace</span><span class="p">,</span>
            <span class="n">node_collection_suffix</span><span class="p">,</span>
            <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
            <span class="n">metadata_collection_suffix</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_extract_doc_metadatas</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Prepare reference document key-value pairs."""</span>
        <span class="n">doc_metadatas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">(</span><span class="n">doc_id</span><span class="p">,</span> <span class="p">{</span><span class="s2">"metadata"</span><span class="p">:</span> <span class="n">doc_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)})</span>
            <span class="k">for</span> <span class="n">doc_id</span><span class="p">,</span> <span class="n">doc_dict</span> <span class="ow">in</span> <span class="n">ref_doc_kv_pairs</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="n">doc_metadatas</span>

    <span class="k">def</span> <span class="nf">add_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add documents to the store."""</span>
        <span class="n">batch_size</span> <span class="o">=</span> <span class="n">batch_size</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span>

        <span class="n">node_kv_pairs</span><span class="p">,</span> <span class="n">metadata_kv_pairs</span><span class="p">,</span> <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_prepare_kv_pairs</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="p">,</span> <span class="n">store_text</span>
        <span class="p">)</span>

        <span class="c1"># Change ref_doc_kv_pairs</span>
        <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_doc_metadatas</span><span class="p">(</span><span class="n">ref_doc_kv_pairs</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
            <span class="n">node_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
            <span class="n">metadata_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
            <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add documents to the store."""</span>
        <span class="n">batch_size</span> <span class="o">=</span> <span class="n">batch_size</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span>

        <span class="p">(</span>
            <span class="n">node_kv_pairs</span><span class="p">,</span>
            <span class="n">metadata_kv_pairs</span><span class="p">,</span>
            <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
        <span class="p">)</span> <span class="o">=</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_async_prepare_kv_pairs</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="p">,</span> <span class="n">store_text</span><span class="p">)</span>

        <span class="c1"># Change ref_doc_kv_pairs</span>
        <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_doc_metadatas</span><span class="p">(</span><span class="n">ref_doc_kv_pairs</span><span class="p">)</span>

        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
                <span class="n">node_kv_pairs</span><span class="p">,</span>
                <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_collection</span><span class="p">,</span>
                <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
                <span class="n">metadata_kv_pairs</span><span class="p">,</span>
                <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
                <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
                <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
                <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span>
                <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
        <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">' and ref_doc_id eq '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="s2">"RowKey"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">node_ids</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">doc_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
        <span class="p">)</span>

        <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"node_ids"</span><span class="p">:</span> <span class="n">node_ids</span><span class="p">,</span>
            <span class="s2">"metadata"</span><span class="p">:</span> <span class="n">doc_metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="c1"># TODO: deprecated legacy support</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
        <span class="n">ref_doc_infos</span><span class="p">,</span> <span class="n">doc_metadata</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">' and ref_doc_id eq '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
                <span class="n">select</span><span class="o">=</span><span class="s2">"RowKey"</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aget</span><span class="p">(</span>
                <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_doc_metadata_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
            <span class="p">),</span>
        <span class="p">)</span>

        <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]</span> <span class="k">async</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">node_ids</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"node_ids"</span><span class="p">:</span> <span class="n">node_ids</span><span class="p">,</span>
            <span class="s2">"metadata"</span><span class="p">:</span> <span class="n">doc_metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="c1"># TODO: deprecated legacy support</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents.</span>
<span class="sd">        """</span>
        <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">,</span> <span class="s2">"ref_doc_id"</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="c1"># TODO: deprecated legacy support</span>
        <span class="n">all_ref_doc_infos</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="p">{</span><span class="s2">"node_ids"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"metadata"</span><span class="p">:</span> <span class="kc">None</span><span class="p">})</span>
        <span class="k">for</span> <span class="n">ref_doc_info</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">:</span>
            <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"ref_doc_id"</span><span class="p">]</span>
            <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span>
            <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"node_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">])</span>

            <span class="k">if</span> <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">ref_doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                    <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
                <span class="p">)</span>
                <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">ref_doc_info_dict</span> <span class="ow">in</span> <span class="n">all_ref_doc_infos</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_ref_doc_infos</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents.</span>
<span class="sd">        """</span>
        <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">,</span> <span class="s2">"ref_doc_id"</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="c1"># TODO: deprecated legacy support</span>
        <span class="n">all_ref_doc_infos</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="p">{</span><span class="s2">"node_ids"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"metadata"</span><span class="p">:</span> <span class="kc">None</span><span class="p">})</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">ref_doc_info</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">:</span>
            <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"ref_doc_id"</span><span class="p">]</span>
            <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span>
            <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"node_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">])</span>

            <span class="k">if</span> <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">ref_doc</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aget</span><span class="p">(</span>
                    <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
                <span class="p">)</span>
                <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">ref_doc_info_dict</span> <span class="ow">in</span> <span class="n">all_ref_doc_infos</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_ref_doc_infos</span>

    <span class="k">def</span> <span class="nf">_remove_from_ref_doc_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper function to remove node doc_id from ref_doc_collection.</span>
<span class="sd">        If ref_doc has no more doc_ids, delete it from the collection.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aremove_from_ref_doc_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper function to remove node doc_id from ref_doc_collection.</span>
<span class="sd">        If ref_doc has no more doc_ids, delete it from the collection.</span>
<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">adelete</span><span class="p">(</span><span class="n">doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_connection\_string `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.from_connection_string "Permanent link")

```
from_connection_string(connection_string: str, namespace: Optional[str] = None, node_collection_suffix: Optional[str] = None, ref_doc_collection_suffix: Optional[str] = None, metadata_collection_suffix: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, **kwargs) -> [AzureDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore "llama_index.storage.docstore.azure.base.AzureDocumentStore")
```

Initialize an AzureDocumentStore from an Azure connection string.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize an AzureDocumentStore from an Azure connection string."""</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
        <span class="n">connection_string</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">azure_kvstore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_account\_and\_key `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.from_account_and_key "Permanent link")

```
from_account_and_key(account_name: str, account_key: str, namespace: Optional[str] = None, node_collection_suffix: Optional[str] = None, ref_doc_collection_suffix: Optional[str] = None, metadata_collection_suffix: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, **kwargs) -> [AzureDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore "llama_index.storage.docstore.azure.base.AzureDocumentStore")
```

Initialize an AzureDocumentStore from an account name and key.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 81</span>
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
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize an AzureDocumentStore from an account name and key."""</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_account_and_key</span><span class="p">(</span>
        <span class="n">account_name</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">azure_kvstore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_sas\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.from_sas_token "Permanent link")

```
from_sas_token(endpoint: str, sas_token: str, namespace: Optional[str] = None, node_collection_suffix: Optional[str] = None, ref_doc_collection_suffix: Optional[str] = None, metadata_collection_suffix: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, **kwargs) -> [AzureDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore "llama_index.storage.docstore.azure.base.AzureDocumentStore")
```

Initialize an AzureDocumentStore from a SAS token.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">110</span>
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
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize an AzureDocumentStore from a SAS token."""</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_sas_token</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span>
        <span class="n">sas_token</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">azure_kvstore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_aad\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.from_aad_token "Permanent link")

```
from_aad_token(endpoint: str, namespace: Optional[str] = None, node_collection_suffix: Optional[str] = None, ref_doc_collection_suffix: Optional[str] = None, metadata_collection_suffix: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None, **kwargs) -> [AzureDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore "llama_index.storage.docstore.azure.base.AzureDocumentStore")
```

Initialize an AzureDocumentStore from an AAD token.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">139</span>
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
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ref_doc_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_collection_suffix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize an AzureDocumentStore from an AAD token."""</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_aad_token</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="o">=</span><span class="n">service_mode</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="o">=</span><span class="n">partition_key</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">azure_kvstore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">,</span>
        <span class="n">node_collection_suffix</span><span class="p">,</span>
        <span class="n">ref_doc_collection_suffix</span><span class="p">,</span>
        <span class="n">metadata_collection_suffix</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.add_documents "Permanent link")

```
add_documents(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], allow_update: bool = True, batch_size: Optional[int] = None, store_text: bool = True) -> None
```

Add documents to the store.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">176</span>
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
<span class="normal">209</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add documents to the store."""</span>
    <span class="n">batch_size</span> <span class="o">=</span> <span class="n">batch_size</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span>

    <span class="n">node_kv_pairs</span><span class="p">,</span> <span class="n">metadata_kv_pairs</span><span class="p">,</span> <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_prepare_kv_pairs</span><span class="p">(</span>
        <span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="p">,</span> <span class="n">store_text</span>
    <span class="p">)</span>

    <span class="c1"># Change ref_doc_kv_pairs</span>
    <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_doc_metadatas</span><span class="p">(</span><span class="n">ref_doc_kv_pairs</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
        <span class="n">node_kv_pairs</span><span class="p">,</span>
        <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_collection</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
        <span class="n">metadata_kv_pairs</span><span class="p">,</span>
        <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put_all</span><span class="p">(</span>
        <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
        <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### async\_add\_documents `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.async_add_documents "Permanent link")

```
async_add_documents(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], allow_update: bool = True, batch_size: Optional[int] = None, store_text: bool = True) -> None
```

Add documents to the store.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">211</span>
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
<span class="normal">246</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add documents to the store."""</span>
    <span class="n">batch_size</span> <span class="o">=</span> <span class="n">batch_size</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span>

    <span class="p">(</span>
        <span class="n">node_kv_pairs</span><span class="p">,</span>
        <span class="n">metadata_kv_pairs</span><span class="p">,</span>
        <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">=</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_async_prepare_kv_pairs</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">allow_update</span><span class="p">,</span> <span class="n">store_text</span><span class="p">)</span>

    <span class="c1"># Change ref_doc_kv_pairs</span>
    <span class="n">ref_doc_kv_pairs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_doc_metadatas</span><span class="p">(</span><span class="n">ref_doc_kv_pairs</span><span class="p">)</span>

    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
            <span class="n">node_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
            <span class="n">metadata_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aput_all</span><span class="p">(</span>
            <span class="n">ref_doc_kv_pairs</span><span class="p">,</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_ref\_doc\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.get_ref_doc_info "Permanent link")

```
get_ref_doc_info(ref_doc_id: str) -> Optional[[RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Get the RefDocInfo for a given ref\_doc\_id.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">248</span>
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
<span class="normal">270</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
    <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">' and ref_doc_id eq '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
        <span class="n">select</span><span class="o">=</span><span class="s2">"RowKey"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">]</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">node_ids</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="n">doc_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
        <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
    <span class="p">)</span>

    <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_ids"</span><span class="p">:</span> <span class="n">node_ids</span><span class="p">,</span>
        <span class="s2">"metadata"</span><span class="p">:</span> <span class="n">doc_metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
    <span class="p">}</span>

    <span class="c1"># TODO: deprecated legacy support</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget\_ref\_doc\_info `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.aget_ref_doc_info "Permanent link")

```
aget_ref_doc_info(ref_doc_id: str) -> Optional[[RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Get the RefDocInfo for a given ref\_doc\_id.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">272</span>
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
<span class="normal">295</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
    <span class="n">ref_doc_infos</span><span class="p">,</span> <span class="n">doc_metadata</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">' and ref_doc_id eq '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
            <span class="n">select</span><span class="o">=</span><span class="s2">"RowKey"</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aget</span><span class="p">(</span>
            <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_doc_metadata_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
        <span class="p">),</span>
    <span class="p">)</span>

    <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">]</span> <span class="k">async</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">]</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">node_ids</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_ids"</span><span class="p">:</span> <span class="n">node_ids</span><span class="p">,</span>
        <span class="s2">"metadata"</span><span class="p">:</span> <span class="n">doc_metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
    <span class="p">}</span>

    <span class="c1"># TODO: deprecated legacy support</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_all\_ref\_doc\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.get_all_ref_doc_info "Permanent link")

```
get_all_ref_doc_info() -> Optional[Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]]
```

Get a mapping of ref\_doc\_id -> RefDocInfo for all ingested documents.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">297</span>
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
<span class="normal">323</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents.</span>
<span class="sd">    """</span>
    <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
        <span class="n">select</span><span class="o">=</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">,</span> <span class="s2">"ref_doc_id"</span><span class="p">],</span>
    <span class="p">)</span>

    <span class="c1"># TODO: deprecated legacy support</span>
    <span class="n">all_ref_doc_infos</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="p">{</span><span class="s2">"node_ids"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"metadata"</span><span class="p">:</span> <span class="kc">None</span><span class="p">})</span>
    <span class="k">for</span> <span class="n">ref_doc_info</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">:</span>
        <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"ref_doc_id"</span><span class="p">]</span>
        <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span>
        <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"node_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">])</span>

        <span class="k">if</span> <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">ref_doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
            <span class="p">)</span>
            <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">ref_doc_info_dict</span> <span class="ow">in</span> <span class="n">all_ref_doc_infos</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">all_ref_doc_infos</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all\_ref\_doc\_info `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/#llama_index.storage.docstore.azure.AzureDocumentStore.aget_all_ref_doc_info "Permanent link")

```
aget_all_ref_doc_info() -> Optional[Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]]
```

Get a mapping of ref\_doc\_id -> RefDocInfo for all ingested documents.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-azure/llama_index/storage/docstore/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">325</span>
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
<span class="normal">351</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents.</span>
<span class="sd">    """</span>
    <span class="n">ref_doc_infos</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"PartitionKey eq '</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">partition_key</span><span class="si">}</span><span class="s2">'"</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_collection</span><span class="p">,</span>
        <span class="n">select</span><span class="o">=</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">,</span> <span class="s2">"ref_doc_id"</span><span class="p">],</span>
    <span class="p">)</span>

    <span class="c1"># TODO: deprecated legacy support</span>
    <span class="n">all_ref_doc_infos</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="p">{</span><span class="s2">"node_ids"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"metadata"</span><span class="p">:</span> <span class="kc">None</span><span class="p">})</span>
    <span class="k">async</span> <span class="k">for</span> <span class="n">ref_doc_info</span> <span class="ow">in</span> <span class="n">ref_doc_infos</span><span class="p">:</span>
        <span class="n">ref_doc_id</span> <span class="o">=</span> <span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"ref_doc_id"</span><span class="p">]</span>
        <span class="n">ref_doc_info_dict</span> <span class="o">=</span> <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span>
        <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"node_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ref_doc_info</span><span class="p">[</span><span class="s2">"RowKey"</span><span class="p">])</span>

        <span class="k">if</span> <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">ref_doc</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">aget</span><span class="p">(</span>
                <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_ref_doc_collection</span><span class="p">,</span> <span class="n">select</span><span class="o">=</span><span class="s2">"metadata"</span>
            <span class="p">)</span>
            <span class="n">ref_doc_info_dict</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">ref_doc_info_dict</span> <span class="ow">in</span> <span class="n">all_ref_doc_infos</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">all_ref_doc_infos</span><span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_legacy_info</span><span class="p">(</span><span class="n">ref_doc_info_dict</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">all_ref_doc_infos</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/)[Next Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/)
