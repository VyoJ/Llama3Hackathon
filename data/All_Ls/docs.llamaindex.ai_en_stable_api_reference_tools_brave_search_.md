Title: Brave search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/

Markdown Content:
Brave search - LlamaIndex


BraveSearchToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/#llama_index.tools.brave_search.BraveSearchToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Brave Search tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-brave-search/llama_index/tools/brave_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
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
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BraveSearchToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Brave Search tool spec.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"brave_search"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize with parameters.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>

    <span class="k">def</span> <span class="nf">_make_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">requests</span><span class="o">.</span><span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a request to the Brave Search API.</span>

<span class="sd">        Args:</span>
<span class="sd">            params (dict): The parameters to be passed to the API.</span>

<span class="sd">        Returns:</span>
<span class="sd">            requests.Response: The response from the API.</span>
<span class="sd">        """</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Accept-Encoding"</span><span class="p">:</span> <span class="s2">"gzip"</span><span class="p">,</span>
            <span class="s2">"X-Subscription-Token"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">url</span> <span class="o">=</span> <span class="n">SEARCH_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">params</span><span class="o">=</span><span class="n">urllib</span><span class="o">.</span><span class="n">parse</span><span class="o">.</span><span class="n">urlencode</span><span class="p">(</span><span class="n">params</span><span class="p">))</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">brave_search</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">search_lang</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span> <span class="n">num_results</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to the Brave Search engine to receive a list of results.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to Brave Search.</span>
<span class="sd">            search_lang (str): The search language preference (ISO 639-1), default is "en".</span>
<span class="sd">            num_results (int): The number of search results returned in response, default is 5.</span>

<span class="sd">        Returns:</span>
<span class="sd">            [Document]: A list of documents containing search results.</span>
<span class="sd">        """</span>
        <span class="n">search_params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"q"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
            <span class="s2">"search_lang"</span><span class="p">:</span> <span class="n">search_lang</span><span class="p">,</span>
            <span class="s2">"count"</span><span class="p">:</span> <span class="n">num_results</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_request</span><span class="p">(</span><span class="n">search_params</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### brave\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/#llama_index.tools.brave_search.BraveSearchToolSpec.brave_search "Permanent link")

```
brave_search(query: str, search_lang: str = 'en', num_results: int = 5) -> [[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Make a query to the Brave Search engine to receive a list of results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to Brave Search.



 | _required_ |
| `search_lang` | `str` | 

The search language preference (ISO 639-1), default is "en".



 | `'en'` |
| `num_results` | `int` | 

The number of search results returned in response, default is 5.



 | `5` |

**Returns:**

| Type | Description |
| --- | --- |
| `[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
\[Document\]: A list of documents containing search results.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-brave-search/llama_index/tools/brave_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
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
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">brave_search</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">search_lang</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span> <span class="n">num_results</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to the Brave Search engine to receive a list of results.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to Brave Search.</span>
<span class="sd">        search_lang (str): The search language preference (ISO 639-1), default is "en".</span>
<span class="sd">        num_results (int): The number of search results returned in response, default is 5.</span>

<span class="sd">    Returns:</span>
<span class="sd">        [Document]: A list of documents containing search results.</span>
<span class="sd">    """</span>
    <span class="n">search_params</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"q"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
        <span class="s2">"search_lang"</span><span class="p">:</span> <span class="n">search_lang</span><span class="p">,</span>
        <span class="s2">"count"</span><span class="p">:</span> <span class="n">num_results</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_request</span><span class="p">(</span><span class="n">search_params</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Bing search](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/)[Next Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/tools/cassandra/)
