Title: Ionic shopping - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/

Markdown Content:
Ionic shopping - LlamaIndex


IonicShoppingToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/#llama_index.tools.ionic_shopping.IonicShoppingToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Ionic Shopping tool spec.

This tool can be used to build e-commerce experiences with LLMs.

Source code in `llama-index-integrations/tools/llama-index-tools-ionic-shopping/llama_index/tools/ionic_shopping/base.py`

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
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IonicShoppingToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Ionic Shopping tool spec.</span>

<span class="sd">    This tool can be used to build e-commerce experiences with LLMs.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"query"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Ionic API Key.</span>

<span class="sd">        Learn more about attribution with Ionic API Keys</span>
<span class="sd">        https://docs.ioniccommerce.com/guides/attribution</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">ionic</span> <span class="kn">import</span> <span class="n">Ionic</span> <span class="k">as</span> <span class="n">IonicSDK</span>

        <span class="k">if</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">IonicSDK</span><span class="p">(</span><span class="n">api_key_header</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">IonicSDK</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">min_price</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_price</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Product</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Use this function to search for products and to get product recommendations.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): A precise query of a product name or product category</span>
<span class="sd">            num_results (Optional[int]): Defaults to 5. The number of product results to return.</span>
<span class="sd">            min_price (Option[int]): The minimum price in cents the requester is willing to pay</span>
<span class="sd">            max_price (Option[int]): The maximum price in cents the requester is willing to pay</span>
<span class="sd">        """</span>
        <span class="n">request</span> <span class="o">=</span> <span class="n">QueryAPIRequest</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">SDKQuery</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
                <span class="n">min_price</span><span class="o">=</span><span class="n">min_price</span><span class="p">,</span>
                <span class="n">max_price</span><span class="o">=</span><span class="n">max_price</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">QueryResponse</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">request</span><span class="o">=</span><span class="n">request</span><span class="p">,</span>
            <span class="n">security</span><span class="o">=</span><span class="n">QuerySecurity</span><span class="p">(),</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">product</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">query_api_response</span><span class="o">.</span><span class="n">results</span>
            <span class="k">for</span> <span class="n">product</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">products</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/#llama_index.tools.ionic_shopping.IonicShoppingToolSpec.query "Permanent link")

```
query(query: str, num_results: Optional[int] = 5, min_price: Optional[int] = None, max_price: Optional[int] = None) -> list[Product]
```

Use this function to search for products and to get product recommendations.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
A precise query of a product name or product category



 | _required_ |
| `num_results` | `Optional[int]` | 

Defaults to 5. The number of product results to return.



 | `5` |
| `min_price` | `Option[int]` | 

The minimum price in cents the requester is willing to pay



 | `None` |
| `max_price` | `Option[int]` | 

The maximum price in cents the requester is willing to pay



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-ionic-shopping/llama_index/tools/ionic_shopping/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
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
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">min_price</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_price</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Product</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Use this function to search for products and to get product recommendations.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): A precise query of a product name or product category</span>
<span class="sd">        num_results (Optional[int]): Defaults to 5. The number of product results to return.</span>
<span class="sd">        min_price (Option[int]): The minimum price in cents the requester is willing to pay</span>
<span class="sd">        max_price (Option[int]): The maximum price in cents the requester is willing to pay</span>
<span class="sd">    """</span>
    <span class="n">request</span> <span class="o">=</span> <span class="n">QueryAPIRequest</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">SDKQuery</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
            <span class="n">min_price</span><span class="o">=</span><span class="n">min_price</span><span class="p">,</span>
            <span class="n">max_price</span><span class="o">=</span><span class="n">max_price</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">QueryResponse</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="n">request</span><span class="o">=</span><span class="n">request</span><span class="p">,</span>
        <span class="n">security</span><span class="o">=</span><span class="n">QuerySecurity</span><span class="p">(),</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">product</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">query_api_response</span><span class="o">.</span><span class="n">results</span>
        <span class="k">for</span> <span class="n">product</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">products</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/tools/)[Next Jina](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/)
