Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/

Markdown Content:
Index - LlamaIndex


Node parser interface.

NodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")`, `ABC`

Base interface for node parser.

Source code in `llama-index-core/llama_index/core/node_parser/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
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
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NodeParser</span><span class="p">(</span><span class="n">TransformComponent</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base interface for node parser."""</span>

    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether or not to consider metadata when splitting."</span>
    <span class="p">)</span>
    <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Include prev/next node relationships."</span>
    <span class="p">)</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>
    <span class="n">id_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Function to generate node IDs."</span><span class="p">,</span>
        <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"id_func"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_validate_id_func</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">default_id_func</span>
        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aparse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_postprocess_parsed_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">parent_doc_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Document</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">parent_doc</span> <span class="o">=</span> <span class="n">parent_doc_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">parent_doc</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">start_char_idx</span> <span class="o">=</span> <span class="n">parent_doc</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
                <span class="p">)</span>

                <span class="c1"># update start/end char idx</span>
                <span class="k">if</span> <span class="n">start_char_idx</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">start_char_idx</span> <span class="o">=</span> <span class="n">start_char_idx</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">end_char_idx</span> <span class="o">=</span> <span class="n">start_char_idx</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span>
                        <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
                    <span class="p">)</span>

                <span class="c1"># update metadata</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_metadata</span><span class="p">:</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">parent_doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_prev_next_rel</span><span class="p">:</span>
                <span class="c1"># establish prev/next relationships if nodes share the same source_node</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="n">i</span> <span class="o">&gt;</span> <span class="mi">0</span>
                    <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span>
                    <span class="ow">and</span> <span class="n">nodes</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">source_node</span>
                    <span class="ow">and</span> <span class="n">nodes</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">source_node</span><span class="o">.</span><span class="n">node_id</span> <span class="o"></span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span><span class="o">.</span><span class="n">node_id</span>
                <span class="p">):</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">NEXT</span><span class="p">]</span> <span class="o">=</span> <span class="n">nodes</span><span class="p">[</span>
                        <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
                    <span class="p">]</span><span class="o">.</span><span class="n">as_related_node_info</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse documents into nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (Sequence[Document]): documents to parse</span>
<span class="sd">            show_progress (bool): whether to show progress bar</span>

<span class="sd">        """</span>
        <span class="n">doc_id_to_document</span> <span class="o">=</span> <span class="p">{</span><span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">:</span> <span class="n">doc</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">}</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">NODE_PARSING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">:</span> <span class="n">documents</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_nodes</span><span class="p">(</span><span class="n">documents</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_postprocess_parsed_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">doc_id_to_document</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">({</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes_from_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">doc_id_to_document</span> <span class="o">=</span> <span class="p">{</span><span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">:</span> <span class="n">doc</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">}</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">NODE_PARSING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">:</span> <span class="n">documents</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aparse_nodes</span><span class="p">(</span>
                <span class="n">documents</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_postprocess_parsed_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">doc_id_to_document</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">({</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_nodes_from_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes\_from\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser.get_nodes_from_documents "Permanent link")

```
get_nodes_from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], show_progress: bool = False, **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Parse documents into nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `documents` | `Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
documents to parse



 | _required_ |
| `show_progress` | `bool` | 

whether to show progress bar



 | `False` |

Source code in `llama-index-core/llama_index/core/node_parser/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">111</span>
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
<span class="normal">134</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes_from_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse documents into nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        documents (Sequence[Document]): documents to parse</span>
<span class="sd">        show_progress (bool): whether to show progress bar</span>

<span class="sd">    """</span>
    <span class="n">doc_id_to_document</span> <span class="o">=</span> <span class="p">{</span><span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">:</span> <span class="n">doc</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">}</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">NODE_PARSING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">:</span> <span class="n">documents</span><span class="p">}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_nodes</span><span class="p">(</span><span class="n">documents</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_postprocess_parsed_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">doc_id_to_document</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">({</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

MetadataAwareTextSplitter [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.MetadataAwareTextSplitter "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `TextSplitter`

Source code in `llama-index-core/llama_index/core/node_parser/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetadataAwareTextSplitter</span><span class="p">(</span><span class="n">TextSplitter</span><span class="p">):</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">split_text_metadata_aware</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">metadata_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">split_texts_metadata_aware</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">metadata_strs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">texts</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">metadata_strs</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Texts and metadata_strs must have the same length"</span><span class="p">)</span>
        <span class="n">nested_texts</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">split_text_metadata_aware</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">text</span><span class="p">,</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">texts</span><span class="p">,</span> <span class="n">metadata_strs</span><span class="p">)</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">nested_texts</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_metadata_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Helper function to get the proper metadata str for splitting."""</span>
        <span class="n">embed_metadata_str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_metadata_str</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span>
        <span class="n">llm_metadata_str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_metadata_str</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span>

        <span class="c1"># use the longest metadata str for splitting</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">embed_metadata_str</span><span class="p">)</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">llm_metadata_str</span><span class="p">):</span>
            <span class="n">metadata_str</span> <span class="o">=</span> <span class="n">embed_metadata_str</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">metadata_str</span> <span class="o">=</span> <span class="n">llm_metadata_str</span>

        <span class="k">return</span> <span class="n">metadata_str</span>

    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing nodes"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">metadata_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_metadata_str</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">split_text_metadata_aware</span><span class="p">(</span>
                <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                <span class="n">metadata_str</span><span class="o">=</span><span class="n">metadata_str</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="n">build_nodes_from_splits</span><span class="p">(</span><span class="n">splits</span><span class="p">,</span> <span class="n">node</span><span class="p">,</span> <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Html](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/)[Next Json](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/)
