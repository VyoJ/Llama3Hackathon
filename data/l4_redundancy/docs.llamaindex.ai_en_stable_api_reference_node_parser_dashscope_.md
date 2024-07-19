Title: Dashscope - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/

Markdown Content:
Dashscope - LlamaIndex


DashScopeJsonNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/#llama_index.node_parser.dashscope.DashScopeJsonNodeParser "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseElementNodeParser`

DashScope Json format element node parser.

Splits a json format document from DashScope Parse into Text Nodes and Index Nodes corresponding to embedded objects (e.g. tables).

Source code in `llama-index-integrations/node_parser/llama-index-node-parser-relational-dashscope/llama_index/node_parser/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 15</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DashScopeJsonNodeParser</span><span class="p">(</span><span class="n">BaseElementNodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DashScope Json format element node parser.</span>

<span class="sd">    Splits a json format document from DashScope Parse into Text Nodes and Index Nodes</span>
<span class="sd">    corresponding to embedded objects (e.g. tables).</span>
<span class="sd">    """</span>

    <span class="n">try_count_limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Maximum number of retry attempts."</span>
    <span class="p">)</span>
    <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">500</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Size of each chunk to process."</span><span class="p">)</span>
    <span class="n">overlap_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Overlap size between consecutive chunks."</span>
    <span class="p">)</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">" |,|，|。|？|！|</span><span class="se">\n</span><span class="s2">|</span><span class="se">\\</span><span class="s2">?|</span><span class="se">\\</span><span class="s2">!"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Separator characters for splitting texts."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">input_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">"idp"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"parse format type."</span><span class="p">)</span>
    <span class="n">language</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"cn"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"language of tokenizor, accept cn, en, any. Notice that &lt;any&gt; mode will be slow."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"DashScopeJsonNodeParser"</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from node."""</span>
        <span class="n">ftype</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parse_fmt_type"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_type</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">ftype</span> <span class="ow">in</span> <span class="p">[</span>
            <span class="s2">"DASHSCOPE_DOCMIND"</span><span class="p">,</span>
            <span class="s2">"idp"</span><span class="p">,</span>
        <span class="p">],</span> <span class="sa">f</span><span class="s2">"Unexpected parse_fmt_type: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'parse_fmt_type'</span><span class="p">,</span><span class="w"> </span><span class="s1">''</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">ftype_map</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"DASHSCOPE_DOCMIND"</span><span class="p">:</span> <span class="s2">"idp"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">my_input</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"text"</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()),</span>
            <span class="s2">"file_type"</span><span class="p">:</span> <span class="n">ftype_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ftype</span><span class="p">,</span> <span class="n">ftype</span><span class="p">),</span>
            <span class="s2">"chunk_size"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="s2">"overlap_size"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">overlap_size</span><span class="p">,</span>
            <span class="s2">"language"</span><span class="p">:</span> <span class="s2">"cn"</span><span class="p">,</span>
            <span class="s2">"separator"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">separator</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">try_count</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">response_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">post_service</span><span class="p">(</span><span class="n">my_input</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">response_text</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">try_count</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_count_limit</span><span class="p">:</span>
            <span class="n">try_count</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">response_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">post_service</span><span class="p">(</span><span class="n">my_input</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response_text</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"DashScopeJsonNodeParser Failed to get response from service"</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_result</span><span class="p">(</span><span class="n">response_text</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">post_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">my_input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
        <span class="n">DASHSCOPE_API_KEY</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">DASHSCOPE_API_KEY</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY is not set"</span><span class="p">)</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY is not set"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Accept-Encoding"</span><span class="p">:</span> <span class="s2">"utf-8"</span><span class="p">,</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="s2">"Bearer "</span> <span class="o">+</span> <span class="n">DASHSCOPE_API_KEY</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">service_url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DASHSCOPE_BASE_URL"</span><span class="p">,</span> <span class="s2">"https://dashscope.aliyuncs.com"</span><span class="p">)</span>
            <span class="o">+</span> <span class="s2">"/api/v1/indices/component/configed_transformations/spliter"</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
                <span class="n">service_url</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">my_input</span><span class="p">),</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span>
            <span class="p">)</span>
            <span class="n">response_text</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="k">if</span> <span class="s2">"chunkService"</span> <span class="ow">in</span> <span class="n">response_text</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">response_text</span><span class="p">[</span><span class="s2">"chunkService"</span><span class="p">][</span><span class="s2">"chunkResult"</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="s2">, try again."</span><span class="p">)</span>
                <span class="k">return</span> <span class="kc">None</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">, try again."</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">parse_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">content_json</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">document</span><span class="p">:</span> <span class="n">TextNode</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">content_json</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="n">data</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hier_title"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span> <span class="n">data</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]]</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                    <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">extract_elements</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"json"</span><span class="p">,</span>
        <span class="n">node_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes\_from\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/#llama_index.node_parser.dashscope.DashScopeJsonNodeParser.get_nodes_from_node "Permanent link")

```
get_nodes_from_node(node: [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from node.

Source code in `llama-index-integrations/node_parser/llama-index-node-parser-relational-dashscope/llama_index/node_parser/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from node."""</span>
    <span class="n">ftype</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parse_fmt_type"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_type</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">ftype</span> <span class="ow">in</span> <span class="p">[</span>
        <span class="s2">"DASHSCOPE_DOCMIND"</span><span class="p">,</span>
        <span class="s2">"idp"</span><span class="p">,</span>
    <span class="p">],</span> <span class="sa">f</span><span class="s2">"Unexpected parse_fmt_type: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'parse_fmt_type'</span><span class="p">,</span><span class="w"> </span><span class="s1">''</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>

    <span class="n">ftype_map</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"DASHSCOPE_DOCMIND"</span><span class="p">:</span> <span class="s2">"idp"</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">my_input</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"text"</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()),</span>
        <span class="s2">"file_type"</span><span class="p">:</span> <span class="n">ftype_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ftype</span><span class="p">,</span> <span class="n">ftype</span><span class="p">),</span>
        <span class="s2">"chunk_size"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">,</span>
        <span class="s2">"overlap_size"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">overlap_size</span><span class="p">,</span>
        <span class="s2">"language"</span><span class="p">:</span> <span class="s2">"cn"</span><span class="p">,</span>
        <span class="s2">"separator"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">separator</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">try_count</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">response_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">post_service</span><span class="p">(</span><span class="n">my_input</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">response_text</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">try_count</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_count_limit</span><span class="p">:</span>
        <span class="n">try_count</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">response_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">post_service</span><span class="p">(</span><span class="n">my_input</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">response_text</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"DashScopeJsonNodeParser Failed to get response from service"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_result</span><span class="p">(</span><span class="n">response_text</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Replicate](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/)[Next Code](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/)
