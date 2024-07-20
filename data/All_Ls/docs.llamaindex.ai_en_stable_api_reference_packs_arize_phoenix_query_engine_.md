Title: Arize phoenix query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/

Markdown Content:
Arize phoenix query engine - LlamaIndex


ArizePhoenixQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/#llama_index.packs.arize_phoenix_query_engine.ArizePhoenixQueryEnginePack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

The Arize-Phoenix LlamaPack show how to instrument your LlamaIndex query engine with tracing. It launches Phoenix in the background, builds an index over an input list of nodes, and instantiates and instruments a query engine over that index so that trace data from each query is sent to Phoenix.

Note: Using this LlamaPack requires that your OpenAI API key is set via the OPENAI\_API\_KEY environment variable.

Source code in `llama-index-packs/llama-index-packs-arize-phoenix-query-engine/llama_index/packs/arize_phoenix_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
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
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ArizePhoenixQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    The Arize-Phoenix LlamaPack show how to instrument your LlamaIndex query</span>
<span class="sd">    engine with tracing. It launches Phoenix in the background, builds an index</span>
<span class="sd">    over an input list of nodes, and instantiates and instruments a query engine</span>
<span class="sd">    over that index so that trace data from each query is sent to Phoenix.</span>

<span class="sd">    Note: Using this LlamaPack requires that your OpenAI API key is set via the</span>
<span class="sd">    OPENAI_API_KEY environment variable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes a new instance of ArizePhoenixQueryEnginePack.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[TextNode]): An input list of nodes over which the index</span>
<span class="sd">            will be built.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">phoenix</span> <span class="k">as</span> <span class="nn">px</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"The arize-phoenix package could not be found. "</span>
                <span class="s2">"Please install with `pip install arize-phoenix`."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">:</span> <span class="s2">"PhoenixSession"</span> <span class="o">=</span> <span class="n">px</span><span class="o">.</span><span class="n">launch_app</span><span class="p">()</span>
        <span class="n">set_global_handler</span><span class="p">(</span><span class="s2">"arize_phoenix"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">            LlamaPack.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">,</span>
            <span class="s2">"session_url"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Runs queries against the index.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Any: A response from the query engine.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/#llama_index.packs.arize_phoenix_query_engine.ArizePhoenixQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Returns a dictionary containing the internals of the LlamaPack.

**Returns:**

| Type | Description |
| --- | --- |
| `Dict[str, Any]` | 
Dict\[str, Any\]: A dictionary containing the internals of the



 |
| `Dict[str, Any]` | 

LlamaPack.



 |

Source code in `llama-index-packs/llama-index-packs-arize-phoenix-query-engine/llama_index/packs/arize_phoenix_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
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
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">        LlamaPack.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="p">,</span>
        <span class="s2">"session_url"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
        <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/#llama_index.packs.arize_phoenix_query_engine.ArizePhoenixQueryEnginePack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Runs queries against the index.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | 
A response from the query engine.



 |

Source code in `llama-index-packs/llama-index-packs-arize-phoenix-query-engine/llama_index/packs/arize_phoenix_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Runs queries against the index.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Any: A response from the query engine.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Amazon product extraction](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/)[Next Auto merging retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/)
