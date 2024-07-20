Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/

Markdown Content:
Index - LlamaIndex


RefDocInfo `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `DataClassJsonMixin`

Dataclass to represent ingested documents.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">RefDocInfo</span><span class="p">(</span><span class="n">DataClassJsonMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Dataclass to represent ingested documents."""</span>

    <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BaseDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 24</span>
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
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseDocumentStore</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
    <span class="c1"># </span>
    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the docstore to a file."""</span>

    <span class="c1"># </span>
    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">docs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">add_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">allow_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">store_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document from the store."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document from the store."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">document_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">adocument_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="c1"># </span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set_document_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">doc_hash</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aset_document_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">doc_hash</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set_document_hashes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_hashes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aset_document_hashes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_hashes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_document_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_document_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_all_document_hashes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all_document_hashes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="c1"># </span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a ref_doc and all it's associated nodes."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a ref_doc and all it's associated nodes."""</span>

    <span class="c1"># </span>
    <span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from docstore.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_ids (List[str]): node ids</span>
<span class="sd">            raise_error (bool): raise error if node_id not found</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span> <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from docstore.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_ids (List[str]): node ids</span>
<span class="sd">            raise_error (bool): raise error if node_id not found</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get node from docstore.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_id (str): node id</span>
<span class="sd">            raise_error (bool): raise error if node_id not found</span>

<span class="sd">        """</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2"> is not a Node."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">doc</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get node from docstore.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_id (str): node id</span>
<span class="sd">            raise_error (bool): raise error if node_id not found</span>

<span class="sd">        """</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2"> is not a Node."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">doc</span>

    <span class="k">def</span> <span class="nf">get_node_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get node dict from docstore given a mapping of index to node ids.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_id_dict (Dict[int, str]): mapping of index to node ids</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">index</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_id_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_node_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get node dict from docstore given a mapping of index to node ids.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_id_dict (Dict[int, str]): mapping of index to node ids</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">index</span><span class="p">:</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_id_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.persist "Permanent link")

```
persist(persist_path: str = DEFAULT_PERSIST_PATH, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the docstore to a file.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the docstore to a file."""</span>
</code></pre></div></td></tr></tbody></table>

### delete\_document `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.delete_document "Permanent link")

```
delete_document(doc_id: str, raise_error: bool = True) -> None
```

Delete a document from the store.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document from the store."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### adelete\_document `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.adelete_document "Permanent link")

```
adelete_document(doc_id: str, raise_error: bool = True) -> None
```

Delete a document from the store.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document from the store."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### get\_all\_ref\_doc\_info `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.get_all_ref_doc_info "Permanent link")

```
get_all_ref_doc_info() -> Optional[Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]]
```

Get a mapping of ref\_doc\_id -> RefDocInfo for all ingested documents.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents."""</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all\_ref\_doc\_info `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.aget_all_ref_doc_info "Permanent link")

```
aget_all_ref_doc_info() -> Optional[Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]]
```

Get a mapping of ref\_doc\_id -> RefDocInfo for all ingested documents.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Get a mapping of ref_doc_id -&gt; RefDocInfo for all ingested documents."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_ref\_doc\_info `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.get_ref_doc_info "Permanent link")

```
get_ref_doc_info(ref_doc_id: str) -> Optional[[RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Get the RefDocInfo for a given ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
</code></pre></div></td></tr></tbody></table>

### aget\_ref\_doc\_info `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.aget_ref_doc_info "Permanent link")

```
aget_ref_doc_info(ref_doc_id: str) -> Optional[[RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Get the RefDocInfo for a given ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aget_ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the RefDocInfo for a given ref_doc_id."""</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, raise_error: bool = True) -> None
```

Delete a ref\_doc and all it's associated nodes.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a ref_doc and all it's associated nodes."""</span>
</code></pre></div></td></tr></tbody></table>

### adelete\_ref\_doc `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.adelete_ref_doc "Permanent link")

```
adelete_ref_doc(ref_doc_id: str, raise_error: bool = True) -> None
```

Delete a ref\_doc and all it's associated nodes.

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a ref_doc and all it's associated nodes."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.get_nodes "Permanent link")

```
get_nodes(node_ids: List[str], raise_error: bool = True) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from docstore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_ids` | `List[str]` | 
node ids



 | _required_ |
| `raise_error` | `bool` | 

raise error if node\_id not found



 | `True` |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from docstore.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_ids (List[str]): node ids</span>
<span class="sd">        raise_error (bool): raise error if node_id not found</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span> <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### aget\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.aget_nodes "Permanent link")

```
aget_nodes(node_ids: List[str], raise_error: bool = True) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from docstore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_ids` | `List[str]` | 
node ids



 | _required_ |
| `raise_error` | `bool` | 

raise error if node\_id not found



 | `True` |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">158</span>
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
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from docstore.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_ids (List[str]): node ids</span>
<span class="sd">        raise_error (bool): raise error if node_id not found</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.get_node "Permanent link")

```
get_node(node_id: str, raise_error: bool = True) -> [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")
```

Get node from docstore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_id` | `str` | 
node id



 | _required_ |
| `raise_error` | `bool` | 

raise error if node\_id not found



 | `True` |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">173</span>
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
<span class="normal">184</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get node from docstore.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_id (str): node id</span>
<span class="sd">        raise_error (bool): raise error if node_id not found</span>

<span class="sd">    """</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2"> is not a Node."</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">doc</span>
</code></pre></div></td></tr></tbody></table>

### aget\_node `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.aget_node "Permanent link")

```
aget_node(node_id: str, raise_error: bool = True) -> [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")
```

Get node from docstore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_id` | `str` | 
node id



 | _required_ |
| `raise_error` | `bool` | 

raise error if node\_id not found



 | `True` |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
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
<span class="normal">197</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get node from docstore.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_id (str): node id</span>
<span class="sd">        raise_error (bool): raise error if node_id not found</span>

<span class="sd">    """</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_document</span><span class="p">(</span><span class="n">node_id</span><span class="p">,</span> <span class="n">raise_error</span><span class="o">=</span><span class="n">raise_error</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2"> is not a Node."</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">doc</span>
</code></pre></div></td></tr></tbody></table>

### get\_node\_dict [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.get_node_dict "Permanent link")

```
get_node_dict(node_id_dict: Dict[int, str]) -> Dict[int, [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get node dict from docstore given a mapping of index to node ids.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_id_dict` | `Dict[int, str]` | 
mapping of index to node ids



 | _required_ |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_node_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get node dict from docstore given a mapping of index to node ids.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_id_dict (Dict[int, str]): mapping of index to node ids</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="n">index</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_id_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### aget\_node\_dict `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore.aget_node_dict "Permanent link")

```
aget_node_dict(node_id_dict: Dict[int, str]) -> Dict[int, [BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get node dict from docstore given a mapping of index to node ids.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_id_dict` | `Dict[int, str]` | 
mapping of index to node ids



 | _required_ |

Source code in `llama-index-core/llama_index/core/storage/docstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_node_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get node dict from docstore given a mapping of index to node ids.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_id_dict (Dict[int, str]): mapping of index to node ids</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="n">index</span><span class="p">:</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aget_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_id_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/)[Next Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/mongodb/)
