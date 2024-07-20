Title: Html - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/

Markdown Content:
Html - LlamaIndex


Node parsers.

HTMLNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/#llama_index.core.node_parser.HTMLNodeParser "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[NodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "llama_index.core.node_parser.interface.NodeParser")`

HTML node parser.

Splits a document into Nodes using custom HTML splitting logic.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `include_metadata` | `bool` | 
whether to include metadata in nodes



 | _required_ |
| `include_prev_next_rel` | `bool` | 

whether to include prev/next relationships



 | _required_ |

Source code in `llama-index-core/llama_index/core/node_parser/file/html.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
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
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HTMLNodeParser</span><span class="p">(</span><span class="n">NodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""HTML node parser.</span>

<span class="sd">    Splits a document into Nodes using custom HTML splitting logic.</span>

<span class="sd">    Args:</span>
<span class="sd">        include_metadata (bool): whether to include metadata in nodes</span>
<span class="sd">        include_prev_next_rel (bool): whether to include prev/next relationships</span>

<span class="sd">    """</span>

    <span class="n">tags</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_TAGS</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"HTML tags to extract text from."</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tags</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">DEFAULT_TAGS</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HTMLNodeParser"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="n">tags</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"HTMLNodeParser"</span>

    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing nodes"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_node</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from document."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"bs4 is required to read HTML files."</span><span class="p">)</span>

        <span class="n">text</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
        <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
        <span class="n">html_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">last_tag</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">current_section</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="n">tags</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">find_all</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tags</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
            <span class="n">tag_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_text_from_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">tag</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="n">last_tag</span> <span class="ow">or</span> <span class="n">last_tag</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">last_tag</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">name</span>
            <span class="n">current_section</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">tag_text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">html_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_from_split</span><span class="p">(</span>
                    <span class="n">current_section</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="n">node</span><span class="p">,</span> <span class="p">{</span><span class="s2">"tag"</span><span class="p">:</span> <span class="n">last_tag</span><span class="p">}</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="n">last_tag</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">name</span>
            <span class="n">current_section</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">tag_text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

    <span class="k">if</span> <span class="n">current_section</span><span class="p">:</span>
        <span class="n">html_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_from_split</span><span class="p">(</span>
                <span class="n">current_section</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="n">node</span><span class="p">,</span> <span class="p">{</span><span class="s2">"tag"</span><span class="p">:</span> <span class="n">last_tag</span><span class="p">}</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">html_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Hierarchical](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/)
