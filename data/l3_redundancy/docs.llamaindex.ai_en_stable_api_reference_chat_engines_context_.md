Title: Context - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/

Markdown Content:
Context - LlamaIndex


ContextChatEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/#llama_index.core.chat_engine.ContextChatEngine "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "llama_index.core.chat_engine.types.BaseChatEngine")`

Context Chat Engine.

Uses a retriever to retrieve a context, set the context in the system prompt, and then uses an LLM to generate a response, for a fluid chat experience.

Source code in `llama-index-core/llama_index/core/chat_engine/context.py`

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
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ContextChatEngine</span><span class="p">(</span><span class="n">BaseChatEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Context Chat Engine.</span>

<span class="sd">    Uses a retriever to retrieve a context, set the context in the system prompt,</span>
<span class="sd">    and then uses an LLM to generate a response, for a fluid chat experience.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span> <span class="o">=</span> <span class="n">memory</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_context_template</span> <span class="o">=</span> <span class="n">context_template</span> <span class="ow">or</span> <span class="n">DEFAULT_CONTEXT_TEMPLATE</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ContextChatEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a ContextChatEngine from default parameters."""</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">token_limit</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">context_window</span> <span class="o">-</span> <span class="mi">256</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
                <span class="p">)</span>
            <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">system_role</span><span class="p">)</span>
            <span class="p">]</span>

        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">),</span>
            <span class="n">context_template</span><span class="o">=</span><span class="n">context_template</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_generate_context</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Generate context information from a message."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">QueryBundle</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="p">)</span>

        <span class="n">context_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">),</span> <span class="n">nodes</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_agenerate_context</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Generate context information from a message."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">QueryBundle</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="n">context_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">),</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">_get_prefix_messages_with_context</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get the prefix messages with context."""</span>
        <span class="c1"># ensure we grab the user-configured system prompt</span>
        <span class="n">system_prompt</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span>
            <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o">==</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span>
        <span class="p">):</span>
            <span class="n">system_prompt</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>

        <span class="n">context_str_w_sys_prompt</span> <span class="o">=</span> <span class="n">system_prompt</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">context_str</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="n">context_str_w_sys_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">system_role</span>
            <span class="p">),</span>
            <span class="o">*</span><span class="n">prefix_messages</span><span class="p">,</span>
        <span class="p">]</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>

        <span class="n">context_str_template</span><span class="p">,</span> <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_context</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_prefix_messages_with_context</span><span class="p">(</span><span class="n">context_str_template</span><span class="p">)</span>
        <span class="n">prefix_messages_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">prefix_messages_token_count</span>
        <span class="p">)</span>
        <span class="n">chat_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="n">ai_message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolOutput</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s2">"retriever"</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                    <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"message"</span><span class="p">:</span> <span class="n">message</span><span class="p">},</span>
                    <span class="n">raw_output</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>

        <span class="n">context_str_template</span><span class="p">,</span> <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_context</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_prefix_messages_with_context</span><span class="p">(</span><span class="n">context_str_template</span><span class="p">)</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
            <span class="n">chat_stream</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolOutput</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s2">"retriever"</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                    <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"message"</span><span class="p">:</span> <span class="n">message</span><span class="p">},</span>
                    <span class="n">raw_output</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="n">chat_response</span><span class="o">.</span><span class="n">write_response_to_history</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">,)</span>
        <span class="p">)</span>
        <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>

        <span class="n">context_str_template</span><span class="p">,</span> <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_context</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_prefix_messages_with_context</span><span class="p">(</span><span class="n">context_str_template</span><span class="p">)</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="n">ai_message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolOutput</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s2">"retriever"</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                    <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"message"</span><span class="p">:</span> <span class="n">message</span><span class="p">},</span>
                    <span class="n">raw_output</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>

        <span class="n">context_str_template</span><span class="p">,</span> <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_context</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_prefix_messages_with_context</span><span class="p">(</span><span class="n">context_str_template</span><span class="p">)</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
            <span class="n">achat_stream</span><span class="o">=</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">astream_chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolOutput</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s2">"retriever"</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                    <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"message"</span><span class="p">:</span> <span class="n">message</span><span class="p">},</span>
                    <span class="n">raw_output</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">awrite_response_to_history</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### chat\_history `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/#llama_index.core.chat_engine.ContextChatEngine.chat_history "Permanent link")

```
chat_history: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/#llama_index.core.chat_engine.ContextChatEngine.from_defaults "Permanent link")

```
from_defaults(retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever"), service_context: Optional[ServiceContext] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = None, system_prompt: Optional[str] = None, prefix_messages: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, node_postprocessors: Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]] = None, context_template: Optional[str] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, **kwargs: Any) -> [ContextChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/#llama_index.core.chat_engine.ContextChatEngine "llama_index.core.chat_engine.context.ContextChatEngine")
```

Initialize a ContextChatEngine from default parameters.

Source code in `llama-index-core/llama_index/core/chat_engine/context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 62</span>
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
<span class="normal">106</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">context_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ContextChatEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a ContextChatEngine from default parameters."""</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

    <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">token_limit</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">context_window</span> <span class="o">-</span> <span class="mi">256</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
            <span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">system_role</span><span class="p">)</span>
        <span class="p">]</span>

    <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">),</span>
        <span class="n">context_template</span><span class="o">=</span><span class="n">context_template</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Condense question](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/)
