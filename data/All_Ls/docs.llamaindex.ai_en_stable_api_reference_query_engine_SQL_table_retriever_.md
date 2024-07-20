Title: SQL table retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/

Markdown Content:
SQL table retriever - LlamaIndex


SQLTableRetrieverQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/#llama_index.core.query_engine.SQLTableRetrieverQueryEngine "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseSQLTableQueryEngine`

SQL Table retriever query engine.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLTableRetrieverQueryEngine</span><span class="p">(</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SQL Table retriever query engine."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">,</span>
        <span class="n">table_retriever</span><span class="p">:</span> <span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_to_sql_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_query_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">synthesize_response</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">response_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_str_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span> <span class="o">=</span> <span class="n">NLSQLRetriever</span><span class="p">(</span>
            <span class="n">sql_database</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">text_to_sql_prompt</span><span class="o">=</span><span class="n">text_to_sql_prompt</span><span class="p">,</span>
            <span class="n">context_query_kwargs</span><span class="o">=</span><span class="n">context_query_kwargs</span><span class="p">,</span>
            <span class="n">table_retriever</span><span class="o">=</span><span class="n">table_retriever</span><span class="p">,</span>
            <span class="n">context_str_prefix</span><span class="o">=</span><span class="n">context_str_prefix</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">sql_only</span><span class="o">=</span><span class="n">sql_only</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">synthesize_response</span><span class="o">=</span><span class="n">synthesize_response</span><span class="p">,</span>
            <span class="n">response_synthesis_prompt</span><span class="o">=</span><span class="n">response_synthesis_prompt</span><span class="p">,</span>
            <span class="n">refine_synthesis_prompt</span><span class="o">=</span><span class="n">refine_synthesis_prompt</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">sql_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NLSQLRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get SQL retriever."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span>
</code></pre></div></td></tr></tbody></table>

### sql\_retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/#llama_index.core.query_engine.SQLTableRetrieverQueryEngine.sql_retriever "Permanent link")

```
sql_retriever: [NLSQLRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever "llama_index.core.indices.struct_store.sql_retriever.NLSQLRetriever")
```

Get SQL retriever.

Back to top

[Previous SQL join](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/)[Next Citation](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/)
