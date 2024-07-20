Title: Hierarchical - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/

Markdown Content:
Hierarchical - LlamaIndex


Node parsers.

HierarchicalNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.HierarchicalNodeParser "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[NodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "llama_index.core.node_parser.interface.NodeParser")`

Hierarchical node parser.

Splits a document into a recursive hierarchy Nodes using a NodeParser.

NOTE: this will return a hierarchy of nodes in a flat list, where there will be overlap between parent nodes (e.g. with a bigger chunk size), and child nodes per parent (e.g. with a smaller chunk size).

For instance, this may return a list of nodes like: - list of top-level nodes with chunk size 2048 - list of second-level nodes, where each node is a child of a top-level node, chunk size 512 - list of third-level nodes, where each node is a child of a second-level node, chunk size 128

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 78</span>
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
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HierarchicalNodeParser</span><span class="p">(</span><span class="n">NodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hierarchical node parser.</span>

<span class="sd">    Splits a document into a recursive hierarchy Nodes using a NodeParser.</span>

<span class="sd">    NOTE: this will return a hierarchy of nodes in a flat list, where there will be</span>
<span class="sd">    overlap between parent nodes (e.g. with a bigger chunk size), and child nodes</span>
<span class="sd">    per parent (e.g. with a smaller chunk size).</span>

<span class="sd">    For instance, this may return a list of nodes like:</span>
<span class="sd">    - list of top-level nodes with chunk size 2048</span>
<span class="sd">    - list of second-level nodes, where each node is a child of a top-level node,</span>
<span class="sd">      chunk size 512</span>
<span class="sd">    - list of third-level nodes, where each node is a child of a second-level node,</span>
<span class="sd">      chunk size 128</span>
<span class="sd">    """</span>

    <span class="n">chunk_sizes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"The chunk sizes to use when splitting documents, in order of level."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">node_parser_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"List of ids for the node parsers to use when splitting documents, "</span>
            <span class="o">+</span> <span class="s2">"in order of level (first id used for first level, etc.)."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">node_parser_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NodeParser</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Map of node parser id to node parser."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chunk_sizes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">node_parser_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_parser_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NodeParser</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HierarchicalNodeParser"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="k">if</span> <span class="n">node_parser_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">chunk_sizes</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">chunk_sizes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2048</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">128</span><span class="p">]</span>

            <span class="n">node_parser_ids</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s2">"chunk_size_</span><span class="si">{</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">chunk_size</span> <span class="ow">in</span> <span class="n">chunk_sizes</span><span class="p">]</span>
            <span class="n">node_parser_map</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">for</span> <span class="n">chunk_size</span><span class="p">,</span> <span class="n">node_parser_id</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">chunk_sizes</span><span class="p">,</span> <span class="n">node_parser_ids</span><span class="p">):</span>
                <span class="n">node_parser_map</span><span class="p">[</span><span class="n">node_parser_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(</span>
                    <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
                    <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
                    <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
                    <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
                    <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">chunk_sizes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot specify both node_parser_ids and chunk_sizes."</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">node_parser_map</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify node_parser_map if using node_parser_ids."</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">chunk_sizes</span><span class="o">=</span><span class="n">chunk_sizes</span><span class="p">,</span>
            <span class="n">node_parser_ids</span><span class="o">=</span><span class="n">node_parser_ids</span><span class="p">,</span>
            <span class="n">node_parser_map</span><span class="o">=</span><span class="n">node_parser_map</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"HierarchicalNodeParser"</span>

    <span class="k">def</span> <span class="nf">_recursively_get_nodes_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Recursively get nodes from nodes."""</span>
        <span class="k">if</span> <span class="n">level</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_parser_ids</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2"> is greater than number of text "</span>
                <span class="sa">f</span><span class="s2">"splitters (</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_parser_ids</span><span class="p">)</span><span class="si">}</span><span class="s2">)."</span>
            <span class="p">)</span>

        <span class="c1"># first split current nodes into sub-nodes</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing documents into nodes"</span>
        <span class="p">)</span>
        <span class="n">sub_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">cur_sub_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser_map</span><span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">node_parser_ids</span><span class="p">[</span><span class="n">level</span><span class="p">]</span>
            <span class="p">]</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">([</span><span class="n">node</span><span class="p">])</span>
            <span class="c1"># add parent relationship from sub node to parent node</span>
            <span class="c1"># add child relationship from parent node to sub node</span>
            <span class="c1"># NOTE: Only add relationships if level &gt; 0, since we don't want to add</span>
            <span class="c1"># relationships for the top-level document objects that we are splitting</span>
            <span class="k">if</span> <span class="n">level</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">sub_node</span> <span class="ow">in</span> <span class="n">cur_sub_nodes</span><span class="p">:</span>
                    <span class="n">_add_parent_child_relationship</span><span class="p">(</span>
                        <span class="n">parent_node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span>
                        <span class="n">child_node</span><span class="o">=</span><span class="n">sub_node</span><span class="p">,</span>
                    <span class="p">)</span>

            <span class="n">sub_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">cur_sub_nodes</span><span class="p">)</span>

        <span class="c1"># now for each sub-node, recursively split into sub-sub-nodes, and add</span>
        <span class="k">if</span> <span class="n">level</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_parser_ids</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">sub_sub_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursively_get_nodes_from_nodes</span><span class="p">(</span>
                <span class="n">sub_nodes</span><span class="p">,</span>
                <span class="n">level</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">sub_sub_nodes</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="n">sub_nodes</span> <span class="o">+</span> <span class="n">sub_sub_nodes</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse document into nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (Sequence[Document]): documents to parse</span>
<span class="sd">            include_metadata (bool): whether to include metadata in nodes</span>

<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">NODE_PARSING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">:</span> <span class="n">documents</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">documents_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
                <span class="n">documents</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing documents into nodes"</span>
            <span class="p">)</span>

            <span class="c1"># TODO: a bit of a hack rn for tqdm</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents_with_progress</span><span class="p">:</span>
                <span class="n">nodes_from_doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursively_get_nodes_from_nodes</span><span class="p">([</span><span class="n">doc</span><span class="p">],</span> <span class="mi">0</span><span class="p">)</span>
                <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes_from_doc</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">all_nodes</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="c1"># Unused abstract method</span>
    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes\_from\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.HierarchicalNodeParser.get_nodes_from_documents "Permanent link")

```
get_nodes_from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], show_progress: bool = False, **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Parse document into nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `documents` | `Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
documents to parse



 | _required_ |
| `include_metadata` | `bool` | 

whether to include metadata in nodes



 | _required_ |

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">207</span>
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
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes_from_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse document into nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        documents (Sequence[Document]): documents to parse</span>
<span class="sd">        include_metadata (bool): whether to include metadata in nodes</span>

<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">NODE_PARSING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">DOCUMENTS</span><span class="p">:</span> <span class="n">documents</span><span class="p">}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">documents_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing documents into nodes"</span>
        <span class="p">)</span>

        <span class="c1"># TODO: a bit of a hack rn for tqdm</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents_with_progress</span><span class="p">:</span>
            <span class="n">nodes_from_doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursively_get_nodes_from_nodes</span><span class="p">([</span><span class="n">doc</span><span class="p">],</span> <span class="mi">0</span><span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes_from_doc</span><span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">all_nodes</span><span class="p">})</span>

    <span class="k">return</span> <span class="n">all_nodes</span>
</code></pre></div></td></tr></tbody></table>

get\_leaf\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.get_leaf_nodes "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

```
get_leaf_nodes(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get leaf nodes.

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_leaf_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get leaf nodes."""</span>
    <span class="n">leaf_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">CHILD</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="n">leaf_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">leaf_nodes</span>
</code></pre></div></td></tr></tbody></table>

get\_root\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.get_root_nodes "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

```
get_root_nodes(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get root nodes.

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_root_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get root nodes."""</span>
    <span class="n">root_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">PARENT</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="n">root_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">root_nodes</span>
</code></pre></div></td></tr></tbody></table>

get\_child\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.get_child_nodes "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
get_child_nodes(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], all_nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get child nodes of nodes from given all\_nodes.

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

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
<span class="normal">60</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_child_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get child nodes of nodes from given all_nodes."""</span>
    <span class="n">children_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">CHILD</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">continue</span>

        <span class="n">children_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
            <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">CHILD</span><span class="p">]]</span>
        <span class="p">)</span>

    <span class="n">child_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">candidate_node</span> <span class="ow">in</span> <span class="n">all_nodes</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">candidate_node</span><span class="o">.</span><span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">children_ids</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">child_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">candidate_node</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">child_nodes</span>
</code></pre></div></td></tr></tbody></table>

get\_deeper\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/#llama_index.core.node_parser.get_deeper_nodes "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
get_deeper_nodes(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], depth: int = 1) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get children of root nodes in given nodes that have given depth.

Source code in `llama-index-core/llama_index/core/node_parser/relational/hierarchical.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">63</span>
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
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_deeper_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get children of root nodes in given nodes that have given depth."""</span>
    <span class="k">if</span> <span class="n">depth</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Depth cannot be a negative number!"</span><span class="p">)</span>
    <span class="n">root_nodes</span> <span class="o">=</span> <span class="n">get_root_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">root_nodes</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"There is no root nodes in given nodes!"</span><span class="p">)</span>

    <span class="n">deeper_nodes</span> <span class="o">=</span> <span class="n">root_nodes</span>
    <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">depth</span><span class="p">):</span>
        <span class="n">deeper_nodes</span> <span class="o">=</span> <span class="n">get_child_nodes</span><span class="p">(</span><span class="n">deeper_nodes</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">deeper_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Code](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/)[Next Html](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/)
