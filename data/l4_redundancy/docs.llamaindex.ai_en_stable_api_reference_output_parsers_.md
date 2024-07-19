Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/

Markdown Content:
Index - LlamaIndex


BaseOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/#llama_index.core.types.BaseOutputParser "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `DispatcherSpanMixin`, `ABC`

Output parser class.

Source code in `llama-index-core/llama_index/core/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseOutputParser</span><span class="p">(</span><span class="n">DispatcherSpanMixin</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Output parser class."""</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__modify_schema__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Avoids serialization issues."""</span>
        <span class="n">schema</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="s2">"object"</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="p">{})</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
        <span class="k">return</span> <span class="n">query</span>

    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format a list of messages with structured output formatting instructions."""</span>
        <span class="c1"># NOTE: apply output parser to either the first message if it's a system message</span>
        <span class="c1">#       or the last message</span>
        <span class="k">if</span> <span class="n">messages</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o"></span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">:</span>
            <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">messages</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Guardrails](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/)[Next Langchain](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/)
