Title: Microsoft onedrive - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/

Markdown Content:
Microsoft onedrive - LlamaIndex


OneDriveReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/#llama_index.readers.microsoft_onedrive.OneDriveReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`, `ResourcesReaderMixin`, `FileSystemReaderMixin`

Microsoft OneDrive reader.

Initializes a new instance of the OneDriveReader.

:param client\_id: The Application (client) ID for the app registered in the Azure Entra (formerly Azure Active directory) portal with MS Graph permission "Files.Read.All". :param tenant\_id: The Directory (tenant) ID of the Azure Active Directory (AAD) tenant the app is registered with. Defaults to "consumers" for multi-tenant applications and OneDrive personal. :param client\_secret: The Application Secret for the app registered in the Azure portal. If provided, the MSAL client credential flow will be used for authentication (ConfidentialClientApplication). If not provided, interactive authentication will be used (Not recommended for CI/CD or scenarios where manual interaction for authentication is not feasible). Required for App authentication. :param userprinciplename: The user principal name (normally organization provided email) whose OneDrive will be accessed. Required for App authentication. Will be used if the parameter is not provided when calling load\_data(). :param folder\_id: The folder ID of the folder to fetch from OneDrive. Will be used if the parameter is not provided when calling load\_data(). :param file\_ids: A list of file IDs of files to fetch from OneDrive. Will be used if the parameter is not provided when calling load\_data(). :param folder\_path (str, optional): The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded. Will be used if the parameter is not provided when calling load\_data(). :param file\_paths (List\[str\], optional): List of specific file paths to download. Will be used if the parameter is not provided when calling load\_data(). :param file\_extractor (Optional\[Dict\[str, BaseReader\]\]): A mapping of file extension to a BaseReader class that specifies how to convert that file to text. See `SimpleDirectoryReader` for more details.

For interactive authentication to work, a browser is used to authenticate, hence the registered application should have a redirect URI set to 'https://localhost' for mobile and native applications.

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-onedrive/llama_index/readers/microsoft_onedrive/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 34</span>
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
<span class="normal">731</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OneDriveReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">,</span> <span class="n">ResourcesReaderMixin</span><span class="p">,</span> <span class="n">FileSystemReaderMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Microsoft OneDrive reader.</span>

<span class="sd">    Initializes a new instance of the OneDriveReader.</span>

<span class="sd">    :param client_id: The Application (client) ID for the app registered in the Azure Entra (formerly Azure Active directory) portal with MS Graph permission "Files.Read.All".</span>
<span class="sd">    :param tenant_id: The Directory (tenant) ID of the Azure Active Directory (AAD) tenant the app is registered with.</span>
<span class="sd">                      Defaults to "consumers" for multi-tenant applications and OneDrive personal.</span>
<span class="sd">    :param client_secret: The Application Secret for the app registered in the Azure portal.</span>
<span class="sd">                          If provided, the MSAL client credential flow will be used for authentication (ConfidentialClientApplication).</span>
<span class="sd">                          If not provided, interactive authentication will be used (Not recommended for CI/CD or scenarios where manual interaction for authentication is not feasible).</span>
<span class="sd">                          Required for App authentication.</span>
<span class="sd">    :param userprinciplename: The user principal name (normally organization provided email) whose OneDrive will be accessed. Required for App authentication. Will be used if the</span>
<span class="sd">                              parameter is not provided when calling load_data().</span>
<span class="sd">    :param folder_id: The folder ID of the folder to fetch from OneDrive. Will be used if the parameter is not provided when calling load_data().</span>
<span class="sd">    :param file_ids: A list of file IDs of files to fetch from OneDrive. Will be used if the parameter is not provided when calling load_data().</span>
<span class="sd">    :param folder_path (str, optional): The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded.  Will be used if the parameter is</span>
<span class="sd">                                        not provided when calling load_data().</span>
<span class="sd">    :param file_paths (List[str], optional): List of specific file paths to download. Will be used if the parameter is not provided when calling load_data().</span>
<span class="sd">    :param file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file extension to a BaseReader class that specifies how to convert that file to text.</span>
<span class="sd">                                                             See `SimpleDirectoryReader` for more details.</span>


<span class="sd">    For interactive authentication to work, a browser is used to authenticate, hence the registered application should have a redirect URI set to 'https://localhost'</span>
<span class="sd">    for mobile and native applications.</span>
<span class="sd">    """</span>

    <span class="n">client_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">tenant_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">file_paths</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>

    <span class="n">_is_interactive_auth</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_authority</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">client_secret</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tenant_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"consumers"</span><span class="p">,</span>
        <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_paths</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_is_interactive_auth</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">client_secret</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_authority</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://login.microsoftonline.com/</span><span class="si">{</span><span class="n">tenant_id</span><span class="si">}</span><span class="s2">/"</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">client_id</span><span class="o">=</span><span class="n">client_id</span><span class="p">,</span>
            <span class="n">client_secret</span><span class="o">=</span><span class="n">client_secret</span><span class="p">,</span>
            <span class="n">tenant_id</span><span class="o">=</span><span class="n">tenant_id</span><span class="p">,</span>
            <span class="n">userprincipalname</span><span class="o">=</span><span class="n">userprincipalname</span><span class="p">,</span>
            <span class="n">folder_id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">,</span>
            <span class="n">file_ids</span><span class="o">=</span><span class="n">file_ids</span><span class="p">,</span>
            <span class="n">folder_path</span><span class="o">=</span><span class="n">folder_path</span><span class="p">,</span>
            <span class="n">file_paths</span><span class="o">=</span><span class="n">file_paths</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_authenticate_with_msal</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Authenticate with MSAL.</span>

<span class="sd">        For interactive authentication to work, a browser is used to authenticate, hence the registered application should have a redirect URI set to 'localhost'</span>
<span class="sd">        for mobile and native applications.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">msal</span>

        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_interactive_auth</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Starting user authentication..."</span><span class="p">)</span>
            <span class="n">app</span> <span class="o">=</span> <span class="n">msal</span><span class="o">.</span><span class="n">PublicClientApplication</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span> <span class="n">authority</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authority</span>
            <span class="p">)</span>

            <span class="c1"># The acquire_token_interactive method will open the default web browser</span>
            <span class="c1"># for the interactive part of the OAuth2 flow. The registered application should have a redirect URI set to 'https://localhost'</span>
            <span class="c1"># under mobile and native applications.</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">app</span><span class="o">.</span><span class="n">acquire_token_interactive</span><span class="p">(</span><span class="n">SCOPES</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Starting app authentication..."</span><span class="p">)</span>
            <span class="n">app</span> <span class="o">=</span> <span class="n">msal</span><span class="o">.</span><span class="n">ConfidentialClientApplication</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span>
                <span class="n">authority</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_authority</span><span class="p">,</span>
                <span class="n">client_credential</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">client_secret</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">result</span> <span class="o">=</span> <span class="n">app</span><span class="o">.</span><span class="n">acquire_token_for_client</span><span class="p">(</span><span class="n">scopes</span><span class="o">=</span><span class="n">CLIENTCREDENTIALSCOPES</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"access_token"</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Authentication is successful..."</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">result</span><span class="p">[</span><span class="s2">"access_token"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"error"</span><span class="p">))</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"error_description"</span><span class="p">))</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"correlation_id"</span><span class="p">))</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"error"</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_construct_endpoint</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">item_ref</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">isRelativePath</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">isFile</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Constructs the appropriate OneDrive API endpoint based on the provided parameters.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            item_ref (str): The reference to the item; could be an item ID or a relative path.</span>
<span class="sd">            isRelativePath (bool): A boolean indicating whether the item_ref is a relative path.</span>
<span class="sd">            isFile (bool): A boolean indicating whether the target is a file.</span>
<span class="sd">            userprincipalname (str, optional): The user principal name; used if authentication is not interactive. Defaults to None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: A string representing the constructed endpoint.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_interactive_auth</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">userprincipalname</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span>
                <span class="s2">"userprincipalname cannot be empty for App authentication. Provide the userprincipalname (usually email) of the user whose OneDrive will be accessed."</span>
            <span class="p">)</span>

        <span class="n">endpoint</span> <span class="o">=</span> <span class="s2">"https://graph.microsoft.com/v1.0/"</span>

        <span class="c1"># Update the base endpoint based on the authentication method</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_interactive_auth</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">+=</span> <span class="s2">"me/drive"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"users/</span><span class="si">{</span><span class="n">userprincipalname</span><span class="si">}</span><span class="s2">/drive"</span>

        <span class="c1"># Update the endpoint for relative paths or item IDs</span>
        <span class="k">if</span> <span class="n">isRelativePath</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"/root:/</span><span class="si">{</span><span class="n">item_ref</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"/items/</span><span class="si">{</span><span class="n">item_ref</span><span class="si">}</span><span class="s2">"</span>

        <span class="c1"># If the target is not a file, adjust the endpoint to retrieve children of a folder</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">isFile</span><span class="p">:</span>
            <span class="n">endpoint</span> <span class="o">+=</span> <span class="s2">":/children"</span> <span class="k">if</span> <span class="n">isRelativePath</span> <span class="k">else</span> <span class="s2">"/children"</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"API Endpoint determined: </span><span class="si">{</span><span class="n">endpoint</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">endpoint</span>

    <span class="k">def</span> <span class="nf">_get_items_in_drive_with_maxretries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">access_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">item_ref</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"root"</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">isFile</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">isRelativePath</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves items from a drive using Microsoft Graph API.</span>

<span class="sd">        Parameters:</span>
<span class="sd">        access_token (str): Access token for API calls.</span>
<span class="sd">        item_ref (Optional[str]): Specific item ID/path or root for root folder.</span>
<span class="sd">        max_retries (int): Max number of retries on rate limit or server errors.</span>
<span class="sd">        userprincipalname: str value indicating the userprincipalname (usually organization-provided email) whose OneDrive will be accessed. Required for App authentication.</span>
<span class="sd">        isFile: bool value to indicate if to query file or folder</span>
<span class="sd">        isRelativePath: bool value to indicate if to query file or folder using relative path</span>
<span class="sd">        Returns:</span>
<span class="sd">        dict/None: JSON response or None after max retries.</span>

<span class="sd">        Raises:</span>
<span class="sd">        Exception: On non-retriable status code.</span>
<span class="sd">        """</span>
        <span class="n">endpoint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_construct_endpoint</span><span class="p">(</span>
            <span class="n">item_ref</span><span class="p">,</span> <span class="n">isRelativePath</span><span class="p">,</span> <span class="n">isFile</span><span class="p">,</span> <span class="n">userprincipalname</span>
        <span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
        <span class="n">retries</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="k">while</span> <span class="n">retries</span> <span class="o">&lt;</span> <span class="n">max_retries</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">endpoint</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="n">resource_id</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_resource_info</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_resource_info</span><span class="p">(</span><span class="n">resource_id</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_resource</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">file_paths</span><span class="o">=</span><span class="p">[</span><span class="n">resource_id</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_resource</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_resource</span><span class="p">(</span><span class="n">resource_id</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="n">payloads</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_downloaded_files_metadata</span><span class="p">(</span>
                <span class="n">file_paths</span><span class="o">=</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)],</span> <span class="n">temp_dir</span><span class="o">=</span><span class="n">temp_dir</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
            <span class="n">local_file_path</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
                <span class="n">payloads</span><span class="o">.</span><span class="n">downloaded_file_path</span>
                <span class="k">for</span> <span class="n">payloads</span> <span class="ow">in</span> <span class="n">payloads</span>
                <span class="k">if</span> <span class="n">payloads</span><span class="o">.</span><span class="n">resource_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">==</span> <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">local_file_path</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"File was not downloaded successfully."</span><span class="p">)</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aread_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_file_content</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/#llama_index.readers.microsoft_onedrive.OneDriveReader.load_data "Permanent link")

```
load_data(folder_id: Optional[str] = None, file_ids: Optional[List[str]] = None, folder_path: Optional[str] = None, file_paths: Optional[List[str]] = None, mime_types: Optional[List[str]] = None, recursive: bool = True, userprincipalname: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the folder id / file ids, f both are not provided download from the root.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `folder_id` | `str` | 
folder id of the folder in OneDrive.



 | `None` |
| `file_ids` | `List[str]` | 

file ids of the files in OneDrive.



 | `None` |
| `folder_path` | `str` | 

The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded.



 | `None` |
| `file_paths` | `List[str]` | 

List of specific file paths to download.



 | `None` |
| `mime_types` | `Optional[List[str]]` | 

the mimeTypes you want to allow e.g.: "application/pdf", default is none, which loads all files found



 | `None` |
| `recursive` | `bool` | 

boolean value to traverse and read subfolder, default is True



 | `True` |
| `userprincipalname` | `Optional[str]` | 

str value indicating the userprincipalname (normally organization-provided email) whose OneDrive will be accessed. Required for App authentication scenarios.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-onedrive/llama_index/readers/microsoft_onedrive/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">582</span>
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
<span class="normal">626</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">file_paths</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the folder id / file ids, f both are not provided download from the root.</span>

<span class="sd">    Args:</span>
<span class="sd">        folder_id (str, optional): folder id of the folder in OneDrive.</span>
<span class="sd">        file_ids (List[str], optional): file ids of the files in OneDrive.</span>
<span class="sd">        folder_path (str, optional): The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded.</span>
<span class="sd">        file_paths (List[str], optional): List of specific file paths to download.</span>
<span class="sd">        mime_types: the mimeTypes you want to allow e.g.: "application/pdf", default is none, which loads all files found</span>
<span class="sd">        recursive: boolean value to traverse and read subfolder, default is True</span>
<span class="sd">        userprincipalname: str value indicating the userprincipalname (normally organization-provided email) whose OneDrive will be accessed. Required for App authentication scenarios.</span>


<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="n">payloads</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_downloaded_files_metadata</span><span class="p">(</span>
                <span class="n">folder_id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">,</span>
                <span class="n">file_ids</span><span class="o">=</span><span class="n">file_ids</span><span class="p">,</span>
                <span class="n">folder_path</span><span class="o">=</span><span class="n">folder_path</span><span class="p">,</span>
                <span class="n">file_paths</span><span class="o">=</span><span class="n">file_paths</span><span class="p">,</span>
                <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
                <span class="n">recursive</span><span class="o">=</span><span class="n">recursive</span><span class="p">,</span>
                <span class="n">userprincipalname</span><span class="o">=</span><span class="n">userprincipalname</span><span class="p">,</span>
                <span class="n">temp_dir</span><span class="o">=</span><span class="n">temp_dir</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Downloaded </span><span class="si">%d</span><span class="s2"> files from OneDriveReader"</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">payloads</span><span class="p">))</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span>
                <span class="n">payloads</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="n">recursive</span>
            <span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"An error occurred while loading the data: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### list\_resources [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/#llama_index.readers.microsoft_onedrive.OneDriveReader.list_resources "Permanent link")

```
list_resources(folder_id: Optional[str] = None, file_ids: Optional[List[str]] = None, folder_path: Optional[str] = None, file_paths: Optional[List[str]] = None, mime_types: Optional[List[str]] = None, recursive: bool = True, userprincipalname: Optional[str] = None) -> List[str]
```

List resources from the folder id / file ids, if both are not provided list from the root.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `folder_id` | `str` | 
folder id of the folder in OneDrive.



 | `None` |
| `file_ids` | `List[str]` | 

file ids of the files in OneDrive.



 | `None` |
| `folder_path` | `str` | 

The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded.



 | `None` |
| `file_paths` | `List[str]` | 

List of specific file paths to download.



 | `None` |
| `mime_types` | `Optional[List[str]]` | 

the mimeTypes you want to allow e.g.: "application/pdf", default is none, which loads all files found



 | `None` |
| `recursive` | `bool` | 

boolean value to traverse and read subfolder, default is True



 | `True` |
| `userprincipalname` | `Optional[str]` | 

str value indicating the userprincipalname (normally organization-provided email) whose OneDrive will be accessed. Required for App authentication scenarios.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
List\[str\]: A list of resources.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-onedrive/llama_index/readers/microsoft_onedrive/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">628</span>
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
<span class="normal">668</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">folder_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">file_paths</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">userprincipalname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    List resources from the folder id / file ids, if both are not provided list from the root.</span>

<span class="sd">    Args:</span>
<span class="sd">        folder_id (str, optional): folder id of the folder in OneDrive.</span>
<span class="sd">        file_ids (List[str], optional): file ids of the files in OneDrive.</span>
<span class="sd">        folder_path (str, optional): The relative path of the OneDrive folder to download. If provided, files within the folder are downloaded.</span>
<span class="sd">        file_paths (List[str], optional): List of specific file paths to download.</span>
<span class="sd">        mime_types: the mimeTypes you want to allow e.g.: "application/pdf", default is none, which loads all files found</span>
<span class="sd">        recursive: boolean value to traverse and read subfolder, default is True</span>
<span class="sd">        userprincipalname: str value indicating the userprincipalname (normally organization-provided email) whose OneDrive will be accessed. Required for App authentication scenarios.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[str]: A list of resources.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">payloads</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_downloaded_files_metadata</span><span class="p">(</span>
            <span class="n">folder_id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">,</span>
            <span class="n">file_ids</span><span class="o">=</span><span class="n">file_ids</span><span class="p">,</span>
            <span class="n">folder_path</span><span class="o">=</span><span class="n">folder_path</span><span class="p">,</span>
            <span class="n">file_paths</span><span class="o">=</span><span class="n">file_paths</span><span class="p">,</span>
            <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
            <span class="n">recursive</span><span class="o">=</span><span class="n">recursive</span><span class="p">,</span>
            <span class="n">userprincipalname</span><span class="o">=</span><span class="n">userprincipalname</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">payload</span><span class="o">.</span><span class="n">resource_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="k">for</span> <span class="n">payload</span> <span class="ow">in</span> <span class="n">payloads</span><span class="p">]</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"An error occurred while listing resources: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>
        <span class="k">raise</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Metal](https://docs.llamaindex.ai/en/stable/api_reference/readers/metal/)[Next Microsoft outlook](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/)
