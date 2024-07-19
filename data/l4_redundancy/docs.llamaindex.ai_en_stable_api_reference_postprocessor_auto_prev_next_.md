Title: Auto prev next - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/

Markdown Content:
Auto prev next - LlamaIndex


Node PostProcessor module.

AutoPrevNextNodePostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/#llama_index.core.postprocessor.AutoPrevNextNodePostprocessor "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Previous/Next Node post-processor.

Allows users to fetch additional nodes from the document store, based on the prev/next relationships of the nodes.

NOTE: difference with PrevNextPostprocessor is that this infers forward/backwards direction.

NOTE: this is a beta feature.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `docstore` | `[BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.BaseDocumentStore")` | 
The document store.



 | _required_ |
| `num_nodes` | `int` | 

The number of nodes to return (default: 1)



 | _required_ |
| `infer_prev_next_tmpl` | `str` | 

The template to use for inference. Required fields are {context\_str} and {query\_str}.



 | _required_ |

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">263</span>
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
<span class="normal">361</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AutoPrevNextNodePostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Previous/Next Node post-processor.</span>

<span class="sd">    Allows users to fetch additional nodes from the document store,</span>
<span class="sd">    based on the prev/next relationships of the nodes.</span>

<span class="sd">    NOTE: difference with PrevNextPostprocessor is that</span>
<span class="sd">    this infers forward/backwards direction.</span>

<span class="sd">    NOTE: this is a beta feature.</span>

<span class="sd">    Args:</span>
<span class="sd">        docstore (BaseDocumentStore): The document store.</span>
<span class="sd">        num_nodes (int): The number of nodes to return (default: 1)</span>
<span class="sd">        infer_prev_next_tmpl (str): The template to use for inference.</span>
<span class="sd">            Required fields are {context_str} and {query_str}.</span>

<span class="sd">    """</span>

    <span class="n">docstore</span><span class="p">:</span> <span class="n">BaseDocumentStore</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">num_nodes</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">infer_prev_next_tmpl</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_INFER_PREV_NEXT_TMPL</span><span class="p">)</span>
    <span class="n">refine_prev_next_tmpl</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_REFINE_INFER_PREV_NEXT_TMPL</span><span class="p">)</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Configuration for this pydantic object."""</span>

        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"AutoPrevNextNodePostprocessor"</span>

    <span class="k">def</span> <span class="nf">_parse_prediction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raw_pred</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Parse prediction."""</span>
        <span class="n">pred</span> <span class="o">=</span> <span class="n">raw_pred</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
        <span class="k">if</span> <span class="s2">"previous"</span> <span class="ow">in</span> <span class="n">pred</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"previous"</span>
        <span class="k">elif</span> <span class="s2">"next"</span> <span class="ow">in</span> <span class="n">pred</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"next"</span>
        <span class="k">elif</span> <span class="s2">"none"</span> <span class="ow">in</span> <span class="n">pred</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"none"</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid prediction: </span><span class="si">{</span><span class="n">raw_pred</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing query bundle."</span><span class="p">)</span>

        <span class="n">infer_prev_next_prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">infer_prev_next_tmpl</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">refine_infer_prev_next_prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">refine_prev_next_tmpl</span><span class="p">)</span>

        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">all_nodes</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="c1"># use response builder instead of llm directly</span>
            <span class="c1"># to be more robust to handling long context</span>
            <span class="n">response_builder</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
                <span class="n">text_qa_template</span><span class="o">=</span><span class="n">infer_prev_next_prompt</span><span class="p">,</span>
                <span class="n">refine_template</span><span class="o">=</span><span class="n">refine_infer_prev_next_prompt</span><span class="p">,</span>
                <span class="n">response_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">response_mode</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">raw_pred</span> <span class="o">=</span> <span class="n">response_builder</span><span class="o">.</span><span class="n">get_response</span><span class="p">(</span>
                <span class="n">text_chunks</span><span class="o">=</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()],</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">raw_pred</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">raw_pred</span><span class="p">)</span>
            <span class="n">mode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_prediction</span><span class="p">(</span><span class="n">raw_pred</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Postprocessor Predicted mode: </span><span class="si">{</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Postprocessor Predicted mode: </span><span class="si">{</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">mode</span> <span class="o"></span> <span class="s2">"previous"</span><span class="p">:</span>
                <span class="n">all_nodes</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
                    <span class="n">get_backward_nodes</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">mode</span> <span class="o">==</span> <span class="s2">"none"</span><span class="p">:</span>
                <span class="k">pass</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid mode: </span><span class="si">{</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">sorted_nodes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">all_nodes</span><span class="o">.</span><span class="n">values</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sorted_nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### Config [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/#llama_index.core.postprocessor.AutoPrevNextNodePostprocessor.Config "Permanent link")

Configuration for this pydantic object.

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Configuration for this pydantic object."""</span>

    <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/PII/)[Next Cohere rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/cohere_rerank/)
