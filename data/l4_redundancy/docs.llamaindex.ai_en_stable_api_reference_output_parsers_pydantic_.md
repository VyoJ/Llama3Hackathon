Title: Pydantic - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/

Markdown Content:
Pydantic - LlamaIndex


Output parsers.

PydanticOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/#llama_index.core.output_parsers.PydanticOutputParser "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ChainableOutputParser`

Pydantic Output Parser.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `output_cls` | `BaseModel` | 
Pydantic output class.



 | _required_ |

Source code in `llama-index-core/llama_index/core/output_parsers/pydantic.py`

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
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PydanticOutputParser</span><span class="p">(</span><span class="n">ChainableOutputParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pydantic Output Parser.</span>

<span class="sd">    Args:</span>
<span class="sd">        output_cls (BaseModel): Pydantic output class.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">],</span>
        <span class="n">excluded_schema_keys_from_format</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">pydantic_format_tmpl</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PYDANTIC_FORMAT_TMPL</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_excluded_schema_keys_from_format</span> <span class="o">=</span> <span class="n">excluded_schema_keys_from_format</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pydantic_format_tmpl</span> <span class="o">=</span> <span class="n">pydantic_format_tmpl</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">format_string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format string."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_format_string</span><span class="p">(</span><span class="n">escape_json</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_format_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">escape_json</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format string."""</span>
        <span class="n">schema_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">schema</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_excluded_schema_keys_from_format</span><span class="p">:</span>
            <span class="k">del</span> <span class="n">schema_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>

        <span class="n">schema_str</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">schema_dict</span><span class="p">)</span>
        <span class="n">output_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pydantic_format_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">schema</span><span class="o">=</span><span class="n">schema_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">escape_json</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">output_str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{"</span><span class="p">,</span> <span class="s2">"{{"</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"}"</span><span class="p">,</span> <span class="s2">"}}"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">output_str</span>

    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
        <span class="n">json_str</span> <span class="o">=</span> <span class="n">extract_json_str</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">json_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
        <span class="k">return</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_format_string</span><span class="p">(</span><span class="n">escape_json</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format\_string `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/#llama_index.core.output_parsers.PydanticOutputParser.format_string "Permanent link")

```
format_string: str
```

Format string.

### get\_format\_string [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/#llama_index.core.output_parsers.PydanticOutputParser.get_format_string "Permanent link")

```
get_format_string(escape_json: bool = True) -> str
```

Format string.

Source code in `llama-index-core/llama_index/core/output_parsers/pydantic.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">46</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_format_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">escape_json</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format string."""</span>
    <span class="n">schema_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">schema</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_excluded_schema_keys_from_format</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">schema_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>

    <span class="n">schema_str</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">schema_dict</span><span class="p">)</span>
    <span class="n">output_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pydantic_format_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">schema</span><span class="o">=</span><span class="n">schema_str</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">escape_json</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">output_str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{"</span><span class="p">,</span> <span class="s2">"{{"</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"}"</span><span class="p">,</span> <span class="s2">"}}"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">output_str</span>
</code></pre></div></td></tr></tbody></table>

### parse [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/#llama_index.core.output_parsers.PydanticOutputParser.parse "Permanent link")

```
parse(text: str) -> Any
```

Parse, validate, and correct errors programmatically.

Source code in `llama-index-core/llama_index/core/output_parsers/pydantic.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Parse, validate, and correct errors programmatically."""</span>
    <span class="n">json_str</span> <span class="o">=</span> <span class="n">extract_json_str</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">json_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/#llama_index.core.output_parsers.PydanticOutputParser.format "Permanent link")

```
format(query: str) -> str
```

Format a query with structured output formatting instructions.

Source code in `llama-index-core/llama_index/core/output_parsers/pydantic.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format a query with structured output formatting instructions."""</span>
    <span class="k">return</span> <span class="n">query</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_format_string</span><span class="p">(</span><span class="n">escape_json</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Langchain](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/)[Next Selection](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/)
