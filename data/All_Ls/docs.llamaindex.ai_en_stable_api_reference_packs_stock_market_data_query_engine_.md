Title: Stock market data query engine

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/

Markdown Content:
Stock market data query engine - LlamaIndex


StockMarketDataQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/#llama_index.packs.stock_market_data_query_engine.StockMarketDataQueryEnginePack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Historical stock market data query engine pack based on yahoo finance.

Source code in `llama-index-packs/llama-index-packs-stock-market-data-query-engine/llama_index/packs/stock_market_data_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="k">class</span> <span class="nc">StockMarketDataQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Historical stock market data query engine pack based on yahoo finance."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tickers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tickers</span> <span class="o">=</span> <span class="n">tickers</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">yfinance</span> <span class="k">as</span> <span class="nn">yf</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Dependencies missing, run `pip install yfinance`"</span><span class="p">)</span>

        <span class="n">stocks_market_data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">ticker</span> <span class="ow">in</span> <span class="n">tickers</span><span class="p">:</span>
            <span class="n">stock</span> <span class="o">=</span> <span class="n">yf</span><span class="o">.</span><span class="n">Ticker</span><span class="p">(</span><span class="n">ticker</span><span class="p">)</span>
            <span class="n">hist</span> <span class="o">=</span> <span class="n">stock</span><span class="o">.</span><span class="n">history</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

            <span class="n">year</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">year</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">hist</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
            <span class="n">hist</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="s2">"year"</span><span class="p">,</span> <span class="n">year</span><span class="p">)</span>
            <span class="n">month</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">month</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">hist</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
            <span class="n">hist</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s2">"month"</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span>
            <span class="n">day</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">day</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">hist</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
            <span class="n">hist</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="s2">"day"</span><span class="p">,</span> <span class="n">day</span><span class="p">)</span>
            <span class="n">hist</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(</span><span class="n">drop</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="n">stocks_market_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hist</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stocks_market_data</span> <span class="o">=</span> <span class="n">stocks_market_data</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">))</span>

        <span class="n">df_price_query_engines</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">PandasQueryEngine</span><span class="p">(</span><span class="n">stock</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">stock</span> <span class="ow">in</span> <span class="n">stocks_market_data</span>
        <span class="p">]</span>

        <span class="n">summaries</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">ticker</span><span class="si">}</span><span class="s2"> historical market data"</span> <span class="k">for</span> <span class="n">ticker</span> <span class="ow">in</span> <span class="n">tickers</span><span class="p">]</span>

        <span class="n">df_price_nodes</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">IndexNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">summary</span><span class="p">,</span> <span class="n">index_id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"pandas</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">summary</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">summaries</span><span class="p">)</span>
        <span class="p">]</span>

        <span class="n">df_price_id_query_engine_mapping</span> <span class="o">=</span> <span class="p">{</span>
            <span class="sa">f</span><span class="s2">"pandas</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">:</span> <span class="n">df_engine</span>
            <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">df_engine</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">df_price_query_engines</span><span class="p">)</span>
        <span class="p">}</span>

        <span class="n">stock_price_vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
            <span class="n">df_price_nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>
        <span class="n">stock_price_vector_retriever</span> <span class="o">=</span> <span class="n">stock_price_vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">1</span>
        <span class="p">)</span>

        <span class="n">stock_price_recursive_retriever</span> <span class="o">=</span> <span class="n">RecursiveRetriever</span><span class="p">(</span>
            <span class="s2">"vector"</span><span class="p">,</span>
            <span class="n">retriever_dict</span><span class="o">=</span><span class="p">{</span><span class="s2">"vector"</span><span class="p">:</span> <span class="n">stock_price_vector_retriever</span><span class="p">},</span>
            <span class="n">query_engine_dict</span><span class="o">=</span><span class="n">df_price_id_query_engine_mapping</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">stock_price_response_synthesizer</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="c1"># service_context=service_context,</span>
            <span class="n">response_mode</span><span class="o">=</span><span class="s2">"compact"</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">stock_price_query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="n">stock_price_recursive_retriever</span><span class="p">,</span>
            <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">stock_price_response_synthesizer</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">stock_price_query_engine</span> <span class="o">=</span> <span class="n">stock_price_query_engine</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"tickers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tickers</span><span class="p">,</span>
            <span class="s2">"stocks market data"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">stocks_market_data</span><span class="p">,</span>
            <span class="s2">"query engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">stock_price_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">stock_price_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/#llama_index.packs.stock_market_data_query_engine.StockMarketDataQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-stock-market-data-query-engine/llama_index/packs/stock_market_data_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"tickers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tickers</span><span class="p">,</span>
        <span class="s2">"stocks market data"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">stocks_market_data</span><span class="p">,</span>
        <span class="s2">"query engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">stock_price_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/#llama_index.packs.stock_market_data_query_engine.StockMarketDataQueryEnginePack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run.

Source code in `llama-index-packs/llama-index-packs-stock-market-data-query-engine/llama_index/packs/stock_market_data_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">stock_price_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Snowflake query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/)[Next Streamlit chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/)

Hi, how can I help you?

🦙
