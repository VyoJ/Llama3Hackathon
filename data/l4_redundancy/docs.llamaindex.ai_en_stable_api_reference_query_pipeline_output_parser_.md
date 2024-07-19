Title: Output parser - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/

Markdown Content:
Output parser - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Output parser component.

Source code in `llama-index-core/llama_index/core/output_parsers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OutputParserComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Output parser component."""</span>

    <span class="n">output_parser</span><span class="p">:</span> <span class="n">BaseOutputParser</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Output parser."</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s2">"input"</span><span class="p">])</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># NOTE: no native async for output parser</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="nb">input</span><span class="p">[</span><span class="s2">"input"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"input"</span><span class="p">])</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"input"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/#llama_index.core.output_parsers.base.OutputParserComponent.input_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: Any
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/#llama_index.core.output_parsers.base.OutputParserComponent.output_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: Any
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/#llama_index.core.output_parsers.base.OutputParserComponent.set_callback_manager "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: Any) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/output_parsers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Object](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/object/)[Next Postprocessor](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/postprocessor/)
