Title: Question - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/

Markdown Content:
Question - LlamaIndex


QuestionsAnsweredExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/#llama_index.core.extractors.QuestionsAnsweredExtractor "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Questions answered extractor. Node-level extractor. Extracts `questions_this_excerpt_can_answer` metadata field.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 
LLM



 | `None` |
| `questions` | `int` | 

number of questions to extract



 | `5` |
| `prompt_template` | `str` | 

template for question extraction,



 | `DEFAULT_QUESTION_GEN_TMPL` |
| `embedding_only` | `bool` | 

whether to use embedding only



 | `True` |

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
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
<span class="normal">320</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QuestionsAnsweredExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Questions answered extractor. Node-level extractor.</span>
<span class="sd">    Extracts `questions_this_excerpt_can_answer` metadata field.</span>

<span class="sd">    Args:</span>
<span class="sd">        llm (Optional[LLM]): LLM</span>
<span class="sd">        questions (int): number of questions to extract</span>
<span class="sd">        prompt_template (str): template for question extraction,</span>
<span class="sd">        embedding_only (bool): whether to use embedding only</span>
<span class="sd">    """</span>

    <span class="n">llm</span><span class="p">:</span> <span class="n">LLMPredictorType</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The LLM to use for generation."</span><span class="p">)</span>
    <span class="n">questions</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of questions to generate."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_QUESTION_GEN_TMPL</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Prompt template to use when generating questions."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">embedding_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to use metadata for emebddings only."</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># TODO: llm_predictor arg is deprecated</span>
        <span class="n">llm_predictor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">questions</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_QUESTION_GEN_TMPL</span><span class="p">,</span>
        <span class="n">embedding_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_NUM_WORKERS</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">questions</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"questions must be &gt;= 1"</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_predictor</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">questions</span><span class="o">=</span><span class="n">questions</span><span class="p">,</span>
            <span class="n">prompt_template</span><span class="o">=</span><span class="n">prompt_template</span><span class="p">,</span>
            <span class="n">embedding_only</span><span class="o">=</span><span class="n">embedding_only</span><span class="p">,</span>
            <span class="n">num_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"QuestionsAnsweredExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aextract_questions_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract questions from a node and return it's metadata dict."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="n">context_str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">)</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_template</span><span class="p">)</span>
        <span class="n">questions</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">prompt</span><span class="p">,</span> <span class="n">num_questions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">questions</span><span class="p">,</span> <span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"questions_this_excerpt_can_answer"</span><span class="p">:</span> <span class="n">questions</span><span class="o">.</span><span class="n">strip</span><span class="p">()}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="n">questions_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">questions_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_aextract_questions_from_node</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>

        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">questions_jobs</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/)[Next Summary](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/)
