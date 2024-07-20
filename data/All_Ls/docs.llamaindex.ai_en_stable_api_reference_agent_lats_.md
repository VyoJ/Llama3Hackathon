Title: Lats - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/

Markdown Content:
Lats - LlamaIndex


LATSAgentWorker [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/#llama_index.agent.lats.LATSAgentWorker "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[CustomSimpleAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.CustomSimpleAgentWorker "llama_index.core.agent.CustomSimpleAgentWorker")`

Agent worker that performs a step of Language Agent Tree Search.

Source paper: https://arxiv.org/pdf/2310.04406v2.pdf.

Continues iterating until there's no errors / task is done.

Source code in `llama-index-integrations/agent/llama-index-agent-lats/llama_index/agent/lats/step.py`

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
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LATSAgentWorker</span><span class="p">(</span><span class="n">CustomSimpleAgentWorker</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Agent worker that performs a step of Language Agent Tree Search.</span>

<span class="sd">    Source paper: https://arxiv.org/pdf/2310.04406v2.pdf.</span>

<span class="sd">    Continues iterating until there's no errors / task is done.</span>

<span class="sd">    """</span>

    <span class="n">num_expansions</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Number of expansions to do."</span><span class="p">)</span>
    <span class="n">reflection_prompt</span><span class="p">:</span> <span class="n">PromptTemplate</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Reflection prompt."</span><span class="p">)</span>
    <span class="n">candiate_expansion_prompt</span><span class="p">:</span> <span class="n">PromptTemplate</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Candidate expansion prompt."</span>
    <span class="p">)</span>
    <span class="n">max_rollouts</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Max rollouts. By default, -1 means that we keep going until the first solution is found."</span>
        <span class="p">),</span>
    <span class="p">)</span>

    <span class="n">chat_formatter</span><span class="p">:</span> <span class="n">ReActChatFormatter</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">ReActChatFormatter</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Chat formatter."</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_expansions</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">max_rollouts</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">reflection_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">candiate_expansion_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># validate that all tools are query engine tools</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">num_expansions</span><span class="o">=</span><span class="n">num_expansions</span><span class="p">,</span>
            <span class="n">max_rollouts</span><span class="o">=</span><span class="n">max_rollouts</span><span class="p">,</span>
            <span class="n">reflection_prompt</span><span class="o">=</span><span class="n">reflection_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_REFLECTION_PROMPT</span><span class="p">,</span>
            <span class="n">candiate_expansion_prompt</span><span class="o">=</span><span class="n">candiate_expansion_prompt</span>
            <span class="ow">or</span> <span class="n">DEFAULT_CANDIDATES_PROMPT</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_initialize_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Initialize state."""</span>
        <span class="c1"># initialize root node</span>
        <span class="n">root_node</span> <span class="o">=</span> <span class="n">SearchNode</span><span class="p">(</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="p">[</span><span class="n">ObservationReasoningStep</span><span class="p">(</span><span class="n">observation</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)],</span>
            <span class="n">evaluation</span><span class="o">=</span><span class="n">Evaluation</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span>  <span class="c1"># evaluation for root node is blank</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"count"</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">"solution_queue"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"root_node"</span><span class="p">:</span> <span class="n">root_node</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_candidate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">SearchNode</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Generate candidate for a given node.</span>

<span class="sd">        Generically we sample the action space to generate new candidate nodes.</span>

<span class="sd">        Practically since we're using a ReAct powered agent, this means</span>
<span class="sd">        using generating a ReAct trajectory, running a tool.</span>

<span class="sd">        """</span>
        <span class="n">output_parser</span> <span class="o">=</span> <span class="n">ReActOutputParser</span><span class="p">()</span>
        <span class="c1"># format react prompt</span>
        <span class="n">formatted_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_formatter</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">(),</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">current_reasoning</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="c1"># run LLM</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">formatted_prompt</span><span class="p">)</span>
        <span class="c1"># parse output into reasoning step</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">ResponseReasoningStep</span><span class="p">(</span>
                <span class="n">thought</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Encountered an error parsing: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># get response or run tool</span>
        <span class="k">if</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">is_done</span><span class="p">:</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ResponseReasoningStep</span><span class="p">,</span> <span class="n">reasoning_step</span><span class="p">)</span>
            <span class="n">current_reasoning</span> <span class="o">=</span> <span class="p">[</span><span class="n">reasoning_step</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ActionReasoningStep</span><span class="p">,</span> <span class="n">reasoning_step</span><span class="p">)</span>
            <span class="n">tool_selection</span> <span class="o">=</span> <span class="n">ToolSelection</span><span class="p">(</span>
                <span class="n">tool_id</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="p">,</span>
                <span class="n">tool_name</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="p">,</span>
                <span class="n">tool_kwargs</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">tool_output</span> <span class="o">=</span> <span class="k">await</span> <span class="n">acall_tool_with_selection</span><span class="p">(</span>
                    <span class="n">tool_selection</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">verbose</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">tool_output</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Encountered error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="n">observation_step</span> <span class="o">=</span> <span class="n">ObservationReasoningStep</span><span class="p">(</span><span class="n">observation</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">))</span>
            <span class="n">current_reasoning</span> <span class="o">=</span> <span class="p">[</span><span class="n">reasoning_step</span><span class="p">,</span> <span class="n">observation_step</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">current_reasoning</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_node</span><span class="p">:</span> <span class="n">SearchNode</span><span class="p">,</span>
        <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span>
        <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluate."""</span>
        <span class="n">all_reasoning</span> <span class="o">=</span> <span class="n">cur_node</span><span class="o">.</span><span class="n">current_reasoning</span> <span class="o">+</span> <span class="n">current_reasoning</span>
        <span class="n">history_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">s</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">all_reasoning</span><span class="p">])</span>
        <span class="n">evaluation</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">astructured_predict</span><span class="p">(</span>
            <span class="n">Evaluation</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reflection_prompt</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span>
            <span class="n">conversation_history</span><span class="o">=</span><span class="n">history_str</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; Evaluation for input </span><span class="si">{</span><span class="nb">input</span><span class="si">}</span><span class="se">\n</span><span class="s2">: </span><span class="si">{</span><span class="n">evaluation</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">evaluation</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_get_next_candidates</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_node</span><span class="p">:</span> <span class="n">SearchNode</span><span class="p">,</span>
        <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get next candidates."""</span>
        <span class="c1"># get candidates</span>
        <span class="n">history_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">s</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">cur_node</span><span class="o">.</span><span class="n">current_reasoning</span><span class="p">])</span>

        <span class="n">candidates</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">astructured_predict</span><span class="p">(</span>
            <span class="n">Candidates</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">candiate_expansion_prompt</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span>
            <span class="n">conversation_history</span><span class="o">=</span><span class="n">history_str</span><span class="p">,</span>
            <span class="n">num_candidates</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">candidate_strs</span> <span class="o">=</span> <span class="n">candidates</span><span class="o">.</span><span class="n">candidates</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Got candidates: </span><span class="si">{</span><span class="n">candidate_strs</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="c1"># ensure we have the right number of candidates</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">candidate_strs</span><span class="p">)</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">(</span><span class="n">candidate_strs</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">)[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">candidate_strs</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_expansions</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_update_state</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">SearchNode</span><span class="p">,</span>
        <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span>
        <span class="n">evaluation</span><span class="p">:</span> <span class="n">Evaluation</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SearchNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update state."""</span>
        <span class="c1"># create child node</span>
        <span class="n">new_node</span> <span class="o">=</span> <span class="n">SearchNode</span><span class="p">(</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">current_reasoning</span> <span class="o">+</span> <span class="n">current_reasoning</span><span class="p">,</span>
            <span class="n">parent</span><span class="o">=</span><span class="n">node</span><span class="p">,</span>
            <span class="n">children</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">evaluation</span><span class="o">=</span><span class="n">evaluation</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">node</span><span class="o">.</span><span class="n">children</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_node</span><span class="p">)</span>

        <span class="c1"># backpropagate the reward</span>
        <span class="n">new_node</span><span class="o">.</span><span class="n">backpropagate</span><span class="p">(</span><span class="n">evaluation</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">new_node</span>

    <span class="k">def</span> <span class="nf">_run_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">AgentChatResponse</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run step.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Tuple of (agent_response, is_done)</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="nb">input</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">AgentChatResponse</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run step.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Tuple of (agent_response, is_done)</span>

<span class="sd">        """</span>
        <span class="n">root_node</span> <span class="o">=</span> <span class="n">state</span><span class="p">[</span><span class="s2">"root_node"</span><span class="p">]</span>
        <span class="n">cur_node</span> <span class="o">=</span> <span class="n">root_node</span><span class="o">.</span><span class="n">get_best_leaf</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; Selecting node to expand: </span><span class="si">{</span><span class="n">cur_node</span><span class="o">.</span><span class="n">answer</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span>
            <span class="p">)</span>

        <span class="c1"># expand the given node, generate n candidate nodes</span>
        <span class="n">new_candidates</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_next_candidates</span><span class="p">(</span>
            <span class="n">cur_node</span><span class="p">,</span>
            <span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">candidate</span> <span class="ow">in</span> <span class="n">new_candidates</span><span class="p">:</span>
            <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_update_state</span><span class="p">(</span>
                    <span class="n">cur_node</span><span class="p">,</span>
                    <span class="p">[</span><span class="n">ObservationReasoningStep</span><span class="p">(</span><span class="n">observation</span><span class="o">=</span><span class="n">candidate</span><span class="p">)],</span>
                    <span class="n">Evaluation</span><span class="p">(</span><span class="n">score</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span>  <span class="c1"># evaluation for candidate node is blank</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="c1"># expand the given node, generate n candidates</span>
        <span class="c1"># for each candidate, run tool, get response</span>

        <span class="n">solution_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SearchNode</span><span class="p">]</span> <span class="o">=</span> <span class="n">state</span><span class="p">[</span><span class="s2">"solution_queue"</span><span class="p">]</span>

        <span class="c1"># first, generate the candidates</span>
        <span class="n">candidate_jobs</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_arun_candidate</span><span class="p">(</span><span class="n">new_node</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span> <span class="k">for</span> <span class="n">new_node</span> <span class="ow">in</span> <span class="n">new_nodes</span>
        <span class="p">]</span>
        <span class="n">all_new_reasoning_steps</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">candidate_jobs</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">new_reasoning_steps</span> <span class="ow">in</span> <span class="n">all_new_reasoning_steps</span><span class="p">:</span>
                <span class="n">out_txt</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">s</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">new_reasoning_steps</span><span class="p">])</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Generated new reasoning step: </span><span class="si">{</span><span class="n">out_txt</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
        <span class="c1"># then, evaluate the candidates</span>
        <span class="n">eval_jobs</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_aevaluate</span><span class="p">(</span><span class="n">new_node</span><span class="p">,</span> <span class="n">new_reasoning_steps</span><span class="p">,</span> <span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">new_node</span><span class="p">,</span> <span class="n">new_reasoning_steps</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">,</span> <span class="n">all_new_reasoning_steps</span><span class="p">)</span>
        <span class="p">]</span>
        <span class="n">evaluations</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">eval_jobs</span><span class="p">)</span>
        <span class="c1"># then, update the state</span>
        <span class="k">for</span> <span class="n">new_reasoning_steps</span><span class="p">,</span> <span class="n">cur_new_node</span><span class="p">,</span> <span class="n">evaluation</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">all_new_reasoning_steps</span><span class="p">,</span> <span class="n">new_nodes</span><span class="p">,</span> <span class="n">evaluations</span>
        <span class="p">):</span>
            <span class="n">new_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_update_state</span><span class="p">(</span><span class="n">cur_new_node</span><span class="p">,</span> <span class="n">new_reasoning_steps</span><span class="p">,</span> <span class="n">evaluation</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">new_node</span><span class="o">.</span><span class="n">is_done</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"&gt; Found solution node: </span><span class="si">{</span><span class="n">new_node</span><span class="o">.</span><span class="n">answer</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"cyan"</span>
                    <span class="p">)</span>
                <span class="n">solution_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_node</span><span class="p">)</span>

        <span class="c1"># check if done</span>
        <span class="n">state</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_rollouts</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span> <span class="ow">and</span> <span class="n">solution_queue</span><span class="p">:</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_rollouts</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">state</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_rollouts</span><span class="p">:</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="c1"># determine response</span>
        <span class="k">if</span> <span class="n">solution_queue</span><span class="p">:</span>
            <span class="n">best_solution_node</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">solution_queue</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">best_solution_node</span><span class="o">.</span><span class="n">answer</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">"I am still thinking."</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Got final response: </span><span class="si">{</span><span class="n">response</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

        <span class="c1"># return response</span>
        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)),</span> <span class="n">is_done</span>

    <span class="k">def</span> <span class="nf">_finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Finalize task."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Introspective](https://docs.llamaindex.ai/en/stable/api_reference/agent/introspective/)[Next Llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/)
