Title: Markdown element - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/

Markdown Content:
Markdown element - LlamaIndex


Node parsers.

MarkdownElementNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/#llama_index.core.node_parser.MarkdownElementNodeParser "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseElementNodeParser`

Markdown element node parser.

Splits a markdown document into Text Nodes and Index Nodes corresponding to embedded objects (e.g. tables).

Source code in `llama-index-core/llama_index/core/node_parser/relational/markdown_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 11</span>
<span class="normal"> 12</span>
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
<span class="normal">223</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MarkdownElementNodeParser</span><span class="p">(</span><span class="n">BaseElementNodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Markdown element node parser.</span>

<span class="sd">    Splits a markdown document into Text Nodes and Index Nodes corresponding to embedded objects</span>
<span class="sd">    (e.g. tables).</span>

<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"MarkdownElementNodeParser"</span>

    <span class="k">def</span> <span class="nf">get_nodes_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from node."""</span>
        <span class="n">elements</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_elements</span><span class="p">(</span>
            <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">],</span> <span class="n">node_id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
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
            <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span> <span class="n">table_filters</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">filter_table</span><span class="p">],</span> <span class="n">node_id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
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
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">node_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
        <span class="c1"># get node id for each node so that we can avoid using the same id for different nodes</span>
<span class="w">        </span><span class="sd">"""Extract elements from text."""</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">currentElement</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Then parse the lines</span>
        <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"```"</span><span class="p">):</span>
                <span class="c1"># check if this is the end of a code block</span>
                <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">currentElement</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">"`"</span><span class="p">:</span>
                    <span class="c1"># check if inline code block (aka have a second ``` in line but not at the end)</span>
                    <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                    <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">"code"</span><span class="p">,</span>
                        <span class="n">element</span><span class="o">=</span><span class="n">line</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">"```"</span><span class="p">),</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">currentElement</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"code"</span><span class="p">:</span>
                <span class="n">currentElement</span><span class="o">.</span><span class="n">element</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">line</span>

            <span class="k">elif</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"|"</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">currentElement</span><span class="o">.</span><span class="n">type</span> <span class="o">!=</span> <span class="s2">"table"</span><span class="p">:</span>
                    <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                    <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"table"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">line</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">currentElement</span><span class="o">.</span><span class="n">element</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">line</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"table"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">line</span>
                    <span class="p">)</span>
            <span class="k">elif</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"#"</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">"title"</span><span class="p">,</span>
                    <span class="n">element</span><span class="o">=</span><span class="n">line</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">"#"</span><span class="p">),</span>
                    <span class="n">title_level</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">-</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">"#"</span><span class="p">)),</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">currentElement</span><span class="o">.</span><span class="n">type</span> <span class="o">!=</span> <span class="s2">"text"</span><span class="p">:</span>
                    <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                    <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">line</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">currentElement</span><span class="o">.</span><span class="n">element</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">line</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">line</span>
                    <span class="p">)</span>
        <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">elements</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">element</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"text"</span>
                <span class="ow">and</span> <span class="n">merged_elements</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"code"</span><span class="p">:</span>
                <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                <span class="n">currentElement</span> <span class="o">=</span> <span class="kc">None</span>
                <span class="c1"># if there is some text after the ``` create a text element with it</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">:</span>
                    <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Element</span><span class="p">(</span>
                            <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                            <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span>
                            <span class="n">element</span><span class="o">=</span><span class="n">line</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">"```"</span><span class="p">),</span>
                        <span class="p">)</span>
                    <span class="p">)</span>

            <span class="k">elif</span> <span class="n">line</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s2">"```"</span><span class="p">)</span> <span class="o"></span> <span class="s2">"text"</span><span class="p">:</span>
                <span class="n">currentElement</span><span class="o">.</span><span class="n">element</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">line</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentElement</span><span class="p">)</span>
                <span class="n">currentElement</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="n">line</span>
                <span class="p">)</span>

        <span class="k">elif</span> <span class="n">currentElement</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">currentElement</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"table"</span><span class="p">:</span>
            <span class="n">should_keep</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="n">perfect_table</span> <span class="o">=</span> <span class="kc">True</span>

            <span class="c1"># verify that the table (markdown) have the same number of columns on each rows</span>
            <span class="n">table_lines</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">table_columns</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"|"</span><span class="p">))</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">table_lines</span><span class="p">]</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">table_columns</span><span class="p">))</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="c1"># if the table have different number of columns on each rows, it's not a perfect table</span>
                <span class="c1"># we will store the raw text for such tables instead of converting them to a dataframe</span>
                <span class="n">perfect_table</span> <span class="o">=</span> <span class="kc">False</span>

            <span class="c1"># verify that the table (markdown) have at least 2 rows</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">table_lines</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
                <span class="n">should_keep</span> <span class="o">=</span> <span class="kc">False</span>

            <span class="c1"># apply the table filter, now only filter empty tables</span>
            <span class="k">if</span> <span class="n">should_keep</span> <span class="ow">and</span> <span class="n">perfect_table</span> <span class="ow">and</span> <span class="n">table_filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">should_keep</span> <span class="o">=</span> <span class="nb">all</span><span class="p">(</span><span class="n">tf</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">tf</span> <span class="ow">in</span> <span class="n">table_filters</span><span class="p">)</span>

            <span class="c1"># if the element is a table, convert it to a dataframe</span>
            <span class="k">if</span> <span class="n">should_keep</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">perfect_table</span><span class="p">:</span>
                    <span class="n">table</span> <span class="o">=</span> <span class="n">md_to_df</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="p">)</span>

                    <span class="n">elements</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span> <span class="k">if</span> <span class="n">node_id</span> <span class="k">else</span> <span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">"table"</span><span class="p">,</span>
                        <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="p">,</span>
                        <span class="n">table</span><span class="o">=</span><span class="n">table</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># for non-perfect tables, we will store the raw text</span>
                    <span class="c1"># and give it a different type to differentiate it from perfect tables</span>
                    <span class="n">elements</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span> <span class="k">if</span> <span class="n">node_id</span> <span class="k">else</span> <span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">"table_text"</span><span class="p">,</span>
                        <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="p">,</span>
                        <span class="c1"># table=table</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">elements</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span> <span class="k">if</span> <span class="n">node_id</span> <span class="k">else</span> <span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span>
                    <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="p">,</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># if the element is not a table, keep it as to text</span>
            <span class="n">elements</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span> <span class="k">if</span> <span class="n">node_id</span> <span class="k">else</span> <span class="sa">f</span><span class="s2">"id_</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">"text"</span><span class="p">,</span>
                <span class="n">element</span><span class="o">=</span><span class="n">element</span><span class="o">.</span><span class="n">element</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="c1"># merge consecutive text elements together for now</span>
    <span class="n">merged_elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">elements</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="nb">len</span><span class="p">(</span><span class="n">merged_elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
            <span class="ow">and</span> <span class="n">element</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"text"</span>
        <span class="p">):</span>
            <span class="n">merged_elements</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">element</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">element</span><span class="o">.</span><span class="n">element</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">merged_elements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">element</span><span class="p">)</span>
    <span class="n">elements</span> <span class="o">=</span> <span class="n">merged_elements</span>
    <span class="k">return</span> <span class="n">merged_elements</span>
</code></pre></div></td></tr></tbody></table>

### filter\_table [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/#llama_index.core.node_parser.MarkdownElementNodeParser.filter_table "Permanent link")

```
filter_table(table_element: Any) -> bool
```

Filter tables.

Source code in `llama-index-core/llama_index/core/node_parser/relational/markdown_element.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">filter_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table_element</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Filter tables."""</span>
    <span class="n">table_df</span> <span class="o">=</span> <span class="n">md_to_df</span><span class="p">(</span><span class="n">table_element</span><span class="o">.</span><span class="n">element</span><span class="p">)</span>

    <span class="c1"># check if table_df is not None, has more than one row, and more than one column</span>
    <span class="k">return</span> <span class="n">table_df</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">table_df</span><span class="o">.</span><span class="n">empty</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">table_df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Markdown](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown/)[Next Semantic splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/)
