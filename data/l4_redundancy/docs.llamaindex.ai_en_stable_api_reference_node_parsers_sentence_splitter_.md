Title: Sentence splitter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/

Markdown Content:
Sentence splitter - LlamaIndex


Node parsers.

SentenceSplitter [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/#llama_index.core.node_parser.SentenceSplitter "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MetadataAwareTextSplitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.MetadataAwareTextSplitter "llama_index.core.node_parser.interface.MetadataAwareTextSplitter")`

Parse text with a preference for complete sentences.

In general, this class tries to keep sentences and paragraphs together. Therefore compared to the original TokenTextSplitter, there are less likely to be hanging sentences or parts of sentences at the end of the node chunk.

Source code in `llama-index-core/llama_index/core/node_parser/text/sentence.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 32</span>
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
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SentenceSplitter</span><span class="p">(</span><span class="n">MetadataAwareTextSplitter</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Parse text with a preference for complete sentences.</span>

<span class="sd">    In general, this class tries to keep sentences and paragraphs together. Therefore</span>
<span class="sd">    compared to the original TokenTextSplitter, there are less likely to be</span>
<span class="sd">    hanging sentences or parts of sentences at the end of the node chunk.</span>
<span class="sd">    """</span>

    <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The token chunk size for each chunk."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">SENTENCE_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The token overlap of each chunk when splitting."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">" "</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Default separator for splitting into words"</span>
    <span class="p">)</span>
    <span class="n">paragraph_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_PARAGRAPH_SEP</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Separator between paragraphs."</span>
    <span class="p">)</span>
    <span class="n">secondary_chunking_regex</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">CHUNKING_REGEX</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Backup regex for splitting into sentences."</span>
    <span class="p">)</span>

    <span class="n">_chunking_tokenizer_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_tokenizer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_split_fns</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_sub_sentence_split_fns</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">SENTENCE_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">paragraph_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PARAGRAPH_SEP</span><span class="p">,</span>
        <span class="n">chunking_tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">secondary_chunking_regex</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">CHUNKING_REGEX</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
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
        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>

        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_chunking_tokenizer_fn</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">chunking_tokenizer_fn</span> <span class="ow">or</span> <span class="n">split_by_sentence_tokenizer</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_split_fns</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">split_by_sep</span><span class="p">(</span><span class="n">paragraph_separator</span><span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_chunking_tokenizer_fn</span><span class="p">,</span>
        <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_sub_sentence_split_fns</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">split_by_regex</span><span class="p">(</span><span class="n">secondary_chunking_regex</span><span class="p">),</span>
            <span class="n">split_by_sep</span><span class="p">(</span><span class="n">separator</span><span class="p">),</span>
            <span class="n">split_by_char</span><span class="p">(),</span>
        <span class="p">]</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
            <span class="n">secondary_chunking_regex</span><span class="o">=</span><span class="n">secondary_chunking_regex</span><span class="p">,</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="n">paragraph_separator</span><span class="o">=</span><span class="n">paragraph_separator</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">SENTENCE_CHUNK_OVERLAP</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">paragraph_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PARAGRAPH_SEP</span><span class="p">,</span>
        <span class="n">chunking_tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">secondary_chunking_regex</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">CHUNKING_REGEX</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SentenceSplitter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
            <span class="n">tokenizer</span><span class="o">=</span><span class="n">tokenizer</span><span class="p">,</span>
            <span class="n">paragraph_separator</span><span class="o">=</span><span class="n">paragraph_separator</span><span class="p">,</span>
            <span class="n">chunking_tokenizer_fn</span><span class="o">=</span><span class="n">chunking_tokenizer_fn</span><span class="p">,</span>
            <span class="n">secondary_chunking_regex</span><span class="o">=</span><span class="n">secondary_chunking_regex</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SentenceSplitter"</span>

    <span class="k">def</span> <span class="nf">split_text_metadata_aware</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">metadata_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">metadata_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">metadata_str</span><span class="p">))</span>
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
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_text</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">chunk_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        _Split incoming text and return chunks with overlap size.</span>

<span class="sd">        Has a preference for complete sentences, phrases, and minimal overlap.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">text</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">new_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">stripped_chunk</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_chunks</span>

    <span class="k">def</span> <span class="nf">_token_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">text</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_get_splits_by_fns</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">split_fn</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_split_fns</span><span class="p">:</span>
            <span class="n">splits</span> <span class="o">=</span> <span class="n">split_fn</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splits</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">splits</span><span class="p">,</span> <span class="kc">True</span>

        <span class="k">for</span> <span class="n">split_fn</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sub_sentence_split_fns</span><span class="p">:</span>
            <span class="n">splits</span> <span class="o">=</span> <span class="n">split_fn</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splits</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">splits</span><span class="p">,</span> <span class="kc">False</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/#llama_index.core.node_parser.SentenceSplitter.from_defaults "Permanent link")

```
from_defaults(separator: str = ' ', chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = SENTENCE_CHUNK_OVERLAP, tokenizer: Optional[Callable] = None, paragraph_separator: str = DEFAULT_PARAGRAPH_SEP, chunking_tokenizer_fn: Optional[Callable[[str], List[str]]] = None, secondary_chunking_regex: str = CHUNKING_REGEX, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, include_metadata: bool = True, include_prev_next_rel: bool = True) -> [SentenceSplitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/#llama_index.core.node_parser.SentenceSplitter "llama_index.core.node_parser.text.sentence.SentenceSplitter")
```

Initialize with parameters.

Source code in `llama-index-core/llama_index/core/node_parser/text/sentence.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">116</span>
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
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
    <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
    <span class="n">chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">SENTENCE_CHUNK_OVERLAP</span><span class="p">,</span>
    <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">paragraph_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PARAGRAPH_SEP</span><span class="p">,</span>
    <span class="n">chunking_tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">secondary_chunking_regex</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">CHUNKING_REGEX</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SentenceSplitter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize with parameters."""</span>
    <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">separator</span><span class="o">=</span><span class="n">separator</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="o">=</span><span class="n">tokenizer</span><span class="p">,</span>
        <span class="n">paragraph_separator</span><span class="o">=</span><span class="n">paragraph_separator</span><span class="p">,</span>
        <span class="n">chunking_tokenizer_fn</span><span class="o">=</span><span class="n">chunking_tokenizer_fn</span><span class="p">,</span>
        <span class="n">secondary_chunking_regex</span><span class="o">=</span><span class="n">secondary_chunking_regex</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Semantic splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/)[Next Sentence window](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)
