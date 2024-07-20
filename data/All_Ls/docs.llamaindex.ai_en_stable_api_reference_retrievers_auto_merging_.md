Title: Auto merging - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/

Markdown Content:
Auto merging - LlamaIndex


AutoMergingRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/#llama_index.core.retrievers.AutoMergingRetriever "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

This retriever will try to merge context into parent context.

The retriever first retrieves chunks from a vector store. Then, it will try to merge the chunks into a single context.

Source code in `llama-index-core/llama_index/core/retrievers/auto_merging_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AutoMergingRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""This retriever will try to merge context into parent context.</span>

<span class="sd">    The retriever first retrieves chunks from a vector store.</span>
<span class="sd">    Then, it will try to merge the chunks into a single context.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">vector_retriever</span><span class="p">:</span> <span class="n">VectorIndexRetriever</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">StorageContext</span><span class="p">,</span>
        <span class="n">simple_ratio_thresh</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_retriever</span> <span class="o">=</span> <span class="n">vector_retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span> <span class="o">=</span> <span class="n">storage_context</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_simple_ratio_thresh</span> <span class="o">=</span> <span class="n">simple_ratio_thresh</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_parents_and_merge</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get parents and merge nodes."""</span>
        <span class="c1"># retrieve all parent nodes</span>
        <span class="n">parent_nodes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">parent_cur_children_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">parent_node</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">parent_node_info</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">parent_node</span>

            <span class="c1"># Fetch actual parent node if doesn't exist in `parent_nodes` cache yet</span>
            <span class="n">parent_node_id</span> <span class="o">=</span> <span class="n">parent_node_info</span><span class="o">.</span><span class="n">node_id</span>
            <span class="k">if</span> <span class="n">parent_node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">parent_nodes</span><span class="p">:</span>
                <span class="n">parent_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span>
                    <span class="n">parent_node_id</span>
                <span class="p">)</span>
                <span class="n">parent_nodes</span><span class="p">[</span><span class="n">parent_node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">,</span> <span class="n">parent_node</span><span class="p">)</span>

            <span class="c1"># add reference to child from parent</span>
            <span class="n">parent_cur_children_dict</span><span class="p">[</span><span class="n">parent_node_id</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="c1"># compute ratios and "merge" nodes</span>
        <span class="c1"># merging: delete some children nodes, add some parent nodes</span>
        <span class="n">node_ids_to_delete</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">nodes_to_add</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">parent_node_id</span><span class="p">,</span> <span class="n">parent_node</span> <span class="ow">in</span> <span class="n">parent_nodes</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">parent_child_nodes</span> <span class="o">=</span> <span class="n">parent_node</span><span class="o">.</span><span class="n">child_nodes</span>
            <span class="n">parent_num_children</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">parent_child_nodes</span><span class="p">)</span> <span class="k">if</span> <span class="n">parent_child_nodes</span> <span class="k">else</span> <span class="mi">1</span>
            <span class="n">parent_cur_children</span> <span class="o">=</span> <span class="n">parent_cur_children_dict</span><span class="p">[</span><span class="n">parent_node_id</span><span class="p">]</span>
            <span class="n">ratio</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">parent_cur_children</span><span class="p">)</span> <span class="o">/</span> <span class="n">parent_num_children</span>

            <span class="c1"># if ratio is high enough, merge</span>
            <span class="k">if</span> <span class="n">ratio</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_simple_ratio_thresh</span><span class="p">:</span>
                <span class="n">node_ids_to_delete</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
                    <span class="nb">set</span><span class="p">({</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">parent_cur_children</span><span class="p">})</span>
                <span class="p">)</span>

                <span class="n">parent_node_text</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span><span class="n">parent_node</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
                <span class="n">info_str</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"&gt; Merging </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">parent_cur_children</span><span class="p">)</span><span class="si">}</span><span class="s2"> nodes into parent node.</span><span class="se">\n</span><span class="s2">"</span>
                    <span class="sa">f</span><span class="s2">"&gt; Parent node id: </span><span class="si">{</span><span class="n">parent_node_id</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span>
                    <span class="sa">f</span><span class="s2">"&gt; Parent node text: </span><span class="si">{</span><span class="n">parent_node_text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
                <span class="p">)</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">info_str</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="n">info_str</span><span class="p">)</span>

                <span class="c1"># add parent node</span>
                <span class="c1"># can try averaging score across embeddings for now</span>

                <span class="n">avg_score</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span>
                    <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">get_score</span><span class="p">()</span> <span class="ow">or</span> <span class="mf">0.0</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">parent_cur_children</span><span class="p">]</span>
                <span class="p">)</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">parent_cur_children</span><span class="p">)</span>
                <span class="n">parent_node_with_score</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">parent_node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">avg_score</span>
                <span class="p">)</span>
                <span class="n">nodes_to_add</span><span class="p">[</span><span class="n">parent_node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">parent_node_with_score</span>

        <span class="c1"># delete old child nodes, add new parent nodes</span>
        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span> <span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node_ids_to_delete</span><span class="p">]</span>
        <span class="c1"># add parent nodes</span>
        <span class="n">new_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">nodes_to_add</span><span class="o">.</span><span class="n">values</span><span class="p">()))</span>

        <span class="n">is_changed</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">node_ids_to_delete</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>

        <span class="k">return</span> <span class="n">new_nodes</span><span class="p">,</span> <span class="n">is_changed</span>

    <span class="k">def</span> <span class="nf">_fill_in_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Fill in nodes."""</span>
        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">is_changed</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">idx</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">cur_node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
            <span class="c1"># if there's a node in the middle, add that to the queue</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="n">cur_node</span><span class="o">.</span><span class="n">next_node</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
                <span class="ow">and</span> <span class="n">cur_node</span><span class="o">.</span><span class="n">next_node</span> <span class="o">==</span> <span class="n">nodes</span><span class="p">[</span><span class="n">idx</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">prev_node</span>
            <span class="p">):</span>
                <span class="n">is_changed</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="n">next_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span>
                    <span class="n">cur_node</span><span class="o">.</span><span class="n">next_node</span><span class="o">.</span><span class="n">node_id</span>
                <span class="p">)</span>
                <span class="n">next_node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">,</span> <span class="n">next_node</span><span class="p">)</span>

                <span class="n">next_node_text</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span><span class="n">next_node</span><span class="o">.</span><span class="n">get_text</span><span class="p">(),</span> <span class="mi">100</span><span class="p">)</span>
                <span class="n">info_str</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"&gt; Filling in node. Node id: </span><span class="si">{</span><span class="n">cur_node</span><span class="o">.</span><span class="n">next_node</span><span class="o">.</span><span class="n">node_id</span><span class="si">}</span><span class="s2">"</span>
                    <span class="sa">f</span><span class="s2">"&gt; Node text: </span><span class="si">{</span><span class="n">next_node_text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
                <span class="p">)</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">info_str</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="n">info_str</span><span class="p">)</span>

                <span class="c1"># set score to be average of current node and next node</span>
                <span class="n">avg_score</span> <span class="o">=</span> <span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_score</span><span class="p">()</span> <span class="o">+</span> <span class="n">nodes</span><span class="p">[</span><span class="n">idx</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">get_score</span><span class="p">())</span> <span class="o">/</span> <span class="mi">2</span>
                <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">next_node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">avg_score</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">new_nodes</span><span class="p">,</span> <span class="n">is_changed</span>

    <span class="k">def</span> <span class="nf">_try_merging</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Try different ways to merge nodes."""</span>
        <span class="c1"># first try filling in nodes</span>
        <span class="n">nodes</span><span class="p">,</span> <span class="n">is_changed_0</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fill_in_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="c1"># then try merging nodes</span>
        <span class="n">nodes</span><span class="p">,</span> <span class="n">is_changed_1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_parents_and_merge</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span><span class="p">,</span> <span class="n">is_changed_0</span> <span class="ow">or</span> <span class="n">is_changed_1</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>
        <span class="n">initial_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

        <span class="n">cur_nodes</span><span class="p">,</span> <span class="n">is_changed</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_try_merging</span><span class="p">(</span><span class="n">initial_nodes</span><span class="p">)</span>
        <span class="c1"># cur_nodes, is_changed = self._get_parents_and_merge(initial_nodes)</span>
        <span class="k">while</span> <span class="n">is_changed</span><span class="p">:</span>
            <span class="n">cur_nodes</span><span class="p">,</span> <span class="n">is_changed</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_try_merging</span><span class="p">(</span><span class="n">cur_nodes</span><span class="p">)</span>
            <span class="c1"># cur_nodes, is_changed = self._get_parents_and_merge(cur_nodes)</span>

        <span class="c1"># sort by similarity</span>
        <span class="n">cur_nodes</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">get_score</span><span class="p">(),</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">cur_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tree summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/)[Next Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/)
