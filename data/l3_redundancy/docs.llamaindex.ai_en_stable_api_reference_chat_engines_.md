Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/

Markdown Content:
Index - LlamaIndex


ChatResponseMode [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatResponseMode "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Flag toggling waiting/streaming in `Agent._chat`.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatResponseMode</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Flag toggling waiting/streaming in `Agent._chat`."""</span>

    <span class="n">WAIT</span> <span class="o">=</span> <span class="s2">"wait"</span>
    <span class="n">STREAM</span> <span class="o">=</span> <span class="s2">"stream"</span>
</code></pre></div></td></tr></tbody></table>

AgentChatResponse `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Agent chat response.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">47</span>
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
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
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
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">AgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Agent chat response."""</span>

    <span class="n">response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">source_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">is_dummy_stream</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sources</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">tool_output</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sources</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool_output</span><span class="o">.</span><span class="n">raw_output</span><span class="p">,</span> <span class="p">(</span><span class="n">Response</span><span class="p">,</span> <span class="n">StreamingResponse</span><span class="p">)):</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">source_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">tool_output</span><span class="o">.</span><span class="n">raw_output</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">response</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">response_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Used for fake streaming, i.e. with tool outputs."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_dummy_stream</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"response_gen is only available for streaming responses. "</span>
                <span class="s2">"Set is_dummy_stream=True if you still want a generator."</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">" "</span><span class="p">):</span>
            <span class="k">yield</span> <span class="n">token</span> <span class="o">+</span> <span class="s2">" "</span>
            <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_response_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Used for fake streaming, i.e. with tool outputs."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_dummy_stream</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"response_gen is only available for streaming responses. "</span>
                <span class="s2">"Set is_dummy_stream=True if you still want a generator."</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">" "</span><span class="p">):</span>
            <span class="k">yield</span> <span class="n">token</span> <span class="o">+</span> <span class="s2">" "</span>
            <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### response\_gen `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse.response_gen "Permanent link")

```
response_gen: Generator[str, None, None]
```

Used for fake streaming, i.e. with tool outputs.

### async\_response\_gen `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse.async_response_gen "Permanent link")

```
async_response_gen() -> AsyncGenerator[str, None]
```

Used for fake streaming, i.e. with tool outputs.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_response_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Used for fake streaming, i.e. with tool outputs."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_dummy_stream</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"response_gen is only available for streaming responses. "</span>
            <span class="s2">"Set is_dummy_stream=True if you still want a generator."</span>
        <span class="p">)</span>

    <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">" "</span><span class="p">):</span>
        <span class="k">yield</span> <span class="n">token</span> <span class="o">+</span> <span class="s2">" "</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

StreamingAgentChatResponse `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.StreamingAgentChatResponse "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Streaming chat response to user and writing to chat history.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 92</span>
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
<span class="normal">295</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">StreamingAgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Streaming chat response to user and writing to chat history."""</span>

    <span class="n">response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">chat_stream</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatResponseGen</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">achat_stream</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatResponseAsyncGen</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">source_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">unformatted_response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">queue</span><span class="p">:</span> <span class="n">Queue</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">Queue</span><span class="p">)</span>
    <span class="n">aqueue</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">Queue</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="c1"># flag when chat message is a function call</span>
    <span class="n">is_function</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="c1"># flag when processing done</span>
    <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="c1"># signal when a new item is added to the queue</span>
    <span class="n">new_item_event</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="c1"># NOTE: async code uses two events rather than one since it yields</span>
    <span class="c1"># control when waiting for queue item</span>
    <span class="c1"># signal when the OpenAI functions stop executing</span>
    <span class="n">is_function_false_event</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="c1"># signal when an OpenAI function is being executed</span>
    <span class="n">is_function_not_none_thread_event</span><span class="p">:</span> <span class="n">Event</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">Event</span><span class="p">)</span>
    <span class="c1"># Track if an exception occurred</span>
    <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sources</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">tool_output</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sources</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool_output</span><span class="o">.</span><span class="n">raw_output</span><span class="p">,</span> <span class="p">(</span><span class="n">Response</span><span class="p">,</span> <span class="n">StreamingResponse</span><span class="p">)):</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">source_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">tool_output</span><span class="o">.</span><span class="n">raw_output</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span><span class="p">:</span>
            <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">queue</span><span class="p">:</span>
                <span class="n">delta</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span> <span class="o">+=</span> <span class="n">delta</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">response</span>

    <span class="k">def</span> <span class="nf">_ensure_async_setup</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">aqueue</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aqueue</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Event</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function_false_event</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">is_function_false_event</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Event</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">put_in_queue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">delta</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_function_not_none_thread_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">aput_in_queue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aqueue</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">delta</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">write_response_to_history</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">on_stream_end_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_stream</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"chat_stream is None. Cannot write to history without chat_stream."</span>
            <span class="p">)</span>

        <span class="c1"># try/except to prevent hanging on error</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatStartEvent</span><span class="p">())</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">final_text</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">chat</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_stream</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span> <span class="o">=</span> <span class="n">is_function</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">:</span>
                    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                        <span class="n">StreamChatDeltaReceivedEvent</span><span class="p">(</span>
                            <span class="n">delta</span><span class="o">=</span><span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">put_in_queue</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">)</span>
                <span class="n">final_text</span> <span class="o">+=</span> <span class="n">chat</span><span class="o">.</span><span class="n">delta</span> <span class="ow">or</span> <span class="s2">""</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># if loop has gone through iteration</span>
                <span class="c1"># NOTE: this is to handle the special case where we consume some of the</span>
                <span class="c1"># chat stream, but not all of it (e.g. in react agent)</span>
                <span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">final_text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>  <span class="c1"># final message</span>
                <span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatErrorEvent</span><span class="p">(</span><span class="n">exception</span><span class="o">=</span><span class="n">e</span><span class="p">))</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="o">=</span> <span class="n">e</span>

            <span class="c1"># This act as is_done events for any consumers waiting</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">is_function_not_none_thread_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>

            <span class="c1"># force the queue reader to see the exception</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">put_in_queue</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
            <span class="k">raise</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatEndEvent</span><span class="p">())</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="c1"># This act as is_done events for any consumers waiting</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_function_not_none_thread_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">on_stream_end_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span><span class="p">:</span>
            <span class="n">on_stream_end_fn</span><span class="p">()</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">awrite_response_to_history</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">on_stream_end_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_async_setup</span><span class="p">()</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">achat_stream</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"achat_stream is None. Cannot asynchronously write to "</span>
                <span class="s2">"history without achat_stream."</span>
            <span class="p">)</span>

        <span class="c1"># try/except to prevent hanging on error</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatStartEvent</span><span class="p">())</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">final_text</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">chat</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">achat_stream</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span> <span class="o">=</span> <span class="n">is_function</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">:</span>
                    <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                        <span class="n">StreamChatDeltaReceivedEvent</span><span class="p">(</span>
                            <span class="n">delta</span><span class="o">=</span><span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">aput_in_queue</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">delta</span><span class="p">)</span>
                <span class="n">final_text</span> <span class="o">+=</span> <span class="n">chat</span><span class="o">.</span><span class="n">delta</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">is_function_false_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># if loop has gone through iteration</span>
                <span class="c1"># NOTE: this is to handle the special case where we consume some of the</span>
                <span class="c1"># chat stream, but not all of it (e.g. in react agent)</span>
                <span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">final_text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>  <span class="c1"># final message</span>
                <span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">chat</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatErrorEvent</span><span class="p">(</span><span class="n">exception</span><span class="o">=</span><span class="n">e</span><span class="p">))</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="o">=</span> <span class="n">e</span>

            <span class="c1"># These act as is_done events for any consumers waiting</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">is_function_false_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>

            <span class="c1"># force the queue reader to see the exception</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aput_in_queue</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
            <span class="k">raise</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">StreamChatEndEvent</span><span class="p">())</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="c1"># These act as is_done events for any consumers waiting</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_function_false_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">new_item_event</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">on_stream_end_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_function</span><span class="p">:</span>
            <span class="n">on_stream_end_fn</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">response_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span> <span class="ow">or</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">delta</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span> <span class="o">+=</span> <span class="n">delta</span>
                <span class="k">yield</span> <span class="n">delta</span>
            <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
                <span class="c1"># Queue is empty, but we're not done yet. Sleep for 0 secs to release the GIL and allow other threads to run.</span>
                <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_response_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_async_setup</span><span class="p">()</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">aqueue</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span> <span class="ow">or</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception</span>

                <span class="k">try</span><span class="p">:</span>
                    <span class="n">delta</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aqueue</span><span class="o">.</span><span class="n">get</span><span class="p">(),</span> <span class="n">timeout</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
                <span class="k">except</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">TimeoutError</span><span class="p">:</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_done</span><span class="p">:</span>
                        <span class="k">break</span>
                    <span class="k">continue</span>
                <span class="k">if</span> <span class="n">delta</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span> <span class="o">+=</span> <span class="n">delta</span>
                    <span class="k">yield</span> <span class="n">delta</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">break</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unformatted_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">print_response_stream</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">token</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aprint_response_stream</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_response_gen</span><span class="p">():</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">token</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BaseChatEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `DispatcherSpanMixin`, `ABC`

Base Chat Engine.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">301</span>
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
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseChatEngine</span><span class="p">(</span><span class="n">DispatcherSpanMixin</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base Chat Engine."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset conversation state."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Main chat interface."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Stream chat interface."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async version of main chat interface."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async version of main chat interface."""</span>

    <span class="k">def</span> <span class="nf">chat_repl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Enter interactive chat REPL."""</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'Type "exit" to exit.</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
        <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">message</span> <span class="o">!=</span> <span class="s2">"exit"</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Assistant: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">streaming_chat_repl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Enter interactive chat REPL with streaming responses."""</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'Type "exit" to exit.</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
        <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">message</span> <span class="o">!=</span> <span class="s2">"exit"</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Assistant: "</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="n">response</span><span class="o">.</span><span class="n">print_response_stream</span><span class="p">()</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

### reset `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.reset "Permanent link")

```
reset() -> None
```

Reset conversation state.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset conversation state."""</span>
</code></pre></div></td></tr></tbody></table>

### chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.chat "Permanent link")

```
chat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None) -> AGENT_CHAT_RESPONSE_TYPE
```

Main chat interface.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Main chat interface."""</span>
</code></pre></div></td></tr></tbody></table>

### stream\_chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.stream_chat "Permanent link")

```
stream_chat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None) -> [StreamingAgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.StreamingAgentChatResponse "llama_index.core.chat_engine.types.StreamingAgentChatResponse")
```

Stream chat interface.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Stream chat interface."""</span>
</code></pre></div></td></tr></tbody></table>

### achat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.achat "Permanent link")

```
achat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None) -> AGENT_CHAT_RESPONSE_TYPE
```

Async version of main chat interface.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async version of main chat interface."""</span>
</code></pre></div></td></tr></tbody></table>

### astream\_chat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.astream_chat "Permanent link")

```
astream_chat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None) -> [StreamingAgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.StreamingAgentChatResponse "llama_index.core.chat_engine.types.StreamingAgentChatResponse")
```

Async version of main chat interface.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async version of main chat interface."""</span>
</code></pre></div></td></tr></tbody></table>

### chat\_repl [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.chat_repl "Permanent link")

```
chat_repl() -> None
```

Enter interactive chat REPL.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">chat_repl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Enter interactive chat REPL."""</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'Type "exit" to exit.</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
    <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">message</span> <span class="o">!=</span> <span class="s2">"exit"</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Assistant: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### streaming\_chat\_repl [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine.streaming_chat_repl "Permanent link")

```
streaming_chat_repl() -> None
```

Enter interactive chat REPL with streaming responses.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">streaming_chat_repl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Enter interactive chat REPL with streaming responses."""</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'Type "exit" to exit.</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
    <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">message</span> <span class="o">!=</span> <span class="s2">"exit"</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Assistant: "</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">print_response_stream</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">message</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Human: "</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ChatMode [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Chat Engine Modes.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatMode</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chat Engine Modes."""</span>

    <span class="n">SIMPLE</span> <span class="o">=</span> <span class="s2">"simple"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `SimpleChatEngine`.</span>

<span class="sd">    Chat with LLM, without making use of a knowledge base.</span>
<span class="sd">    """</span>

    <span class="n">CONDENSE_QUESTION</span> <span class="o">=</span> <span class="s2">"condense_question"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `CondenseQuestionChatEngine`.</span>

<span class="sd">    First generate a standalone question from conversation context and last message,</span>
<span class="sd">    then query the query engine for a response.</span>
<span class="sd">    """</span>

    <span class="n">CONTEXT</span> <span class="o">=</span> <span class="s2">"context"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `ContextChatEngine`.</span>

<span class="sd">    First retrieve text from the index using the user's message, then use the context</span>
<span class="sd">    in the system prompt to generate a response.</span>
<span class="sd">    """</span>

    <span class="n">CONDENSE_PLUS_CONTEXT</span> <span class="o">=</span> <span class="s2">"condense_plus_context"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `CondensePlusContextChatEngine`.</span>

<span class="sd">    First condense a conversation and latest user message to a standalone question.</span>
<span class="sd">    Then build a context for the standalone question from a retriever,</span>
<span class="sd">    Then pass the context along with prompt and user message to LLM to generate a response.</span>
<span class="sd">    """</span>

    <span class="n">REACT</span> <span class="o">=</span> <span class="s2">"react"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `ReActAgent`.</span>

<span class="sd">    Use a ReAct agent loop with query engine tools.</span>
<span class="sd">    """</span>

    <span class="n">OPENAI</span> <span class="o">=</span> <span class="s2">"openai"</span>
<span class="w">    </span><span class="sd">"""Corresponds to `OpenAIAgent`.</span>

<span class="sd">    Use an OpenAI function calling agent loop.</span>

<span class="sd">    NOTE: only works with OpenAI models that support function calling API.</span>
<span class="sd">    """</span>

    <span class="n">BEST</span> <span class="o">=</span> <span class="s2">"best"</span>
<span class="w">    </span><span class="sd">"""Select the best chat engine based on the current LLM.</span>

<span class="sd">    Corresponds to `OpenAIAgent` if using an OpenAI model that supports</span>
<span class="sd">    function calling API, otherwise, corresponds to `ReActAgent`.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

### SIMPLE `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.SIMPLE "Permanent link")

```
SIMPLE = 'simple'
```

Corresponds to `SimpleChatEngine`.

Chat with LLM, without making use of a knowledge base.

### CONDENSE\_QUESTION `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.CONDENSE_QUESTION "Permanent link")

```
CONDENSE_QUESTION = 'condense_question'
```

Corresponds to `CondenseQuestionChatEngine`.

First generate a standalone question from conversation context and last message, then query the query engine for a response.

### CONTEXT `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.CONTEXT "Permanent link")

```
CONTEXT = 'context'
```

Corresponds to `ContextChatEngine`.

First retrieve text from the index using the user's message, then use the context in the system prompt to generate a response.

### CONDENSE\_PLUS\_CONTEXT `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.CONDENSE_PLUS_CONTEXT "Permanent link")

```
CONDENSE_PLUS_CONTEXT = 'condense_plus_context'
```

Corresponds to `CondensePlusContextChatEngine`.

First condense a conversation and latest user message to a standalone question. Then build a context for the standalone question from a retriever, Then pass the context along with prompt and user message to LLM to generate a response.

### REACT `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.REACT "Permanent link")

```
REACT = 'react'
```

Corresponds to `ReActAgent`.

Use a ReAct agent loop with query engine tools.

### OPENAI `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.OPENAI "Permanent link")

```
OPENAI = 'openai'
```

Corresponds to `OpenAIAgent`.

Use an OpenAI function calling agent loop.

NOTE: only works with OpenAI models that support function calling API.

### BEST `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.ChatMode.BEST "Permanent link")

```
BEST = 'best'
```

Select the best chat engine based on the current LLM.

Corresponds to `OpenAIAgent` if using an OpenAI model that supports function calling API, otherwise, corresponds to `ReActAgent`.

is\_function [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.is_function "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

```
is_function(message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")) -> bool
```

Utility for ChatMessage responses from OpenAI models.

Source code in `llama-index-core/llama_index/core/chat_engine/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">is_function</span><span class="p">(</span><span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Utility for ChatMessage responses from OpenAI models."""</span>
    <span class="k">return</span> <span class="s2">"tool_calls"</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/)[Next Simple](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/)
