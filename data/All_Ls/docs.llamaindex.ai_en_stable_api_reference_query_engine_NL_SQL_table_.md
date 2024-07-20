Title: NL SQL table - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/

Markdown Content:
NL SQL table - LlamaIndex


NLSQLTableQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/#llama_index.core.query_engine.NLSQLTableQueryEngine "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseSQLTableQueryEngine`

Natural language SQL Table query engine.

Read NLStructStoreQueryEngine's docstring for more info on NL SQL.

NOTE: Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">460</span>
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
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NLSQLTableQueryEngine</span><span class="p">(</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Natural language SQL Table query engine.</span>

<span class="sd">    Read NLStructStoreQueryEngine's docstring for more info on NL SQL.</span>

<span class="sd">    NOTE: Any Text-to-SQL application should be aware that executing</span>
<span class="sd">    arbitrary SQL queries can be a security risk. It is recommended to</span>
<span class="sd">    take precautions as needed, such as using restricted roles, read-only</span>
<span class="sd">    databases, sandboxing, etc.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_to_sql_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_query_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">synthesize_response</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">response_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Table</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_str_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sql_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="c1"># self._tables = tables</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span> <span class="o">=</span> <span class="n">NLSQLRetriever</span><span class="p">(</span>
            <span class="n">sql_database</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">text_to_sql_prompt</span><span class="o">=</span><span class="n">text_to_sql_prompt</span><span class="p">,</span>
            <span class="n">context_query_kwargs</span><span class="o">=</span><span class="n">context_query_kwargs</span><span class="p">,</span>
            <span class="n">tables</span><span class="o">=</span><span class="n">tables</span><span class="p">,</span>
            <span class="n">context_str_prefix</span><span class="o">=</span><span class="n">context_str_prefix</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">sql_only</span><span class="o">=</span><span class="n">sql_only</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">synthesize_response</span><span class="o">=</span><span class="n">synthesize_response</span><span class="p">,</span>
            <span class="n">response_synthesis_prompt</span><span class="o">=</span><span class="n">response_synthesis_prompt</span><span class="p">,</span>
            <span class="n">refine_synthesis_prompt</span><span class="o">=</span><span class="n">refine_synthesis_prompt</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">sql_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NLSQLRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get SQL retriever."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span>
</code></pre></div></td></tr></tbody></table>

### sql\_retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/#llama_index.core.query_engine.NLSQLTableQueryEngine.sql_retriever "Permanent link")

```
sql_retriever: [NLSQLRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever "llama_index.core.indices.struct_store.sql_retriever.NLSQLRetriever")
```

Get SQL retriever.

Back to top

[Previous JSONalayze](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/)[Next PGVector SQL](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/)
