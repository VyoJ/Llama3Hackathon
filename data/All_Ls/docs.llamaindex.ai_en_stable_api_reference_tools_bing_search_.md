Title: Bing search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/

Markdown Content:
Bing search - LlamaIndex


BingSearchToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/#llama_index.tools.bing_search.BingSearchToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Bing Search tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-bing-search/llama_index/tools/bing_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BingSearchToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Bing Search tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"bing_news_search"</span><span class="p">,</span> <span class="s2">"bing_image_search"</span><span class="p">,</span> <span class="s2">"bing_video_search"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"en-US"</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">lang</span> <span class="o">=</span> <span class="n">lang</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_bing_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">ENDPOINT_BASE_URL</span> <span class="o">+</span> <span class="n">endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"Ocp-Apim-Subscription-Key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">},</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"q"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span> <span class="s2">"mkt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang</span><span class="p">,</span> <span class="s2">"count"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">},</span>
        <span class="p">)</span>
        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[[</span><span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">]</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]]</span>

    <span class="k">def</span> <span class="nf">bing_news_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to bing news search. Useful for finding news on a query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to bing.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"news/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"description"</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">bing_image_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to bing images search. Useful for finding an image of a query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to bing.</span>

<span class="sd">        returns a url of the images found</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"images/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"contentUrl"</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">bing_video_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to bing video search. Useful for finding a video related to a query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to bing.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"videos/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"contentUrl"</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### bing\_news\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/#llama_index.tools.bing_search.BingSearchToolSpec.bing_news_search "Permanent link")

```
bing_news_search(query: str)
```

Make a query to bing news search. Useful for finding news on a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to bing.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-bing-search/llama_index/tools/bing_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">bing_news_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to bing news search. Useful for finding news on a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to bing.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"news/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"description"</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### bing\_image\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/#llama_index.tools.bing_search.BingSearchToolSpec.bing_image_search "Permanent link")

```
bing_image_search(query: str)
```

Make a query to bing images search. Useful for finding an image of a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to bing.



 | _required_ |

returns a url of the images found

Source code in `llama-index-integrations/tools/llama-index-tools-bing-search/llama_index/tools/bing_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">bing_image_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to bing images search. Useful for finding an image of a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to bing.</span>

<span class="sd">    returns a url of the images found</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"images/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"contentUrl"</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### bing\_video\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/#llama_index.tools.bing_search.BingSearchToolSpec.bing_video_search "Permanent link")

```
bing_video_search(query: str)
```

Make a query to bing video search. Useful for finding a video related to a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to bing.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-bing-search/llama_index/tools/bing_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">bing_video_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to bing video search. Useful for finding a video related to a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to bing.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bing_request</span><span class="p">(</span><span class="s2">"videos/search"</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"contentUrl"</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure translate](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)[Next Brave search](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/)
