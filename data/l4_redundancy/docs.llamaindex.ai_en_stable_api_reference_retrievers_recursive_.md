Title: Recursive - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/

Markdown Content:
Recursive - LlamaIndex


RecursiveRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/#llama_index.core.retrievers.RecursiveRetriever "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Recursive retriever.

This retriever will recursively explore links from nodes to other retrievers/query engines.

For any retrieved nodes, if any of the nodes are IndexNodes, then it will explore the linked retriever/query engine, and query that.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `root_id` | `str` | 
The root id of the query graph.



 | _required_ |
| `retriever_dict` | `Optional[Dict[str, [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")]]` | 

A dictionary of id to retrievers.



 | _required_ |
| `query_engine_dict` | `Optional[Dict[str, [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")]]` | 

A dictionary of id to query engines.



 | `None` |

Source code in `llama-index-core/llama_index/core/retrievers/recursive_retriever.py`

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
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
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
<span class="normal">217</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RecursiveRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Recursive retriever.</span>

<span class="sd">    This retriever will recursively explore links from nodes to other</span>
<span class="sd">    retrievers/query engines.</span>

<span class="sd">    For any retrieved nodes, if any of the nodes are IndexNodes,</span>
<span class="sd">    then it will explore the linked retriever/query engine, and query that.</span>

<span class="sd">    Args:</span>
<span class="sd">        root_id (str): The root id of the query graph.</span>
<span class="sd">        retriever_dict (Optional[Dict[str, BaseRetriever]]): A dictionary</span>
<span class="sd">            of id to retrievers.</span>
<span class="sd">        query_engine_dict (Optional[Dict[str, BaseQueryEngine]]): A dictionary of</span>
<span class="sd">            id to query engines.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">root_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">retriever_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseRetriever</span><span class="p">],</span>
        <span class="n">query_engine_dict</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseQueryEngine</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_dict</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_response_tmpl</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_root_id</span> <span class="o">=</span> <span class="n">root_id</span>
        <span class="k">if</span> <span class="n">root_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">retriever_dict</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Root id </span><span class="si">{</span><span class="n">root_id</span><span class="si">}</span><span class="s2"> not in retriever_dict, it must be a retriever."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_dict</span> <span class="o">=</span> <span class="n">retriever_dict</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine_dict</span> <span class="o">=</span> <span class="n">query_engine_dict</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_dict</span> <span class="o">=</span> <span class="n">node_dict</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="c1"># make sure keys don't overlap</span>
        <span class="k">if</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_retriever_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">&amp;</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">()):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Retriever and query engine ids must not overlap."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_query_response_tmpl</span> <span class="o">=</span> <span class="n">query_response_tmpl</span> <span class="ow">or</span> <span class="n">DEFAULT_QUERY_RESPONSE_TMPL</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_deduplicate_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes_with_score</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Deduplicate nodes according to node id.</span>
<span class="sd">        Keep the node with the highest score/first returned.</span>
<span class="sd">        """</span>
        <span class="n">node_ids</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">deduplicate_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes_with_score</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">id_</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">:</span>
                <span class="n">node_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span><span class="p">)</span>
                <span class="n">deduplicate_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_score</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">deduplicate_nodes</span>

    <span class="k">def</span> <span class="nf">_query_retrieved_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span> <span class="n">nodes_with_score</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Query for retrieved nodes.</span>

<span class="sd">        If node is an IndexNode, then recursively query the retriever/query engine.</span>
<span class="sd">        If node is a TextNode, then simply return the node.</span>

<span class="sd">        """</span>
        <span class="n">nodes_to_add</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">additional_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">visited_ids</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>

        <span class="c1"># dedup index nodes that reference same index id</span>
        <span class="n">new_nodes_with_score</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes_with_score</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">index_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">visited_ids</span><span class="p">:</span>
                    <span class="n">visited_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">)</span>
                    <span class="n">new_nodes_with_score</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_score</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">new_nodes_with_score</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_score</span><span class="p">)</span>

        <span class="n">nodes_with_score</span> <span class="o">=</span> <span class="n">new_nodes_with_score</span>

        <span class="c1"># recursively retrieve</span>
        <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes_with_score</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span>
                        <span class="s2">"Retrieved node with id, entering: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                        <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="n">cur_retrieved_nodes</span><span class="p">,</span> <span class="n">cur_additional_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_rec</span><span class="p">(</span>
                    <span class="n">query_bundle</span><span class="p">,</span>
                    <span class="n">query_id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">,</span>
                    <span class="n">cur_similarity</span><span class="o">=</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">score</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span>
                        <span class="s2">"Retrieving text node: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                        <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="n">cur_retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node_with_score</span><span class="p">]</span>
                <span class="n">cur_additional_nodes</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">nodes_to_add</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">cur_retrieved_nodes</span><span class="p">)</span>
            <span class="n">additional_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">cur_additional_nodes</span><span class="p">)</span>

        <span class="c1"># dedup nodes in case some nodes could be retrieved from multiple sources</span>
        <span class="n">nodes_to_add</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deduplicate_nodes</span><span class="p">(</span><span class="n">nodes_to_add</span><span class="p">)</span>
        <span class="n">additional_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deduplicate_nodes</span><span class="p">(</span><span class="n">additional_nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes_to_add</span><span class="p">,</span> <span class="n">additional_nodes</span>

    <span class="k">def</span> <span class="nf">_get_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RQN_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Fetch retriever or query engine."""</span>
        <span class="n">node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">query_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">node</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">node</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">query_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">retriever</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">retriever</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">query_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">query_engine</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">query_engine</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Query id </span><span class="si">{</span><span class="n">query_id</span><span class="si">}</span><span class="s2"> not found in either `retriever_dict` "</span>
            <span class="s2">"or `query_engine_dict`."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve_rec</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">query_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cur_similarity</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Query recursively."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Retrieving with query id </span><span class="si">{</span><span class="n">query_id</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="n">query_id</span> <span class="o">=</span> <span class="n">query_id</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root_id</span>
        <span class="n">cur_similarity</span> <span class="o">=</span> <span class="n">cur_similarity</span> <span class="ow">or</span> <span class="mf">1.0</span>

        <span class="n">obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_object</span><span class="p">(</span><span class="n">query_id</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="n">nodes_to_add</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">obj</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">cur_similarity</span><span class="p">)]</span>
            <span class="n">additional_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseRetriever</span><span class="p">):</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">})</span>

            <span class="n">nodes_to_add</span><span class="p">,</span> <span class="n">additional_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_retrieved_nodes</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span>
            <span class="p">)</span>

        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseQueryEngine</span><span class="p">):</span>
            <span class="n">sub_resp</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Got response: </span><span class="si">{</span><span class="n">sub_resp</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="c1"># format with both the query and the response</span>
            <span class="n">node_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_response_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">sub_resp</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">node_text</span><span class="p">)</span>
            <span class="n">nodes_to_add</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">cur_similarity</span><span class="p">)]</span>
            <span class="n">additional_nodes</span> <span class="o">=</span> <span class="n">sub_resp</span><span class="o">.</span><span class="n">source_nodes</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must be a retriever or query engine."</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes_to_add</span><span class="p">,</span> <span class="n">additional_nodes</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_rec</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">query_id</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retrieved_nodes</span>

    <span class="k">def</span> <span class="nf">retrieve_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Retrieve all nodes.</span>

<span class="sd">        Unlike default `retrieve` method, this also fetches additional sources.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_rec</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">query_id</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/#llama_index.core.retrievers.RecursiveRetriever.retrieve_all "Permanent link")

```
retrieve_all(query_bundle: [QueryBundle](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.QueryBundle "llama_index.core.schema.QueryBundle")) -> Tuple[List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")], List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]]
```

Retrieve all nodes.

Unlike default `retrieve` method, this also fetches additional sources.

Source code in `llama-index-core/llama_index/core/retrievers/recursive_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Retrieve all nodes.</span>

<span class="sd">    Unlike default `retrieve` method, this also fetches additional sources.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_rec</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">query_id</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Query fusion](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/)[Next Router](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)
