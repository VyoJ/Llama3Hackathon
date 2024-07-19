Title: Snowflake query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/

Markdown Content:
Snowflake query engine - LlamaIndex


SnowflakeQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/#llama_index.packs.snowflake_query_engine.SnowflakeQueryEnginePack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Snowflake query engine pack. It uses snowflake-sqlalchemy to connect to Snowflake, then calls NLSQLTableQueryEngine to query data.

Source code in `llama-index-packs/llama-index-packs-snowflake-query-engine/llama_index/packs/snowflake_query_engine/base.py`

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
<span class="normal">65</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="k">class</span> <span class="nc">SnowflakeQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Snowflake query engine pack.</span>
<span class="sd">    It uses snowflake-sqlalchemy to connect to Snowflake, then calls</span>
<span class="sd">    NLSQLTableQueryEngine to query data.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">account</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">schema</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">warehouse</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">role</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tables</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># workaround for https://github.com/snowflakedb/snowflake-sqlalchemy/issues/380.</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">snowflake_sqlalchemy_20_monkey_patches</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please run `pip install snowflake-sqlalchemy`"</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"OPENAI_API_KEY"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"OpenAI API Token is missing or blank."</span><span class="p">)</span>

        <span class="n">snowflake_uri</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"snowflake://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">account</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">database</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">schema</span><span class="si">}</span><span class="s2">?warehouse=</span><span class="si">{</span><span class="n">warehouse</span><span class="si">}</span><span class="s2">&amp;role=</span><span class="si">{</span><span class="n">role</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span><span class="n">snowflake_uri</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span> <span class="o">=</span> <span class="n">SQLDatabase</span><span class="p">(</span><span class="n">engine</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tables</span> <span class="o">=</span> <span class="n">tables</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">NLSQLTableQueryEngine</span><span class="p">(</span>
            <span class="n">sql_database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="p">,</span>
            <span class="n">tables</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tables</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span><span class="p">,</span>
            <span class="s2">"sql_database"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/#llama_index.packs.snowflake_query_engine.SnowflakeQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-snowflake-query-engine/llama_index/packs/snowflake_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span><span class="p">,</span>
        <span class="s2">"sql_database"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/#llama_index.packs.snowflake_query_engine.SnowflakeQueryEnginePack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-snowflake-query-engine/llama_index/packs/snowflake_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sentence window retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/sentence_window_retriever/)[Next Stock market data query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/)

Hi, how can I help you?

🦙
