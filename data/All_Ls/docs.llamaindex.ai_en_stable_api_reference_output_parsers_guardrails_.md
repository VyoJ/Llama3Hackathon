Title: Guardrails - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/

Markdown Content:
Guardrails - LlamaIndex


GuardrailsOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ChainableOutputParser`

Guardrails output parser.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-guardrails/llama_index/output_parsers/guardrails/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
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
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GuardrailsOutputParser</span><span class="p">(</span><span class="n">ChainableOutputParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Guardrails output parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">guard</span><span class="p">:</span> <span class="n">Guard</span><span class="p">,</span>
        <span class="n">format_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a Guardrails output parser."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="p">:</span> <span class="n">Guard</span> <span class="o">=</span> <span class="n">guard</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">format_key</span> <span class="o">=</span> <span class="n">format_key</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@deprecated</span><span class="p">(</span><span class="n">version</span><span class="o">=</span><span class="s2">"0.8.46"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">from_rail</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">rail</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuardrailsOutputParser"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From rail."""</span>
        <span class="k">if</span> <span class="n">Guard</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Guardrails is not installed. Run `pip install guardrails-ai`. "</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">Guard</span><span class="o">.</span><span class="n">from_rail</span><span class="p">(</span><span class="n">rail</span><span class="p">))</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@deprecated</span><span class="p">(</span><span class="n">version</span><span class="o">=</span><span class="s2">"0.8.46"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">from_rail_string</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">rail_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuardrailsOutputParser"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From rail string."""</span>
        <span class="k">if</span> <span class="n">Guard</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Guardrails is not installed. Run `pip install guardrails-ai`. "</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">Guard</span><span class="o">.</span><span class="n">from_rail_string</span><span class="p">(</span><span class="n">rail_string</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">validated_output</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
        <span class="n">output_schema_text</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">rail</span><span class="o">.</span><span class="n">prompt</span><span class="p">)</span>

        <span class="c1"># Add format instructions here.</span>
        <span class="n">format_instructions_tmpl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">raw_prompt</span><span class="o">.</span><span class="n">format_instructions</span>
        <span class="c1"># NOTE: output_schema is fixed</span>
        <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">output_schema</span><span class="o">=</span><span class="n">output_schema_text</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">format_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">format_key</span><span class="p">:</span> <span class="n">format_instructions</span><span class="p">})</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">format_instructions</span>

        <span class="k">return</span> <span class="n">fmt_query</span>
</code></pre></div></td></tr></tbody></table>

### from\_rail `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser.from_rail "Permanent link")

```
from_rail(rail: str) -> [GuardrailsOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser "llama_index.output_parsers.guardrails.base.GuardrailsOutputParser")
```

From rail.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-guardrails/llama_index/output_parsers/guardrails/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@deprecated</span><span class="p">(</span><span class="n">version</span><span class="o">=</span><span class="s2">"0.8.46"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">from_rail</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">rail</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuardrailsOutputParser"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From rail."""</span>
    <span class="k">if</span> <span class="n">Guard</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Guardrails is not installed. Run `pip install guardrails-ai`. "</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">Guard</span><span class="o">.</span><span class="n">from_rail</span><span class="p">(</span><span class="n">rail</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### from\_rail\_string `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser.from_rail_string "Permanent link")

```
from_rail_string(rail_string: str) -> [GuardrailsOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser "llama_index.output_parsers.guardrails.base.GuardrailsOutputParser")
```

From rail string.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-guardrails/llama_index/output_parsers/guardrails/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@deprecated</span><span class="p">(</span><span class="n">version</span><span class="o">=</span><span class="s2">"0.8.46"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">from_rail_string</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">rail_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuardrailsOutputParser"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From rail string."""</span>
    <span class="k">if</span> <span class="n">Guard</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Guardrails is not installed. Run `pip install guardrails-ai`. "</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">Guard</span><span class="o">.</span><span class="n">from_rail_string</span><span class="p">(</span><span class="n">rail_string</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### parse [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser.parse "Permanent link")

```
parse(output: str, *args: Any, **kwargs: Any) -> Any
```

Parse, validate, and correct errors programmatically.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-guardrails/llama_index/output_parsers/guardrails/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">validated_output</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/#llama_index.output_parsers.guardrails.GuardrailsOutputParser.format "Permanent link")

```
format(query: str) -> str
```

Format a query with structured output formatting instructions.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-guardrails/llama_index/output_parsers/guardrails/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
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
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
    <span class="n">output_schema_text</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">rail</span><span class="o">.</span><span class="n">prompt</span><span class="p">)</span>

    <span class="c1"># Add format instructions here.</span>
    <span class="n">format_instructions_tmpl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">guard</span><span class="o">.</span><span class="n">raw_prompt</span><span class="o">.</span><span class="n">format_instructions</span>
    <span class="c1"># NOTE: output_schema is fixed</span>
    <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
        <span class="n">output_schema</span><span class="o">=</span><span class="n">output_schema_text</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">format_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">format_key</span><span class="p">:</span> <span class="n">format_instructions</span><span class="p">})</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">format_instructions</span>

    <span class="k">return</span> <span class="n">fmt_query</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/objects/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/)
