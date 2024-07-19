Title: Microsoft sharepoint - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/

Markdown Content:
Microsoft sharepoint - LlamaIndex


SharePointReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/#llama_index.readers.microsoft_sharepoint.SharePointReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`, `ResourcesReaderMixin`, `FileSystemReaderMixin`

SharePoint reader.

Reads folders from the SharePoint site from a folder under documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `client_id` | `str` | 
The Application ID for the app registered in Microsoft Azure Portal. The application must also be configured with MS Graph permissions "Files.ReadAll", "Sites.ReadAll" and BrowserSiteLists.Read.All.



 | _required_ |
| `client_secret` | `str` | 

The application secret for the app registered in Azure.



 | _required_ |
| `tenant_id` | `str` | 

Unique identifier of the Azure Active Directory Instance.



 | _required_ |
| `sharepoint_site_name` | `Optional[str]` | 

The name of the SharePoint site to download from.



 | `None` |
| `sharepoint_folder_path` | `Optional[str]` | 

The path of the SharePoint folder to download from.



 | `None` |
| `sharepoint_folder_id` | `Optional[str]` | 

The ID of the SharePoint folder to download from. Overrides sharepoint\_folder\_path.



 | `None` |
| `drive_name` | `Optional[str]` | 

The name of the drive to download from.



 | `None` |
| `drive_id` | `Optional[str]` | 

The ID of the drive to download from. Overrides drive\_name.



 | `None` |
| `file_extractor` | `Optional[Dict[str, [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")]]` | 

A mapping of file extension to a BaseReader class that specifies how to convert that file to text. See `SimpleDirectoryReader` for more details.



 | `None` |
| `attach_permission_metadata` | `bool` | 

If True, the reader will attach permission metadata to the documents. Set to False if your vector store only supports flat metadata (i.e. no nested fields or lists), or to avoid the additional API calls.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-sharepoint/llama_index/readers/microsoft_sharepoint/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
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
<span class="normal">797</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SharePointReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">,</span> <span class="n">ResourcesReaderMixin</span><span class="p">,</span> <span class="n">FileSystemReaderMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    SharePoint reader.</span>


<span class="sd">    Reads folders from the SharePoint site from a folder under documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        client_id (str): The Application ID for the app registered in Microsoft Azure Portal.</span>
<span class="sd">            The application must also be configured with MS Graph permissions "Files.ReadAll", "Sites.ReadAll" and BrowserSiteLists.Read.All.</span>
<span class="sd">        client_secret (str): The application secret for the app registered in Azure.</span>
<span class="sd">        tenant_id (str): Unique identifier of the Azure Active Directory Instance.</span>
<span class="sd">        sharepoint_site_name (Optional[str]): The name of the SharePoint site to download from.</span>
<span class="sd">        sharepoint_folder_path (Optional[str]): The path of the SharePoint folder to download from.</span>
<span class="sd">        sharepoint_folder_id (Optional[str]): The ID of the SharePoint folder to download from. Overrides sharepoint_folder_path.</span>
<span class="sd">        drive_name (Optional[str]): The name of the drive to download from.</span>
<span class="sd">        drive_id (Optional[str]): The ID of the drive to download from. Overrides drive_name.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file extension to a BaseReader class that specifies how to convert that</span>
<span class="sd">                                                          file to text. See `SimpleDirectoryReader` for more details.</span>
<span class="sd">        attach_permission_metadata (bool): If True, the reader will attach permission metadata to the documents. Set to False if your vector store</span>
<span class="sd">                                           only supports flat metadata (i.e. no nested fields or lists), or to avoid the additional API calls.</span>
<span class="sd">    """</span>

    <span class="n">client_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">client_secret</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">tenant_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>
    <span class="n">attach_permission_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">drive_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">_authorization_headers</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_drive_id_endpoint</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_drive_id</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">client_secret</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tenant_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">drive_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">client_id</span><span class="o">=</span><span class="n">client_id</span><span class="p">,</span>
            <span class="n">client_secret</span><span class="o">=</span><span class="n">client_secret</span><span class="p">,</span>
            <span class="n">tenant_id</span><span class="o">=</span><span class="n">tenant_id</span><span class="p">,</span>
            <span class="n">sharepoint_site_name</span><span class="o">=</span><span class="n">sharepoint_site_name</span><span class="p">,</span>
            <span class="n">sharepoint_folder_path</span><span class="o">=</span><span class="n">sharepoint_folder_path</span><span class="p">,</span>
            <span class="n">sharepoint_folder_id</span><span class="o">=</span><span class="n">sharepoint_folder_id</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="n">drive_name</span><span class="o">=</span><span class="n">drive_name</span><span class="p">,</span>
            <span class="n">drive_id</span><span class="o">=</span><span class="n">drive_id</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SharePointReader"</span>

    <span class="k">def</span> <span class="nf">_get_access_token</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Gets the access_token for accessing file from SharePoint.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The access_token for accessing the file.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If there is an error in obtaining the access_token.</span>
<span class="sd">        """</span>
        <span class="n">authority</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://login.microsoftonline.com/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">tenant_id</span><span class="si">}</span><span class="s2">/oauth2/token"</span>

        <span class="n">payload</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"grant_type"</span><span class="p">:</span> <span class="s2">"client_credentials"</span><span class="p">,</span>
            <span class="s2">"client_id"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span>
            <span class="s2">"client_secret"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">client_secret</span><span class="p">,</span>
            <span class="s2">"resource"</span><span class="p">:</span> <span class="s2">"https://graph.microsoft.com/"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">authority</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="mi">200</span> <span class="ow">and</span> <span class="s2">"value"</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">():</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span>
                <span class="ow">and</span> <span class="s2">"id"</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
            <span class="p">):</span>
                <span class="c1"># find the site with the specified name</span>
                <span class="k">for</span> <span class="n">site</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">]:</span>
                    <span class="k">if</span> <span class="n">site</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o"></span> <span class="mi">200</span> <span class="ow">and</span> <span class="s2">"value"</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">():</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">drive_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">drive</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">]:</span>
                    <span class="k">if</span> <span class="n">drive</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o"></span> <span class="mi">200</span> <span class="ow">and</span> <span class="s2">"id"</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">():</span>
            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"id"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"error"</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">_download_files_and_extract_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">folder_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">include_subfolders</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Downloads files from the specified folder ID and extracts metadata.</span>

<span class="sd">        Args:</span>
<span class="sd">            folder_id (str): The ID of the folder from which the files should be downloaded.</span>
<span class="sd">            download_dir (str): The directory where the files should be downloaded.</span>
<span class="sd">            include_subfolders (bool): If True, files from all subfolders are downloaded.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, str]: A dictionary containing the metadata of the downloaded files.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If there is an error in downloading the files.</span>
<span class="sd">        """</span>
        <span class="n">files_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_resources</span><span class="p">(</span>
            <span class="n">sharepoint_site_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span><span class="p">,</span>
            <span class="n">sharepoint_folder_id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">for</span> <span class="n">file_path</span> <span class="ow">in</span> <span class="n">files_path</span><span class="p">:</span>
            <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_item_from_path</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
            <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_download_file</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">download_dir</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">metadata</span>

    <span class="k">def</span> <span class="nf">_get_file_content_by_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves the content of the file from the provided URL.</span>

<span class="sd">        Args:</span>
<span class="sd">            item (Dict[str, Any]): Dictionary containing file metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            bytes: The content of the file.</span>
<span class="sd">        """</span>
        <span class="n">file_download_url</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"@microsoft.graph.downloadUrl"</span><span class="p">]</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">file_download_url</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"error"</span><span class="p">])</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"error_description"</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span>

    <span class="k">def</span> <span class="nf">_download_file_by_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Downloads the file from the provided URL.</span>

<span class="sd">        Args:</span>
<span class="sd">            item (Dict[str, Any]): Dictionary containing file metadata.</span>
<span class="sd">            download_dir (str): The directory where the files should be downloaded.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The path of the downloaded file in the temporary directory.</span>
<span class="sd">        """</span>
        <span class="c1"># Get the download URL for the file.</span>
        <span class="n">file_name</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>

        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_file_content_by_url</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>

        <span class="c1"># Create the directory if it does not exist and save the file.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">download_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">download_dir</span><span class="p">)</span>
        <span class="n">file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">download_dir</span><span class="p">,</span> <span class="n">file_name</span><span class="p">)</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">file_path</span>

    <span class="k">def</span> <span class="nf">_get_permissions_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Extracts the permissions information for the file. For more information, see:</span>
<span class="sd">        https://learn.microsoft.com/en-us/graph/api/resources/permission?view=graph-rest-1.0.</span>

<span class="sd">        Args:</span>
<span class="sd">            item (Dict[str, Any]): Dictionary containing file metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, str]: A dictionary containing the extracted permissions information.</span>
<span class="sd">        """</span>
        <span class="n">item_id</span> <span class="o">=</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span>
        <span class="n">permissions_info_endpoint</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id_endpoint</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span><span class="si">}</span><span class="s2">/items/</span><span class="si">{</span><span class="n">item_id</span><span class="si">}</span><span class="s2">/permissions"</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">permissions_info_endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authorization_headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">permissions</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="n">identity_sets</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">permission</span> <span class="ow">in</span> <span class="n">permissions</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]:</span>
            <span class="c1"># user type permissions</span>
            <span class="n">granted_to</span> <span class="o">=</span> <span class="n">permission</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"grantedToV2"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">granted_to</span><span class="p">:</span>
                <span class="n">identity_sets</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">granted_to</span><span class="p">)</span>

            <span class="c1"># link type permissions</span>
            <span class="n">granted_to_identities</span> <span class="o">=</span> <span class="n">permission</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"grantedToIdentitiesV2"</span><span class="p">,</span> <span class="p">[])</span>
            <span class="k">for</span> <span class="n">identity</span> <span class="ow">in</span> <span class="n">granted_to_identities</span><span class="p">:</span>
                <span class="n">identity_sets</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">identity</span><span class="p">)</span>

        <span class="c1"># Extract the identity information from each identity set</span>
        <span class="c1"># they can be 'application', 'device', 'user', 'group', 'siteUser' or 'siteGroup'</span>
        <span class="c1"># 'siteUser' and 'siteGroup' are site-specific, 'group' is for Microsoft 365 groups</span>
        <span class="n">permissions_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">identity_set</span> <span class="ow">in</span> <span class="n">identity_sets</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">identity</span><span class="p">,</span> <span class="n">identity_info</span> <span class="ow">in</span> <span class="n">identity_set</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="nb">id</span> <span class="o">=</span> <span class="n">identity_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span>
                <span class="n">display_name</span> <span class="o">=</span> <span class="n">identity_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"displayName"</span><span class="p">)</span>
                <span class="n">ids_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"allowed_</span><span class="si">{</span><span class="n">identity</span><span class="si">}</span><span class="s2">_ids"</span>
                <span class="n">display_names_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"allowed_</span><span class="si">{</span><span class="n">identity</span><span class="si">}</span><span class="s2">_display_names"</span>

                <span class="k">if</span> <span class="n">ids_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">permissions_dict</span><span class="p">:</span>
                    <span class="n">permissions_dict</span><span class="p">[</span><span class="n">ids_key</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">if</span> <span class="n">display_names_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">permissions_dict</span><span class="p">:</span>
                    <span class="n">permissions_dict</span><span class="p">[</span><span class="n">display_names_key</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

                <span class="n">permissions_dict</span><span class="p">[</span><span class="n">ids_key</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span>
                <span class="n">permissions_dict</span><span class="p">[</span><span class="n">display_names_key</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">display_name</span><span class="p">)</span>

        <span class="c1"># sort to get consistent results, if possible</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">permissions_dict</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">permissions_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">permissions_dict</span><span class="p">[</span><span class="n">key</span><span class="p">])</span>
            <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span>
                <span class="k">pass</span>

        <span class="k">return</span> <span class="n">permissions_dict</span>

    <span class="k">def</span> <span class="nf">_extract_metadata_for_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Extracts metadata related to the file.</span>

<span class="sd">        Parameters:</span>
<span class="sd">        - item (Dict[str, str]): Dictionary containing file metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">        - Dict[str, str]: A dictionary containing the extracted metadata.</span>
<span class="sd">        """</span>
        <span class="c1"># Extract the required metadata for file.</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">attach_permission_metadata</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_permissions_info</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"file_id"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">),</span>
                <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">),</span>
                <span class="s2">"url"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"webUrl"</span><span class="p">),</span>
                <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_path"</span><span class="p">),</span>
            <span class="p">}</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">metadata</span>

    <span class="k">def</span> <span class="nf">_download_file</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">file_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_file_by_url</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">download_dir</span><span class="p">)</span>

        <span class="n">metadata</span><span class="p">[</span><span class="n">file_path</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_metadata_for_file</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">metadata</span>

    <span class="k">def</span> <span class="nf">_download_files_from_sharepoint</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Downloads files from the specified folder and returns the metadata for the downloaded files.</span>

<span class="sd">        Args:</span>
<span class="sd">            download_dir (str): The directory where the files should be downloaded.</span>
<span class="sd">            sharepoint_site_name (str): The name of the SharePoint site.</span>
<span class="sd">            sharepoint_folder_path (str): The path of the folder in the SharePoint site.</span>
<span class="sd">            recursive (bool): If True, files from all subfolders are downloaded.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, str]: A dictionary containing the metadata of the downloaded files.</span>

<span class="sd">        """</span>
        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_access_token</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_site_id_with_host_name</span><span class="p">(</span>
            <span class="n">access_token</span><span class="p">,</span> <span class="n">sharepoint_site_name</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_drive_id</span><span class="p">()</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span> <span class="ow">and</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
            <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_sharepoint_folder_id</span><span class="p">(</span>
                <span class="n">sharepoint_folder_path</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_files_and_extract_metadata</span><span class="p">(</span>
            <span class="n">sharepoint_folder_id</span><span class="p">,</span>
            <span class="n">download_dir</span><span class="p">,</span>
            <span class="n">recursive</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_exclude_access_control_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Excludes the access control metadata from the documents for embedding and LLM calls.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (List[Document]): A list of documents.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents with access control metadata excluded.</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">access_control_keys</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">key</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">metadata</span> <span class="k">if</span> <span class="n">key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"allowed_"</span><span class="p">)</span>
            <span class="p">]</span>

            <span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">access_control_keys</span><span class="p">)</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">access_control_keys</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">_load_documents_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">files_metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Loads the documents from the downloaded files.</span>

<span class="sd">        Args:</span>
<span class="sd">            files_metadata (Dict[str,Any]): A dictionary containing the metadata of the downloaded files.</span>
<span class="sd">            download_dir (str): The directory where the files should be downloaded.</span>
<span class="sd">            recursive (bool): If True, files from all subfolders are downloaded.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list containing the documents with metadata.</span>
<span class="sd">        """</span>

        <span class="k">def</span> <span class="nf">get_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">files_metadata</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span>

        <span class="n">simple_loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
            <span class="n">download_dir</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_metadata</span><span class="p">,</span>
            <span class="n">recursive</span><span class="o">=</span><span class="n">recursive</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="n">simple_loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">attach_permission_metadata</span><span class="p">:</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_access_control_metadata</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Loads the files from the specified folder in the SharePoint site.</span>

<span class="sd">        Args:</span>
<span class="sd">            sharepoint_site_name (Optional[str]): The name of the SharePoint site.</span>
<span class="sd">            sharepoint_folder_path (Optional[str]): The path of the folder in the SharePoint site.</span>
<span class="sd">            recursive (bool): If True, files from all subfolders are downloaded.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list containing the documents with metadata.</span>

<span class="sd">        Raises:</span>
<span class="sd">            Exception: If an error occurs while accessing SharePoint site.</span>
<span class="sd">        """</span>
        <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
            <span class="n">sharepoint_site_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
            <span class="n">sharepoint_folder_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_path</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
            <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_id</span>

        <span class="c1"># TODO: make both of these values optional —&nbsp;and just default to the client ID defaults</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"sharepoint_site_name must be provided."</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
                <span class="n">files_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_files_from_sharepoint</span><span class="p">(</span>
                    <span class="n">temp_dir</span><span class="p">,</span>
                    <span class="n">sharepoint_site_name</span><span class="p">,</span>
                    <span class="n">sharepoint_folder_path</span><span class="p">,</span>
                    <span class="n">sharepoint_folder_id</span><span class="p">,</span>
                    <span class="n">recursive</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="c1"># return self.files_metadata</span>
                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span>
                    <span class="n">files_metadata</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="n">recursive</span>
                <span class="p">)</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An error occurred while accessing SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_list_folder_contents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">folder_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">current_path</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper method to fetch the contents of a folder.</span>

<span class="sd">        Args:</span>
<span class="sd">            folder_id (str): ID of the folder whose contents are to be listed.</span>
<span class="sd">            recursive (bool): Whether to include subfolders recursively.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Path]: List of file paths.</span>
<span class="sd">        """</span>
        <span class="n">folder_contents_endpoint</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id_endpoint</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span><span class="si">}</span><span class="s2">/items/</span><span class="si">{</span><span class="n">folder_id</span><span class="si">}</span><span class="s2">/children"</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">folder_contents_endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authorization_headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"value"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="n">file_paths</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"folder"</span> <span class="ow">in</span> <span class="n">item</span> <span class="ow">and</span> <span class="n">recursive</span><span class="p">:</span>
                <span class="c1"># Recursive call for subfolder</span>
                <span class="n">subfolder_id</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
                <span class="n">subfolder_paths</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_folder_contents</span><span class="p">(</span>
                    <span class="n">subfolder_id</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
                <span class="p">)</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">subfolder_paths</span><span class="p">)</span>
            <span class="k">elif</span> <span class="s2">"file"</span> <span class="ow">in</span> <span class="n">item</span><span class="p">:</span>
                <span class="c1"># Append file path</span>
                <span class="n">file_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]))</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">file_paths</span>

    <span class="k">def</span> <span class="nf">_list_drive_contents</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper method to fetch the contents of the drive.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Path]: List of file paths.</span>
<span class="sd">        """</span>
        <span class="n">drive_contents_endpoint</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id_endpoint</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span><span class="si">}</span><span class="s2">/root/children"</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">drive_contents_endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authorization_headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"value"</span><span class="p">,</span> <span class="p">[])</span>

        <span class="n">file_paths</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"folder"</span> <span class="ow">in</span> <span class="n">item</span><span class="p">:</span>
                <span class="c1"># Append folder path</span>
                <span class="n">folder_paths</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_folder_contents</span><span class="p">(</span>
                    <span class="n">item</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">current_path</span><span class="o">=</span><span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">folder_paths</span><span class="p">)</span>
            <span class="k">elif</span> <span class="s2">"file"</span> <span class="ow">in</span> <span class="n">item</span><span class="p">:</span>
                <span class="c1"># Append file path</span>
                <span class="n">file_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">file_paths</span>

    <span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Lists the files in the specified folder in the SharePoint site.</span>

<span class="sd">        Args:</span>
<span class="sd">            **kwargs: Additional keyword arguments.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Path]: A list of paths of the files in the specified folder.</span>

<span class="sd">        Raises:</span>
<span class="sd">            Exception: If an error occurs while accessing SharePoint site.</span>
<span class="sd">        """</span>
        <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
            <span class="n">sharepoint_site_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
            <span class="n">sharepoint_folder_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_path</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
            <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_id</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"sharepoint_site_name must be provided."</span><span class="p">)</span>

        <span class="n">file_paths</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_access_token</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_site_id_with_host_name</span><span class="p">(</span>
                <span class="n">access_token</span><span class="p">,</span> <span class="n">sharepoint_site_name</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_drive_id</span><span class="p">()</span>

            <span class="k">if</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
                    <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_sharepoint_folder_id</span><span class="p">(</span>
                        <span class="n">sharepoint_folder_path</span>
                    <span class="p">)</span>
                <span class="c1"># Fetch folder contents</span>
                <span class="n">folder_contents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_folder_contents</span><span class="p">(</span>
                    <span class="n">sharepoint_folder_id</span><span class="p">,</span>
                    <span class="n">recursive</span><span class="p">,</span>
                    <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">sharepoint_site_name</span><span class="p">,</span> <span class="n">sharepoint_folder_path</span><span class="p">),</span>
                <span class="p">)</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">folder_contents</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Fetch drive contents</span>
                <span class="n">drive_contents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_drive_contents</span><span class="p">()</span>
                <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">drive_contents</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An error occurred while listing files in SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>
            <span class="k">raise</span>

        <span class="k">return</span> <span class="n">file_paths</span>

    <span class="k">def</span> <span class="nf">_get_item_from_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves the item details for a specified file in SharePoint.</span>

<span class="sd">        Args:</span>
<span class="sd">            input_file (Path): The path of the file in SharePoint.</span>
<span class="sd">                Should include the SharePoint site name and the folder path. e.g. "site_name/folder_path/file_name".</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: Dictionary containing the item details.</span>
<span class="sd">        """</span>
        <span class="c1"># Get the file ID</span>
        <span class="c1"># remove the site_name prefix</span>
        <span class="n">file_path</span> <span class="o">=</span> <span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span><span class="si">}</span><span class="s2">/"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">endpoint</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id_endpoint</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span><span class="si">}</span><span class="s2">/root:/</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authorization_headers</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_resource_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves metadata for a specified file in SharePoint without downloading it.</span>

<span class="sd">        Args:</span>
<span class="sd">            input_file (Path): The path of the file in SharePoint. The path should include</span>
<span class="sd">                                the SharePoint site name and the folder path. e.g. "site_name/folder_path/file_name".</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_item_from_path</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">resource_id</span><span class="p">))</span>

            <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">resource_id</span><span class="p">,</span>
                <span class="s2">"size"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"size"</span><span class="p">),</span>
                <span class="s2">"created_at"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"createdDateTime"</span><span class="p">),</span>
                <span class="s2">"modified_at"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lastModifiedDateTime"</span><span class="p">),</span>
                <span class="s2">"etag"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"eTag"</span><span class="p">),</span>
            <span class="p">}</span>

            <span class="k">if</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">attach_permission_metadata</span>
            <span class="p">):</span>  <span class="c1"># changes in access control should trigger a reingestion of the file</span>
                <span class="n">permissions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_permissions_info</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
                <span class="n">info_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">permissions</span><span class="p">)</span>

            <span class="k">return</span> <span class="p">{</span>
                <span class="n">meta_key</span><span class="p">:</span> <span class="n">meta_value</span>
                <span class="k">for</span> <span class="n">meta_key</span><span class="p">,</span> <span class="n">meta_value</span> <span class="ow">in</span> <span class="n">info_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">meta_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="p">}</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="s2">"An error occurred while fetching file information from SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">exp</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">load_resource</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_access_token</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_site_id_with_host_name</span><span class="p">(</span>
                <span class="n">access_token</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_drive_id</span><span class="p">()</span>

            <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span>

            <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_item_from_path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

            <span class="n">input_file_dir</span> <span class="o">=</span> <span class="n">path</span><span class="o">.</span><span class="n">parent</span>

            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_file</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="n">input_file_dir</span><span class="p">)</span>
                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span>
                    <span class="n">metadata</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">False</span>
                <span class="p">)</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="s2">"An error occurred while reading file from SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span>
            <span class="p">)</span>
            <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_access_token</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_site_id_with_host_name</span><span class="p">(</span>
                <span class="n">access_token</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_drive_id</span><span class="p">()</span>

            <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_item_from_path</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_file_content_by_url</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="s2">"An error occurred while reading file content from SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span>
            <span class="p">)</span>
            <span class="k">raise</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/#llama_index.readers.microsoft_sharepoint.SharePointReader.load_data "Permanent link")

```
load_data(sharepoint_site_name: Optional[str] = None, sharepoint_folder_path: Optional[str] = None, sharepoint_folder_id: Optional[str] = None, recursive: bool = True) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads the files from the specified folder in the SharePoint site.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sharepoint_site_name` | `Optional[str]` | 
The name of the SharePoint site.



 | `None` |
| `sharepoint_folder_path` | `Optional[str]` | 

The path of the folder in the SharePoint site.



 | `None` |
| `recursive` | `bool` | 

If True, files from all subfolders are downloaded.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list containing the documents with metadata.



 |

**Raises:**

| Type | Description |
| --- | --- |
| `Exception` | 
If an error occurs while accessing SharePoint site.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-sharepoint/llama_index/readers/microsoft_sharepoint/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">510</span>
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
<span class="normal">561</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Loads the files from the specified folder in the SharePoint site.</span>

<span class="sd">    Args:</span>
<span class="sd">        sharepoint_site_name (Optional[str]): The name of the SharePoint site.</span>
<span class="sd">        sharepoint_folder_path (Optional[str]): The path of the folder in the SharePoint site.</span>
<span class="sd">        recursive (bool): If True, files from all subfolders are downloaded.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list containing the documents with metadata.</span>

<span class="sd">    Raises:</span>
<span class="sd">        Exception: If an error occurs while accessing SharePoint site.</span>
<span class="sd">    """</span>
    <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
        <span class="n">sharepoint_site_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
        <span class="n">sharepoint_folder_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_path</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
        <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_id</span>

    <span class="c1"># TODO: make both of these values optional —&nbsp;and just default to the client ID defaults</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"sharepoint_site_name must be provided."</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="n">files_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_files_from_sharepoint</span><span class="p">(</span>
                <span class="n">temp_dir</span><span class="p">,</span>
                <span class="n">sharepoint_site_name</span><span class="p">,</span>
                <span class="n">sharepoint_folder_path</span><span class="p">,</span>
                <span class="n">sharepoint_folder_id</span><span class="p">,</span>
                <span class="n">recursive</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># return self.files_metadata</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span>
                <span class="n">files_metadata</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="n">recursive</span>
            <span class="p">)</span>

    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An error occurred while accessing SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### list\_resources [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/#llama_index.readers.microsoft_sharepoint.SharePointReader.list_resources "Permanent link")

```
list_resources(sharepoint_site_name: Optional[str] = None, sharepoint_folder_path: Optional[str] = None, sharepoint_folder_id: Optional[str] = None, recursive: bool = True) -> List[Path]
```

Lists the files in the specified folder in the SharePoint site.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `**kwargs` |  | 
Additional keyword arguments.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[Path]` | 
List\[Path\]: A list of paths of the files in the specified folder.



 |

**Raises:**

| Type | Description |
| --- | --- |
| `Exception` | 
If an error occurs while accessing SharePoint site.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-sharepoint/llama_index/readers/microsoft_sharepoint/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">631</span>
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
<span class="normal">691</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">sharepoint_site_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sharepoint_folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sharepoint_folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Lists the files in the specified folder in the SharePoint site.</span>

<span class="sd">    Args:</span>
<span class="sd">        **kwargs: Additional keyword arguments.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Path]: A list of paths of the files in the specified folder.</span>

<span class="sd">    Raises:</span>
<span class="sd">        Exception: If an error occurs while accessing SharePoint site.</span>
<span class="sd">    """</span>
    <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
        <span class="n">sharepoint_site_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_site_name</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
        <span class="n">sharepoint_folder_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_path</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
        <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sharepoint_folder_id</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_site_name</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"sharepoint_site_name must be provided."</span><span class="p">)</span>

    <span class="n">file_paths</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_access_token</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_site_id_with_host_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_site_id_with_host_name</span><span class="p">(</span>
            <span class="n">access_token</span><span class="p">,</span> <span class="n">sharepoint_site_name</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_drive_id</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">sharepoint_folder_path</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">sharepoint_folder_id</span><span class="p">:</span>
                <span class="n">sharepoint_folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_sharepoint_folder_id</span><span class="p">(</span>
                    <span class="n">sharepoint_folder_path</span>
                <span class="p">)</span>
            <span class="c1"># Fetch folder contents</span>
            <span class="n">folder_contents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_folder_contents</span><span class="p">(</span>
                <span class="n">sharepoint_folder_id</span><span class="p">,</span>
                <span class="n">recursive</span><span class="p">,</span>
                <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">sharepoint_site_name</span><span class="p">,</span> <span class="n">sharepoint_folder_path</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">folder_contents</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Fetch drive contents</span>
            <span class="n">drive_contents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_list_drive_contents</span><span class="p">()</span>
            <span class="n">file_paths</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">drive_contents</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An error occurred while listing files in SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>
        <span class="k">raise</span>

    <span class="k">return</span> <span class="n">file_paths</span>
</code></pre></div></td></tr></tbody></table>

### get\_resource\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/#llama_index.readers.microsoft_sharepoint.SharePointReader.get_resource_info "Permanent link")

```
get_resource_info(resource_id: str, **kwargs) -> Dict
```

Retrieves metadata for a specified file in SharePoint without downloading it.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_file` | `Path` | 
The path of the file in SharePoint. The path should include the SharePoint site name and the folder path. e.g. "site\_name/folder\_path/file\_name".



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-sharepoint/llama_index/readers/microsoft_sharepoint/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">718</span>
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
<span class="normal">754</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_resource_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieves metadata for a specified file in SharePoint without downloading it.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_file (Path): The path of the file in SharePoint. The path should include</span>
<span class="sd">                            the SharePoint site name and the folder path. e.g. "site_name/folder_path/file_name".</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_item_from_path</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">resource_id</span><span class="p">))</span>

        <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">resource_id</span><span class="p">,</span>
            <span class="s2">"size"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"size"</span><span class="p">),</span>
            <span class="s2">"created_at"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"createdDateTime"</span><span class="p">),</span>
            <span class="s2">"modified_at"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lastModifiedDateTime"</span><span class="p">),</span>
            <span class="s2">"etag"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"eTag"</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">attach_permission_metadata</span>
        <span class="p">):</span>  <span class="c1"># changes in access control should trigger a reingestion of the file</span>
            <span class="n">permissions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_permissions_info</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
            <span class="n">info_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">permissions</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="n">meta_key</span><span class="p">:</span> <span class="n">meta_value</span>
            <span class="k">for</span> <span class="n">meta_key</span><span class="p">,</span> <span class="n">meta_value</span> <span class="ow">in</span> <span class="n">info_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">meta_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">}</span>

    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
            <span class="s2">"An error occurred while fetching file information from SharePoint: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span>
            <span class="n">exp</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">raise</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Microsoft outlook](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/)[Next Milvus](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/)
