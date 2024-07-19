Title: Semantic splitter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/

Markdown Content:
Semantic splitter - LlamaIndex


Node parsers.

SemanticSplitterNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/#llama_index.core.node_parser.SemanticSplitterNodeParser "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[NodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "llama_index.core.node_parser.interface.NodeParser")`

Semantic node parser.

Splits a document into Nodes, with each node being a group of semantically related sentences.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `buffer_size` | `int` | 
number of sentences to group together when evaluating semantic similarity



 | _required_ |
| `embed_model` |  | 

(BaseEmbedding): embedding model to use



 | _required_ |
| `sentence_splitter` | `Optional[Callable]` | 

splits text into sentences



 | _required_ |
| `include_metadata` | `bool` | 

whether to include metadata in nodes



 | _required_ |
| `include_prev_next_rel` | `bool` | 

whether to include prev/next relationships



 | _required_ |

Source code in `llama-index-core/llama_index/core/node_parser/text/semantic_splitter.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 27</span>
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
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SemanticSplitterNodeParser</span><span class="p">(</span><span class="n">NodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Semantic node parser.</span>

<span class="sd">    Splits a document into Nodes, with each node being a group of semantically related sentences.</span>

<span class="sd">    Args:</span>
<span class="sd">        buffer_size (int): number of sentences to group together when evaluating semantic similarity</span>
<span class="sd">        embed_model: (BaseEmbedding): embedding model to use</span>
<span class="sd">        sentence_splitter (Optional[Callable]): splits text into sentences</span>
<span class="sd">        include_metadata (bool): whether to include metadata in nodes</span>
<span class="sd">        include_prev_next_rel (bool): whether to include prev/next relationships</span>
<span class="sd">    """</span>

    <span class="n">sentence_splitter</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">split_by_sentence_tokenizer</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The text splitter to use when splitting documents."</span><span class="p">,</span>
        <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The embedding model to use to for semantic comparison"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">buffer_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"The number of sentences to group together when evaluating semantic similarity. "</span>
            <span class="s2">"Set to 1 to consider each sentence individually. "</span>
            <span class="s2">"Set to &gt;1 to group sentences together."</span>
        <span class="p">),</span>
    <span class="p">)</span>

    <span class="n">breakpoint_percentile_threshold</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">95</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"The percentile of cosine dissimilarity that must be exceeded between a "</span>
            <span class="s2">"group of sentences and the next to form a node.  The smaller this "</span>
            <span class="s2">"number is, the more nodes will be generated"</span>
        <span class="p">),</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SemanticSplitterNodeParser"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">breakpoint_percentile_threshold</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">95</span><span class="p">,</span>
        <span class="n">buffer_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">sentence_splitter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">original_text_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_OG_TEXT_METADATA_KEY</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SemanticSplitterNodeParser"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="n">sentence_splitter</span> <span class="o">=</span> <span class="n">sentence_splitter</span> <span class="ow">or</span> <span class="n">split_by_sentence_tokenizer</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">embed_model</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.embeddings.openai</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">OpenAIEmbedding</span><span class="p">,</span>
                <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">OpenAIEmbedding</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"`llama-index-embeddings-openai` package not found, "</span>
                    <span class="s2">"please run `pip install llama-index-embeddings-openai`"</span>
                <span class="p">)</span>

        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">breakpoint_percentile_threshold</span><span class="o">=</span><span class="n">breakpoint_percentile_threshold</span><span class="p">,</span>
            <span class="n">buffer_size</span><span class="o">=</span><span class="n">buffer_size</span><span class="p">,</span>
            <span class="n">sentence_splitter</span><span class="o">=</span><span class="n">sentence_splitter</span><span class="p">,</span>
            <span class="n">original_text_metadata_key</span><span class="o">=</span><span class="n">original_text_metadata_key</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse document into nodes."""</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing nodes"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_semantic_nodes_from_documents</span><span class="p">([</span><span class="n">node</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="k">def</span> <span class="nf">build_semantic_nodes_from_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Build window nodes from documents."""</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">text</span>
            <span class="n">text_splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sentence_splitter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

            <span class="n">sentences</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_sentence_groups</span><span class="p">(</span><span class="n">text_splits</span><span class="p">)</span>

            <span class="n">combined_sentence_embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
                <span class="p">[</span><span class="n">s</span><span class="p">[</span><span class="s2">"combined_sentence"</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">sentences</span><span class="p">],</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">combined_sentence_embeddings</span><span class="p">):</span>
                <span class="n">sentences</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">"combined_sentence_embedding"</span><span class="p">]</span> <span class="o">=</span> <span class="n">embedding</span>

            <span class="n">distances</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_distances_between_sentence_groups</span><span class="p">(</span><span class="n">sentences</span><span class="p">)</span>

            <span class="n">chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_chunks</span><span class="p">(</span><span class="n">sentences</span><span class="p">,</span> <span class="n">distances</span><span class="p">)</span>

            <span class="n">nodes</span> <span class="o">=</span> <span class="n">build_nodes_from_splits</span><span class="p">(</span>
                <span class="n">chunks</span><span class="p">,</span>
                <span class="n">doc</span><span class="p">,</span>
                <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="k">def</span> <span class="nf">_build_sentence_groups</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">text_splits</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SentenceCombination</span><span class="p">]:</span>
        <span class="n">sentences</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SentenceCombination</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">"sentence"</span><span class="p">:</span> <span class="n">x</span><span class="p">,</span>
                <span class="s2">"index"</span><span class="p">:</span> <span class="n">i</span><span class="p">,</span>
                <span class="s2">"combined_sentence"</span><span class="p">:</span> <span class="s2">""</span><span class="p">,</span>
                <span class="s2">"combined_sentence_embedding"</span><span class="p">:</span> <span class="p">[],</span>
            <span class="p">}</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">text_splits</span><span class="p">)</span>
        <span class="p">]</span>

        <span class="c1"># Group sentences and calculate embeddings for sentence groups</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sentences</span><span class="p">)):</span>
            <span class="n">combined_sentence</span> <span class="o">=</span> <span class="s2">""</span>

            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">i</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">buffer_size</span><span class="p">,</span> <span class="n">i</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">j</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">combined_sentence</span> <span class="o">+=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">j</span><span class="p">][</span><span class="s2">"sentence"</span><span class="p">]</span>

            <span class="n">combined_sentence</span> <span class="o">+=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">"sentence"</span><span class="p">]</span>

            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">buffer_size</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">sentences</span><span class="p">):</span>
                    <span class="n">combined_sentence</span> <span class="o">+=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">j</span><span class="p">][</span><span class="s2">"sentence"</span><span class="p">]</span>

            <span class="n">sentences</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">"combined_sentence"</span><span class="p">]</span> <span class="o">=</span> <span class="n">combined_sentence</span>

        <span class="k">return</span> <span class="n">sentences</span>

    <span class="k">def</span> <span class="nf">_calculate_distances_between_sentence_groups</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sentences</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SentenceCombination</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
        <span class="n">distances</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sentences</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">):</span>
            <span class="n">embedding_current</span> <span class="o">=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">"combined_sentence_embedding"</span><span class="p">]</span>
            <span class="n">embedding_next</span> <span class="o">=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">][</span><span class="s2">"combined_sentence_embedding"</span><span class="p">]</span>

            <span class="n">similarity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">similarity</span><span class="p">(</span><span class="n">embedding_current</span><span class="p">,</span> <span class="n">embedding_next</span><span class="p">)</span>

            <span class="n">distance</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">similarity</span>

            <span class="n">distances</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">distance</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">distances</span>

    <span class="k">def</span> <span class="nf">_build_node_chunks</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sentences</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SentenceCombination</span><span class="p">],</span> <span class="n">distances</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">chunks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">distances</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">breakpoint_distance_threshold</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">percentile</span><span class="p">(</span>
                <span class="n">distances</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">breakpoint_percentile_threshold</span>
            <span class="p">)</span>

            <span class="n">indices_above_threshold</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">i</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">distances</span><span class="p">)</span> <span class="k">if</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="n">breakpoint_distance_threshold</span>
            <span class="p">]</span>

            <span class="c1"># Chunk sentences into semantic groups based on percentile breakpoints</span>
            <span class="n">start_index</span> <span class="o">=</span> <span class="mi">0</span>

            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">indices_above_threshold</span><span class="p">:</span>
                <span class="n">group</span> <span class="o">=</span> <span class="n">sentences</span><span class="p">[</span><span class="n">start_index</span> <span class="p">:</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span>
                <span class="n">combined_text</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">d</span><span class="p">[</span><span class="s2">"sentence"</span><span class="p">]</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">group</span><span class="p">])</span>
                <span class="n">chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">combined_text</span><span class="p">)</span>

                <span class="n">start_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>

            <span class="k">if</span> <span class="n">start_index</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">sentences</span><span class="p">):</span>
                <span class="n">combined_text</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="n">d</span><span class="p">[</span><span class="s2">"sentence"</span><span class="p">]</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">sentences</span><span class="p">[</span><span class="n">start_index</span><span class="p">:]]</span>
                <span class="p">)</span>
                <span class="n">chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">combined_text</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># If, for some reason we didn't get any distances (i.e. very, very small documents) just</span>
            <span class="c1"># treat the whole document as a single node</span>
            <span class="n">chunks</span> <span class="o">=</span> <span class="p">[</span><span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">s</span><span class="p">[</span><span class="s2">"sentence"</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">sentences</span><span class="p">])]</span>

        <span class="k">return</span> <span class="n">chunks</span>
</code></pre></div></td></tr></tbody></table>

### build\_semantic\_nodes\_from\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/#llama_index.core.node_parser.SemanticSplitterNodeParser.build_semantic_nodes_from_documents "Permanent link")

```
build_semantic_nodes_from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], show_progress: bool = False) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Build window nodes from documents.

Source code in `llama-index-core/llama_index/core/node_parser/text/semantic_splitter.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">131</span>
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
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">build_semantic_nodes_from_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Build window nodes from documents."""</span>
    <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">text</span>
        <span class="n">text_splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sentence_splitter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

        <span class="n">sentences</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_sentence_groups</span><span class="p">(</span><span class="n">text_splits</span><span class="p">)</span>

        <span class="n">combined_sentence_embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span>
            <span class="p">[</span><span class="n">s</span><span class="p">[</span><span class="s2">"combined_sentence"</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">sentences</span><span class="p">],</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">embedding</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">combined_sentence_embeddings</span><span class="p">):</span>
            <span class="n">sentences</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">"combined_sentence_embedding"</span><span class="p">]</span> <span class="o">=</span> <span class="n">embedding</span>

        <span class="n">distances</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_distances_between_sentence_groups</span><span class="p">(</span><span class="n">sentences</span><span class="p">)</span>

        <span class="n">chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_chunks</span><span class="p">(</span><span class="n">sentences</span><span class="p">,</span> <span class="n">distances</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="n">build_nodes_from_splits</span><span class="p">(</span>
            <span class="n">chunks</span><span class="p">,</span>
            <span class="n">doc</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">all_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Markdown element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/)[Next Sentence splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/)
