Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/question_gen/

Markdown Content:
Index - LlamaIndex


BaseQuestionGenerator [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.BaseQuestionGenerator "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PromptMixin`, `DispatcherSpanMixin`

Source code in `llama-index-core/llama_index/core/question_gen/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseQuestionGenerator</span><span class="p">(</span><span class="n">PromptMixin</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">generate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

SubQuestionList [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.SubQuestionList "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

A pydantic object wrapping a list of sub-questions.

This is mostly used to make getting a json schema easier.

Source code in `llama-index-core/llama_index/core/question_gen/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubQuestionList</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A pydantic object wrapping a list of sub-questions.</span>

<span class="sd">    This is mostly used to make getting a json schema easier.</span>
<span class="sd">    """</span>

    <span class="n">items</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

SubQuestion [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.SubQuestion "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Source code in `llama-index-core/llama_index/core/question_gen/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubQuestion</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">sub_question</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Guidance](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/)[Next Llm question gen](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/)
