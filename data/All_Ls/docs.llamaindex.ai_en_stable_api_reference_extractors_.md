Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/

Markdown Content:
Index - LlamaIndex


Node parser interface.

BaseExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")`

Metadata extractor.

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 21</span>
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
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseExtractor</span><span class="p">(</span><span class="n">TransformComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Metadata extractor."""</span>

    <span class="n">is_text_node_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to show progress."</span><span class="p">)</span>

    <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Metadata mode to use when reading nodes."</span>
    <span class="p">)</span>

    <span class="n">node_text_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_NODE_TEXT_TEMPLATE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Template to represent how node text is mixed with metadata text."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">disable_template_rewrite</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Disable the node template rewrite."</span>
    <span class="p">)</span>

    <span class="n">in_place</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to process nodes in place."</span>
    <span class="p">)</span>

    <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Number of workers to use for concurrent async processing."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">data</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"class_name"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="n">llm_predictor</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"llm_predictor"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">llm_predictor</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.llm_predictor.loading</span> <span class="kn">import</span> <span class="n">load_predictor</span>

            <span class="n">llm_predictor</span> <span class="o">=</span> <span class="n">load_predictor</span><span class="p">(</span><span class="n">llm_predictor</span><span class="p">)</span>
            <span class="n">data</span><span class="p">[</span><span class="s2">"llm_predictor"</span><span class="p">]</span> <span class="o">=</span> <span class="n">llm_predictor</span>

        <span class="n">llm</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"llm"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">llm</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.llms.loading</span> <span class="kn">import</span> <span class="n">load_llm</span>

            <span class="n">llm</span> <span class="o">=</span> <span class="n">load_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">)</span>
            <span class="n">data</span><span class="p">[</span><span class="s2">"llm"</span><span class="p">]</span> <span class="o">=</span> <span class="n">llm</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">data</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"MetadataExtractor"</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extracts metadata for a sequence of nodes, returning a list of</span>
<span class="sd">        metadata dictionaries corresponding to each node.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (Sequence[Document]): nodes to extract metadata from</span>

<span class="sd">        """</span>

    <span class="k">def</span> <span class="nf">extract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extracts metadata for a sequence of nodes, returning a list of</span>
<span class="sd">        metadata dictionaries corresponding to each node.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (Sequence[Document]): nodes to extract metadata from</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aextract</span><span class="p">(</span><span class="n">nodes</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">excluded_embed_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">excluded_llm_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Post process nodes parsed from documents.</span>

<span class="sd">        Allows extractors to be chained.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[BaseNode]): nodes to post-process</span>
<span class="sd">            excluded_embed_metadata_keys (Optional[List[str]]):</span>
<span class="sd">                keys to exclude from embed metadata</span>
<span class="sd">            excluded_llm_metadata_keys (Optional[List[str]]):</span>
<span class="sd">                keys to exclude from llm metadata</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_place</span><span class="p">:</span>
            <span class="n">new_nodes</span> <span class="o">=</span> <span class="n">nodes</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

        <span class="n">cur_metadata_list</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aextract</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">):</span>
            <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cur_metadata_list</span><span class="p">[</span><span class="n">idx</span><span class="p">])</span>

        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">excluded_embed_metadata_keys</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">node</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">excluded_embed_metadata_keys</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">excluded_llm_metadata_keys</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">node</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">excluded_llm_metadata_keys</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_template_rewrite</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
                    <span class="n">cast</span><span class="p">(</span><span class="n">TextNode</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span><span class="o">.</span><span class="n">text_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_text_template</span>

        <span class="k">return</span> <span class="n">new_nodes</span>

    <span class="k">def</span> <span class="nf">process_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">excluded_embed_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">excluded_llm_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span>
                <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
                <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Post process nodes parsed from documents.</span>

<span class="sd">        Allows extractors to be chained.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[BaseNode]): nodes to post-process</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Post process nodes parsed from documents.</span>

<span class="sd">        Allows extractors to be chained.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[BaseNode]): nodes to post-process</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aprocess_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"MetadataExtractor"</span>
</code></pre></div></td></tr></tbody></table>

### aextract `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor.aextract "Permanent link")

```
aextract(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[Dict]
```

Extracts metadata for a sequence of nodes, returning a list of metadata dictionaries corresponding to each node.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
nodes to extract metadata from



 | _required_ |

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Extracts metadata for a sequence of nodes, returning a list of</span>
<span class="sd">    metadata dictionaries corresponding to each node.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (Sequence[Document]): nodes to extract metadata from</span>

<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

### extract [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor.extract "Permanent link")

```
extract(nodes: Sequence[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[Dict]
```

Extracts metadata for a sequence of nodes, returning a list of metadata dictionaries corresponding to each node.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
nodes to extract metadata from



 | _required_ |

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">extract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Extracts metadata for a sequence of nodes, returning a list of</span>
<span class="sd">    metadata dictionaries corresponding to each node.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (Sequence[Document]): nodes to extract metadata from</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aextract</span><span class="p">(</span><span class="n">nodes</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### aprocess\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor.aprocess_nodes "Permanent link")

```
aprocess_nodes(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], excluded_embed_metadata_keys: Optional[List[str]] = None, excluded_llm_metadata_keys: Optional[List[str]] = None, **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Post process nodes parsed from documents.

Allows extractors to be chained.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
nodes to post-process



 | _required_ |
| `excluded_embed_metadata_keys` | `Optional[List[str]]` | 

keys to exclude from embed metadata



 | `None` |
| `excluded_llm_metadata_keys` | `Optional[List[str]]` | 

keys to exclude from llm metadata



 | `None` |

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 97</span>
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
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aprocess_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="n">excluded_embed_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">excluded_llm_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Post process nodes parsed from documents.</span>

<span class="sd">    Allows extractors to be chained.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode]): nodes to post-process</span>
<span class="sd">        excluded_embed_metadata_keys (Optional[List[str]]):</span>
<span class="sd">            keys to exclude from embed metadata</span>
<span class="sd">        excluded_llm_metadata_keys (Optional[List[str]]):</span>
<span class="sd">            keys to exclude from llm metadata</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_place</span><span class="p">:</span>
        <span class="n">new_nodes</span> <span class="o">=</span> <span class="n">nodes</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="n">cur_metadata_list</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aextract</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">):</span>
        <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cur_metadata_list</span><span class="p">[</span><span class="n">idx</span><span class="p">])</span>

    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">excluded_embed_metadata_keys</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">node</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">excluded_embed_metadata_keys</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">excluded_llm_metadata_keys</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">node</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">excluded_llm_metadata_keys</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_template_rewrite</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
                <span class="n">cast</span><span class="p">(</span><span class="n">TextNode</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span><span class="o">.</span><span class="n">text_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_text_template</span>

    <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

### acall `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor.acall "Permanent link")

```
acall(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Post process nodes parsed from documents.

Allows extractors to be chained.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
nodes to post-process



 | _required_ |

Source code in `llama-index-core/llama_index/core/extractors/interface.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Post process nodes parsed from documents.</span>

<span class="sd">    Allows extractors to be chained.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode]): nodes to post-process</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aprocess_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Entity](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/)[Next Keyword](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/)
