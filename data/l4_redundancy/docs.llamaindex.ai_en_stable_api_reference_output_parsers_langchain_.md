Title: Langchain - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/

Markdown Content:
Langchain - LlamaIndex


LangchainOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/#llama_index.output_parsers.langchain.LangchainOutputParser "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ChainableOutputParser`

Langchain output parser.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-langchain/llama_index/output_parsers/langchain/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
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
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LangchainOutputParser</span><span class="p">(</span><span class="n">ChainableOutputParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Langchain output parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">output_parser</span><span class="p">:</span> <span class="s2">"LCOutputParser"</span><span class="p">,</span> <span class="n">format_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_format_key</span> <span class="o">=</span> <span class="n">format_key</span>

    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
        <span class="c1"># TODO: this object may be stringified by our upstream llmpredictor,</span>
        <span class="c1"># figure out better</span>
        <span class="c1"># ways to "convert" the object to a proper string format.</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
        <span class="n">format_instructions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">get_format_instructions</span><span class="p">()</span>

        <span class="c1"># TODO: this is a temporary hack. if there's curly brackets in the format</span>
        <span class="c1"># instructions (and query is a string template), we need to</span>
        <span class="c1"># escape the curly brackets in the format instructions to preserve the</span>
        <span class="c1"># overall template.</span>
        <span class="n">query_tmpl_vars</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">v</span> <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">Formatter</span><span class="p">()</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_tmpl_vars</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{"</span><span class="p">,</span> <span class="s2">"{{"</span><span class="p">)</span>
            <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"}"</span><span class="p">,</span> <span class="s2">"}}"</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_key</span><span class="p">:</span> <span class="n">format_instructions</span><span class="p">})</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">format_instructions</span>

        <span class="k">return</span> <span class="n">fmt_query</span>
</code></pre></div></td></tr></tbody></table>

### parse [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/#llama_index.output_parsers.langchain.LangchainOutputParser.parse "Permanent link")

```
parse(output: str) -> Any
```

Parse, validate, and correct errors programmatically.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-langchain/llama_index/output_parsers/langchain/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
    <span class="c1"># TODO: this object may be stringified by our upstream llmpredictor,</span>
    <span class="c1"># figure out better</span>
    <span class="c1"># ways to "convert" the object to a proper string format.</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/#llama_index.output_parsers.langchain.LangchainOutputParser.format "Permanent link")

```
format(query: str) -> str
```

Format a query with structured output formatting instructions.

Source code in `llama-index-integrations/output_parsers/llama-index-output-parsers-langchain/llama_index/output_parsers/langchain/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
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
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
    <span class="n">format_instructions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">get_format_instructions</span><span class="p">()</span>

    <span class="c1"># TODO: this is a temporary hack. if there's curly brackets in the format</span>
    <span class="c1"># instructions (and query is a string template), we need to</span>
    <span class="c1"># escape the curly brackets in the format instructions to preserve the</span>
    <span class="c1"># overall template.</span>
    <span class="n">query_tmpl_vars</span> <span class="o">=</span> <span class="p">{</span>
        <span class="n">v</span> <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">Formatter</span><span class="p">()</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">}</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_tmpl_vars</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{"</span><span class="p">,</span> <span class="s2">"{{"</span><span class="p">)</span>
        <span class="n">format_instructions</span> <span class="o">=</span> <span class="n">format_instructions</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"}"</span><span class="p">,</span> <span class="s2">"}}"</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_format_key</span><span class="p">:</span> <span class="n">format_instructions</span><span class="p">})</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">fmt_query</span> <span class="o">=</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">format_instructions</span>

    <span class="k">return</span> <span class="n">fmt_query</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/)[Next Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/)
