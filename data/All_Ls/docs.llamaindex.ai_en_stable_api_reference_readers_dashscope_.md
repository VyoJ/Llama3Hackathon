Title: Dashscope - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/

Markdown Content:
Dashscope - LlamaIndex


DashScopeParse [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

A smart-parser for files.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 38</span>
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
<span class="normal">432</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DashScopeParse</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A smart-parser for files."""</span>

    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The API key for the DashScope API."</span><span class="p">)</span>
    <span class="n">workspace_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The Workspace  for the DashScope API.If not set, "</span>
        <span class="s2">"it will use the default workspace."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">category_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DASHSCOPE_DEFAULT_DC_CATEGORY</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The dc category for the DashScope API.If not set, "</span>
        <span class="s2">"it will use the default dc category."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DASHSCOPE_DEFAULT_BASE_URL</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The base URL of the DashScope Parsing API."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n">ResultType</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">ResultType</span><span class="o">.</span><span class="n">DASHSCOPE_DOCMIND</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The result type for the parser."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">lt</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of workers to use sending API requests for parsing."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">check_interval</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The interval in seconds to check if the parsing is done."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">max_timeout</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The maximum timeout in seconds to wait for the parsing to finish."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to print the progress of the parsing."</span>
    <span class="p">)</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Show progress when parsing multiple files."</span>
    <span class="p">)</span>
    <span class="n">ignore_errors</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Whether or not to ignore and skip errors raised during parsing."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">parse_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Whether or not to return parsed text content."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_api_key</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate the API key."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">os</span>

            <span class="n">api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"The API key [DASHSCOPE_API_KEY] is required."</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">api_key</span>

        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"workspace_id"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_workspace_id</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate the Workspace."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">os</span>

            <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_WORKSPACE_ID"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"category_id"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_category_id</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate the category."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">os</span>

            <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_CATEGORY_ID"</span><span class="p">,</span> <span class="n">DASHSCOPE_DEFAULT_DC_CATEGORY</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"base_url"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_base_url</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate the base URL."""</span>
        <span class="k">if</span> <span class="n">v</span> <span class="ow">and</span> <span class="n">v</span> <span class="o">!=</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">v</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">url</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_BASE_URL"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                <span class="ow">or</span> <span class="s2">"https://dashscope.aliyuncs.com"</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">url</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">((</span><span class="s2">"http://"</span><span class="p">,</span> <span class="s2">"https://"</span><span class="p">)):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"The DASHSCOPE_BASE_URL must start with http or https. "</span>
                <span class="p">)</span>
            <span class="k">return</span> <span class="n">url</span> <span class="ow">or</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span>

    <span class="k">def</span> <span class="nf">_get_dashscope_header</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"X-DashScope-WorkSpace"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">workspace_id</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"X-DashScope-OpenAPISource"</span><span class="p">:</span> <span class="s2">"CloudSDK"</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="c1"># upload a document and get back a job_id</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_create_job</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">file_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
        <span class="n">UploadFileLeaseResult</span><span class="o">.</span><span class="n">is_file_valid</span><span class="p">(</span><span class="n">file_path</span><span class="o">=</span><span class="n">file_path</span><span class="p">)</span>

        <span class="n">headers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_dashscope_header</span><span class="p">()</span>

        <span class="c1"># load data</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">upload_file_lease_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__upload_lease</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">headers</span><span class="p">)</span>

            <span class="n">upload_file_lease_result</span><span class="o">.</span><span class="n">upload</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>

            <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/api/v1/datacenter/category/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">category_id</span><span class="si">}</span><span class="s2">/add_file"</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_timeout</span><span class="p">)</span> <span class="k">as</span> <span class="n">client</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">client</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
                    <span class="n">url</span><span class="p">,</span>
                    <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
                    <span class="n">json</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"lease_id"</span><span class="p">:</span> <span class="n">upload_file_lease_result</span><span class="o">.</span><span class="n">lease_id</span><span class="p">,</span>
                        <span class="s2">"parser"</span><span class="p">:</span> <span class="n">ResultType</span><span class="o">.</span><span class="n">DASHSCOPE_DOCMIND</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="n">add_file_result</span> <span class="o">=</span> <span class="n">dashscope_response_handler</span><span class="p">(</span>
                <span class="n">response</span><span class="p">,</span> <span class="s2">"add_file"</span><span class="p">,</span> <span class="n">AddFileResult</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="n">url</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">add_file_result</span><span class="o">.</span><span class="n">file_id</span>

    <span class="nd">@retry</span><span class="p">(</span>
        <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_delay</span><span class="p">(</span><span class="mi">60</span><span class="p">),</span>
        <span class="n">wait</span><span class="o">=</span><span class="n">wait_exponential</span><span class="p">(</span><span class="n">multiplier</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="nb">max</span><span class="o">=</span><span class="mi">60</span><span class="p">),</span>
        <span class="n">before_sleep</span><span class="o">=</span><span class="n">before_sleep_log</span><span class="p">(</span><span class="n">logger</span><span class="p">,</span> <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">),</span>
        <span class="n">after</span><span class="o">=</span><span class="n">after_log</span><span class="p">(</span><span class="n">logger</span><span class="p">,</span> <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">),</span>
        <span class="n">reraise</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">retry</span><span class="o">=</span><span class="n">retry_if_exception_type</span><span class="p">(</span><span class="n">RetryException</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">__upload_lease</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">,</span> <span class="n">headers</span><span class="p">):</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/api/v1/datacenter/category/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">category_id</span><span class="si">}</span><span class="s2">/upload_lease"</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">httpx</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_timeout</span><span class="p">)</span> <span class="k">as</span> <span class="n">client</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
                    <span class="n">url</span><span class="p">,</span>
                    <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
                    <span class="n">json</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">file_path</span><span class="p">),</span>
                        <span class="s2">"size_bytes"</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">file_path</span><span class="p">),</span>
                        <span class="s2">"content_md5"</span><span class="p">:</span> <span class="n">get_file_md5</span><span class="p">(</span><span class="n">file_path</span><span class="p">),</span>
                    <span class="p">},</span>
                <span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">ConnectTimeout</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Connect timeout"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">ReadTimeout</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Read timeout"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">NetworkError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Network error"</span><span class="p">)</span>

        <span class="n">upload_file_lease_result</span> <span class="o">=</span> <span class="n">dashscope_response_handler</span><span class="p">(</span>
            <span class="n">response</span><span class="p">,</span> <span class="s2">"upload_lease"</span><span class="p">,</span> <span class="n">UploadFileLeaseResult</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="n">url</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> upload lease result: </span><span class="si">{</span><span class="n">upload_file_lease_result</span><span class="o">.</span><span class="n">lease_id</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">upload_file_lease_result</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_get_job_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">data_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="n">result_url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/api/v1/datacenter/category/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">category_id</span><span class="si">}</span><span class="s2">/file/</span><span class="si">{</span><span class="n">data_id</span><span class="si">}</span><span class="s2">/download_lease"</span>
        <span class="n">status_url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/api/v1/datacenter/category/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">category_id</span><span class="si">}</span><span class="s2">/file/</span><span class="si">{</span><span class="n">data_id</span><span class="si">}</span><span class="s2">/query"</span>

        <span class="n">headers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_dashscope_header</span><span class="p">()</span>

        <span class="n">start</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
        <span class="n">tries</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
            <span class="n">tries</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">query_file_result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dashscope_query</span><span class="p">(</span>
                <span class="n">data_id</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">status_url</span>
            <span class="p">)</span>

            <span class="n">status</span> <span class="o">=</span> <span class="n">query_file_result</span><span class="o">.</span><span class="n">status</span>
            <span class="k">if</span> <span class="n">DatahubDataStatusEnum</span><span class="o">.</span><span class="n">PARSE_SUCCESS</span><span class="o">.</span><span class="n">value</span> <span class="o"></span> <span class="n">status</span>
                <span class="ow">or</span> <span class="n">DatahubDataStatusEnum</span><span class="o">.</span><span class="n">INIT</span><span class="o">.</span><span class="n">value</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"."</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

                <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">check_interval</span><span class="p">)</span>

                <span class="k">continue</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Failed to parse the file: </span><span class="si">{</span><span class="n">data_id</span><span class="si">}</span><span class="s2">, status: </span><span class="si">{</span><span class="n">status</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>

    <span class="nd">@retry</span><span class="p">(</span>
        <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_delay</span><span class="p">(</span><span class="mi">60</span><span class="p">),</span>
        <span class="n">wait</span><span class="o">=</span><span class="n">wait_exponential</span><span class="p">(</span><span class="n">multiplier</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="nb">max</span><span class="o">=</span><span class="mi">60</span><span class="p">),</span>
        <span class="n">before_sleep</span><span class="o">=</span><span class="n">before_sleep_log</span><span class="p">(</span><span class="n">logger</span><span class="p">,</span> <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">),</span>
        <span class="n">after</span><span class="o">=</span><span class="n">after_log</span><span class="p">(</span><span class="n">logger</span><span class="p">,</span> <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">),</span>
        <span class="n">reraise</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">retry</span><span class="o">=</span><span class="n">retry_if_exception_type</span><span class="p">(</span><span class="n">RetryException</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_dashscope_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data_id</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">status_url</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_timeout</span><span class="p">)</span> <span class="k">as</span> <span class="n">client</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">client</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
                    <span class="n">status_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"file_id"</span><span class="p">:</span> <span class="n">data_id</span><span class="p">}</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">dashscope_response_handler</span><span class="p">(</span>
                    <span class="n">response</span><span class="p">,</span> <span class="s2">"query"</span><span class="p">,</span> <span class="n">QueryFileResult</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="n">status_url</span>
                <span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">ConnectTimeout</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Connect timeout"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">ReadTimeout</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Read timeout"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">httpx</span><span class="o">.</span><span class="n">NetworkError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">RetryException</span><span class="p">(</span><span class="s2">"Network error"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aload_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input path."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">data_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_job</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Started parsing the file [</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">] under [</span><span class="si">{</span><span class="n">data_id</span><span class="si">}</span><span class="s2">]"</span><span class="p">)</span>

            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_job_result</span><span class="p">(</span>
                <span class="n">data_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_type</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span>
            <span class="p">)</span>

            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">result_type</span><span class="o">.</span><span class="n">value</span><span class="p">],</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
            <span class="n">document</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="n">data_id</span>

            <span class="k">return</span> <span class="p">[</span><span class="n">document</span><span class="p">]</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error while parsing the file '</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">':</span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ignore_errors</span><span class="p">:</span>
                <span class="k">return</span> <span class="p">[]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input path."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Path</span><span class="p">)):</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aload_data</span><span class="p">(</span>
                <span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="n">jobs</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_aload_data</span><span class="p">(</span>
                    <span class="n">f</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
                    <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">file_path</span>
            <span class="p">]</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                    <span class="n">jobs</span><span class="p">,</span>
                    <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
                    <span class="n">desc</span><span class="o">=</span><span class="s2">"Parsing files"</span><span class="p">,</span>
                    <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="c1"># return flattened results</span>
                <span class="k">return</span> <span class="p">[</span><span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">results</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span><span class="p">]</span>
            <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"The input file_path must be a string or a list of strings."</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"parse_fmt_type"</span><span class="p">:</span> <span class="n">ResultType</span><span class="o">.</span><span class="n">DASHSCOPE_DOCMIND</span><span class="o">.</span><span class="n">value</span><span class="p">}</span>
<span class="w">        </span><span class="sd">"""Load data from the input path."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aload_data</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input path."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">job_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_job</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Started parsing the file under job_id </span><span class="si">%s</span><span class="s2">"</span> <span class="o">%</span> <span class="n">job_id</span><span class="p">)</span>

            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_job_result</span><span class="p">(</span>
                <span class="n">job_id</span><span class="p">,</span> <span class="n">ResultType</span><span class="o">.</span><span class="n">DASHSCOPE_DOCMIND</span><span class="o">.</span><span class="n">value</span>
            <span class="p">)</span>
            <span class="n">result</span><span class="p">[</span><span class="s2">"job_id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">job_id</span>
            <span class="n">result</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">=</span> <span class="n">file_path</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error while parsing the file '</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">':"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ignore_errors</span><span class="p">:</span>
                <span class="k">return</span> <span class="p">[]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input path."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Path</span><span class="p">)):</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_json</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="n">jobs</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_json</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">file_path</span><span class="p">]</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                    <span class="n">jobs</span><span class="p">,</span>
                    <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
                    <span class="n">desc</span><span class="o">=</span><span class="s2">"Parsing files"</span><span class="p">,</span>
                    <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="c1"># return flattened results</span>
                <span class="k">return</span> <span class="p">[</span><span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">results</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span><span class="p">]</span>
            <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"The input file_path must be a string or a list of strings."</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_json_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"parse_fmt_type"</span><span class="p">:</span> <span class="n">ResultType</span><span class="o">.</span><span class="n">DASHSCOPE_DOCMIND</span><span class="o">.</span><span class="n">value</span><span class="p">}</span>
<span class="w">        </span><span class="sd">"""Parse the input path."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aget_json</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">get_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">json_result</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">],</span> <span class="n">download_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### validate\_api\_key [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.validate_api_key "Permanent link")

```
validate_api_key(v: str) -> str
```

Validate the API key.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 89</span>
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
<span class="normal">100</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_api_key</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate the API key."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="n">api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"The API key [DASHSCOPE_API_KEY] is required."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">api_key</span>

    <span class="k">return</span> <span class="n">v</span>
</code></pre></div></td></tr></tbody></table>

### validate\_workspace\_id [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.validate_workspace_id "Permanent link")

```
validate_workspace_id(v: str) -> str
```

Validate the Workspace.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"workspace_id"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_workspace_id</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate the Workspace."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_WORKSPACE_ID"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">v</span>
</code></pre></div></td></tr></tbody></table>

### validate\_category\_id [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.validate_category_id "Permanent link")

```
validate_category_id(v: str) -> str
```

Validate the category.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"category_id"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_category_id</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate the category."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_CATEGORY_ID"</span><span class="p">,</span> <span class="n">DASHSCOPE_DEFAULT_DC_CATEGORY</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">v</span>
</code></pre></div></td></tr></tbody></table>

### validate\_base\_url [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.validate_base_url "Permanent link")

```
validate_base_url(v: str) -> str
```

Validate the base URL.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
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
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"base_url"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">always</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_base_url</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate the base URL."""</span>
    <span class="k">if</span> <span class="n">v</span> <span class="ow">and</span> <span class="n">v</span> <span class="o">!=</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">v</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_BASE_URL"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="ow">or</span> <span class="s2">"https://dashscope.aliyuncs.com"</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">url</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">((</span><span class="s2">"http://"</span><span class="p">,</span> <span class="s2">"https://"</span><span class="p">)):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"The DASHSCOPE_BASE_URL must start with http or https. "</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">url</span> <span class="ow">or</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span>
</code></pre></div></td></tr></tbody></table>

### aload\_data `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.aload_data "Permanent link")

```
aload_data(file_path: Union[List[str], str], extra_info: Optional[dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input path.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">317</span>
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
<span class="normal">352</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input path."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Path</span><span class="p">)):</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aload_data</span><span class="p">(</span>
            <span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">jobs</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_aload_data</span><span class="p">(</span>
                <span class="n">f</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">file_path</span>
        <span class="p">]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                <span class="n">jobs</span><span class="p">,</span>
                <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
                <span class="n">desc</span><span class="o">=</span><span class="s2">"Parsing files"</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># return flattened results</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">results</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"The input file_path must be a string or a list of strings."</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget\_json `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/#llama_index.readers.dashscope.DashScopeParse.aget_json "Permanent link")

```
aget_json(file_path: Union[List[str], str], extra_info: Optional[dict] = None) -> List[dict]
```

Load data from the input path.

Source code in `llama-index-integrations/readers/llama-index-readers-dashscope/llama_index/readers/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">390</span>
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
<span class="normal">416</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_json</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input path."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Path</span><span class="p">)):</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_json</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">jobs</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_json</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">file_path</span><span class="p">]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                <span class="n">jobs</span><span class="p">,</span>
                <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
                <span class="n">desc</span><span class="o">=</span><span class="s2">"Parsing files"</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># return flattened results</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">results</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">nest_asyncio_err</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">nest_asyncio_msg</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"The input file_path must be a string or a list of strings."</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dad jokes](https://docs.llamaindex.ai/en/stable/api_reference/readers/dad_jokes/)[Next Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/)
