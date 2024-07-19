Title: Unstructured element - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/

Markdown Content:
Unstructured element - LlamaIndex


Node parsers.

UnstructuredElementNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/#llama_index.core.node_parser.UnstructuredElementNodeParser "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseElementNodeParser`

Unstructured element node parser.

Splits a document into Text Nodes and Index Nodes corresponding to embedded objects (e.g. tables).

Source code in `llama-index-core/llama_index/core/node_parser/relational/unstructured_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
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
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">UnstructuredElementNodeParser</span><span class="p">(</span><span class="n">BaseElementNodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Unstructured element node parser.</span>

<span class="sd">    Splits a document into Text Nodes and Index Nodes corresponding to embedded objects</span>
<span class="sd">    (e.g. tables).</span>

<span class="sd">    """</span>

    <span class="n">partitioning_parameters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="p">{},</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Extra dictionary representing parameters of the partitioning process."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summary_query_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_SUMMARY_QUERY_STR</span><span class="p">,</span>
        <span class="n">partitioning_parameters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{},</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">lxml</span>  <span class="c1"># noqa  # pants: no-infer-dep</span>
            <span class="kn">import</span> <span class="nn">unstructured</span>  <span class="c1"># noqa  # pants: no-infer-dep</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"You must install the `unstructured` and `lxml` "</span>
                <span class="s2">"package to use this node parser."</span>
            <span class="p">)</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">summary_query_str</span><span class="o">=</span><span class="n">summary_query_str</span><span class="p">,</span>
            <span class="n">partitioning_parameters</span><span class="o">=</span><span class="n">partitioning_parameters</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"UnstructuredElementNodeParser"</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from node."""</span>
        <span class="n">elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_elements</span><span class="p">(</span>
            <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">table_elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_table_elements</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span>
        <span class="c1"># extract summaries over table elements</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">extract_table_summaries</span><span class="p">(</span><span class="n">table_elements</span><span class="p">)</span>
        <span class="c1"># convert into nodes</span>
        <span class="c1"># will return a list of Nodes and Index Nodes</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_elements</span><span class="p">(</span>
            <span class="n">elements</span><span class="p">,</span> <span class="n">node</span><span class="p">,</span> <span class="n">ref_doc_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="n">source_document</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span> <span class="ow">or</span> <span class="n">node</span><span class="o">.</span><span class="n">as_related_node_info</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">n</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">]</span> <span class="o">=</span> <span class="n">source_document</span>
            <span class="n">n</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from node."""</span>
        <span class="n">elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_elements</span><span class="p">(</span>
            <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">table_elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_table_elements</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span>
        <span class="c1"># extract summaries over table elements</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aextract_table_summaries</span><span class="p">(</span><span class="n">table_elements</span><span class="p">)</span>
        <span class="c1"># convert into nodes</span>
        <span class="c1"># will return a list of Nodes and Index Nodes</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_elements</span><span class="p">(</span>
            <span class="n">elements</span><span class="p">,</span> <span class="n">node</span><span class="p">,</span> <span class="n">ref_doc_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="n">source_document</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span> <span class="ow">or</span> <span class="n">node</span><span class="o">.</span><span class="n">as_related_node_info</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">n</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">]</span> <span class="o">=</span> <span class="n">source_document</span>
            <span class="n">n</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">extract_elements</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">table_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract elements from text."""</span>
        <span class="kn">from</span> <span class="nn">unstructured.partition.html</span> <span class="kn">import</span> <span class="n">partition_html</span>  <span class="c1"># pants: no-infer-dep</span>

        <span class="n">table_filters</span> <span class="o">=</span> <span class="n">table_filters</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">elements</span> <span class="o">=</span> <span class="n">partition_html</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">partitioning_parameters</span><span class="p">)</span>
        <span class="n">output_els</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">elements</span><span class="p">):</span>
            <span class="k">if</span> <span class="s2">"unstructured.documents.elements.Table"</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">element</span><span class="p">)):</span>
                <span class="n">should_keep</span> <span class="o">=</span> <span class="nb">all</span><span class="p">(</span><span class="n">tf</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">tf</span> <span class="ow">in</span> <span class="n">table_filters</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">should_keep</span><span class="p">:</span>
                    <span class="n">table_df</span> <span class="o">=</span> <span class="n">html_to_df</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">text_as_html</span><span class="p">))</span>
                    <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Element</span><span class="p">(</span>
                            <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                            <span class="nb">type</span><span class="o">=</span><span class="s2">"table"</span><span class="p">,</span>
                            <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="p">,</span>
                            <span class="n">table</span><span class="o">=</span><span class="n">table_df</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># if not a table, keep it as Text as we don't want to lose context</span>
                    <span class="kn">from</span> <span class="nn">unstructured.documents.elements</span> <span class="kn">import</span> <span class="n">Text</span>

                    <span class="n">new_element</span> <span class="o">=</span> <span class="n">Text</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">element</span><span class="p">))</span>
                    <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Element</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">new_element</span><span class="p">)</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Element</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">output_els</span>

    <span class="k">def</span> <span class="nf">filter_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table_element</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Filter tables."""</span>
        <span class="n">table_df</span> <span class="o">=</span> <span class="n">html_to_df</span><span class="p">(</span><span class="n">table_element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">text_as_html</span><span class="p">)</span>

        <span class="c1"># check if table_df is not None, has more than one row, and more than one column</span>
        <span class="k">return</span> <span class="n">table_df</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">table_df</span><span class="o">.</span><span class="n">empty</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">table_df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes\_from\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/#llama_index.core.node_parser.UnstructuredElementNodeParser.get_nodes_from_node "Permanent link")

```
get_nodes_from_node(node: [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from node.

Source code in `llama-index-core/llama_index/core/node_parser/relational/unstructured_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">60</span>
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
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from node."""</span>
    <span class="n">elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_elements</span><span class="p">(</span>
        <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="n">table_elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_table_elements</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span>
    <span class="c1"># extract summaries over table elements</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">extract_table_summaries</span><span class="p">(</span><span class="n">table_elements</span><span class="p">)</span>
    <span class="c1"># convert into nodes</span>
    <span class="c1"># will return a list of Nodes and Index Nodes</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_elements</span><span class="p">(</span>
        <span class="n">elements</span><span class="p">,</span> <span class="n">node</span><span class="p">,</span> <span class="n">ref_doc_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>
    <span class="p">)</span>

    <span class="n">source_document</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span> <span class="ow">or</span> <span class="n">node</span><span class="o">.</span><span class="n">as_related_node_info</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">n</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">]</span> <span class="o">=</span> <span class="n">source_document</span>
        <span class="n">n</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### aget\_nodes\_from\_node `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/#llama_index.core.node_parser.UnstructuredElementNodeParser.aget_nodes_from_node "Permanent link")

```
aget_nodes_from_node(node: [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from node.

Source code in `llama-index-core/llama_index/core/node_parser/relational/unstructured_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from node."""</span>
    <span class="n">elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_elements</span><span class="p">(</span>
        <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="n">table_elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_table_elements</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span>
    <span class="c1"># extract summaries over table elements</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aextract_table_summaries</span><span class="p">(</span><span class="n">table_elements</span><span class="p">)</span>
    <span class="c1"># convert into nodes</span>
    <span class="c1"># will return a list of Nodes and Index Nodes</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_elements</span><span class="p">(</span>
        <span class="n">elements</span><span class="p">,</span> <span class="n">node</span><span class="p">,</span> <span class="n">ref_doc_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>
    <span class="p">)</span>

    <span class="n">source_document</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span> <span class="ow">or</span> <span class="n">node</span><span class="o">.</span><span class="n">as_related_node_info</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">n</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">]</span> <span class="o">=</span> <span class="n">source_document</span>
        <span class="n">n</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### extract\_elements [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/#llama_index.core.node_parser.UnstructuredElementNodeParser.extract_elements "Permanent link")

```
extract_elements(text: str, table_filters: Optional[List[Callable]] = None, **kwargs: Any) -> List[Element]
```

Extract elements from text.

Source code in `llama-index-core/llama_index/core/node_parser/relational/unstructured_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">extract_elements</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">table_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Extract elements from text."""</span>
    <span class="kn">from</span> <span class="nn">unstructured.partition.html</span> <span class="kn">import</span> <span class="n">partition_html</span>  <span class="c1"># pants: no-infer-dep</span>

    <span class="n">table_filters</span> <span class="o">=</span> <span class="n">table_filters</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">elements</span> <span class="o">=</span> <span class="n">partition_html</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">partitioning_parameters</span><span class="p">)</span>
    <span class="n">output_els</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">elements</span><span class="p">):</span>
        <span class="k">if</span> <span class="s2">"unstructured.documents.elements.Table"</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">element</span><span class="p">)):</span>
            <span class="n">should_keep</span> <span class="o">=</span> <span class="nb">all</span><span class="p">(</span><span class="n">tf</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">tf</span> <span class="ow">in</span> <span class="n">table_filters</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">should_keep</span><span class="p">:</span>
                <span class="n">table_df</span> <span class="o">=</span> <span class="n">html_to_df</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">text_as_html</span><span class="p">))</span>
                <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">"table"</span><span class="p">,</span>
                        <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="p">,</span>
                        <span class="n">table</span><span class="o">=</span><span class="n">table_df</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># if not a table, keep it as Text as we don't want to lose context</span>
                <span class="kn">from</span> <span class="nn">unstructured.documents.elements</span> <span class="kn">import</span> <span class="n">Text</span>

                <span class="n">new_element</span> <span class="o">=</span> <span class="n">Text</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">element</span><span class="p">))</span>
                <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Element</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">new_element</span><span class="p">)</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">output_els</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Element</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">output_els</span>
</code></pre></div></td></tr></tbody></table>

### filter\_table [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/#llama_index.core.node_parser.UnstructuredElementNodeParser.filter_table "Permanent link")

```
filter_table(table_element: Any) -> bool
```

Filter tables.

Source code in `llama-index-core/llama_index/core/node_parser/relational/unstructured_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">filter_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table_element</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Filter tables."""</span>
    <span class="n">table_df</span> <span class="o">=</span> <span class="n">html_to_df</span><span class="p">(</span><span class="n">table_element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">text_as_html</span><span class="p">)</span>

    <span class="c1"># check if table_df is not None, has more than one row, and more than one column</span>
    <span class="k">return</span> <span class="n">table_df</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">table_df</span><span class="o">.</span><span class="n">empty</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">table_df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Token text splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/)[Next NER PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/NER_PII/)
