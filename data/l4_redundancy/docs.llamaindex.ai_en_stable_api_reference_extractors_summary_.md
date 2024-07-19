Title: Summary - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/

Markdown Content:
Summary - LlamaIndex


SummaryExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/#llama_index.core.extractors.SummaryExtractor "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Summary extractor. Node-level extractor with adjacent sharing. Extracts `section_summary`, `prev_section_summary`, `next_section_summary` metadata fields.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 
LLM



 | `None` |
| `summaries` | `List[str]` | 

list of summaries to extract: 'self', 'prev', 'next'



 | `['self']` |
| `prompt_template` | `str` | 

template for summary extraction



 | `DEFAULT_SUMMARY_EXTRACT_TEMPLATE` |

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">332</span>
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
<span class="normal">422</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SummaryExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Summary extractor. Node-level extractor with adjacent sharing.</span>
<span class="sd">    Extracts `section_summary`, `prev_section_summary`, `next_section_summary`</span>
<span class="sd">    metadata fields.</span>

<span class="sd">    Args:</span>
<span class="sd">        llm (Optional[LLM]): LLM</span>
<span class="sd">        summaries (List[str]): list of summaries to extract: 'self', 'prev', 'next'</span>
<span class="sd">        prompt_template (str): template for summary extraction</span>
<span class="sd">    """</span>

    <span class="n">llm</span><span class="p">:</span> <span class="n">LLMPredictorType</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The LLM to use for generation."</span><span class="p">)</span>
    <span class="n">summaries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"List of summaries to extract: 'self', 'prev', 'next'"</span>
    <span class="p">)</span>
    <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_SUMMARY_EXTRACT_TEMPLATE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Template to use when generating summaries."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">_self_summary</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_prev_summary</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_next_summary</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># TODO: llm_predictor arg is deprecated</span>
        <span class="n">llm_predictor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summaries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"self"</span><span class="p">],</span>
        <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_SUMMARY_EXTRACT_TEMPLATE</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_NUM_WORKERS</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="c1"># validation</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span><span class="n">s</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"self"</span><span class="p">,</span> <span class="s2">"prev"</span><span class="p">,</span> <span class="s2">"next"</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">summaries</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"summaries must be one of ['self', 'prev', 'next']"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_self_summary</span> <span class="o">=</span> <span class="s2">"self"</span> <span class="ow">in</span> <span class="n">summaries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prev_summary</span> <span class="o">=</span> <span class="s2">"prev"</span> <span class="ow">in</span> <span class="n">summaries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_next_summary</span> <span class="o">=</span> <span class="s2">"next"</span> <span class="ow">in</span> <span class="n">summaries</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_predictor</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">summaries</span><span class="o">=</span><span class="n">summaries</span><span class="p">,</span>
            <span class="n">prompt_template</span><span class="o">=</span><span class="n">prompt_template</span><span class="p">,</span>
            <span class="n">num_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SummaryExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_agenerate_node_summary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a summary for a node."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="s2">""</span>

        <span class="n">context_str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">)</span>
        <span class="n">summary</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_template</span><span class="p">),</span> <span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">summary</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Only `TextNode` is allowed for `Summary` extractor"</span><span class="p">)</span>

        <span class="n">node_summaries_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node_summaries_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_node_summary</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>

        <span class="n">node_summaries</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">node_summaries_jobs</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Extract node-level summary metadata</span>
        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[{}</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">metadata_list</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prev_summary</span> <span class="ow">and</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"prev_section_summary"</span><span class="p">]</span> <span class="o">=</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_summary</span> <span class="ow">and</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"next_section_summary"</span><span class="p">]</span> <span class="o">=</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_self_summary</span> <span class="ow">and</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span><span class="p">]:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"section_summary"</span><span class="p">]</span> <span class="o">=</span> <span class="n">node_summaries</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Question](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/)[Next Title](https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/)
