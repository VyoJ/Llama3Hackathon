Title: Simple directory reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/

Markdown Content:
Simple directory reader - LlamaIndex


Simple reader that reads files of different formats from a directory.

SimpleDirectoryReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`, `ResourcesReaderMixin`, `FileSystemReaderMixin`

Simple directory reader.

Load files from file directory. Automatically select the best file reader given file extensions.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_dir` | `str` | 
Path to the directory.



 | `None` |
| `input_files` | `List` | 

List of file paths to read (Optional; overrides input\_dir, exclude)



 | `None` |
| `exclude` | `List` | 

glob of python file paths to exclude (Optional)



 | `None` |
| `exclude_hidden` | `bool` | 

Whether to exclude hidden files (dotfiles).



 | `True` |
| `encoding` | `str` | 

Encoding of the files. Default is utf-8.



 | `'utf-8'` |
| `errors` | `str` | 

how encoding and decoding errors are to be handled, see https://docs.python.org/3/library/functions.html#open



 | `'ignore'` |
| `recursive` | `bool` | 

Whether to recursively search in subdirectories. False by default.



 | `False` |
| `filename_as_id` | `bool` | 

Whether to use the filename as the document id. False by default.



 | `False` |
| `required_exts` | `Optional[List[str]]` | 

List of required extensions. Default is None.



 | `None` |
| `file_extractor` | `Optional[Dict[str, [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")]]` | 

A mapping of file extension to a BaseReader class that specifies how to convert that file to text. If not specified, use default from DEFAULT\_FILE\_READER\_CLS.



 | `None` |
| `num_files_limit` | `Optional[int]` | 

Maximum number of files to read. Default is None.



 | `None` |
| `file_metadata` | `Optional[Callable[str, Dict]]` | 

A function that takes in a filename and returns a Dict of metadata for the Document. Default is None.



 | `None` |
| `raise_on_error` | `bool` | 

Whether to raise an error if a file cannot be read.



 | `False` |
| `fs` | `Optional[AbstractFileSystem]` | 

File system to use. Defaults



 | `None` |

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">177</span>
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
<span class="normal">771</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleDirectoryReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">,</span> <span class="n">ResourcesReaderMixin</span><span class="p">,</span> <span class="n">FileSystemReaderMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Simple directory reader.</span>

<span class="sd">    Load files from file directory.</span>
<span class="sd">    Automatically select the best file reader given file extensions.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_dir (str): Path to the directory.</span>
<span class="sd">        input_files (List): List of file paths to read</span>
<span class="sd">            (Optional; overrides input_dir, exclude)</span>
<span class="sd">        exclude (List): glob of python file paths to exclude (Optional)</span>
<span class="sd">        exclude_hidden (bool): Whether to exclude hidden files (dotfiles).</span>
<span class="sd">        encoding (str): Encoding of the files.</span>
<span class="sd">            Default is utf-8.</span>
<span class="sd">        errors (str): how encoding and decoding errors are to be handled,</span>
<span class="sd">              see https://docs.python.org/3/library/functions.html#open</span>
<span class="sd">        recursive (bool): Whether to recursively search in subdirectories.</span>
<span class="sd">            False by default.</span>
<span class="sd">        filename_as_id (bool): Whether to use the filename as the document id.</span>
<span class="sd">            False by default.</span>
<span class="sd">        required_exts (Optional[List[str]]): List of required extensions.</span>
<span class="sd">            Default is None.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. If not specified, use default from DEFAULT_FILE_READER_CLS.</span>
<span class="sd">        num_files_limit (Optional[int]): Maximum number of files to read.</span>
<span class="sd">            Default is None.</span>
<span class="sd">        file_metadata (Optional[Callable[str, Dict]]): A function that takes</span>
<span class="sd">            in a filename and returns a Dict of metadata for the Document.</span>
<span class="sd">            Default is None.</span>
<span class="sd">        raise_on_error (bool): Whether to raise an error if a file cannot be read.</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): File system to use. Defaults</span>
<span class="sd">        to using the local file system. Can be changed to use any remote file system</span>
<span class="sd">        exposed via the fsspec interface.</span>
<span class="sd">    """</span>

    <span class="n">supported_suffix_fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">_try_loading_included_file_formats</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">input_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">input_files</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">exclude</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">exclude_hidden</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
        <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">encoding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span>
        <span class="n">filename_as_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">required_exts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_files_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">raise_on_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">input_dir</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">input_files</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either `input_dir` or `input_files`."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">errors</span> <span class="o">=</span> <span class="n">errors</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="o">=</span> <span class="n">encoding</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span> <span class="o">=</span> <span class="n">exclude</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span> <span class="o">=</span> <span class="n">recursive</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">exclude_hidden</span> <span class="o">=</span> <span class="n">exclude_hidden</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">required_exts</span> <span class="o">=</span> <span class="n">required_exts</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_files_limit</span> <span class="o">=</span> <span class="n">num_files_limit</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span> <span class="o">=</span> <span class="n">raise_on_error</span>
        <span class="n">_Path</span> <span class="o">=</span> <span class="n">Path</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">PurePosixPath</span>

        <span class="k">if</span> <span class="n">input_files</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">input_files</span><span class="p">:</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"File </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> does not exist."</span><span class="p">)</span>
                <span class="n">input_file</span> <span class="o">=</span> <span class="n">_Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">input_dir</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">input_dir</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Directory </span><span class="si">{</span><span class="n">input_dir</span><span class="si">}</span><span class="s2"> does not exist."</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">input_dir</span> <span class="o">=</span> <span class="n">_Path</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span> <span class="o">=</span> <span class="n">exclude</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_files</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_dir</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">file_extractor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span> <span class="o">=</span> <span class="n">file_metadata</span> <span class="ow">or</span> <span class="n">_DefaultFileMetadataFunc</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span> <span class="o">=</span> <span class="n">filename_as_id</span>

    <span class="k">def</span> <span class="nf">is_hidden</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">part</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"."</span><span class="p">)</span> <span class="ow">and</span> <span class="n">part</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"."</span><span class="p">,</span> <span class="s2">".."</span><span class="p">]</span> <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">path</span><span class="o">.</span><span class="n">parts</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_add_files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_dir</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add files."""</span>
        <span class="n">all_files</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">rejected_files</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">rejected_dirs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="c1"># Default to POSIX paths for non-default file systems (e.g. S3)</span>
        <span class="n">_Path</span> <span class="o">=</span> <span class="n">Path</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">PurePosixPath</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">excluded_pattern</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
                    <span class="c1"># Recursive glob</span>
                    <span class="n">excluded_glob</span> <span class="o">=</span> <span class="n">_Path</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">_Path</span><span class="p">(</span><span class="s2">"**"</span><span class="p">)</span> <span class="o">/</span> <span class="n">excluded_pattern</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># Non-recursive glob</span>
                    <span class="n">excluded_glob</span> <span class="o">=</span> <span class="n">_Path</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">excluded_pattern</span>
                <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">excluded_glob</span><span class="p">)):</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">file</span><span class="p">):</span>
                        <span class="n">rejected_dirs</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">_Path</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">rejected_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">_Path</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>

        <span class="n">file_refs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
            <span class="n">file_refs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"/**/*"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">file_refs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"/*"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">ref</span> <span class="ow">in</span> <span class="n">file_refs</span><span class="p">:</span>
            <span class="c1"># Manually check if file is hidden or directory instead of</span>
            <span class="c1"># in glob for backwards compatibility.</span>
            <span class="n">ref</span> <span class="o">=</span> <span class="n">_Path</span><span class="p">(</span><span class="n">ref</span><span class="p">)</span>
            <span class="n">is_dir</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">ref</span><span class="p">)</span>
            <span class="n">skip_because_hidden</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude_hidden</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_hidden</span><span class="p">(</span><span class="n">ref</span><span class="p">)</span>
            <span class="n">skip_because_bad_ext</span> <span class="o">=</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">required_exts</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">ref</span><span class="o">.</span><span class="n">suffix</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_exts</span>
            <span class="p">)</span>
            <span class="n">skip_because_excluded</span> <span class="o">=</span> <span class="n">ref</span> <span class="ow">in</span> <span class="n">rejected_files</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">skip_because_excluded</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">is_dir</span><span class="p">:</span>
                    <span class="n">ref_parent_dir</span> <span class="o">=</span> <span class="n">ref</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">ref_parent_dir</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">_parent</span><span class="p">(</span><span class="n">ref</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">rejected_dir</span> <span class="ow">in</span> <span class="n">rejected_dirs</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">str</span><span class="p">(</span><span class="n">ref_parent_dir</span><span class="p">)</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">rejected_dir</span><span class="p">)):</span>
                        <span class="n">skip_because_excluded</span> <span class="o">=</span> <span class="kc">True</span>
                        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                            <span class="s2">"Skipping </span><span class="si">%s</span><span class="s2"> because it in parent dir </span><span class="si">%s</span><span class="s2"> which is in </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span>
                            <span class="n">ref</span><span class="p">,</span>
                            <span class="n">ref_parent_dir</span><span class="p">,</span>
                            <span class="n">rejected_dir</span><span class="p">,</span>
                        <span class="p">)</span>
                        <span class="k">break</span>

            <span class="k">if</span> <span class="p">(</span>
                <span class="n">is_dir</span>
                <span class="ow">or</span> <span class="n">skip_because_hidden</span>
                <span class="ow">or</span> <span class="n">skip_because_bad_ext</span>
                <span class="ow">or</span> <span class="n">skip_because_excluded</span>
            <span class="p">):</span>
                <span class="k">continue</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">all_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">ref</span><span class="p">)</span>

        <span class="n">new_input_files</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">all_files</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">new_input_files</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"No files found in </span><span class="si">{</span><span class="n">input_dir</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_files_limit</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_files_limit</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">new_input_files</span> <span class="o">=</span> <span class="n">new_input_files</span><span class="p">[</span><span class="mi">0</span> <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_files_limit</span><span class="p">]</span>

        <span class="c1"># print total number of files added</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"&gt; [SimpleDirectoryReader] Total files added: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">new_input_files</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">new_input_files</span>

    <span class="k">def</span> <span class="nf">_exclude_metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Exclude metadata from documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (List[Document]): List of documents.</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="c1"># Keep only metadata['file_path'] in both embedding and llm content</span>
            <span class="c1"># str, which contain extreme important context that about the chunks.</span>
            <span class="c1"># Dates is provided for convenience of postprocessor such as</span>
            <span class="c1"># TimeWeightedPostprocessor, but excluded for embedding and LLMprompts</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="s2">"file_name"</span><span class="p">,</span>
                    <span class="s2">"file_type"</span><span class="p">,</span>
                    <span class="s2">"file_size"</span><span class="p">,</span>
                    <span class="s2">"creation_date"</span><span class="p">,</span>
                    <span class="s2">"last_modified_date"</span><span class="p">,</span>
                    <span class="s2">"last_accessed_date"</span><span class="p">,</span>
                <span class="p">]</span>
            <span class="p">)</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="s2">"file_name"</span><span class="p">,</span>
                    <span class="s2">"file_type"</span><span class="p">,</span>
                    <span class="s2">"file_size"</span><span class="p">,</span>
                    <span class="s2">"creation_date"</span><span class="p">,</span>
                    <span class="s2">"last_modified_date"</span><span class="p">,</span>
                    <span class="s2">"last_accessed_date"</span><span class="p">,</span>
                <span class="p">]</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""List files in the given filesystem."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>

    <span class="k">def</span> <span class="nf">get_resource_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="n">info_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span>

        <span class="n">creation_date</span> <span class="o">=</span> <span class="n">_format_file_timestamp</span><span class="p">(</span>
            <span class="n">info_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"created"</span><span class="p">),</span> <span class="n">include_time</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>
        <span class="n">last_modified_date</span> <span class="o">=</span> <span class="n">_format_file_timestamp</span><span class="p">(</span>
            <span class="n">info_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"mtime"</span><span class="p">),</span> <span class="n">include_time</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

        <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">resource_id</span><span class="p">,</span>
            <span class="s2">"file_size"</span><span class="p">:</span> <span class="n">info_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"size"</span><span class="p">),</span>
            <span class="s2">"creation_date"</span><span class="p">:</span> <span class="n">creation_date</span><span class="p">,</span>
            <span class="s2">"last_modified_date"</span><span class="p">:</span> <span class="n">last_modified_date</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="c1"># Ignore None values</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">meta_key</span><span class="p">:</span> <span class="n">meta_value</span>
            <span class="k">for</span> <span class="n">meta_key</span><span class="p">,</span> <span class="n">meta_value</span> <span class="ow">in</span> <span class="n">info_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">meta_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_resource</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">file_metadata</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_metadata"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">)</span>
        <span class="n">file_extractor</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_extractor"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">)</span>
        <span class="n">filename_as_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"filename_as_id"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">)</span>
        <span class="n">encoding</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"encoding"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span>
        <span class="n">errors</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"errors"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">)</span>
        <span class="n">raise_on_error</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"raise_on_error"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">)</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fs"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span>

        <span class="n">path_func</span> <span class="o">=</span> <span class="n">Path</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">PurePosixPath</span>

        <span class="k">return</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">(</span>
            <span class="n">input_file</span><span class="o">=</span><span class="n">path_func</span><span class="p">(</span><span class="n">resource_id</span><span class="p">),</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="n">file_metadata</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="n">filename_as_id</span><span class="o">=</span><span class="n">filename_as_id</span><span class="p">,</span>
            <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">,</span>
            <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">,</span>
            <span class="n">raise_on_error</span><span class="o">=</span><span class="n">raise_on_error</span><span class="p">,</span>
            <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_resource</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">file_metadata</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_metadata"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">)</span>
        <span class="n">file_extractor</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_extractor"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">)</span>
        <span class="n">filename_as_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"filename_as_id"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">)</span>
        <span class="n">encoding</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"encoding"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span>
        <span class="n">errors</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"errors"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">)</span>
        <span class="n">raise_on_error</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"raise_on_error"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">)</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fs"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">aload_file</span><span class="p">(</span>
            <span class="n">input_file</span><span class="o">=</span><span class="n">Path</span><span class="p">(</span><span class="n">resource_id</span><span class="p">),</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="n">file_metadata</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="n">filename_as_id</span><span class="o">=</span><span class="n">filename_as_id</span><span class="p">,</span>
            <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">,</span>
            <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">,</span>
            <span class="n">raise_on_error</span><span class="o">=</span><span class="n">raise_on_error</span><span class="p">,</span>
            <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Read file content."""</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fs"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">load_file</span><span class="p">(</span>
        <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">file_metadata</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Dict</span><span class="p">],</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">],</span>
        <span class="n">filename_as_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">encoding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span>
        <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
        <span class="n">raise_on_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Static method for loading file.</span>

<span class="sd">        NOTE: necessarily as a static method for parallel processing.</span>

<span class="sd">        Args:</span>
<span class="sd">            input_file (Path): _description_</span>
<span class="sd">            file_metadata (Callable[[str], Dict]): _description_</span>
<span class="sd">            file_extractor (Dict[str, BaseReader]): _description_</span>
<span class="sd">            filename_as_id (bool, optional): _description_. Defaults to False.</span>
<span class="sd">            encoding (str, optional): _description_. Defaults to "utf-8".</span>
<span class="sd">            errors (str, optional): _description_. Defaults to "ignore".</span>
<span class="sd">            fs (Optional[fsspec.AbstractFileSystem], optional): _description_. Defaults to None.</span>

<span class="sd">        input_file (Path): File path to read</span>
<span class="sd">        file_metadata ([Callable[str, Dict]]): A function that takes</span>
<span class="sd">            in a filename and returns a Dict of metadata for the Document.</span>
<span class="sd">        file_extractor (Dict[str, BaseReader]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text.</span>
<span class="sd">        filename_as_id (bool): Whether to use the filename as the document id.</span>
<span class="sd">        encoding (str): Encoding of the files.</span>
<span class="sd">            Default is utf-8.</span>
<span class="sd">        errors (str): how encoding and decoding errors are to be handled,</span>
<span class="sd">              see https://docs.python.org/3/library/functions.html#open</span>
<span class="sd">        raise_on_error (bool): Whether to raise an error if a file cannot be read.</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): File system to use. Defaults</span>
<span class="sd">            to using the local file system. Can be changed to use any remote file system</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: loaded documents</span>
<span class="sd">        """</span>
        <span class="c1"># TODO: make this less redundant</span>
        <span class="n">default_file_reader_cls</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">supported_suffix_fn</span><span class="p">()</span>
        <span class="n">default_file_reader_suffix</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">default_file_reader_cls</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">file_metadata</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">file_metadata</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span>

        <span class="n">file_suffix</span> <span class="o">=</span> <span class="n">input_file</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">default_file_reader_suffix</span> <span class="ow">or</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">file_extractor</span><span class="p">:</span>
            <span class="c1"># use file readers</span>
            <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">file_extractor</span><span class="p">:</span>
                <span class="c1"># instantiate file reader if not already</span>
                <span class="n">reader_cls</span> <span class="o">=</span> <span class="n">default_file_reader_cls</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>
                <span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span> <span class="o">=</span> <span class="n">reader_cls</span><span class="p">()</span>
            <span class="n">reader</span> <span class="o">=</span> <span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>

            <span class="c1"># load data -- catch all errors except for ImportError</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"extra_info"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">}</span>
                <span class="k">if</span> <span class="n">fs</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">):</span>
                    <span class="n">kwargs</span><span class="p">[</span><span class="s2">"fs"</span><span class="p">]</span> <span class="o">=</span> <span class="n">fs</span>
                <span class="n">docs</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="c1"># ensure that ImportError is raised so user knows</span>
                <span class="c1"># about missing dependencies</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">raise_on_error</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Error loading file"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
                <span class="c1"># otherwise, just skip the file and report the error</span>
                <span class="nb">print</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Failed to load file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">. Skipping..."</span><span class="p">,</span>
                    <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="p">[]</span>

            <span class="c1"># iterate over docs if needed</span>
            <span class="k">if</span> <span class="n">filename_as_id</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
                    <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">input_file</span><span class="si">!s}</span><span class="s2">_part_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># do standard read</span>
            <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">)</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="k">if</span> <span class="n">filename_as_id</span><span class="p">:</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file asynchronously."""</span>
        <span class="c1"># TODO: make this less redundant</span>
        <span class="n">default_file_reader_cls</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">supported_suffix_fn</span><span class="p">()</span>
        <span class="n">default_file_reader_suffix</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">default_file_reader_cls</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span>

        <span class="n">file_suffix</span> <span class="o">=</span> <span class="n">input_file</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">default_file_reader_suffix</span>
            <span class="ow">or</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span>
        <span class="p">):</span>
            <span class="c1"># use file readers</span>
            <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">:</span>
                <span class="c1"># instantiate file reader if not already</span>
                <span class="n">reader_cls</span> <span class="o">=</span> <span class="n">default_file_reader_cls</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span> <span class="o">=</span> <span class="n">reader_cls</span><span class="p">()</span>
            <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>

            <span class="c1"># load data -- catch all errors except for ImportError</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"extra_info"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">}</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">):</span>
                    <span class="n">kwargs</span><span class="p">[</span><span class="s2">"fs"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>
                <span class="n">docs</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">aload_data</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="c1"># ensure that ImportError is raised so user knows</span>
                <span class="c1"># about missing dependencies</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">:</span>
                    <span class="k">raise</span>
                <span class="c1"># otherwise, just skip the file and report the error</span>
                <span class="nb">print</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Failed to load file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">. Skipping..."</span><span class="p">,</span>
                    <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="p">[]</span>

            <span class="c1"># iterate over docs if needed</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
                    <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">input_file</span><span class="si">!s}</span><span class="s2">_part_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># do standard read</span>
            <span class="n">fs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">)</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">:</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">            num_workers  (Optional[int]): Number of workers to parallelize data-loading over.</span>
<span class="sd">            fs (Optional[fsspec.AbstractFileSystem]): File system to use. If fs was specified</span>
<span class="sd">                in the constructor, it will override the fs parameter here.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>

        <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">():</span>
                <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                    <span class="s2">"Specified num_workers exceed number of CPUs in the system. "</span>
                    <span class="s2">"Setting `num_workers` down to the maximum CPU count."</span>
                <span class="p">)</span>
            <span class="k">with</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">get_context</span><span class="p">(</span><span class="s2">"spawn"</span><span class="p">)</span><span class="o">.</span><span class="n">Pool</span><span class="p">(</span><span class="n">num_workers</span><span class="p">)</span> <span class="k">as</span> <span class="n">p</span><span class="p">:</span>
                <span class="n">results</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">starmap</span><span class="p">(</span>
                    <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">,</span>
                    <span class="nb">zip</span><span class="p">(</span>
                        <span class="n">files_to_process</span><span class="p">,</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">),</span>
                        <span class="n">repeat</span><span class="p">(</span><span class="n">fs</span><span class="p">),</span>
                    <span class="p">),</span>
                <span class="p">)</span>
                <span class="n">documents</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">results</span><span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                <span class="n">files_to_process</span> <span class="o">=</span> <span class="n">tqdm</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Loading files"</span><span class="p">,</span> <span class="n">unit</span><span class="o">=</span><span class="s2">"file"</span>
                <span class="p">)</span>
            <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">(</span>
                        <span class="n">input_file</span><span class="o">=</span><span class="n">input_file</span><span class="p">,</span>
                        <span class="n">file_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">,</span>
                        <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
                        <span class="n">filename_as_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">,</span>
                        <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span>
                        <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span>
                        <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">,</span>
                        <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">            num_workers  (Optional[int]): Number of workers to parallelize data-loading over.</span>
<span class="sd">            fs (Optional[fsspec.AbstractFileSystem]): File system to use. If fs was specified</span>
<span class="sd">                in the constructor, it will override the fs parameter here.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>

        <span class="n">coroutines</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">aload_file</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span> <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">num_workers</span><span class="p">:</span>
            <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
                <span class="n">coroutines</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="n">num_workers</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="n">_asyncio</span> <span class="o">=</span> <span class="n">get_asyncio_module</span><span class="p">(</span><span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">)</span>
            <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">coroutines</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">coroutines</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span> <span class="k">for</span> <span class="n">doc_list</span> <span class="ow">in</span> <span class="n">document_lists</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">doc_list</span><span class="p">]</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">iter_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data iteratively from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Generator[List[Document]]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>

        <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="n">files_to_process</span> <span class="o">=</span> <span class="n">tqdm</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_files</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Loading files"</span><span class="p">,</span> <span class="n">unit</span><span class="o">=</span><span class="s2">"file"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">:</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">(</span>
                <span class="n">input_file</span><span class="o">=</span><span class="n">input_file</span><span class="p">,</span>
                <span class="n">file_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">,</span>
                <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
                <span class="n">filename_as_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">,</span>
                <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span>
                <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span>
                <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">,</span>
                <span class="n">fs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">yield</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### list\_resources [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.list_resources "Permanent link")

```
list_resources(*args: Any, **kwargs: Any) -> List[Path]
```

List files in the given filesystem.

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Path</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""List files in the given filesystem."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>
</code></pre></div></td></tr></tbody></table>

### read\_file\_content [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.read_file_content "Permanent link")

```
read_file_content(input_file: Path, **kwargs) -> bytes
```

Read file content.

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Read file content."""</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fs"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">)</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_file `staticmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.load_file "Permanent link")

```
load_file(input_file: Path, file_metadata: Callable[[str], Dict], file_extractor: Dict[str, [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")], filename_as_id: bool = False, encoding: str = 'utf-8', errors: str = 'ignore', raise_on_error: bool = False, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Static method for loading file.

NOTE: necessarily as a static method for parallel processing.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_file` | `Path` | 
_description_



 | _required_ |
| `file_metadata` | `Callable[[str], Dict]` | 

_description_



 | _required_ |
| `file_extractor` | `Dict[str, [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")]` | 

_description_



 | _required_ |
| `filename_as_id` | `bool` | 

_description_. Defaults to False.



 | `False` |
| `encoding` | `str` | 

_description_. Defaults to "utf-8".



 | `'utf-8'` |
| `errors` | `str` | 

_description_. Defaults to "ignore".



 | `'ignore'` |
| `fs` | `Optional[AbstractFileSystem]` | 

_description_. Defaults to None.



 | `None` |

input\_file (Path): File path to read file\_metadata (\[Callable\[str, Dict\]\]): A function that takes in a filename and returns a Dict of metadata for the Document. file\_extractor (Dict\[str, BaseReader\]): A mapping of file extension to a BaseReader class that specifies how to convert that file to text. filename\_as\_id (bool): Whether to use the filename as the document id. encoding (str): Encoding of the files. Default is utf-8. errors (str): how encoding and decoding errors are to be handled, see https://docs.python.org/3/library/functions.html#open raise\_on\_error (bool): Whether to raise an error if a file cannot be read. fs (Optional\[fsspec.AbstractFileSystem\]): File system to use. Defaults to using the local file system. Can be changed to use any remote file system

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: loaded documents



 |

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">474</span>
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
<span class="normal">573</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@staticmethod</span>
<span class="k">def</span> <span class="nf">load_file</span><span class="p">(</span>
    <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">file_metadata</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Dict</span><span class="p">],</span>
    <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">],</span>
    <span class="n">filename_as_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">encoding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span>
    <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
    <span class="n">raise_on_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Static method for loading file.</span>

<span class="sd">    NOTE: necessarily as a static method for parallel processing.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_file (Path): _description_</span>
<span class="sd">        file_metadata (Callable[[str], Dict]): _description_</span>
<span class="sd">        file_extractor (Dict[str, BaseReader]): _description_</span>
<span class="sd">        filename_as_id (bool, optional): _description_. Defaults to False.</span>
<span class="sd">        encoding (str, optional): _description_. Defaults to "utf-8".</span>
<span class="sd">        errors (str, optional): _description_. Defaults to "ignore".</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem], optional): _description_. Defaults to None.</span>

<span class="sd">    input_file (Path): File path to read</span>
<span class="sd">    file_metadata ([Callable[str, Dict]]): A function that takes</span>
<span class="sd">        in a filename and returns a Dict of metadata for the Document.</span>
<span class="sd">    file_extractor (Dict[str, BaseReader]): A mapping of file</span>
<span class="sd">        extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">        to text.</span>
<span class="sd">    filename_as_id (bool): Whether to use the filename as the document id.</span>
<span class="sd">    encoding (str): Encoding of the files.</span>
<span class="sd">        Default is utf-8.</span>
<span class="sd">    errors (str): how encoding and decoding errors are to be handled,</span>
<span class="sd">          see https://docs.python.org/3/library/functions.html#open</span>
<span class="sd">    raise_on_error (bool): Whether to raise an error if a file cannot be read.</span>
<span class="sd">    fs (Optional[fsspec.AbstractFileSystem]): File system to use. Defaults</span>
<span class="sd">        to using the local file system. Can be changed to use any remote file system</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: loaded documents</span>
<span class="sd">    """</span>
    <span class="c1"># TODO: make this less redundant</span>
    <span class="n">default_file_reader_cls</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">supported_suffix_fn</span><span class="p">()</span>
    <span class="n">default_file_reader_suffix</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">default_file_reader_cls</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="n">file_metadata</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">file_metadata</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span>

    <span class="n">file_suffix</span> <span class="o">=</span> <span class="n">input_file</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">default_file_reader_suffix</span> <span class="ow">or</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">file_extractor</span><span class="p">:</span>
        <span class="c1"># use file readers</span>
        <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">file_extractor</span><span class="p">:</span>
            <span class="c1"># instantiate file reader if not already</span>
            <span class="n">reader_cls</span> <span class="o">=</span> <span class="n">default_file_reader_cls</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>
            <span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span> <span class="o">=</span> <span class="n">reader_cls</span><span class="p">()</span>
        <span class="n">reader</span> <span class="o">=</span> <span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>

        <span class="c1"># load data -- catch all errors except for ImportError</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"extra_info"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">}</span>
            <span class="k">if</span> <span class="n">fs</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">):</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"fs"</span><span class="p">]</span> <span class="o">=</span> <span class="n">fs</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># ensure that ImportError is raised so user knows</span>
            <span class="c1"># about missing dependencies</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">raise_on_error</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Error loading file"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
            <span class="c1"># otherwise, just skip the file and report the error</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Failed to load file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">. Skipping..."</span><span class="p">,</span>
                <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="c1"># iterate over docs if needed</span>
        <span class="k">if</span> <span class="n">filename_as_id</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">input_file</span><span class="si">!s}</span><span class="s2">_part_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># do standard read</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="n">errors</span><span class="p">)</span>

        <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="k">if</span> <span class="n">filename_as_id</span><span class="p">:</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>

        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### aload\_file `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.aload_file "Permanent link")

```
aload_file(input_file: Path) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file asynchronously.

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">575</span>
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
<span class="normal">636</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aload_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file asynchronously."""</span>
    <span class="c1"># TODO: make this less redundant</span>
    <span class="n">default_file_reader_cls</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">supported_suffix_fn</span><span class="p">()</span>
    <span class="n">default_file_reader_suffix</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">default_file_reader_cls</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span>

    <span class="n">file_suffix</span> <span class="o">=</span> <span class="n">input_file</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">file_suffix</span> <span class="ow">in</span> <span class="n">default_file_reader_suffix</span>
        <span class="ow">or</span> <span class="n">file_suffix</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span>
    <span class="p">):</span>
        <span class="c1"># use file readers</span>
        <span class="k">if</span> <span class="n">file_suffix</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">:</span>
            <span class="c1"># instantiate file reader if not already</span>
            <span class="n">reader_cls</span> <span class="o">=</span> <span class="n">default_file_reader_cls</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span> <span class="o">=</span> <span class="n">reader_cls</span><span class="p">()</span>
        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">[</span><span class="n">file_suffix</span><span class="p">]</span>

        <span class="c1"># load data -- catch all errors except for ImportError</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"extra_info"</span><span class="p">:</span> <span class="n">metadata</span><span class="p">}</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">):</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"fs"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">aload_data</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># ensure that ImportError is raised so user knows</span>
            <span class="c1"># about missing dependencies</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">:</span>
                <span class="k">raise</span>
            <span class="c1"># otherwise, just skip the file and report the error</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Failed to load file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">. Skipping..."</span><span class="p">,</span>
                <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="c1"># iterate over docs if needed</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">input_file</span><span class="si">!s}</span><span class="s2">_part_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># do standard read</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span> <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">)</span>

        <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">:</span>
            <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>

        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.load_data "Permanent link")

```
load_data(show_progress: bool = False, num_workers: Optional[int] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `num_workers` | ` (Optional[int]` | 

Number of workers to parallelize data-loading over.



 | `None` |
| `fs` | `Optional[AbstractFileSystem]` | 

File system to use. If fs was specified in the constructor, it will override the fs parameter here.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">638</span>
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
<span class="normal">702</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">        num_workers  (Optional[int]): Number of workers to parallelize data-loading over.</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): File system to use. If fs was specified</span>
<span class="sd">            in the constructor, it will override the fs parameter here.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>

    <span class="k">if</span> <span class="n">num_workers</span> <span class="ow">and</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">num_workers</span> <span class="o">&gt;</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">cpu_count</span><span class="p">():</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"Specified num_workers exceed number of CPUs in the system. "</span>
                <span class="s2">"Setting `num_workers` down to the maximum CPU count."</span>
            <span class="p">)</span>
        <span class="k">with</span> <span class="n">multiprocessing</span><span class="o">.</span><span class="n">get_context</span><span class="p">(</span><span class="s2">"spawn"</span><span class="p">)</span><span class="o">.</span><span class="n">Pool</span><span class="p">(</span><span class="n">num_workers</span><span class="p">)</span> <span class="k">as</span> <span class="n">p</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">starmap</span><span class="p">(</span>
                <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">,</span>
                <span class="nb">zip</span><span class="p">(</span>
                    <span class="n">files_to_process</span><span class="p">,</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">),</span>
                    <span class="n">repeat</span><span class="p">(</span><span class="n">fs</span><span class="p">),</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">results</span><span class="p">)</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="n">files_to_process</span> <span class="o">=</span> <span class="n">tqdm</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Loading files"</span><span class="p">,</span> <span class="n">unit</span><span class="o">=</span><span class="s2">"file"</span>
            <span class="p">)</span>
        <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">(</span>
                    <span class="n">input_file</span><span class="o">=</span><span class="n">input_file</span><span class="p">,</span>
                    <span class="n">file_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">,</span>
                    <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
                    <span class="n">filename_as_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">,</span>
                    <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span>
                    <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span>
                    <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">,</span>
                    <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aload\_data `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.aload_data "Permanent link")

```
aload_data(show_progress: bool = False, num_workers: Optional[int] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Whether to show tqdm progress bars. Defaults to False.



 | `False` |
| `num_workers` | ` (Optional[int]` | 

Number of workers to parallelize data-loading over.



 | `None` |
| `fs` | `Optional[AbstractFileSystem]` | 

File system to use. If fs was specified in the constructor, it will override the fs parameter here.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">704</span>
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
<span class="normal">737</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">num_workers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">        num_workers  (Optional[int]): Number of workers to parallelize data-loading over.</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): File system to use. If fs was specified</span>
<span class="sd">            in the constructor, it will override the fs parameter here.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span>

    <span class="n">coroutines</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">aload_file</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span> <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">num_workers</span><span class="p">:</span>
        <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">coroutines</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="n">num_workers</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">show_progress</span><span class="p">:</span>
        <span class="n">_asyncio</span> <span class="o">=</span> <span class="n">get_asyncio_module</span><span class="p">(</span><span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">)</span>
        <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">_asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">coroutines</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">document_lists</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">coroutines</span><span class="p">)</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span> <span class="k">for</span> <span class="n">doc_list</span> <span class="ow">in</span> <span class="n">document_lists</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">doc_list</span><span class="p">]</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### iter\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/#llama_index.core.readers.file.base.SimpleDirectoryReader.iter_data "Permanent link")

```
iter_data(show_progress: bool = False) -> Generator[List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], Any, Any]
```

Load data iteratively from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Whether to show tqdm progress bars. Defaults to False.



 | `False` |

**Returns:**

| Type | Description |
| --- | --- |
| `Generator[List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], Any, Any]` | 
Generator\[List\[Document\]\]: A list of documents.



 |

Source code in `llama-index-core/llama_index/core/readers/file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">739</span>
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
<span class="normal">771</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">iter_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load data iteratively from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Generator[List[Document]]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">files_to_process</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_files</span>

    <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
        <span class="n">files_to_process</span> <span class="o">=</span> <span class="n">tqdm</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_files</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Loading files"</span><span class="p">,</span> <span class="n">unit</span><span class="o">=</span><span class="s2">"file"</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">files_to_process</span><span class="p">:</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="o">.</span><span class="n">load_file</span><span class="p">(</span>
            <span class="n">input_file</span><span class="o">=</span><span class="n">input_file</span><span class="p">,</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_metadata</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="n">filename_as_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">filename_as_id</span><span class="p">,</span>
            <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">,</span>
            <span class="n">errors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">errors</span><span class="p">,</span>
            <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">raise_on_error</span><span class="p">,</span>
            <span class="n">fs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_metadata</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">yield</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Semanticscholar](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/)[Next Singlestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/)
