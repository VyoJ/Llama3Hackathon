Title: Duckduckgo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/

Markdown Content:
Duckduckgo - LlamaIndex


DuckDuckGoSearchToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/#llama_index.tools.duckduckgo.DuckDuckGoSearchToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

DuckDuckGoSearch tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-duckduckgo/llama_index/tools/duckduckgo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
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
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DuckDuckGoSearchToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DuckDuckGoSearch tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"duckduckgo_instant_search"</span><span class="p">,</span> <span class="s2">"duckduckgo_full_search"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span><span class="s2">"duckduckgo_search"</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"DuckDuckGoSearchToolSpec requires the duckduckgo_search package to be installed."</span>
            <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">duckduckgo_instant_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to DuckDuckGo api to receive an instant answer.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to DuckDuckGo.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">duckduckgo_search</span> <span class="kn">import</span> <span class="n">DDGS</span>

        <span class="k">with</span> <span class="n">DDGS</span><span class="p">()</span> <span class="k">as</span> <span class="n">ddg</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ddg</span><span class="o">.</span><span class="n">answers</span><span class="p">(</span><span class="n">query</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">duckduckgo_full_search</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"wt-wt"</span><span class="p">,</span>
        <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to DuckDuckGo search to receive a full search results.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to DuckDuckGo.</span>
<span class="sd">            region (Optional[str]): The region to be used for the search in [country-language] convention, ex us-en, uk-en, ru-ru, etc...</span>
<span class="sd">            max_results (Optional[int]): The maximum number of results to be returned.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">duckduckgo_search</span> <span class="kn">import</span> <span class="n">DDGS</span>

        <span class="n">params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"keywords"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
            <span class="s2">"region"</span><span class="p">:</span> <span class="n">region</span><span class="p">,</span>
            <span class="s2">"max_results"</span><span class="p">:</span> <span class="n">max_results</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="k">with</span> <span class="n">DDGS</span><span class="p">()</span> <span class="k">as</span> <span class="n">ddg</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ddg</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="o">**</span><span class="n">params</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### duckduckgo\_instant\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/#llama_index.tools.duckduckgo.DuckDuckGoSearchToolSpec.duckduckgo_instant_search "Permanent link")

```
duckduckgo_instant_search(query: str) -> List[Dict]
```

Make a query to DuckDuckGo api to receive an instant answer.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to DuckDuckGo.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-duckduckgo/llama_index/tools/duckduckgo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">duckduckgo_instant_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to DuckDuckGo api to receive an instant answer.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to DuckDuckGo.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">duckduckgo_search</span> <span class="kn">import</span> <span class="n">DDGS</span>

    <span class="k">with</span> <span class="n">DDGS</span><span class="p">()</span> <span class="k">as</span> <span class="n">ddg</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ddg</span><span class="o">.</span><span class="n">answers</span><span class="p">(</span><span class="n">query</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### duckduckgo\_full\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/#llama_index.tools.duckduckgo.DuckDuckGoSearchToolSpec.duckduckgo_full_search "Permanent link")

```
duckduckgo_full_search(query: str, region: Optional[str] = 'wt-wt', max_results: Optional[int] = 10) -> List[Dict]
```

Make a query to DuckDuckGo search to receive a full search results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to DuckDuckGo.



 | _required_ |
| `region` | `Optional[str]` | 

The region to be used for the search in \[country-language\] convention, ex us-en, uk-en, ru-ru, etc...



 | `'wt-wt'` |
| `max_results` | `Optional[int]` | 

The maximum number of results to be returned.



 | `10` |

Source code in `llama-index-integrations/tools/llama-index-tools-duckduckgo/llama_index/tools/duckduckgo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">30</span>
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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">duckduckgo_full_search</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"wt-wt"</span><span class="p">,</span>
    <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to DuckDuckGo search to receive a full search results.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to DuckDuckGo.</span>
<span class="sd">        region (Optional[str]): The region to be used for the search in [country-language] convention, ex us-en, uk-en, ru-ru, etc...</span>
<span class="sd">        max_results (Optional[int]): The maximum number of results to be returned.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">duckduckgo_search</span> <span class="kn">import</span> <span class="n">DDGS</span>

    <span class="n">params</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"keywords"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
        <span class="s2">"region"</span><span class="p">:</span> <span class="n">region</span><span class="p">,</span>
        <span class="s2">"max_results"</span><span class="p">:</span> <span class="n">max_results</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="k">with</span> <span class="n">DDGS</span><span class="p">()</span> <span class="k">as</span> <span class="n">ddg</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ddg</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="o">**</span><span class="n">params</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Database](https://docs.llamaindex.ai/en/stable/api_reference/tools/database/)[Next Exa](https://docs.llamaindex.ai/en/stable/api_reference/tools/exa/)
