Title: Query fusion - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/

Markdown Content:
Query fusion - LlamaIndex


QueryFusionRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/#llama_index.core.retrievers.QueryFusionRetriever "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.retrievers.BaseRetriever")`

Source code in `llama-index-core/llama_index/core/retrievers/fusion_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 33</span>
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
<span class="normal">296</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryFusionRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retrievers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseRetriever</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_gen_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">FUSION_MODES</span> <span class="o">=</span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">SIMPLE</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">num_queries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retriever_weights</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_queries</span> <span class="o">=</span> <span class="n">num_queries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_gen_prompt</span> <span class="o">=</span> <span class="n">query_gen_prompt</span> <span class="ow">or</span> <span class="n">QUERY_GEN_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">=</span> <span class="n">mode</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_async</span> <span class="o">=</span> <span class="n">use_async</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span> <span class="o">=</span> <span class="n">retrievers</span>
        <span class="k">if</span> <span class="n">retriever_weights</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_weights</span> <span class="o">=</span> <span class="p">[</span><span class="mf">1.0</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">retrievers</span><span class="p">)]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">retrievers</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Sum of retriever_weights must be 1</span>
            <span class="n">total_weight</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">retriever_weights</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_retriever_weights</span> <span class="o">=</span> <span class="p">[</span><span class="n">w</span> <span class="o">/</span> <span class="n">total_weight</span> <span class="k">for</span> <span class="n">w</span> <span class="ow">in</span> <span class="n">retriever_weights</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">resolve_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span> <span class="k">if</span> <span class="n">llm</span> <span class="k">else</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"query_gen_prompt"</span><span class="p">:</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query_gen_prompt</span><span class="p">)}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"query_gen_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_gen_prompt</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
                <span class="n">PromptTemplate</span><span class="p">,</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"query_gen_prompt"</span><span class="p">]</span>
            <span class="p">)</span><span class="o">.</span><span class="n">template</span>

    <span class="k">def</span> <span class="nf">_get_queries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">original_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]:</span>
        <span class="n">prompt_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_gen_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">num_queries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_queries</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="n">original_query</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span><span class="n">prompt_str</span><span class="p">)</span>

        <span class="c1"># assume LLM proper put each query on a newline</span>
        <span class="n">queries</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">queries</span> <span class="o">=</span> <span class="p">[</span><span class="n">q</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">queries</span> <span class="k">if</span> <span class="n">q</span><span class="o">.</span><span class="n">strip</span><span class="p">()]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">queries_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">queries</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Generated queries:</span><span class="se">\n</span><span class="si">{</span><span class="n">queries_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># The LLM often returns more queries than we asked for, so trim the list.</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">QueryBundle</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_queries</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]]</span>

    <span class="k">def</span> <span class="nf">_reciprocal_rerank_fusion</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Apply reciprocal rank fusion.</span>

<span class="sd">        The original paper uses k=60 for best results:</span>
<span class="sd">        https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf</span>
<span class="sd">        """</span>
        <span class="n">k</span> <span class="o">=</span> <span class="mf">60.0</span>  <span class="c1"># `k` is a parameter used to control the impact of outlier rankings.</span>
        <span class="n">fused_scores</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">text_to_node</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="c1"># compute reciprocal rank scores</span>
        <span class="k">for</span> <span class="n">nodes_with_scores</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">rank</span><span class="p">,</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span>
                <span class="nb">sorted</span><span class="p">(</span><span class="n">nodes_with_scores</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="ow">or</span> <span class="mf">0.0</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="p">):</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>
                <span class="n">text_to_node</span><span class="p">[</span><span class="n">text</span><span class="p">]</span> <span class="o">=</span> <span class="n">node_with_score</span>
                <span class="k">if</span> <span class="n">text</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">fused_scores</span><span class="p">:</span>
                    <span class="n">fused_scores</span><span class="p">[</span><span class="n">text</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.0</span>
                <span class="n">fused_scores</span><span class="p">[</span><span class="n">text</span><span class="p">]</span> <span class="o">+=</span> <span class="mf">1.0</span> <span class="o">/</span> <span class="p">(</span><span class="n">rank</span> <span class="o">+</span> <span class="n">k</span><span class="p">)</span>

        <span class="c1"># sort results</span>
        <span class="n">reranked_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
            <span class="nb">sorted</span><span class="p">(</span><span class="n">fused_scores</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># adjust node scores</span>
        <span class="n">reranked_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">text</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">reranked_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">reranked_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text_to_node</span><span class="p">[</span><span class="n">text</span><span class="p">])</span>
            <span class="n">reranked_nodes</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="n">score</span>

        <span class="k">return</span> <span class="n">reranked_nodes</span>

    <span class="k">def</span> <span class="nf">_relative_score_fusion</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]],</span>
        <span class="n">dist_based</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Apply relative score fusion."""</span>
        <span class="c1"># MinMax scale scores of each result set (highest value becomes 1, lowest becomes 0)</span>
        <span class="c1"># then scale by the weight of the retriever</span>
        <span class="n">min_max_scores</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">query_tuple</span><span class="p">,</span> <span class="n">nodes_with_scores</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes_with_scores</span><span class="p">:</span>
                <span class="n">min_max_scores</span><span class="p">[</span><span class="n">query_tuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span>
                <span class="k">continue</span>
            <span class="n">scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes_with_scores</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">dist_based</span><span class="p">:</span>
                <span class="c1"># Set min and max based on mean and std dev</span>
                <span class="n">mean_score</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span>
                <span class="n">std_dev</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="nb">sum</span><span class="p">((</span><span class="n">x</span> <span class="o">-</span> <span class="n">mean_score</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">scores</span><span class="p">)</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span>
                <span class="p">)</span> <span class="o">**</span> <span class="mf">0.5</span>
                <span class="n">min_score</span> <span class="o">=</span> <span class="n">mean_score</span> <span class="o">-</span> <span class="mi">3</span> <span class="o">*</span> <span class="n">std_dev</span>
                <span class="n">max_score</span> <span class="o">=</span> <span class="n">mean_score</span> <span class="o">+</span> <span class="mi">3</span> <span class="o">*</span> <span class="n">std_dev</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">min_score</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span>
                <span class="n">max_score</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span>
            <span class="n">min_max_scores</span><span class="p">[</span><span class="n">query_tuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">min_score</span><span class="p">,</span> <span class="n">max_score</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">query_tuple</span><span class="p">,</span> <span class="n">nodes_with_scores</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes_with_scores</span><span class="p">:</span>
                <span class="n">min_score</span><span class="p">,</span> <span class="n">max_score</span> <span class="o">=</span> <span class="n">min_max_scores</span><span class="p">[</span><span class="n">query_tuple</span><span class="p">]</span>
                <span class="c1"># Scale the score to be between 0 and 1</span>
                <span class="k">if</span> <span class="n">max_score</span> <span class="o"></span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">RECIPROCAL_RANK</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reciprocal_rerank_fusion</span><span class="p">(</span><span class="n">results</span><span class="p">)[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">]</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">DIST_BASED_SCORE</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relative_score_fusion</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="n">dist_based</span><span class="o">=</span><span class="kc">True</span><span class="p">)[</span>
                <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span>
            <span class="p">]</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">RECIPROCAL_RANK</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reciprocal_rerank_fusion</span><span class="p">(</span><span class="n">results</span><span class="p">)[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">]</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">DIST_BASED_SCORE</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relative_score_fusion</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="n">dist_based</span><span class="o">=</span><span class="kc">True</span><span class="p">)[</span>
                <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span>
            <span class="p">]</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="n">FUSION_MODES</span><span class="o">.</span><span class="n">SIMPLE</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_simple_fusion</span><span class="p">(</span><span class="n">results</span><span class="p">)[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid fusion mode: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pathway](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/)[Next Recursive](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/)
