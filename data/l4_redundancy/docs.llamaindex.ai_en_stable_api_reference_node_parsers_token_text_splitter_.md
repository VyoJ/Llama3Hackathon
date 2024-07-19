Title: Token text splitter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/

Markdown Content:
Token text splitter - LlamaIndex


Node parsers.

TokenTextSplitter [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/#llama_index.core.node_parser.TokenTextSplitter "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MetadataAwareTextSplitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.MetadataAwareTextSplitter "llama_index.core.node_parser.interface.MetadataAwareTextSplitter")`

Implementation of splitting text that looks at word tokens.

Source code in `llama-index-core/llama_index/core/node_parser/text/token.py`

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
<span class="normal">225</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TokenTextSplitter</span><span class="p">(</span><span class="n">MetadataAwareTextSplitter</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Implementation of splitting text that looks at word tokens."""</span>

    <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The token chunk size for each chunk."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The token overlap of each chunk when splitting."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">" "</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Default separator for splitting into words"</span>
    <span class="p">)</span>
    <span class="n">backup_separators</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Additional separators for splitting."</span>
    <span class="p">)</span>

    <span class="n">_tokenizer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_split_fns</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
        <span class="n">backup_separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">],</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">chunk_overlap</span> <span class="o">&gt;</span> <span class="n">chunk_size</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Got a larger chunk overlap (</span><span class="si">{</span><span class="n">chunk_overlap</span><span class="si">}</span><span class="s2">) than chunk size "</span>
                <span class="sa">f</span><span class="s2">"(</span><span class="si">{</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">), should be smaller."</span>
            <span class="p">)</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">()</span>

        <span class="n">all_seps</span> <span class="o">=</span> <span class="p">[</span><span class="n">separator</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">backup_separators</span> <span class="ow">or</span> <span class="p">[])</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_split_fns</span> <span class="o">=</span> <span class="p">[</span><span class="n">split_by_sep</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span> <span class="k">for</span> <span class="n">sep</span> <span class="ow">in</span> <span class="n">all_seps</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="n">split_by_char</span><span class="p">()]</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="n">backup_separators</span><span class="o">=</span><span class="n">backup_separators</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
        <span class="n">backup_separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">],</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"TokenTextSplitter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with default parameters."""</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="n">backup_separators</span><span class="o">=</span><span class="n">backup_separators</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"TokenTextSplitter"</span>

    <span class="k">def</span> <span class="nf">split_text_metadata_aware</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">metadata_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Split text into chunks, reserving space required for metadata str."""</span>
        <span class="n">metadata_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">metadata_str</span><span class="p">))</span> <span class="o">+</span> <span class="n">DEFAULT_METADATA_FORMAT_LEN</span>
        <span class="n">effective_chunk_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span> <span class="o">-</span> <span class="n">metadata_len</span>
        <span class="k">if</span> <span class="n">effective_chunk_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Metadata length (</span><span class="si">{</span><span class="n">metadata_len</span><span class="si">}</span><span class="s2">) is longer than chunk size "</span>
                <span class="sa">f</span><span class="s2">"(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">). Consider increasing the chunk size or "</span>
                <span class="s2">"decreasing the size of your metadata to avoid this."</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">effective_chunk_size</span> <span class="o">&lt;</span> <span class="mi">50</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Metadata length (</span><span class="si">{</span><span class="n">metadata_len</span><span class="si">}</span><span class="s2">) is close to chunk size "</span>
                <span class="sa">f</span><span class="s2">"(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">). Resulting chunks are less than 50 tokens. "</span>
                <span class="s2">"Consider increasing the chunk size or decreasing the size of "</span>
                <span class="s2">"your metadata to avoid this."</span><span class="p">,</span>
                <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="n">effective_chunk_size</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Split text into chunks."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Split text into chunks up to chunk_size."""</span>
        <span class="k">if</span> <span class="n">text</span> <span class="o">==</span> <span class="s2">""</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">text</span><span class="p">]</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">]}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">)</span>
            <span class="n">chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_merge</span><span class="p">(</span><span class="n">splits</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">)</span>

            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">chunks</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">chunks</span>

    <span class="k">def</span> <span class="nf">_split</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Break text into splits that are smaller than chunk size.</span>

<span class="sd">        The order of splitting is:</span>
<span class="sd">        1. split by separator</span>
<span class="sd">        2. split by backup separators (if any)</span>
<span class="sd">        3. split by characters</span>

<span class="sd">        NOTE: the splits contain the separators.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">text</span><span class="p">))</span> <span class="o">&lt;=</span> <span class="n">chunk_size</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">text</span><span class="p">]</span>

        <span class="k">for</span> <span class="n">split_fn</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_fns</span><span class="p">:</span>
            <span class="n">splits</span> <span class="o">=</span> <span class="n">split_fn</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splits</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="n">new_splits</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">split</span> <span class="ow">in</span> <span class="n">splits</span><span class="p">:</span>
            <span class="n">split_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">split</span><span class="p">))</span>
            <span class="k">if</span> <span class="n">split_len</span> <span class="o">&lt;=</span> <span class="n">chunk_size</span><span class="p">:</span>
                <span class="n">new_splits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">split</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># recursively split</span>
                <span class="n">new_splits</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_split</span><span class="p">(</span><span class="n">split</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">new_splits</span>

    <span class="k">def</span> <span class="nf">_merge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">splits</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Merge splits into chunks.</span>

<span class="sd">        The high-level idea is to keep adding splits to a chunk until we</span>
<span class="sd">        exceed the chunk size, then we start a new chunk with overlap.</span>

<span class="sd">        When we start a new chunk, we pop off the first element of the previous</span>
<span class="sd">        chunk until the total length is less than the chunk size.</span>
<span class="sd">        """</span>
        <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">cur_chunk</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">cur_len</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">split</span> <span class="ow">in</span> <span class="n">splits</span><span class="p">:</span>
            <span class="n">split_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">split</span><span class="p">))</span>
            <span class="k">if</span> <span class="n">split_len</span> <span class="o">&gt;</span> <span class="n">chunk_size</span><span class="p">:</span>
                <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Got a split of size </span><span class="si">{</span><span class="n">split_len</span><span class="si">}</span><span class="s2">, "</span><span class="p">,</span>
                    <span class="sa">f</span><span class="s2">"larger than chunk size </span><span class="si">{</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">."</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="c1"># if we exceed the chunk size after adding the new split, then</span>
            <span class="c1"># we need to end the current chunk and start a new one</span>
            <span class="k">if</span> <span class="n">cur_len</span> <span class="o">+</span> <span class="n">split_len</span> <span class="o">&gt;</span> <span class="n">chunk_size</span><span class="p">:</span>
                <span class="c1"># end the previous chunk</span>
                <span class="n">chunk</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">cur_chunk</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">chunk</span><span class="p">:</span>
                    <span class="n">chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>

                <span class="c1"># start a new chunk with overlap</span>
                <span class="c1"># keep popping off the first element of the previous chunk until:</span>
                <span class="c1">#   1. the current chunk length is less than chunk overlap</span>
                <span class="c1">#   2. the total length is less than chunk size</span>
                <span class="k">while</span> <span class="n">cur_len</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_overlap</span> <span class="ow">or</span> <span class="n">cur_len</span> <span class="o">+</span> <span class="n">split_len</span> <span class="o">&gt;</span> <span class="n">chunk_size</span><span class="p">:</span>
                    <span class="c1"># pop off the first element</span>
                    <span class="n">first_chunk</span> <span class="o">=</span> <span class="n">cur_chunk</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
                    <span class="n">cur_len</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">first_chunk</span><span class="p">))</span>

            <span class="n">cur_chunk</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">split</span><span class="p">)</span>
            <span class="n">cur_len</span> <span class="o">+=</span> <span class="n">split_len</span>

        <span class="c1"># handle the last chunk</span>
        <span class="n">chunk</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">cur_chunk</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">chunk</span><span class="p">:</span>
            <span class="n">chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">chunks</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/#llama_index.core.node_parser.TokenTextSplitter.from_defaults "Permanent link")

```
from_defaults(chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = DEFAULT_CHUNK_OVERLAP, separator: str = ' ', backup_separators: Optional[List[str]] = ['\n'], callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, include_metadata: bool = True, include_prev_next_rel: bool = True, id_func: Optional[Callable[[int, [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], str]] = None) -> [TokenTextSplitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/#llama_index.core.node_parser.TokenTextSplitter "llama_index.core.node_parser.text.token.TokenTextSplitter")
```

Initialize with default parameters.

Source code in `llama-index-core/llama_index/core/node_parser/text/token.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 80</span>
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
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
    <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_OVERLAP</span><span class="p">,</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
    <span class="n">backup_separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">],</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"TokenTextSplitter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize with default parameters."""</span>
    <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
        <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
        <span class="n">backup_separators</span><span class="o">=</span><span class="n">backup_separators</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
        <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### split\_text\_metadata\_aware [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/#llama_index.core.node_parser.TokenTextSplitter.split_text_metadata_aware "Permanent link")

```
split_text_metadata_aware(text: str, metadata_str: str) -> List[str]
```

Split text into chunks, reserving space required for metadata str.

Source code in `llama-index-core/llama_index/core/node_parser/text/token.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
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
<span class="normal">128</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">split_text_metadata_aware</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">metadata_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Split text into chunks, reserving space required for metadata str."""</span>
    <span class="n">metadata_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">metadata_str</span><span class="p">))</span> <span class="o">+</span> <span class="n">DEFAULT_METADATA_FORMAT_LEN</span>
    <span class="n">effective_chunk_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span> <span class="o">-</span> <span class="n">metadata_len</span>
    <span class="k">if</span> <span class="n">effective_chunk_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Metadata length (</span><span class="si">{</span><span class="n">metadata_len</span><span class="si">}</span><span class="s2">) is longer than chunk size "</span>
            <span class="sa">f</span><span class="s2">"(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">). Consider increasing the chunk size or "</span>
            <span class="s2">"decreasing the size of your metadata to avoid this."</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">effective_chunk_size</span> <span class="o">&lt;</span> <span class="mi">50</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Metadata length (</span><span class="si">{</span><span class="n">metadata_len</span><span class="si">}</span><span class="s2">) is close to chunk size "</span>
            <span class="sa">f</span><span class="s2">"(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="si">}</span><span class="s2">). Resulting chunks are less than 50 tokens. "</span>
            <span class="s2">"Consider increasing the chunk size or decreasing the size of "</span>
            <span class="s2">"your metadata to avoid this."</span><span class="p">,</span>
            <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="n">effective_chunk_size</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### split\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/#llama_index.core.node_parser.TokenTextSplitter.split_text "Permanent link")

```
split_text(text: str) -> List[str]
```

Split text into chunks.

Source code in `llama-index-core/llama_index/core/node_parser/text/token.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Split text into chunks."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sentence window](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)[Next Unstructured element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/)
