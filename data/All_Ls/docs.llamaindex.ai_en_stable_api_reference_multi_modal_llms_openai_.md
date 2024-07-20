Title: Openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/

Markdown Content:
Openai - LlamaIndex


OpenAIMultiModal [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/#llama_index.multi_modal_llms.openai.OpenAIMultiModal "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MultiModalLLM](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "llama_index.core.multi_modal_llms.MultiModalLLM")`

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-openai/llama_index/multi_modal_llms/openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIMultiModal</span><span class="p">(</span><span class="n">MultiModalLLM</span><span class="p">):</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The Multi-Modal model to use from OpenAI."</span><span class="p">)</span>
    <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The temperature to use for sampling."</span><span class="p">)</span>
    <span class="n">max_new_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">" The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt"</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">context_window</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The maximum number of context tokens for the model."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">image_detail</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The level of details for image in API calls. Can be low, high, or auto"</span>
    <span class="p">)</span>
    <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Maximum number of retries."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mf">60.0</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The timeout, in seconds, for API requests."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The OpenAI API key."</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">api_base</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The base URL for OpenAI API."</span><span class="p">)</span>
    <span class="n">api_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The API version for OpenAI API."</span><span class="p">)</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Additional kwargs for the OpenAI API."</span>
    <span class="p">)</span>
    <span class="n">default_headers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The default headers for API requests."</span>
    <span class="p">)</span>

    <span class="n">_messages_to_prompt</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_completion_to_prompt</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_client</span><span class="p">:</span> <span class="n">SyncOpenAI</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_aclient</span><span class="p">:</span> <span class="n">AsyncOpenAI</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_http_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">httpx</span><span class="o">.</span><span class="n">Client</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">DEFAULT_TEMPERATURE</span><span class="p">,</span>
        <span class="n">max_new_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">300</span><span class="p">,</span>
        <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_window</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_CONTEXT_WINDOW</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">60.0</span><span class="p">,</span>
        <span class="n">image_detail</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"low"</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_base</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_version</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">messages_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">completion_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">default_headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">httpx</span><span class="o">.</span><span class="n">Client</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_messages_to_prompt</span> <span class="o">=</span> <span class="n">messages_to_prompt</span> <span class="ow">or</span> <span class="n">generic_messages_to_prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_completion_to_prompt</span> <span class="o">=</span> <span class="n">completion_to_prompt</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">)</span>
        <span class="n">api_key</span><span class="p">,</span> <span class="n">api_base</span><span class="p">,</span> <span class="n">api_version</span> <span class="o">=</span> <span class="n">resolve_openai_credentials</span><span class="p">(</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">api_base</span><span class="o">=</span><span class="n">api_base</span><span class="p">,</span>
            <span class="n">api_version</span><span class="o">=</span><span class="n">api_version</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">max_new_tokens</span><span class="o">=</span><span class="n">max_new_tokens</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">additional_kwargs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">context_window</span><span class="o">=</span><span class="n">context_window</span><span class="p">,</span>
            <span class="n">image_detail</span><span class="o">=</span><span class="n">image_detail</span><span class="p">,</span>
            <span class="n">max_retries</span><span class="o">=</span><span class="n">max_retries</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">api_base</span><span class="o">=</span><span class="n">api_base</span><span class="p">,</span>
            <span class="n">api_version</span><span class="o">=</span><span class="n">api_version</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">default_headers</span><span class="o">=</span><span class="n">default_headers</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_http_client</span> <span class="o">=</span> <span class="n">http_client</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_clients</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_clients</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">SyncOpenAI</span><span class="p">,</span> <span class="n">AsyncOpenAI</span><span class="p">]:</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">SyncOpenAI</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_credential_kwargs</span><span class="p">())</span>
        <span class="n">aclient</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_credential_kwargs</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">client</span><span class="p">,</span> <span class="n">aclient</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"openai_multi_modal_llm"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Multi Modal LLM metadata."""</span>
        <span class="k">return</span> <span class="n">MultiModalLLMMetadata</span><span class="p">(</span>
            <span class="n">num_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_new_tokens</span> <span class="ow">or</span> <span class="n">DEFAULT_NUM_OUTPUTS</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_credential_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"api_key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="s2">"base_url"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_base</span><span class="p">,</span>
            <span class="s2">"max_retries"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span><span class="p">,</span>
            <span class="s2">"default_headers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_headers</span><span class="p">,</span>
            <span class="s2">"http_client"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_http_client</span><span class="p">,</span>
            <span class="s2">"timeout"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_multi_modal_chat_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">role</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatCompletionMessageParam</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">to_openai_message_dicts</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="n">generate_openai_multi_modal_chat_message</span><span class="p">(</span>
                    <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span>
                    <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span><span class="p">,</span>
                    <span class="n">image_detail</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">image_detail</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="p">)</span>

    <span class="c1"># Model Params for OpenAI GPT4V model.</span>
    <span class="k">def</span> <span class="nf">_get_model_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">GPT4V_MODELS</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Invalid model </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="si">}</span><span class="s2">. "</span>
                <span class="sa">f</span><span class="s2">"Available models are: </span><span class="si">{</span><span class="nb">list</span><span class="p">(</span><span class="n">GPT4V_MODELS</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="n">base_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="s2">"temperature"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">temperature</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_new_tokens</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># If max_tokens is None, don't include in the payload:</span>
            <span class="c1"># https://platform.openai.com/docs/api-reference/chat</span>
            <span class="c1"># https://platform.openai.com/docs/api-reference/completions</span>
            <span class="n">base_kwargs</span><span class="p">[</span><span class="s2">"max_tokens"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_new_tokens</span>
        <span class="k">return</span> <span class="p">{</span><span class="o">**</span><span class="n">base_kwargs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_response_token_counts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raw_response</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the token usage reported by the response."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">raw_response</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="n">usage</span> <span class="o">=</span> <span class="n">raw_response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"usage"</span><span class="p">,</span> <span class="p">{})</span>
        <span class="c1"># NOTE: other model providers that use the OpenAI client may not report usage</span>
        <span class="k">if</span> <span class="n">usage</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"prompt_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"prompt_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
            <span class="s2">"completion_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"completion_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
            <span class="s2">"total_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"total_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
        <span class="p">}</span>

    <span class="nd">@llm_completion_callback</span><span class="p">()</span>
    <span class="k">def</span> <span class="nf">_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">message_dict</span><span class="p">,</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">CompletionResponse</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="nd">@llm_chat_callback</span><span class="p">()</span>
    <span class="k">def</span> <span class="nf">_chat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dicts</span> <span class="o">=</span> <span class="n">to_openai_message_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">message_dicts</span><span class="p">,</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">openai_message</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">message</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">from_openai_message</span><span class="p">(</span><span class="n">openai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="nd">@llm_completion_callback</span><span class="p">()</span>
    <span class="k">def</span> <span class="nf">_stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span>
        <span class="p">)</span>

        <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

            <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">message_dict</span><span class="p">,</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
            <span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ChatCompletionChunk</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">delta</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">ChoiceDelta</span><span class="p">()</span>

                <span class="c1"># update using deltas</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">content_delta</span>

                <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="nd">@llm_chat_callback</span><span class="p">()</span>
    <span class="k">def</span> <span class="nf">_stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
        <span class="n">message_dicts</span> <span class="o">=</span> <span class="n">to_openai_message_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">tool_calls</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChoiceDeltaToolCall</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="n">is_function</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">message_dicts</span><span class="p">,</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
            <span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ChatCompletionChunk</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">delta</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">ChoiceDelta</span><span class="p">()</span>

                <span class="c1"># check if this chunk is the start of a function call</span>
                <span class="k">if</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_calls</span><span class="p">:</span>
                    <span class="n">is_function</span> <span class="o">=</span> <span class="kc">True</span>

                <span class="c1"># update using deltas</span>
                <span class="n">role</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">role</span> <span class="ow">or</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="n">content</span> <span class="o">+=</span> <span class="n">content_delta</span>

                <span class="n">additional_kwargs</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">if</span> <span class="n">is_function</span><span class="p">:</span>
                    <span class="n">tool_calls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_update_tool_calls</span><span class="p">(</span><span class="n">tool_calls</span><span class="p">,</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_calls</span><span class="p">)</span>
                    <span class="n">additional_kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool_calls</span>

                <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
                    <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span>
                        <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
                        <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">additional_kwargs</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chat</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_chat</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="c1"># </span>

    <span class="nd">@llm_completion_callback</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">message_dict</span><span class="p">,</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">CompletionResponse</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_acomplete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@llm_completion_callback</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span>
        <span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

            <span class="k">async</span> <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">message_dict</span><span class="p">,</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
            <span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ChatCompletionChunk</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">delta</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">ChoiceDelta</span><span class="p">()</span>

                <span class="c1"># update using deltas</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">content_delta</span>

                <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="nd">@llm_chat_callback</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">message_dicts</span> <span class="o">=</span> <span class="n">to_openai_message_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">message_dicts</span><span class="p">,</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">all_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">openai_message</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">message</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">from_openai_message</span><span class="p">(</span><span class="n">openai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="nd">@llm_chat_callback</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
        <span class="n">message_dicts</span> <span class="o">=</span> <span class="n">to_openai_message_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">tool_calls</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChoiceDeltaToolCall</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="n">is_function</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">completions</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">message_dicts</span><span class="p">,</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
            <span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ChatCompletionChunk</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">delta</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="n">ChoiceDelta</span><span class="p">()</span>

                <span class="c1"># check if this chunk is the start of a function call</span>
                <span class="k">if</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_calls</span><span class="p">:</span>
                    <span class="n">is_function</span> <span class="o">=</span> <span class="kc">True</span>

                <span class="c1"># update using deltas</span>
                <span class="n">role</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">role</span> <span class="ow">or</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">delta</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="n">content</span> <span class="o">+=</span> <span class="n">content_delta</span>

                <span class="n">additional_kwargs</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">if</span> <span class="n">is_function</span><span class="p">:</span>
                    <span class="n">tool_calls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_update_tool_calls</span><span class="p">(</span><span class="n">tool_calls</span><span class="p">,</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_calls</span><span class="p">)</span>
                    <span class="n">additional_kwargs</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool_calls</span>

                <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
                    <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span>
                        <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
                        <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">additional_kwargs</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">additional_kwargs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_response_token_counts</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_astream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_achat</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_astream_chat</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### metadata `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/#llama_index.multi_modal_llms.openai.OpenAIMultiModal.metadata "Permanent link")

```
metadata: MultiModalLLMMetadata
```

Multi Modal LLM metadata.

Back to top

[Previous Ollama](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/)[Next Replicate](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/)
