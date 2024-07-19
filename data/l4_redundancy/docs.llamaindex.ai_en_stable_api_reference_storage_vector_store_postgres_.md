Title: Postgres - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/

Markdown Content:
Postgres - LlamaIndex


PGVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/#llama_index.vector_stores.postgres.PGVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Postgres Vector Store.

**Examples:**

`pip install llama-index-vector-stores-postgres`

```
from llama_index.vector_stores.postgres import PGVectorStore

# Create PGVectorStore instance
vector_store = PGVectorStore.from_params(
    database="vector_db",
    host="localhost",
    password="password",
    port=5432,
    user="postgres",
    table_name="paul_graham_essay",
    embed_dim=1536  # openai embedding dimension
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-postgres/llama_index/vector_stores/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
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
<span class="normal">773</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PGVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Postgres Vector Store.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-postgres`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.postgres import PGVectorStore</span>

<span class="sd">        # Create PGVectorStore instance</span>
<span class="sd">        vector_store = PGVectorStore.from_params(</span>
<span class="sd">            database="vector_db",</span>
<span class="sd">            host="localhost",</span>
<span class="sd">            password="password",</span>
<span class="sd">            port=5432,</span>
<span class="sd">            user="postgres",</span>
<span class="sd">            table_name="paul_graham_essay",</span>
<span class="sd">            embed_dim=1536  # openai embedding dimension</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="kn">from</span> <span class="nn">sqlalchemy.sql.selectable</span> <span class="kn">import</span> <span class="n">Select</span>

    <span class="n">stores_text</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">]</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">embed_dim</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">text_search_config</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">cache_ok</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="n">_base</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_table_class</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_engine</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_session</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_async_engine</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_async_session</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_is_initialized</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">],</span>
        <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">],</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">text_search_config</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"english"</span><span class="p">,</span>
        <span class="n">embed_dim</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1536</span><span class="p">,</span>
        <span class="n">cache_ok</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">table_name</span> <span class="o">=</span> <span class="n">table_name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="n">schema_name</span> <span class="o">=</span> <span class="n">schema_name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">hybrid_search</span> <span class="ow">and</span> <span class="n">text_search_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Sparse vector index creation requires "</span>
                <span class="s2">"a text search configuration specification."</span>
            <span class="p">)</span>

        <span class="kn">from</span> <span class="nn">sqlalchemy.orm</span> <span class="kn">import</span> <span class="n">declarative_base</span>

        <span class="c1"># sqlalchemy model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base</span> <span class="o">=</span> <span class="n">declarative_base</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span> <span class="o">=</span> <span class="n">get_data_model</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base</span><span class="p">,</span>
            <span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="p">,</span>
            <span class="n">hybrid_search</span><span class="p">,</span>
            <span class="n">text_search_config</span><span class="p">,</span>
            <span class="n">cache_ok</span><span class="p">,</span>
            <span class="n">embed_dim</span><span class="o">=</span><span class="n">embed_dim</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="o">=</span><span class="n">connection_string</span><span class="p">,</span>
            <span class="n">async_connection_string</span><span class="o">=</span><span class="n">async_connection_string</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
            <span class="n">hybrid_search</span><span class="o">=</span><span class="n">hybrid_search</span><span class="p">,</span>
            <span class="n">text_search_config</span><span class="o">=</span><span class="n">text_search_config</span><span class="p">,</span>
            <span class="n">embed_dim</span><span class="o">=</span><span class="n">embed_dim</span><span class="p">,</span>
            <span class="n">cache_ok</span><span class="o">=</span><span class="n">cache_ok</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span><span class="p">:</span>
            <span class="k">return</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">close_all</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_engine</span><span class="o">.</span><span class="n">dispose</span><span class="p">()</span>

        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_engine</span><span class="o">.</span><span class="n">dispose</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PGVectorStore"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llamaindex"</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">text_search_config</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"english"</span><span class="p">,</span>
        <span class="n">embed_dim</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1536</span><span class="p">,</span>
        <span class="n">cache_ok</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PGVectorStore"</span><span class="p">:</span>
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
            <span class="n">hybrid_search</span><span class="o">=</span><span class="n">hybrid_search</span><span class="p">,</span>
            <span class="n">text_search_config</span><span class="o">=</span><span class="n">text_search_config</span><span class="p">,</span>
            <span class="n">embed_dim</span><span class="o">=</span><span class="n">embed_dim</span><span class="p">,</span>
            <span class="n">cache_ok</span><span class="o">=</span><span class="n">cache_ok</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_engine</span>

    <span class="k">def</span> <span class="nf">_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">create_engine</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.ext.asyncio</span> <span class="kn">import</span> <span class="n">AsyncSession</span><span class="p">,</span> <span class="n">create_async_engine</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.orm</span> <span class="kn">import</span> <span class="n">sessionmaker</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">connection_string</span><span class="p">,</span> <span class="n">echo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span> <span class="o">=</span> <span class="n">sessionmaker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_engine</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_async_engine</span> <span class="o">=</span> <span class="n">create_async_engine</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_connection_string</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span> <span class="o">=</span> <span class="n">sessionmaker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_async_engine</span><span class="p">,</span> <span class="n">class_</span><span class="o">=</span><span class="n">AsyncSession</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

    <span class="k">def</span> <span class="nf">_create_schema_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^[A-Za-z_][A-Za-z0-9_]*$"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid schema_name: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="c1"># Check if the specified schema exists with "CREATE" statement</span>
            <span class="n">check_schema_statement</span> <span class="o">=</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema_name"</span>
            <span class="p">)</span><span class="o">.</span><span class="n">bindparams</span><span class="p">(</span><span class="n">schema_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="p">)</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">check_schema_statement</span><span class="p">)</span><span class="o">.</span><span class="n">fetchone</span><span class="p">()</span>

            <span class="c1"># If the schema does not exist, then create it</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
                <span class="n">create_schema_statement</span> <span class="o">=</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">text</span><span class="p">(</span>
                    <span class="c1"># DDL won't tolerate quoted string literal here for schema_name,</span>
                    <span class="c1"># so use a format string to embed the schema_name directly, instead of a param.</span>
                    <span class="sa">f</span><span class="s2">"CREATE SCHEMA IF NOT EXISTS </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_name</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">create_schema_statement</span><span class="p">)</span>

            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_create_tables_if_not_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">create_all</span><span class="p">(</span><span class="n">session</span><span class="o">.</span><span class="n">connection</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">_create_extension</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">sqlalchemy</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="n">statement</span> <span class="o">=</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="s2">"CREATE EXTENSION IF NOT EXISTS vector"</span><span class="p">)</span>
            <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">statement</span><span class="p">)</span>
            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_initialize</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_connect</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">perform_setup</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_extension</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_schema_if_not_exists</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_create_tables_if_not_exists</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_is_initialized</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_node_to_table_row</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">(</span>
            <span class="n">node_id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="n">text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
            <span class="n">metadata_</span><span class="o">=</span><span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
                <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_to_table_row</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
                <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_to_table_row</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
            <span class="k">await</span> <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">_to_postgres_operator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">operator</span><span class="p">:</span> <span class="n">FilterOperator</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">GT</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"&gt;"</span>
        <span class="k">elif</span> <span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">NE</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"!="</span>
        <span class="k">elif</span> <span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">LTE</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"&lt;="</span>
        <span class="k">elif</span> <span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">NIN</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"NOT IN"</span>
        <span class="k">elif</span> <span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">CONTAINS</span><span class="p">:</span>
            <span class="c1"># Expects a list stored in the metadata, and a single value to compare</span>
            <span class="k">return</span> <span class="n">text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"metadata_::jsonb-&gt;'</span><span class="si">{</span><span class="n">filter_</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2">' "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_to_postgres_operator</span><span class="p">(</span><span class="n">filter_</span><span class="o">.</span><span class="n">operator</span><span class="p">)</span><span class="si">}</span><span class="s2"> "</span>
                <span class="sa">f</span><span class="s2">"'[</span><span class="se">\"</span><span class="si">{</span><span class="n">filter_</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\"</span><span class="s2">]'"</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Check if value is a number. If so, cast the metadata value to a float</span>
            <span class="c1"># This is necessary because the metadata is stored as a string</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"(metadata_-&gt;&gt;'</span><span class="si">{</span><span class="n">filter_</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2">')::float "</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_to_postgres_operator</span><span class="p">(</span><span class="n">filter_</span><span class="o">.</span><span class="n">operator</span><span class="p">)</span><span class="si">}</span><span class="s2"> "</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="nb">float</span><span class="p">(</span><span class="n">filter_</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                <span class="c1"># If not a number, then treat it as a string</span>
                <span class="k">return</span> <span class="n">text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"metadata_-&gt;&gt;'</span><span class="si">{</span><span class="n">filter_</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2">' "</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_to_postgres_operator</span><span class="p">(</span><span class="n">filter_</span><span class="o">.</span><span class="n">operator</span><span class="p">)</span><span class="si">}</span><span class="s2"> "</span>
                    <span class="sa">f</span><span class="s2">"'</span><span class="si">{</span><span class="n">filter_</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">'"</span>
                <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_recursively_apply_filters</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filters</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a sqlalchemy where clause.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">sqlalchemy</span>

        <span class="n">sqlalchemy_conditions</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"or"</span><span class="p">:</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">or_</span><span class="p">,</span>
            <span class="s2">"and"</span><span class="p">:</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">and_</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="k">if</span> <span class="n">filters</span><span class="o">.</span><span class="n">condition</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">sqlalchemy_conditions</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Invalid condition: </span><span class="si">{</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="si">}</span><span class="s2">. "</span>
                <span class="sa">f</span><span class="s2">"Must be one of </span><span class="si">{</span><span class="nb">list</span><span class="p">(</span><span class="n">sqlalchemy_conditions</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">sqlalchemy_conditions</span><span class="p">[</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="p">](</span>
            <span class="o">*</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_build_filter_clause</span><span class="p">(</span><span class="n">filter_</span><span class="p">)</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">filter_</span><span class="p">,</span> <span class="n">MetadataFilters</span><span class="p">)</span>
                    <span class="k">else</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursively_apply_filters</span><span class="p">(</span><span class="n">filter_</span><span class="p">)</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">filter_</span> <span class="ow">in</span> <span class="n">filters</span><span class="o">.</span><span class="n">filters</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_apply_filters_and_limit</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">stmt</span><span class="p">:</span> <span class="n">Select</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">metadata_filters</span><span class="p">:</span>
            <span class="n">stmt</span> <span class="o">=</span> <span class="n">stmt</span><span class="o">.</span><span class="n">where</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_recursively_apply_filters</span><span class="p">(</span><span class="n">metadata_filters</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">stmt</span><span class="o">.</span><span class="n">limit</span><span class="p">(</span><span class="n">limit</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

    <span class="k">def</span> <span class="nf">_build_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span><span class="p">,</span> <span class="n">text</span>

        <span class="n">stmt</span> <span class="o">=</span> <span class="n">select</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">embedding</span><span class="o">.</span><span class="n">cosine_distance</span><span class="p">(</span><span class="n">embedding</span><span class="p">)</span><span class="o">.</span><span class="n">label</span><span class="p">(</span><span class="s2">"distance"</span><span class="p">),</span>
        <span class="p">)</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="n">text</span><span class="p">(</span><span class="s2">"distance asc"</span><span class="p">))</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_filters_and_limit</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query_with_score</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="n">stmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_query</span><span class="p">(</span><span class="n">embedding</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">text</span>

            <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"ivfflat_probes"</span><span class="p">):</span>
                <span class="n">ivfflat_probes</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"ivfflat_probes"</span><span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="n">text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SET ivfflat.probes = :ivfflat_probes"</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"ivfflat_probes"</span><span class="p">:</span> <span class="n">ivfflat_probes</span><span class="p">},</span>
                <span class="p">)</span>
            <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hnsw_ef_search"</span><span class="p">):</span>
                <span class="n">hnsw_ef_search</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hnsw_ef_search"</span><span class="p">)</span>
                <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="n">text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SET hnsw.ef_search = :hnsw_ef_search"</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"hnsw_ef_search"</span><span class="p">:</span> <span class="n">hnsw_ef_search</span><span class="p">},</span>
                <span class="p">)</span>

            <span class="n">res</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                <span class="n">stmt</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">DBEmbeddingRow</span><span class="p">(</span>
                    <span class="n">node_id</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
                    <span class="n">similarity</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">item</span><span class="o">.</span><span class="n">distance</span><span class="p">)</span> <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">distance</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="mi">0</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
            <span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery_with_score</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="n">stmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_query</span><span class="p">(</span><span class="n">embedding</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">async_session</span><span class="p">,</span> <span class="n">async_session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">text</span>

            <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hnsw_ef_search"</span><span class="p">):</span>
                <span class="n">hnsw_ef_search</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hnsw_ef_search"</span><span class="p">)</span>
                <span class="k">await</span> <span class="n">async_session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="n">text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SET hnsw.ef_search = :hnsw_ef_search"</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"hnsw_ef_search"</span><span class="p">:</span> <span class="n">hnsw_ef_search</span><span class="p">},</span>
                <span class="p">)</span>
            <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"ivfflat_probes"</span><span class="p">):</span>
                <span class="n">ivfflat_probes</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"ivfflat_probes"</span><span class="p">)</span>
                <span class="k">await</span> <span class="n">async_session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
                    <span class="n">text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"SET ivfflat.probes = :ivfflat_probes"</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"ivfflat_probes"</span><span class="p">:</span> <span class="n">ivfflat_probes</span><span class="p">},</span>
                <span class="p">)</span>

            <span class="n">res</span> <span class="o">=</span> <span class="k">await</span> <span class="n">async_session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">DBEmbeddingRow</span><span class="p">(</span>
                    <span class="n">node_id</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
                    <span class="n">similarity</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">item</span><span class="o">.</span><span class="n">distance</span><span class="p">)</span> <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">distance</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="mi">0</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
            <span class="p">]</span>

    <span class="k">def</span> <span class="nf">_build_sparse_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">select</span><span class="p">,</span> <span class="n">type_coerce</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.sql</span> <span class="kn">import</span> <span class="n">func</span><span class="p">,</span> <span class="n">text</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy.types</span> <span class="kn">import</span> <span class="n">UserDefinedType</span>

        <span class="k">class</span> <span class="nc">REGCONFIG</span><span class="p">(</span><span class="n">UserDefinedType</span><span class="p">):</span>
            <span class="c1"># The TypeDecorator.cache_ok class-level flag indicates if this custom TypeDecorator is safe to be used as part of a cache key.</span>
            <span class="c1"># If the TypeDecorator is not guaranteed to produce the same bind/result behavior and SQL generation every time,</span>
            <span class="c1"># this flag should be set to False; otherwise if the class produces the same behavior each time, it may be set to True.</span>
            <span class="n">cache_ok</span> <span class="o">=</span> <span class="kc">True</span>

            <span class="k">def</span> <span class="nf">get_col_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
                <span class="k">return</span> <span class="s2">"regconfig"</span>

        <span class="k">if</span> <span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str must be specified for a sparse vector query."</span><span class="p">)</span>

        <span class="c1"># Replace '&amp;' with '|' to perform an OR search for higher recall</span>
        <span class="n">ts_query</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="n">to_tsquery</span><span class="p">(</span>
            <span class="n">func</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
                <span class="n">func</span><span class="o">.</span><span class="n">text</span><span class="p">(</span>
                    <span class="n">func</span><span class="o">.</span><span class="n">plainto_tsquery</span><span class="p">(</span>
                        <span class="n">type_coerce</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_search_config</span><span class="p">,</span> <span class="n">REGCONFIG</span><span class="p">),</span> <span class="n">query_str</span>
                    <span class="p">)</span>
                <span class="p">),</span>
                <span class="s2">"&amp;"</span><span class="p">,</span>
                <span class="s2">"|"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">stmt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">select</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
                <span class="n">func</span><span class="o">.</span><span class="n">ts_rank</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">text_search_tsv</span><span class="p">,</span> <span class="n">ts_query</span><span class="p">)</span><span class="o">.</span><span class="n">label</span><span class="p">(</span><span class="s2">"rank"</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">text_search_tsv</span><span class="o">.</span><span class="n">op</span><span class="p">(</span><span class="s2">"@@"</span><span class="p">)(</span><span class="n">ts_query</span><span class="p">))</span>
            <span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="n">text</span><span class="p">(</span><span class="s2">"rank desc"</span><span class="p">))</span>
        <span class="p">)</span>

        <span class="c1"># type: ignore</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_filters_and_limit</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_sparse_query_with_rank</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="n">stmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_sparse_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">async_session</span><span class="p">,</span> <span class="n">async_session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="n">res</span> <span class="o">=</span> <span class="k">await</span> <span class="n">async_session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">DBEmbeddingRow</span><span class="p">(</span>
                    <span class="n">node_id</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
                    <span class="n">similarity</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">rank</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
            <span class="p">]</span>

    <span class="k">def</span> <span class="nf">_sparse_query_with_rank</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="n">stmt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_sparse_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">limit</span><span class="p">,</span> <span class="n">metadata_filters</span><span class="p">)</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="n">res</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">DBEmbeddingRow</span><span class="p">(</span>
                    <span class="n">node_id</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">metadata_</span><span class="p">,</span>
                    <span class="n">similarity</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">rank</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
            <span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_hybrid_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="kn">import</span> <span class="nn">asyncio</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"postgres hybrid search does not support alpha parameter."</span><span class="p">)</span>

        <span class="n">sparse_top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">sparse_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_aquery_with_score</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_async_sparse_query_with_rank</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">sparse_top_k</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span>
            <span class="p">),</span>
        <span class="p">)</span>

        <span class="n">dense_results</span><span class="p">,</span> <span class="n">sparse_results</span> <span class="o">=</span> <span class="n">results</span>
        <span class="n">all_results</span> <span class="o">=</span> <span class="n">dense_results</span> <span class="o">+</span> <span class="n">sparse_results</span>
        <span class="k">return</span> <span class="n">_dedup_results</span><span class="p">(</span><span class="n">all_results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_hybrid_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"postgres hybrid search does not support alpha parameter."</span><span class="p">)</span>

        <span class="n">sparse_top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">sparse_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

        <span class="n">dense_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_with_score</span><span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">sparse_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_query_with_rank</span><span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">sparse_top_k</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span>
        <span class="p">)</span>

        <span class="n">all_results</span> <span class="o">=</span> <span class="n">dense_results</span> <span class="o">+</span> <span class="n">sparse_results</span>
        <span class="k">return</span> <span class="n">_dedup_results</span><span class="p">(</span><span class="n">all_results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_db_rows_to_query_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">rows</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">DBEmbeddingRow</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">db_embedding_row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">text</span><span class="p">))</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">similarity</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">db_embedding_row</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span>
            <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aquery_with_score</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query mode: </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_rows_to_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_with_score</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query mode: </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_rows_to_query_result</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">delete</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_initialize</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">,</span> <span class="n">session</span><span class="o">.</span><span class="n">begin</span><span class="p">():</span>
            <span class="n">stmt</span> <span class="o">=</span> <span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="p">)</span><span class="o">.</span><span class="n">where</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_table_class</span><span class="o">.</span><span class="n">metadata_</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span><span class="o">.</span><span class="n">astext</span> <span class="o">==</span> <span class="n">ref_doc_id</span>
            <span class="p">)</span>

            <span class="n">session</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">stmt</span><span class="p">)</span>
            <span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### from\_params `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/#llama_index.vector_stores.postgres.PGVectorStore.from_params "Permanent link")

```
from_params(host: Optional[str] = None, port: Optional[str] = None, database: Optional[str] = None, user: Optional[str] = None, password: Optional[str] = None, table_name: str = 'llamaindex', schema_name: str = 'public', connection_string: Optional[Union[str, URL]] = None, async_connection_string: Optional[Union[str, URL]] = None, hybrid_search: bool = False, text_search_config: str = 'english', embed_dim: int = 1536, cache_ok: bool = False, perform_setup: bool = True, debug: bool = False, use_jsonb: bool = False) -> [PGVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/#llama_index.vector_stores.postgres.PGVectorStore "llama_index.vector_stores.postgres.base.PGVectorStore")
```

Return connection string from database parameters.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-postgres/llama_index/vector_stores/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">224</span>
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
<span class="normal">264</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llamaindex"</span><span class="p">,</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">async_connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">sqlalchemy</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">URL</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">text_search_config</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"english"</span><span class="p">,</span>
    <span class="n">embed_dim</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1536</span><span class="p">,</span>
    <span class="n">cache_ok</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PGVectorStore"</span><span class="p">:</span>
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
        <span class="n">hybrid_search</span><span class="o">=</span><span class="n">hybrid_search</span><span class="p">,</span>
        <span class="n">text_search_config</span><span class="o">=</span><span class="n">text_search_config</span><span class="p">,</span>
        <span class="n">embed_dim</span><span class="o">=</span><span class="n">embed_dim</span><span class="p">,</span>
        <span class="n">cache_ok</span><span class="o">=</span><span class="n">cache_ok</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
        <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pinecone](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/)[Next Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/)
