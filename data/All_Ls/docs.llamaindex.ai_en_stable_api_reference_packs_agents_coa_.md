Title: Agents coa - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/

Markdown Content:
Agents coa - LlamaIndex


CoAAgentPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Chain-of-abstraction Agent Pack.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tools` | `List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")]` | 
List of tools to use.



 | _required_ |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

LLM to use. Defaults to gpt-4.



 | `None` |

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
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
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CoAAgentPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chain-of-abstraction Agent Pack.</span>

<span class="sd">    Args:</span>
<span class="sd">        tools (List[BaseTool]): List of tools to use.</span>
<span class="sd">        llm (Optional[LLM]): LLM to use. Defaults to gpt-4.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">agent_worker_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">agent_runner_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span> <span class="o">=</span> <span class="n">CoAAgentWorker</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="o">**</span><span class="p">(</span><span class="n">agent_worker_kwargs</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">AgentRunner</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="o">**</span><span class="p">(</span><span class="n">agent_runner_kwargs</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"callback_manager"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
            <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"callback_manager"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">,</span>
        <span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

CoAAgentWorker [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.BaseAgentWorker "llama_index.core.agent.types.BaseAgentWorker")`

Chain-of-abstraction Agent Worker.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">275</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CoAAgentWorker</span><span class="p">(</span><span class="n">BaseAgentWorker</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chain-of-abstraction Agent Worker."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">reasoning_prompt_template</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">refine_reasoning_prompt_template</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">BaseOutputParser</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>

        <span class="k">if</span> <span class="n">tools</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">tool_retriever</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Either tools or tool_retriever must be provided."</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tool_retriever</span> <span class="o">=</span> <span class="n">tool_retriever</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_prompt_template</span> <span class="o">=</span> <span class="n">reasoning_prompt_template</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">refine_reasoning_prompt_template</span> <span class="o">=</span> <span class="n">refine_reasoning_prompt_template</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reasoning_prompt_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_reasoning_prompt_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CoAAgentWorker"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convenience constructor method from set of of BaseTools (Optional).</span>

<span class="sd">        Returns:</span>
<span class="sd">            LLMCompilerAgentWorker: the LLMCompilerAgentWorker instance</span>

<span class="sd">        """</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="n">reasoning_prompt_template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">reasoning_prompt_template</span> <span class="ow">or</span> <span class="n">REASONING_PROMPT_TEMPALTE</span>
        <span class="p">)</span>
        <span class="n">refine_reasoning_prompt_template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">refine_reasoning_prompt_template</span> <span class="ow">or</span> <span class="n">REFINE_REASONING_PROMPT_TEMPALTE</span>
        <span class="p">)</span>
        <span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span> <span class="ow">or</span> <span class="n">ChainOfAbstractionParser</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">llm</span><span class="p">,</span>
            <span class="n">reasoning_prompt_template</span><span class="p">,</span>
            <span class="n">refine_reasoning_prompt_template</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize step from task."""</span>
        <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># temporary memory for new messages</span>
        <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

        <span class="c1"># put current history in new memory</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
            <span class="n">new_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

        <span class="c1"># initialize task state</span>
        <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
            <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
            <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
            <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
            <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
            <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"prev_reasoning"</span><span class="p">:</span> <span class="s2">""</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_retriever</span><span class="p">:</span>
            <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tools</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
        <span class="n">tools_by_name</span> <span class="o">=</span> <span class="p">{</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">tool</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">}</span>
        <span class="n">tools_strs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool</span><span class="p">,</span> <span class="n">FunctionTool</span><span class="p">):</span>
                <span class="n">description</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span>
                <span class="c1"># remove function def, we will make our own</span>
                <span class="k">if</span> <span class="s2">"def "</span> <span class="ow">in</span> <span class="n">description</span><span class="p">:</span>
                    <span class="n">description</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">description</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)[</span><span class="mi">1</span><span class="p">:])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">description</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span>

            <span class="n">tool_str</span> <span class="o">=</span> <span class="n">json_schema_to_python</span><span class="p">(</span>
                <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">fn_schema_str</span><span class="p">,</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span>
            <span class="p">)</span>
            <span class="n">tools_strs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool_str</span><span class="p">)</span>

        <span class="n">prev_reasoning</span> <span class="o">=</span> <span class="n">step</span><span class="o">.</span><span class="n">step_state</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"prev_reasoning"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

        <span class="c1"># show available functions if first step</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">prev_reasoning</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">""</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">tool_str</span> <span class="ow">in</span> <span class="n">tools_strs</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="n">tool_str</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">prev_reasoning</span><span class="p">:</span>
            <span class="c1"># get the reasoning prompt</span>
            <span class="n">reasoning_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reasoning_prompt_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">functions</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tools_strs</span><span class="p">),</span> <span class="n">question</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">input</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># get the refine reasoning prompt</span>
            <span class="n">reasoning_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">refine_reasoning_prompt_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">question</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">input</span><span class="p">,</span> <span class="n">prev_reasoning</span><span class="o">=</span><span class="n">prev_reasoning</span>
            <span class="p">)</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="n">reasoning_message</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">reasoning_prompt</span><span class="p">)</span>
        <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">reasoning_message</span><span class="p">)</span>

        <span class="c1"># run the reasoning prompt</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="c1"># print the chain of abstraction if first step</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">prev_reasoning</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">""</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>

        <span class="c1"># parse the output, run functions</span>
        <span class="n">parsed_response</span><span class="p">,</span> <span class="n">tool_sources</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">aparse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">tools_by_name</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tool_sources</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">prev_reasoning</span><span class="p">:</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="c1"># only add to memory when we are done</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">parsed_response</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">TaskStep</span><span class="p">(</span>
                    <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
                    <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
                    <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
                    <span class="n">step_state</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"prev_reasoning"</span><span class="p">:</span> <span class="n">parsed_response</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">]</span>

        <span class="n">agent_response</span> <span class="o">=</span> <span class="n">AgentChatResponse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="n">parsed_response</span><span class="p">,</span> <span class="n">sources</span><span class="o">=</span><span class="n">tool_sources</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">TaskStepOutput</span><span class="p">(</span>
            <span class="n">output</span><span class="o">=</span><span class="n">agent_response</span><span class="p">,</span>
            <span class="n">task_step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span>
            <span class="n">is_last</span><span class="o">=</span><span class="n">is_done</span><span class="p">,</span>
            <span class="n">next_steps</span><span class="o">=</span><span class="n">new_steps</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">arun_step</span><span class="p">(</span><span class="n">step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (async)."""</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (stream)."""</span>
        <span class="c1"># Streaming isn't really possible, because we need the full response to know if we are done</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (async stream)."""</span>
        <span class="c1"># Streaming isn't really possible, because we need the full response to know if we are done</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
        <span class="c1"># add new messages to memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">())</span>
        <span class="c1"># reset new memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.from_tools "Permanent link")

```
from_tools(tools: Optional[Sequence[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, tool_retriever: Optional[[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, reasoning_prompt_template: Optional[str] = None, refine_reasoning_prompt_template: Optional[str] = None, output_parser: Optional[[BaseOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/#llama_index.core.types.BaseOutputParser "llama_index.core.output_parsers.base.BaseOutputParser")] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, verbose: bool = False, **kwargs: Any) -> [CoAAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker "llama_index.packs.agents_coa.step.CoAAgentWorker")
```

Convenience constructor method from set of of BaseTools (Optional).

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `LLMCompilerAgentWorker` | `[CoAAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker "llama_index.packs.agents_coa.step.CoAAgentWorker")` | 
the LLMCompilerAgentWorker instance



 |

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 74</span>
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
<span class="normal">114</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">reasoning_prompt_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">refine_reasoning_prompt_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CoAAgentWorker"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convenience constructor method from set of of BaseTools (Optional).</span>

<span class="sd">    Returns:</span>
<span class="sd">        LLMCompilerAgentWorker: the LLMCompilerAgentWorker instance</span>

<span class="sd">    """</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="n">reasoning_prompt_template</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">reasoning_prompt_template</span> <span class="ow">or</span> <span class="n">REASONING_PROMPT_TEMPALTE</span>
    <span class="p">)</span>
    <span class="n">refine_reasoning_prompt_template</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">refine_reasoning_prompt_template</span> <span class="ow">or</span> <span class="n">REFINE_REASONING_PROMPT_TEMPALTE</span>
    <span class="p">)</span>
    <span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span> <span class="ow">or</span> <span class="n">ChainOfAbstractionParser</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">llm</span><span class="p">,</span>
        <span class="n">reasoning_prompt_template</span><span class="p">,</span>
        <span class="n">refine_reasoning_prompt_template</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">,</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### initialize\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.initialize_step "Permanent link")

```
initialize_step(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep")
```

Initialize step from task.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

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
<span class="normal">139</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize step from task."""</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># temporary memory for new messages</span>
    <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

    <span class="c1"># put current history in new memory</span>
    <span class="n">messages</span> <span class="o">=</span> <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
        <span class="n">new_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="c1"># initialize task state</span>
    <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
        <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
        <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
        <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
        <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
        <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"prev_reasoning"</span><span class="p">:</span> <span class="s2">""</span><span class="p">},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_tools [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.get_tools "Permanent link")

```
get_tools(query_str: str) -> List[[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")]
```

Get tools.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get tools."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_retriever</span><span class="p">:</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### run\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.run_step "Permanent link")

```
run_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step."""</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">arun_step</span><span class="p">(</span><span class="n">step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="o">=</span><span class="n">task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### arun\_step `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.arun_step "Permanent link")

```
arun_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (async).

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (async)."""</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### stream\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.stream_step "Permanent link")

```
stream_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (stream).

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (stream)."""</span>
    <span class="c1"># Streaming isn't really possible, because we need the full response to know if we are done</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### astream\_step `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.astream_step "Permanent link")

```
astream_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (async stream).

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">astream_step</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (async stream)."""</span>
    <span class="c1"># Streaming isn't really possible, because we need the full response to know if we are done</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### finalize\_task [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/#llama_index.packs.agents_coa.CoAAgentWorker.finalize_task "Permanent link")

```
finalize_task(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> None
```

Finalize task, after all the steps are completed.

Source code in `llama-index-packs/llama-index-packs-agents-coa/llama_index/packs/agents_coa/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
    <span class="c1"># add new messages to memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">())</span>
    <span class="c1"># reset new memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Agent search retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/agent_search_retriever/)[Next Agents lats](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/)
