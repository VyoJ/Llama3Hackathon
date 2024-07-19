Title: Pydantic - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/

Markdown Content:
Pydantic - LlamaIndex


PydanticProgramExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/#llama_index.core.extractors.PydanticProgramExtractor "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Pydantic program extractor.

Uses an LLM to extract out a Pydantic object. Return attributes of that object in a dictionary.

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">455</span>
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
<span class="normal">505</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PydanticProgramExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pydantic program extractor.</span>

<span class="sd">    Uses an LLM to extract out a Pydantic object. Return attributes of that object</span>
<span class="sd">    in a dictionary.</span>

<span class="sd">    """</span>

    <span class="n">program</span><span class="p">:</span> <span class="n">BasePydanticProgram</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Pydantic program to extract."</span>
    <span class="p">)</span>
    <span class="n">input_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"input"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Key to use as input to the program (the program "</span>
            <span class="s2">"template string must expose this key)."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">extract_template_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_EXTRACT_TEMPLATE_STR</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Template to use for extraction."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PydanticModelExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_acall_program</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Call the program on a node."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="n">extract_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_template_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">context_str</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">),</span>
            <span class="n">class_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">program</span><span class="o">.</span><span class="n">output_cls</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">ret_object</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">program</span><span class="o">.</span><span class="n">acall</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">input_key</span><span class="p">:</span> <span class="n">extract_str</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">ret_object</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract pydantic program."""</span>
        <span class="n">program_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">program_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_acall_program</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>

        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">program_jobs</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

### aextract `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/#llama_index.core.extractors.PydanticProgramExtractor.aextract "Permanent link")

```
aextract(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[Dict]
```

Extract pydantic program.

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Extract pydantic program."""</span>
    <span class="n">program_jobs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">program_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_acall_program</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>

    <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
        <span class="n">program_jobs</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Marvin](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/)[Next Question](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/)
