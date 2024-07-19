Title: Yelp - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/

Markdown Content:
Yelp - LlamaIndex


YelpToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Yelp tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-yelp/llama_index/tools/yelp/base.py`

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
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">YelpToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Yelp tool spec."""</span>

    <span class="c1"># TODO add disclaimer</span>
    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"business_search"</span><span class="p">,</span> <span class="s2">"business_reviews"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">client_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="kn">from</span> <span class="nn">yelpapi</span> <span class="kn">import</span> <span class="n">YelpAPI</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">YelpAPI</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">business_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">term</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">radius</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to Yelp to find businesses given a location to search.</span>

<span class="sd">        Args:</span>
<span class="sd">            Businesses returned in the response may not be strictly within the specified location.</span>
<span class="sd">            term (str): Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks"</span>
<span class="sd">            radius (int): A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.</span>


<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search_query</span><span class="p">(</span><span class="n">location</span><span class="o">=</span><span class="n">location</span><span class="p">,</span> <span class="n">term</span><span class="o">=</span><span class="n">term</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">))]</span>

    <span class="k">def</span> <span class="nf">business_reviews</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to Yelp to find a business uising an id from business_search.</span>

<span class="sd">        Args:</span>
<span class="sd">            # The id</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">reviews_query</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="nb">id</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">))]</span>
</code></pre></div></td></tr></tbody></table>

### business\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec.business_search "Permanent link")

```
business_search(location: str, term: str, radius: Optional[int] = None)
```

Make a query to Yelp to find businesses given a location to search.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `term` | `str` | 
Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks"



 | _required_ |
| `radius` | `int` | 

A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-yelp/llama_index/tools/yelp/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
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
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">business_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">term</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">radius</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to Yelp to find businesses given a location to search.</span>

<span class="sd">    Args:</span>
<span class="sd">        Businesses returned in the response may not be strictly within the specified location.</span>
<span class="sd">        term (str): Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks"</span>
<span class="sd">        radius (int): A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.</span>


<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search_query</span><span class="p">(</span><span class="n">location</span><span class="o">=</span><span class="n">location</span><span class="p">,</span> <span class="n">term</span><span class="o">=</span><span class="n">term</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">))]</span>
</code></pre></div></td></tr></tbody></table>

### business\_reviews [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec.business_reviews "Permanent link")

```
business_reviews(id: str)
```

Make a query to Yelp to find a business uising an id from business\_search.

Source code in `llama-index-integrations/tools/llama-index-tools-yelp/llama_index/tools/yelp/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">business_reviews</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to Yelp to find a business uising an id from business_search.</span>

<span class="sd">    Args:</span>
<span class="sd">        # The id</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">reviews_query</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="nb">id</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">))]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Yahoo finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/yahoo_finance/)[Next Zapier](https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/)
