Title: Custom - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/

Markdown Content:
Custom - LlamaIndex


CustomQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/#llama_index.core.query_engine.CustomQueryEngine "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`, `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Custom query engine.

Subclasses can define additional attributes as Pydantic fields. Subclasses must implement the `custom_query` method, which takes a query string and returns either a Response object or a string as output.

They can optionally implement the `acustom_query` method for async support.

Source code in `llama-index-core/llama_index/core/query_engine/custom.py`

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
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CustomQueryEngine</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Custom query engine.</span>

<span class="sd">    Subclasses can define additional attributes as Pydantic fields.</span>
<span class="sd">    Subclasses must implement the `custom_query` method, which takes a query string</span>
<span class="sd">    and returns either a Response object or a string as output.</span>

<span class="sd">    They can optionally implement the `acustom_query` method for async support.</span>

<span class="sd">    """</span>

    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">([]),</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"query"</span><span class="p">):</span>
            <span class="c1"># if query bundle, just run the query</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="n">QueryBundle</span><span class="p">):</span>
                <span class="n">query_str</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span><span class="o">.</span><span class="n">query_str</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">query_str</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
            <span class="n">raw_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="n">Response</span><span class="p">(</span><span class="n">raw_response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">raw_response</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
                <span class="k">else</span> <span class="n">raw_response</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"query"</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="n">QueryBundle</span><span class="p">):</span>
                <span class="n">query_str</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span><span class="o">.</span><span class="n">query_str</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">query_str</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
            <span class="n">raw_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">acustom_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="n">Response</span><span class="p">(</span><span class="n">raw_response</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">raw_response</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
                <span class="k">else</span> <span class="n">raw_response</span>
            <span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">custom_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">STR_OR_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run a custom query."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acustom_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">STR_OR_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run a custom query asynchronously."""</span>
        <span class="c1"># by default, just run the synchronous version</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"This query engine does not support _query."</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"This query engine does not support _aquery."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### custom\_query `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/#llama_index.core.query_engine.CustomQueryEngine.custom_query "Permanent link")

```
custom_query(query_str: str) -> STR_OR_RESPONSE_TYPE
```

Run a custom query.

Source code in `llama-index-core/llama_index/core/query_engine/custom.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">custom_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">STR_OR_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run a custom query."""</span>
</code></pre></div></td></tr></tbody></table>

### acustom\_query `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/#llama_index.core.query_engine.CustomQueryEngine.acustom_query "Permanent link")

```
acustom_query(query_str: str) -> STR_OR_RESPONSE_TYPE
```

Run a custom query asynchronously.

Source code in `llama-index-core/llama_index/core/query_engine/custom.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">acustom_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">STR_OR_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run a custom query asynchronously."""</span>
    <span class="c1"># by default, just run the synchronous version</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/)
