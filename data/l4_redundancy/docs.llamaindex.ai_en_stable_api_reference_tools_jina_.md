Title: Jina - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/

Markdown Content:
Jina - LlamaIndex


JinaToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/#llama_index.tools.jina.JinaToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Jina tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-jina/llama_index/tools/jina/base.py`

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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JinaToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Jina tool spec.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"jina_search"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_make_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">requests</span><span class="o">.</span><span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a request to the Jina Search API.</span>

<span class="sd">        Args:</span>
<span class="sd">            params (dict): The parameters to be passed to the API.</span>

<span class="sd">        Returns:</span>
<span class="sd">            requests.Response: The response from the API.</span>
<span class="sd">        """</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">url</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">URL</span><span class="p">(</span><span class="n">JINA_SEARCH_URL_ENDPOINT</span> <span class="o">+</span> <span class="n">params</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"query"</span><span class="p">)))</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">jina_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to the Jina Search engine to receive a list of results.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to Jina Search.</span>

<span class="sd">        Returns:</span>
<span class="sd">            [Document]: A list of documents containing search results.</span>
<span class="sd">        """</span>
        <span class="n">search_params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_request</span><span class="p">(</span><span class="n">search_params</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"content"</span><span class="p">],</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                    <span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                    <span class="s2">"description"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"description"</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### jina\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/#llama_index.tools.jina.JinaToolSpec.jina_search "Permanent link")

```
jina_search(query: str) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Make a query to the Jina Search engine to receive a list of results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to Jina Search.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
\[Document\]: A list of documents containing search results.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-jina/llama_index/tools/jina/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">jina_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to the Jina Search engine to receive a list of results.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to Jina Search.</span>

<span class="sd">    Returns:</span>
<span class="sd">        [Document]: A list of documents containing search results.</span>
<span class="sd">    """</span>
    <span class="n">search_params</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_request</span><span class="p">(</span><span class="n">search_params</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"content"</span><span class="p">],</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                <span class="s2">"description"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"description"</span><span class="p">],</span>
            <span class="p">},</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Ionic shopping](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/)[Next Load and search](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/)
