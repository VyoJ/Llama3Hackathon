Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/

Markdown Content:
Index - LlamaIndex


Base retriever.

BaseRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[ChainableMixin](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "llama_index.core.base.query_pipeline.query.ChainableMixin")`, `PromptMixin`, `DispatcherSpanMixin`

Base retriever.

Source code in `llama-index-core/llama_index/core/base/base_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 43</span>
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
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseRetriever</span><span class="p">(</span><span class="n">ChainableMixin</span><span class="p">,</span> <span class="n">PromptMixin</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base retriever."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">objects</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">object_map</span> <span class="o">=</span> <span class="p">{</span><span class="n">obj</span><span class="o">.</span><span class="n">index_id</span><span class="p">:</span> <span class="n">obj</span><span class="o">.</span><span class="n">obj</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">objects</span><span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">object_map</span> <span class="o">=</span> <span class="n">object_map</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">_check_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check callback manager."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"callback_manager"</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>

    <span class="k">def</span> <span class="nf">_retrieve_from_object</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">score</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes from object."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Retrieving from object </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2"> with query </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">color</span><span class="o">=</span><span class="s2">"llama_pink"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">NodeWithScore</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">obj</span><span class="p">]</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">obj</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">)]</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseQueryEngine</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}),</span>
                    <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseRetriever</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">QueryComponent</span><span class="p">):</span>
            <span class="n">component_keys</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">input_keys</span><span class="o">.</span><span class="n">required_keys</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">component_keys</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"QueryComponent </span><span class="si">{</span><span class="n">obj</span><span class="si">}</span><span class="s2"> has more than one input key: </span><span class="si">{</span><span class="n">component_keys</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">component_keys</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">component_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">obj</span><span class="o">.</span><span class="n">arun_component</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">component_keys</span><span class="p">)):</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
                <span class="n">component_response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">obj</span><span class="o">.</span><span class="n">arun_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

            <span class="n">result_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">component_response</span><span class="o">.</span><span class="n">values</span><span class="p">())))</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result_output</span><span class="p">),</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">)]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Object </span><span class="si">{</span><span class="n">obj</span><span class="si">}</span><span class="s2"> is not retrievable."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_handle_recursive_retrieval</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">retrieved_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">node</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">score</span> <span class="ow">or</span> <span class="mf">1.0</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
                <span class="n">obj</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">obj</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">object_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">obj</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"Retrieval entering </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                            <span class="n">color</span><span class="o">=</span><span class="s2">"llama_turquoise"</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_from_object</span><span class="p">(</span>
                            <span class="n">obj</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>

        <span class="n">seen</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">n</span>
            <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span> <span class="ow">in</span> <span class="n">seen</span> <span class="ow">or</span> <span class="n">seen</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">))</span>  <span class="c1"># type: ignore[func-returns-value]</span>
        <span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_ahandle_recursive_retrieval</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">retrieved_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">node</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">score</span> <span class="ow">or</span> <span class="mf">1.0</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">IndexNode</span><span class="p">):</span>
                <span class="n">obj</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">obj</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">object_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">obj</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                        <span class="n">print_text</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"Retrieval entering </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">index_id</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                            <span class="n">color</span><span class="o">=</span><span class="s2">"llama_turquoise"</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="c1"># TODO: Add concurrent execution via `run_jobs()` ?</span>
                    <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve_from_object</span><span class="p">(</span>
                            <span class="n">obj</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">retrieved_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>

        <span class="c1"># remove any duplicates based on hash and ref_doc_id</span>
        <span class="n">seen</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">n</span>
            <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="p">((</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">,</span> <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">)</span> <span class="ow">in</span> <span class="n">seen</span> <span class="ow">or</span> <span class="n">seen</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">,</span> <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">)))</span>  <span class="c1"># type: ignore[func-returns-value]</span>
        <span class="p">]</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query.</span>

<span class="sd">        Args:</span>
<span class="sd">            str_or_query_bundle (QueryType): Either a query string or</span>
<span class="sd">                a QueryBundle object.</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_check_callback_manager</span><span class="p">()</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">RetrievalStartEvent</span><span class="p">(</span>
                <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"query"</span><span class="p">):</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_recursive_retrieval</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>
                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
                <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">RetrievalEndEvent</span><span class="p">(</span>
                <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_check_callback_manager</span><span class="p">()</span>

        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">RetrievalStartEvent</span><span class="p">(</span>
                <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"query"</span><span class="p">):</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ahandle_recursive_retrieval</span><span class="p">(</span>
                    <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span>
                <span class="p">)</span>
                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
                <span class="p">)</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">RetrievalEndEvent</span><span class="p">(</span>
                <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>

    <span class="c1"># TODO: make this abstract</span>
    <span class="c1"># @abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Asynchronously retrieve nodes given query.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_service_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Attempts to resolve a service context.</span>
<span class="sd">        Short-circuits at self.service_context, self._service_context,</span>
<span class="sd">        or self._index.service_context.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"service_context"</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"_service_context"</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>
        <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"_index"</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span> <span class="s2">"service_context"</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a query component."""</span>
        <span class="k">return</span> <span class="n">RetrieverComponent</span><span class="p">(</span><span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever.retrieve "Permanent link")

```
retrieve(str_or_query_bundle: QueryType) -> List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]
```

Retrieve nodes given query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `str_or_query_bundle` | `QueryType` | 
Either a query string or a QueryBundle object.



 | _required_ |

Source code in `llama-index-core/llama_index/core/base/base_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">219</span>
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
<span class="normal">254</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
<span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve nodes given query.</span>

<span class="sd">    Args:</span>
<span class="sd">        str_or_query_bundle (QueryType): Either a query string or</span>
<span class="sd">            a QueryBundle object.</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_check_callback_manager</span><span class="p">()</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">RetrievalStartEvent</span><span class="p">(</span>
            <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">as_trace</span><span class="p">(</span><span class="s2">"query"</span><span class="p">):</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_recursive_retrieval</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>
            <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
            <span class="p">)</span>
    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">RetrievalEndEvent</span><span class="p">(</span>
            <span class="n">str_or_query_bundle</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### get\_service\_context [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever.get_service_context "Permanent link")

```
get_service_context() -> Optional[ServiceContext]
```

Attempts to resolve a service context. Short-circuits at self.service\_context, self.\_service\_context, or self.\_index.service\_context.

Source code in `llama-index-core/llama_index/core/base/base_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_service_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Attempts to resolve a service context.</span>
<span class="sd">    Short-circuits at self.service_context, self._service_context,</span>
<span class="sd">    or self._index.service_context.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"service_context"</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"_service_context"</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>
    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"_index"</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span> <span class="s2">"service_context"</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">service_context</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

BaseImageRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.image_retriever.BaseImageRetriever "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PromptMixin`, `DispatcherSpanMixin`

Base Image Retriever Abstraction.

Source code in `llama-index-core/llama_index/core/image_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 10</span>
<span class="normal"> 11</span>
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
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseImageRetriever</span><span class="p">(</span><span class="n">PromptMixin</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base Image Retriever Abstraction."""</span>

    <span class="k">def</span> <span class="nf">text_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve image nodes given query or single image input.</span>

<span class="sd">        Args:</span>
<span class="sd">            str_or_query_bundle (QueryType): a query text</span>
<span class="sd">            string or a QueryBundle object.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_text_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve image nodes or documents given query text.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>

    <span class="k">def</span> <span class="nf">image_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve image nodes given single image input.</span>

<span class="sd">        Args:</span>
<span class="sd">            str_or_query_bundle (QueryType): a image path</span>
<span class="sd">            string or a QueryBundle object.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="c1"># leave query_str as empty since we are using image_path for image retrieval</span>
            <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">image_path</span><span class="o">=</span><span class="n">str_or_query_bundle</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_image_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_image_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve image nodes or documents given image.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>

    <span class="c1"># Async Methods</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">atext_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_atext_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_atext_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Async retrieve image nodes or documents given query text.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aimage_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="c1"># leave query_str as empty since we are using image_path for image retrieval</span>
            <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span>
                <span class="n">query_str</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">image_path</span><span class="o">=</span><span class="n">str_or_query_bundle</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aimage_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aimage_to_image_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Async retrieve image nodes or documents given image.</span>

<span class="sd">        Implemented by the user.</span>

<span class="sd">        """</span>
</code></pre></div></td></tr></tbody></table>

### text\_to\_image\_retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.image_retriever.BaseImageRetriever.text_to_image_retrieve "Permanent link")

```
text_to_image_retrieve(str_or_query_bundle: QueryType) -> List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]
```

Retrieve image nodes given query or single image input.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `str_or_query_bundle` | `QueryType` | 
a query text



 | _required_ |

Source code in `llama-index-core/llama_index/core/image_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">text_to_image_retrieve</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve image nodes given query or single image input.</span>

<span class="sd">    Args:</span>
<span class="sd">        str_or_query_bundle (QueryType): a query text</span>
<span class="sd">        string or a QueryBundle object.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### image\_to\_image\_retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.image_retriever.BaseImageRetriever.image_to_image_retrieve "Permanent link")

```
image_to_image_retrieve(str_or_query_bundle: QueryType) -> List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]
```

Retrieve image nodes given single image input.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `str_or_query_bundle` | `QueryType` | 
a image path



 | _required_ |

Source code in `llama-index-core/llama_index/core/image_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">image_to_image_retrieve</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Retrieve image nodes given single image input.</span>

<span class="sd">    Args:</span>
<span class="sd">        str_or_query_bundle (QueryType): a image path</span>
<span class="sd">        string or a QueryBundle object.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="c1"># leave query_str as empty since we are using image_path for image retrieval</span>
        <span class="n">str_or_query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">image_path</span><span class="o">=</span><span class="n">str_or_query_bundle</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_image_to_image_retrieve</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Duckdb retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/duckdb_retriever/)[Next Keyword](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/)
