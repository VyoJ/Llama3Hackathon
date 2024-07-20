Title: Json - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/

Markdown Content:
Json - LlamaIndex


Node parsers.

JSONNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/#llama_index.core.node_parser.JSONNodeParser "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[NodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "llama_index.core.node_parser.interface.NodeParser")`

JSON node parser.

Splits a document into Nodes using custom JSON splitting logic.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `include_metadata` | `bool` | 
whether to include metadata in nodes



 | _required_ |
| `include_prev_next_rel` | `bool` | 

whether to include prev/next relationships



 | _required_ |

Source code in `llama-index-core/llama_index/core/node_parser/file/json.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
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
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JSONNodeParser</span><span class="p">(</span><span class="n">NodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""JSON node parser.</span>

<span class="sd">    Splits a document into Nodes using custom JSON splitting logic.</span>

<span class="sd">    Args:</span>
<span class="sd">        include_metadata (bool): whether to include metadata in nodes</span>
<span class="sd">        include_prev_next_rel (bool): whether to include prev/next relationships</span>

<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"JSONNodeParser"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"JSONNodeParser"</span>

    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing nodes"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_node</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from document."""</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
            <span class="c1"># Handle invalid JSON input here</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">json_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[])]</span>
            <span class="n">json_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="n">build_nodes_from_splits</span><span class="p">([</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)],</span> <span class="n">node</span><span class="p">,</span> <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">json_object</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
                <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">json_object</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[])]</span>
                <span class="n">json_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="n">build_nodes_from_splits</span><span class="p">(</span>
                        <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)],</span> <span class="n">node</span><span class="p">,</span> <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"JSON is invalid"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">json_nodes</span>

    <span class="k">def</span> <span class="nf">_depth_first_yield</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">levels_back</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Do depth first yield of all of the leaf nodes of a JSON.</span>

<span class="sd">        Combines keys in the JSON tree using spaces.</span>

<span class="sd">        If levels_back is set to 0, prints all levels.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_data</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">json_data</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">new_path</span> <span class="o">=</span> <span class="n">path</span><span class="p">[:]</span>
                <span class="n">new_path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
                <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">levels_back</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_data</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">json_data</span><span class="p">):</span>
                <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">levels_back</span><span class="p">,</span> <span class="n">path</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">new_path</span> <span class="o">=</span> <span class="n">path</span><span class="p">[</span><span class="o">-</span><span class="n">levels_back</span><span class="p">:]</span>
            <span class="n">new_path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">json_data</span><span class="p">))</span>
            <span class="k">yield</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">new_path</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/#llama_index.core.node_parser.JSONNodeParser.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/node_parser/file/json.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"JSONNodeParser"</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes\_from\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/#llama_index.core.node_parser.JSONNodeParser.get_nodes_from_node "Permanent link")

```
get_nodes_from_node(node: [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")) -> List[[TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")]
```

Get nodes from document.

Source code in `llama-index-core/llama_index/core/node_parser/file/json.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
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
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from document."""</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
        <span class="c1"># Handle invalid JSON input here</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="n">json_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[])]</span>
        <span class="n">json_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
            <span class="n">build_nodes_from_splits</span><span class="p">([</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)],</span> <span class="n">node</span><span class="p">,</span> <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">)</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">json_object</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_depth_first_yield</span><span class="p">(</span><span class="n">json_object</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[])]</span>
            <span class="n">json_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="n">build_nodes_from_splits</span><span class="p">(</span>
                    <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)],</span> <span class="n">node</span><span class="p">,</span> <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span>
                <span class="p">)</span>
            <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"JSON is invalid"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">json_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/)[Next Langchain](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/)
