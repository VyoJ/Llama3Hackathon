Title: Compact accumulate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/

Markdown Content:
Compact accumulate - LlamaIndex


CompactAndAccumulate [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/#llama_index.core.response_synthesizers.compact_and_accumulate.CompactAndAccumulate "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[Accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/accumulate/#llama_index.core.response_synthesizers.Accumulate "llama_index.core.response_synthesizers.Accumulate")`

Accumulate responses across compact text chunks.

Source code in `llama-index-core/llama_index/core/response_synthesizers/compact_and_accumulate.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
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
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CompactAndAccumulate</span><span class="p">(</span><span class="n">Accumulate</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Accumulate responses across compact text chunks."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">---------------------</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get compact response."""</span>
        <span class="c1"># use prompt helper to fix compact text_chunks under the prompt limitation</span>
        <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">temp_set_attrs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="p">):</span>
            <span class="n">new_texts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="p">)</span>

            <span class="k">return</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">aget_response</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">text_chunks</span><span class="o">=</span><span class="n">new_texts</span><span class="p">,</span>
                <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">---------------------</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get compact response."""</span>
        <span class="c1"># use prompt helper to fix compact text_chunks under the prompt limitation</span>
        <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">temp_set_attrs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="p">):</span>
            <span class="n">new_texts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="p">)</span>

            <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">get_response</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">text_chunks</span><span class="o">=</span><span class="n">new_texts</span><span class="p">,</span>
                <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget\_response `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/#llama_index.core.response_synthesizers.compact_and_accumulate.CompactAndAccumulate.aget_response "Permanent link")

```
aget_response(query_str: str, text_chunks: Sequence[str], separator: str = '\n---------------------\n', **response_kwargs: Any) -> RESPONSE_TEXT_TYPE
```

Get compact response.

Source code in `llama-index-core/llama_index/core/response_synthesizers/compact_and_accumulate.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
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
<span class="normal">30</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">---------------------</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get compact response."""</span>
    <span class="c1"># use prompt helper to fix compact text_chunks under the prompt limitation</span>
    <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">temp_set_attrs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="p">):</span>
        <span class="n">new_texts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">aget_response</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">text_chunks</span><span class="o">=</span><span class="n">new_texts</span><span class="p">,</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_response [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/#llama_index.core.response_synthesizers.compact_and_accumulate.CompactAndAccumulate.get_response "Permanent link")

```
get_response(query_str: str, text_chunks: Sequence[str], separator: str = '\n---------------------\n', **response_kwargs: Any) -> RESPONSE_TEXT_TYPE
```

Get compact response.

Source code in `llama-index-core/llama_index/core/response_synthesizers/compact_and_accumulate.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
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
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">---------------------</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
    <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get compact response."""</span>
    <span class="c1"># use prompt helper to fix compact text_chunks under the prompt limitation</span>
    <span class="n">text_qa_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">temp_set_attrs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="p">):</span>
        <span class="n">new_texts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">repack</span><span class="p">(</span><span class="n">text_qa_template</span><span class="p">,</span> <span class="n">text_chunks</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">get_response</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">text_chunks</span><span class="o">=</span><span class="n">new_texts</span><span class="p">,</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/accumulate/)[Next Compact and refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_and_refine/)
