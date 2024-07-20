Title: Llm - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/

Markdown Content:
Llm - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Base LLM component.

Source code in `llama-index-core/llama_index/core/llms/llm.py`

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
<span class="normal">715</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseLLMComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base LLM component."""</span>

    <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"LLM"</span><span class="p">)</span>
    <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Streaming mode"</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/#llama_index.core.llms.llm.BaseLLMComponent.set_callback_manager "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: Any) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/llms/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

Bases: `BaseLLMComponent`

LLM completion component.

Source code in `llama-index-core/llama_index/core/llms/llm.py`

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
<span class="normal">766</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMCompleteComponent</span><span class="p">(</span><span class="n">BaseLLMComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLM completion component."""</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="k">if</span> <span class="s2">"prompt"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Prompt must be in input dict."</span><span class="p">)</span>

        <span class="c1"># do special check to see if prompt is a list of chat messages</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">],</span> <span class="n">get_args</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])):</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">messages_to_prompt</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">])</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">])</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">completion_to_prompt</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">])</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="c1"># non-trivial to figure how to support chat/complete/etc.</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span>
        <span class="c1"># ignore all other kwargs for now</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">streaming</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">stream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">formatted</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">formatted</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="c1"># non-trivial to figure how to support chat/complete/etc.</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span>
        <span class="c1"># ignore all other kwargs for now</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">formatted</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"prompt"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/#llama_index.core.llms.llm.LLMCompleteComponent.input_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/#llama_index.core.llms.llm.LLMCompleteComponent.output_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

Bases: `BaseLLMComponent`

LLM chat component.

Source code in `llama-index-core/llama_index/core/llms/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">769</span>
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
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMChatComponent</span><span class="p">(</span><span class="n">BaseLLMComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLM chat component."""</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="k">if</span> <span class="s2">"messages"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Messages must be in input dict."</span><span class="p">)</span>

        <span class="c1"># if `messages` is a string, convert to a list of chat message</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">],</span> <span class="n">get_args</span><span class="p">(</span><span class="n">StringableInput</span><span class="p">)):</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">])</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span> <span class="o">=</span> <span class="n">prompt_to_messages</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]))</span>

        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">ChatMessage</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Messages must be a list of ChatMessage"</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="c1"># non-trivial to figure how to support chat/complete/etc.</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">streaming</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="c1"># non-trivial to figure how to support chat/complete/etc.</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">streaming</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">astream_chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"messages"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/#llama_index.core.llms.llm.LLMChatComponent.input_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/#llama_index.core.llms.llm.LLMChatComponent.output_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

Back to top

[Previous Input](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/input/)[Next Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/multi_modal/)
