Title: PGVector SQL - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/

Markdown Content:
PGVector SQL - LlamaIndex


PGVectorSQLQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/#llama_index.core.query_engine.PGVectorSQLQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseSQLTableQueryEngine`

PGvector SQL query engine.

A modified version of the normal text-to-SQL query engine because we can infer embedding vectors in the sql query.

NOTE: this is a beta feature

NOTE: Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

Source code in `llama-index-core/llama_index/core/indices/struct_store/sql_query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PGVectorSQLQueryEngine</span><span class="p">(</span><span class="n">BaseSQLTableQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PGvector SQL query engine.</span>

<span class="sd">    A modified version of the normal text-to-SQL query engine because</span>
<span class="sd">    we can infer embedding vectors in the sql query.</span>

<span class="sd">    NOTE: this is a beta feature</span>

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
        <span class="n">sql_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="n">text_to_sql_prompt</span> <span class="o">=</span> <span class="n">text_to_sql_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_TO_SQL_PGVECTOR_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_retriever</span> <span class="o">=</span> <span class="n">NLSQLRetriever</span><span class="p">(</span>
            <span class="n">sql_database</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">text_to_sql_prompt</span><span class="o">=</span><span class="n">text_to_sql_prompt</span><span class="p">,</span>
            <span class="n">context_query_kwargs</span><span class="o">=</span><span class="n">context_query_kwargs</span><span class="p">,</span>
            <span class="n">tables</span><span class="o">=</span><span class="n">tables</span><span class="p">,</span>
            <span class="n">sql_parser_mode</span><span class="o">=</span><span class="n">SQLParserMode</span><span class="o">.</span><span class="n">PGVECTOR</span><span class="p">,</span>
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

### sql\_retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/#llama_index.core.query_engine.PGVectorSQLQueryEngine.sql_retriever "Permanent link")

```
sql_retriever: [NLSQLRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/#llama_index.core.retrievers.NLSQLRetriever "llama_index.core.indices.struct_store.sql_retriever.NLSQLRetriever")
```

Get SQL retriever.

Back to top

[Previous NL SQL table](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/)[Next SQL join](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/)
