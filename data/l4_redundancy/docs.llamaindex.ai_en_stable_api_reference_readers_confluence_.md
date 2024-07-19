Title: Confluence - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/

Markdown Content:
Confluence - LlamaIndex


ConfluenceReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/#llama_index.readers.confluence.ConfluenceReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Confluence reader.

Reads a set of confluence pages given a space key and optionally a list of page ids

For more on OAuth login, checkout: - https://atlassian-python-api.readthedocs.io/index.html - https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `oauth2` | `dict` | 
Atlassian OAuth 2.0, minimum fields are `client_id` and `token`, where `token` is a dict and must at least contain "access\_token" and "token\_type".



 | `None` |
| `base_url` | `str` | 

'base\_url' for confluence cloud instance, this is suffixed with '/wiki', eg 'https://yoursite.atlassian.com/wiki'



 | `None` |
| `cloud` | `bool` | 

connecting to Confluence Cloud or self-hosted instance



 | `True` |
| `api_token` | `str` | 

Confluence API token, see https://confluence.atlassian.com/cloud/api-tokens-938839638.html



 | `None` |
| `user_name` | `str` | 

Confluence username, used for basic auth. Must be used with `password`.



 | `None` |
| `password` | `str` | 

Confluence password, used for basic auth. Must be used with `user_name`.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-confluence/llama_index/readers/confluence/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ConfluenceReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Confluence reader.</span>

<span class="sd">    Reads a set of confluence pages given a space key and optionally a list of page ids</span>

<span class="sd">    For more on OAuth login, checkout:</span>
<span class="sd">        - https://atlassian-python-api.readthedocs.io/index.html</span>
<span class="sd">        - https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/</span>

<span class="sd">    Args:</span>
<span class="sd">        oauth2 (dict): Atlassian OAuth 2.0, minimum fields are `client_id` and `token`, where `token` is a dict and must at least contain "access_token" and "token_type".</span>
<span class="sd">        base_url (str): 'base_url' for confluence cloud instance, this is suffixed with '/wiki', eg 'https://yoursite.atlassian.com/wiki'</span>
<span class="sd">        cloud (bool): connecting to Confluence Cloud or self-hosted instance</span>
<span class="sd">        api_token (str): Confluence API token, see https://confluence.atlassian.com/cloud/api-tokens-938839638.html</span>
<span class="sd">        user_name (str): Confluence username, used for basic auth. Must be used with `password`.</span>
<span class="sd">        password (str): Confluence password, used for basic auth. Must be used with `user_name`.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">oauth2</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cloud</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">api_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">base_url</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide `base_url`"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">base_url</span> <span class="o">=</span> <span class="n">base_url</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">atlassian</span> <span class="kn">import</span> <span class="n">Confluence</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`atlassian` package not found, please run `pip install"</span>
                <span class="s2">" atlassian-python-api`"</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="p">:</span> <span class="n">Confluence</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">oauth2</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span> <span class="o">=</span> <span class="n">Confluence</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">oauth2</span><span class="o">=</span><span class="n">oauth2</span><span class="p">,</span> <span class="n">cloud</span><span class="o">=</span><span class="n">cloud</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">api_token</span> <span class="o">=</span> <span class="n">api_token</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="n">CONFLUENCE_API_TOKEN</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">api_token</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span> <span class="o">=</span> <span class="n">Confluence</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="n">api_token</span><span class="p">,</span> <span class="n">cloud</span><span class="o">=</span><span class="n">cloud</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">user_name</span> <span class="o">=</span> <span class="n">user_name</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="n">CONFLUENCE_USERNAME</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">user_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"Must set environment variable `CONFLUENCE_USERNAME` if oauth,"</span>
                        <span class="s2">" oauth2, or `CONFLUENCE_API_TOKEN` are not provided."</span>
                    <span class="p">)</span>
                <span class="n">password</span> <span class="o">=</span> <span class="n">password</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="n">CONFLUENCE_PASSWORD</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">password</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"Must set environment variable `CONFLUENCE_PASSWORD` if oauth,"</span>
                        <span class="s2">" oauth2, or `CONFLUENCE_API_TOKEN` are not provided."</span>
                    <span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span> <span class="o">=</span> <span class="n">Confluence</span><span class="p">(</span>
                    <span class="n">url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">username</span><span class="o">=</span><span class="n">user_name</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">,</span> <span class="n">cloud</span><span class="o">=</span><span class="n">cloud</span>
                <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_next_cursor</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">space_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">page_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">page_status</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">label</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cql</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_attachments</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">include_children</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">start</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cursor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load Confluence pages from Confluence, specifying by one of four mutually exclusive methods:</span>
<span class="sd">        `space_key`, `page_ids`, `label`, or `cql`</span>
<span class="sd">        (Confluence Query Language https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/ ).</span>

<span class="sd">        Args:</span>
<span class="sd">            space_key (str): Confluence space key, eg 'DS'</span>
<span class="sd">            page_ids (list): List of page ids, eg ['123456', '123457']</span>
<span class="sd">            page_status (str): Page status, one of None (all statuses), 'current', 'draft', 'archived'.  Only compatible with space_key.</span>
<span class="sd">            label (str): Confluence label, eg 'my-label'</span>
<span class="sd">            cql (str): Confluence Query Language query, eg 'label="my-label"'</span>
<span class="sd">            include_attachments (bool): If True, include attachments.</span>
<span class="sd">            include_children (bool): If True, do a DFS of the descendants of each page_id in `page_ids`.  Only compatible with `page_ids`.</span>
<span class="sd">            start (int): Skips over the first n elements. Used only with space_key</span>
<span class="sd">            cursor (str): Skips to the cursor. Used with cql and label, set when the max limit has been hit for cql based search</span>
<span class="sd">            limit (int): Deprecated, use `max_num_results` instead.</span>
<span class="sd">            max_num_results (int): Maximum number of results to return.  If None, return all results.  Requests are made in batches to achieve the desired number of results.</span>
<span class="sd">        """</span>
        <span class="n">num_space_key_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">space_key</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="n">num_page_ids_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">page_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="n">num_label_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">label</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="n">num_cql_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">cql</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">num_space_key_parameter</span>
            <span class="o">+</span> <span class="n">num_page_ids_parameter</span>
            <span class="o">+</span> <span class="n">num_label_parameter</span>
            <span class="o">+</span> <span class="n">num_cql_parameter</span>
            <span class="o">!=</span> <span class="mi">1</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Must specify exactly one among `space_key`, `page_ids`, `label`, `cql`"</span>
                <span class="s2">" parameters."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">cursor</span> <span class="ow">and</span> <span class="n">start</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must not specify `start` when `cursor` is specified"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">space_key</span> <span class="ow">and</span> <span class="n">cursor</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must not specify `cursor` when `space_key` is specified"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">page_status</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">space_key</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Must specify `space_key` when `page_status` is specified."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">include_children</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">page_ids</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Must specify `page_ids` when `include_children` is specified."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">limit</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">max_num_results</span> <span class="o">=</span> <span class="n">limit</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"`limit` is deprecated and no longer relates to the Confluence server's"</span>
                <span class="s2">" API limits.  If you wish to limit the number of returned results"</span>
                <span class="s2">" please use `max_num_results` instead."</span>
            <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">html2text</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`html2text` package not found, please run `pip install html2text`"</span>
            <span class="p">)</span>

        <span class="n">text_maker</span> <span class="o">=</span> <span class="n">html2text</span><span class="o">.</span><span class="n">HTML2Text</span><span class="p">()</span>
        <span class="n">text_maker</span><span class="o">.</span><span class="n">ignore_links</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="n">text_maker</span><span class="o">.</span><span class="n">ignore_images</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">start</span><span class="p">:</span>
            <span class="n">start</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="n">pages</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">space_key</span><span class="p">:</span>
            <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_paging</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">get_all_pages_from_space</span><span class="p">,</span>
                    <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                    <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                    <span class="n">space</span><span class="o">=</span><span class="n">space_key</span><span class="p">,</span>
                    <span class="n">status</span><span class="o">=</span><span class="n">page_status</span><span class="p">,</span>
                    <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                    <span class="n">content_type</span><span class="o">=</span><span class="s2">"page"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">label</span><span class="p">:</span>
            <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_get_cql_data_with_paging</span><span class="p">(</span>
                    <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                    <span class="n">cursor</span><span class="o">=</span><span class="n">cursor</span><span class="p">,</span>
                    <span class="n">cql</span><span class="o">=</span><span class="sa">f</span><span class="s1">'type="page" AND label="</span><span class="si">{</span><span class="n">label</span><span class="si">}</span><span class="s1">"'</span><span class="p">,</span>
                    <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                    <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">cql</span><span class="p">:</span>
            <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_get_cql_data_with_paging</span><span class="p">(</span>
                    <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                    <span class="n">cursor</span><span class="o">=</span><span class="n">cursor</span><span class="p">,</span>
                    <span class="n">cql</span><span class="o">=</span><span class="n">cql</span><span class="p">,</span>
                    <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                    <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">page_ids</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">include_children</span><span class="p">:</span>
                <span class="n">dfs_page_ids</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="n">max_num_remaining</span> <span class="o">=</span> <span class="n">max_num_results</span>
                <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
                    <span class="n">current_dfs_page_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dfs_page_ids</span><span class="p">(</span>
                        <span class="n">page_id</span><span class="p">,</span> <span class="n">max_num_remaining</span>
                    <span class="p">)</span>
                    <span class="n">dfs_page_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">current_dfs_page_ids</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">max_num_remaining</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_dfs_page_ids</span><span class="p">)</span>
                        <span class="k">if</span> <span class="n">max_num_remaining</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
                            <span class="k">break</span>
                <span class="n">page_ids</span> <span class="o">=</span> <span class="n">dfs_page_ids</span>
            <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="p">(</span>
                <span class="n">page_ids</span><span class="p">[:</span><span class="n">max_num_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">page_ids</span>
            <span class="p">):</span>
                <span class="n">pages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_retry</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">get_page_by_id</span><span class="p">,</span>
                        <span class="n">page_id</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span>
                        <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">:</span>
            <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_page</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">include_attachments</span><span class="p">,</span> <span class="n">text_maker</span><span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">_dfs_page_ids</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page_id</span><span class="p">,</span> <span class="n">max_num_results</span><span class="p">):</span>
        <span class="n">ret</span> <span class="o">=</span> <span class="p">[</span><span class="n">page_id</span><span class="p">]</span>
        <span class="n">max_num_remaining</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">(</span><span class="n">max_num_results</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">max_num_remaining</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ret</span>

        <span class="n">child_page_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_paging</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">get_child_id_list</span><span class="p">,</span>
            <span class="n">page_id</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">"page"</span><span class="p">,</span>
            <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_remaining</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">child_page_id</span> <span class="ow">in</span> <span class="n">child_page_ids</span><span class="p">:</span>
            <span class="n">dfs_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dfs_page_ids</span><span class="p">(</span><span class="n">child_page_id</span><span class="p">,</span> <span class="n">max_num_remaining</span><span class="p">)</span>
            <span class="n">ret</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">dfs_ids</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">max_num_remaining</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="n">dfs_ids</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">max_num_remaining</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="k">break</span>
        <span class="k">return</span> <span class="n">ret</span>

    <span class="k">def</span> <span class="nf">_get_data_with_paging</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">paged_function</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">max_num_results</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">):</span>
        <span class="n">max_num_remaining</span> <span class="o">=</span> <span class="n">max_num_results</span>
        <span class="n">ret</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_retry</span><span class="p">(</span>
                <span class="n">paged_function</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">max_num_remaining</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
            <span class="n">ret</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="nb">len</span><span class="p">(</span><span class="n">results</span><span class="p">)</span> <span class="o"></span> <span class="s2">"application/pdf"</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing PDF attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pdf</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="p">(</span>
                <span class="n">media_type</span> <span class="o"></span> <span class="s2">"image/jpg"</span>
                <span class="ow">or</span> <span class="n">media_type</span> <span class="o"></span> <span class="s2">"image/webp"</span>
            <span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing image attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_image</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="p">(</span>
                <span class="n">media_type</span>
                <span class="o"></span> <span class="s2">"application/vnd.ms-excel"</span>
                <span class="ow">or</span> <span class="n">media_type</span>
                <span class="o"></span> <span class="s2">"application/vnd.ms-excel.sheet.macroenabled.12"</span>
            <span class="p">):</span>
                <span class="k">if</span> <span class="n">title</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".csv"</span><span class="p">)</span> <span class="ow">or</span> <span class="n">absolute_url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".csv"</span><span class="p">):</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing CSV attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_csv</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing XLS attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_xls</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">media_type</span> <span class="o"></span> <span class="s2">"text/csv"</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing CSV attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_csv</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">media_type</span> <span class="o"></span> <span class="s2">"text/html"</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"  Processing HTML attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_html</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">media_type</span> <span class="o"></span> <span class="s2">"image/svg+xml"</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Processing SVG attachment "</span> <span class="o">+</span> <span class="n">absolute_url</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_svg</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="p">(</span>
                <span class="n">media_type</span>
                <span class="o"></span> <span class="s2">"application/vnd.ms-powerpoint.presentation.macroenabled.12"</span>
            <span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                    <span class="s2">"Processing PowerPoint attachment "</span>
                    <span class="o">+</span> <span class="n">absolute_url</span>
                    <span class="o">+</span> <span class="s2">" ("</span>
                    <span class="o">+</span> <span class="n">media_type</span>
                    <span class="o">+</span> <span class="s2">")"</span>
                <span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_ppt</span><span class="p">(</span><span class="n">absolute_url</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Skipping unsupported attachment </span><span class="si">{</span><span class="n">absolute_url</span><span class="si">}</span><span class="s2"> of media_type </span><span class="si">{</span><span class="n">media_type</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
                <span class="k">continue</span>
            <span class="n">texts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">texts</span>

    <span class="k">def</span> <span class="nf">process_pdf</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">link</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pytesseract</span>  <span class="c1"># type: ignore</span>
            <span class="kn">from</span> <span class="nn">pdf2image</span> <span class="kn">import</span> <span class="n">convert_from_bytes</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`pytesseract` or `pdf2image` package not found, please run `pip"</span>
                <span class="s2">" install pytesseract pdf2image`"</span>
            <span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">link</span><span class="p">,</span> <span class="n">absolute</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="o"></span> <span class="mi">200</span> <span class="ow">and</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">pytesseract</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
                    <span class="c1"># Handle errors that occur while opening or processing the image</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Error processing image at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: Unable to open or read the image content."</span>
                    <span class="p">)</span>
                    <span class="k">return</span> <span class="n">text</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Log non-200 responses here if needed</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Error fetching image at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: HTTP status code </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">."</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">text</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># This catches any Requests-related exceptions, including HTTPError, ConnectionError, etc.</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Request error while fetching image at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">text</span>

        <span class="k">return</span> <span class="n">text</span>

    <span class="k">def</span> <span class="nf">process_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">link</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>
            <span class="kn">import</span> <span class="nn">docx2txt</span>
            <span class="kn">import</span> <span class="nn">zipfile</span>  <span class="c1"># Import zipfile to catch BadZipFile exceptions</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`docx2txt` package not found, please run `pip install docx2txt`"</span>
            <span class="p">)</span>

        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">link</span><span class="p">,</span> <span class="n">absolute</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span> <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="ow">in</span> <span class="p">[</span><span class="sa">b</span><span class="s2">""</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Error fetching document at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: HTTP status code </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">."</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">text</span>

            <span class="n">file_data</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">file_data</span><span class="p">)</span>
            <span class="k">except</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">BadZipFile</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Error processing Word document at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: File is not a zip file."</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">text</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unexpected error processing document at </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">text</span>

        <span class="k">return</span> <span class="n">text</span>

    <span class="k">def</span> <span class="nf">process_ppt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">link</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>
            <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`python-pptx` package not found, please run `pip install python-pptx`"</span>
            <span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">link</span><span class="p">,</span> <span class="n">absolute</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="o"></span> <span class="sa">b</span><span class="s2">""</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="n">text</span>

        <span class="n">file_data</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

        <span class="c1"># Try to read the Excel file</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># Use pandas to read all sheets; returns a dict of DataFrame</span>
            <span class="n">sheets</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file_data</span><span class="p">,</span> <span class="n">sheet_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">engine</span><span class="o">=</span><span class="s2">"openpyxl"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s2">"Failed to read Excel file: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span>

        <span class="k">for</span> <span class="n">sheet_name</span><span class="p">,</span> <span class="n">sheet_data</span> <span class="ow">in</span> <span class="n">sheets</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sheet_name</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="s2">"</span>
            <span class="k">for</span> <span class="n">row_index</span><span class="p">,</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">sheet_data</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">row</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>

        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">process_xlsb</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">link</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
            <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`pandas` package not found, please run `pip install pandas`"</span>
            <span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">link</span><span class="p">,</span> <span class="n">absolute</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="o"></span> <span class="sa">b</span><span class="s2">""</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="n">text</span>

        <span class="n">file_data</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># Assuming CSV uses default comma delimiter. If delimiter varies, consider detecting it.</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file_data</span><span class="p">,</span> <span class="n">low_memory</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
            <span class="c1"># Convert the DataFrame to a text string, including headers</span>
            <span class="n">text_rows</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
                <span class="n">text_rows</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)))</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_rows</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error processing CSV file: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"Error processing CSV file."</span>

        <span class="k">return</span> <span class="n">text</span>

    <span class="k">def</span> <span class="nf">process_svg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">link</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>  <span class="c1"># type: ignore</span>

            <span class="kn">import</span> <span class="nn">pytesseract</span>  <span class="c1"># type: ignore</span>
            <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># type: ignore</span>
            <span class="kn">from</span> <span class="nn">reportlab.graphics</span> <span class="kn">import</span> <span class="n">renderPM</span>  <span class="c1"># type: ignore</span>
            <span class="kn">from</span> <span class="nn">svglib.svglib</span> <span class="kn">import</span> <span class="n">svg2rlg</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`pytesseract`, `Pillow`, or `svglib` package not found, please run"</span>
                <span class="s2">" `pip install pytesseract Pillow svglib`"</span>
            <span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">link</span><span class="p">,</span> <span class="n">absolute</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="o">==</span> <span class="sa">b</span><span class="s2">""</span>
            <span class="ow">or</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="n">text</span>

        <span class="n">drawing</span> <span class="o">=</span> <span class="n">svg2rlg</span><span class="p">(</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>

        <span class="n">img_data</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">()</span>
        <span class="n">renderPM</span><span class="o">.</span><span class="n">drawToFile</span><span class="p">(</span><span class="n">drawing</span><span class="p">,</span> <span class="n">img_data</span><span class="p">,</span> <span class="n">fmt</span><span class="o">=</span><span class="s2">"PNG"</span><span class="p">)</span>
        <span class="n">img_data</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">img_data</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">pytesseract</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/#llama_index.readers.confluence.ConfluenceReader.load_data "Permanent link")

```
load_data(space_key: Optional[str] = None, page_ids: Optional[List[str]] = None, page_status: Optional[str] = None, label: Optional[str] = None, cql: Optional[str] = None, include_attachments=False, include_children=False, start: Optional[int] = None, cursor: Optional[str] = None, limit: Optional[int] = None, max_num_results: Optional[int] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load Confluence pages from Confluence, specifying by one of four mutually exclusive methods: `space_key`, `page_ids`, `label`, or `cql` (Confluence Query Language https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/ ).

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `space_key` | `str` | 
Confluence space key, eg 'DS'



 | `None` |
| `page_ids` | `list` | 

List of page ids, eg \['123456', '123457'\]



 | `None` |
| `page_status` | `str` | 

Page status, one of None (all statuses), 'current', 'draft', 'archived'. Only compatible with space\_key.



 | `None` |
| `label` | `str` | 

Confluence label, eg 'my-label'



 | `None` |
| `cql` | `str` | 

Confluence Query Language query, eg 'label="my-label"'



 | `None` |
| `include_attachments` | `bool` | 

If True, include attachments.



 | `False` |
| `include_children` | `bool` | 

If True, do a DFS of the descendants of each page\_id in `page_ids`. Only compatible with `page_ids`.



 | `False` |
| `start` | `int` | 

Skips over the first n elements. Used only with space\_key



 | `None` |
| `cursor` | `str` | 

Skips to the cursor. Used with cql and label, set when the max limit has been hit for cql based search



 | `None` |
| `limit` | `int` | 

Deprecated, use `max_num_results` instead.



 | `None` |
| `max_num_results` | `int` | 

Maximum number of results to return. If None, return all results. Requests are made in batches to achieve the desired number of results.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-confluence/llama_index/readers/confluence/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 86</span>
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
<span class="normal">234</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">space_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">page_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">page_status</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">label</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cql</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_attachments</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">include_children</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">start</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cursor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load Confluence pages from Confluence, specifying by one of four mutually exclusive methods:</span>
<span class="sd">    `space_key`, `page_ids`, `label`, or `cql`</span>
<span class="sd">    (Confluence Query Language https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/ ).</span>

<span class="sd">    Args:</span>
<span class="sd">        space_key (str): Confluence space key, eg 'DS'</span>
<span class="sd">        page_ids (list): List of page ids, eg ['123456', '123457']</span>
<span class="sd">        page_status (str): Page status, one of None (all statuses), 'current', 'draft', 'archived'.  Only compatible with space_key.</span>
<span class="sd">        label (str): Confluence label, eg 'my-label'</span>
<span class="sd">        cql (str): Confluence Query Language query, eg 'label="my-label"'</span>
<span class="sd">        include_attachments (bool): If True, include attachments.</span>
<span class="sd">        include_children (bool): If True, do a DFS of the descendants of each page_id in `page_ids`.  Only compatible with `page_ids`.</span>
<span class="sd">        start (int): Skips over the first n elements. Used only with space_key</span>
<span class="sd">        cursor (str): Skips to the cursor. Used with cql and label, set when the max limit has been hit for cql based search</span>
<span class="sd">        limit (int): Deprecated, use `max_num_results` instead.</span>
<span class="sd">        max_num_results (int): Maximum number of results to return.  If None, return all results.  Requests are made in batches to achieve the desired number of results.</span>
<span class="sd">    """</span>
    <span class="n">num_space_key_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">space_key</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">num_page_ids_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">page_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">num_label_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">label</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">num_cql_parameter</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">cql</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">num_space_key_parameter</span>
        <span class="o">+</span> <span class="n">num_page_ids_parameter</span>
        <span class="o">+</span> <span class="n">num_label_parameter</span>
        <span class="o">+</span> <span class="n">num_cql_parameter</span>
        <span class="o">!=</span> <span class="mi">1</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Must specify exactly one among `space_key`, `page_ids`, `label`, `cql`"</span>
            <span class="s2">" parameters."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">cursor</span> <span class="ow">and</span> <span class="n">start</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must not specify `start` when `cursor` is specified"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">space_key</span> <span class="ow">and</span> <span class="n">cursor</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must not specify `cursor` when `space_key` is specified"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">page_status</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">space_key</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Must specify `space_key` when `page_status` is specified."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">include_children</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">page_ids</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Must specify `page_ids` when `include_children` is specified."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">limit</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">max_num_results</span> <span class="o">=</span> <span class="n">limit</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"`limit` is deprecated and no longer relates to the Confluence server's"</span>
            <span class="s2">" API limits.  If you wish to limit the number of returned results"</span>
            <span class="s2">" please use `max_num_results` instead."</span>
        <span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">html2text</span>  <span class="c1"># type: ignore</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"`html2text` package not found, please run `pip install html2text`"</span>
        <span class="p">)</span>

    <span class="n">text_maker</span> <span class="o">=</span> <span class="n">html2text</span><span class="o">.</span><span class="n">HTML2Text</span><span class="p">()</span>
    <span class="n">text_maker</span><span class="o">.</span><span class="n">ignore_links</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">text_maker</span><span class="o">.</span><span class="n">ignore_images</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">start</span><span class="p">:</span>
        <span class="n">start</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="n">pages</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">space_key</span><span class="p">:</span>
        <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_paging</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">get_all_pages_from_space</span><span class="p">,</span>
                <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                <span class="n">space</span><span class="o">=</span><span class="n">space_key</span><span class="p">,</span>
                <span class="n">status</span><span class="o">=</span><span class="n">page_status</span><span class="p">,</span>
                <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                <span class="n">content_type</span><span class="o">=</span><span class="s2">"page"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">label</span><span class="p">:</span>
        <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_cql_data_with_paging</span><span class="p">(</span>
                <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                <span class="n">cursor</span><span class="o">=</span><span class="n">cursor</span><span class="p">,</span>
                <span class="n">cql</span><span class="o">=</span><span class="sa">f</span><span class="s1">'type="page" AND label="</span><span class="si">{</span><span class="n">label</span><span class="si">}</span><span class="s1">"'</span><span class="p">,</span>
                <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">cql</span><span class="p">:</span>
        <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_cql_data_with_paging</span><span class="p">(</span>
                <span class="n">start</span><span class="o">=</span><span class="n">start</span><span class="p">,</span>
                <span class="n">cursor</span><span class="o">=</span><span class="n">cursor</span><span class="p">,</span>
                <span class="n">cql</span><span class="o">=</span><span class="n">cql</span><span class="p">,</span>
                <span class="n">max_num_results</span><span class="o">=</span><span class="n">max_num_results</span><span class="p">,</span>
                <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">page_ids</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">include_children</span><span class="p">:</span>
            <span class="n">dfs_page_ids</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">max_num_remaining</span> <span class="o">=</span> <span class="n">max_num_results</span>
            <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
                <span class="n">current_dfs_page_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dfs_page_ids</span><span class="p">(</span>
                    <span class="n">page_id</span><span class="p">,</span> <span class="n">max_num_remaining</span>
                <span class="p">)</span>
                <span class="n">dfs_page_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">current_dfs_page_ids</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">max_num_remaining</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_dfs_page_ids</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">max_num_remaining</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
                        <span class="k">break</span>
            <span class="n">page_ids</span> <span class="o">=</span> <span class="n">dfs_page_ids</span>
        <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="n">page_ids</span><span class="p">[:</span><span class="n">max_num_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">max_num_results</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">page_ids</span>
        <span class="p">):</span>
            <span class="n">pages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_get_data_with_retry</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">confluence</span><span class="o">.</span><span class="n">get_page_by_id</span><span class="p">,</span>
                    <span class="n">page_id</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span>
                    <span class="n">expand</span><span class="o">=</span><span class="s2">"body.export_view.value"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">:</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_page</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">include_attachments</span><span class="p">,</span> <span class="n">text_maker</span><span class="p">)</span>
        <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### get\_next\_cursor [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/#llama_index.readers.confluence.ConfluenceReader.get_next_cursor "Permanent link")

```
get_next_cursor()
```

Returns: The last set cursor from a cql based search.

Source code in `llama-index-integrations/readers/llama-index-readers-confluence/llama_index/readers/confluence/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_next_cursor</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns: The last set cursor from a cql based search.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_cursor</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/)[Next Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/)
