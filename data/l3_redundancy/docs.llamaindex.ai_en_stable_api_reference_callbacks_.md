Title: Core Callback Classes - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/

Markdown Content:
Core Callback Classes - LlamaIndex


CallbackManager [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`, `ABC`

Callback manager that handles callbacks for events within LlamaIndex.

The callback manager provides a way to call handlers on event starts/ends.

Additionally, the callback manager traces the current stack of events. It does this by using a few key attributes. - trace\_stack - The current stack of events that have not ended yet. When an event ends, it's removed from the stack. Since this is a contextvar, it is unique to each thread/task. - trace\_map - A mapping of event ids to their children events. On the start of events, the bottom of the trace stack is used as the current parent event for the trace map. - trace\_id - A simple name for the current trace, usually denoting the entrypoint (query, index\_construction, insert, etc.)

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `handlers` | `List[[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")]` | 
list of handlers to use.



 | `None` |

Usagewith callback\_manager.event(CBEventType.QUERY) as event: event.on\_start(payload={key, val}) ... event.on\_end(payload={key, val})

Source code in `llama-index-core/llama_index/core/callbacks/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
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
<span class="normal">251</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CallbackManager</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback manager that handles callbacks for events within LlamaIndex.</span>

<span class="sd">    The callback manager provides a way to call handlers on event starts/ends.</span>

<span class="sd">    Additionally, the callback manager traces the current stack of events.</span>
<span class="sd">    It does this by using a few key attributes.</span>
<span class="sd">    - trace_stack - The current stack of events that have not ended yet.</span>
<span class="sd">                    When an event ends, it's removed from the stack.</span>
<span class="sd">                    Since this is a contextvar, it is unique to each</span>
<span class="sd">                    thread/task.</span>
<span class="sd">    - trace_map - A mapping of event ids to their children events.</span>
<span class="sd">                  On the start of events, the bottom of the trace stack</span>
<span class="sd">                  is used as the current parent event for the trace map.</span>
<span class="sd">    - trace_id - A simple name for the current trace, usually denoting the</span>
<span class="sd">                 entrypoint (query, index_construction, insert, etc.)</span>

<span class="sd">    Args:</span>
<span class="sd">        handlers (List[BaseCallbackHandler]): list of handlers to use.</span>

<span class="sd">    Usage:</span>
<span class="sd">        with callback_manager.event(CBEventType.QUERY) as event:</span>
<span class="sd">            event.on_start(payload={key, val})</span>
<span class="sd">            ...</span>
<span class="sd">            event.on_end(payload={key, val})</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handlers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseCallbackHandler</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize the manager with a list of handlers."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core</span> <span class="kn">import</span> <span class="n">global_handler</span>

        <span class="n">handlers</span> <span class="o">=</span> <span class="n">handlers</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="c1"># add eval handlers based on global defaults</span>
        <span class="k">if</span> <span class="n">global_handler</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">new_handler</span> <span class="o">=</span> <span class="n">global_handler</span>
            <span class="c1"># go through existing handlers, check if any are same type as new handler</span>
            <span class="c1"># if so, error</span>
            <span class="k">for</span> <span class="n">existing_handler</span> <span class="ow">in</span> <span class="n">handlers</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">existing_handler</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_handler</span><span class="p">)):</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"Cannot add two handlers of the same type "</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">new_handler</span><span class="p">)</span><span class="si">}</span><span class="s2"> to the callback manager."</span>
                    <span class="p">)</span>
            <span class="n">handlers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_handler</span><span class="p">)</span>

        <span class="c1"># if we passed in no handlers, use the global default</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">handlers</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_reset_trace_events</span><span class="p">()</span>

                <span class="k">for</span> <span class="n">handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">handlers</span><span class="p">:</span>
                    <span class="n">handler</span><span class="o">.</span><span class="n">start_trace</span><span class="p">(</span><span class="n">trace_id</span><span class="o">=</span><span class="n">trace_id</span><span class="p">)</span>

                <span class="n">current_trace_stack_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">trace_id</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">current_trace_stack_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">trace_id</span><span class="p">)</span>

        <span class="n">global_stack_trace_ids</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run when an overall trace is exited."""</span>
        <span class="n">current_trace_stack_ids</span> <span class="o">=</span> <span class="n">global_stack_trace_ids</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">trace_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">current_trace_stack_ids</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_reset_trace_events</span><span class="p">()</span>

            <span class="k">for</span> <span class="n">handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">handlers</span><span class="p">:</span>
                <span class="n">handler</span><span class="o">.</span><span class="n">start_trace</span><span class="p">(</span><span class="n">trace_id</span><span class="o">=</span><span class="n">trace_id</span><span class="p">)</span>

            <span class="n">current_trace_stack_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">trace_id</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">current_trace_stack_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">trace_id</span><span class="p">)</span>

    <span class="n">global_stack_trace_ids</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### end\_trace [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager.end_trace "Permanent link")

```
end_trace(trace_id: Optional[str] = None, trace_map: Optional[Dict[str, List[str]]] = None) -> None
```

Run when an overall trace is exited.

Source code in `llama-index-core/llama_index/core/callbacks/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run when an overall trace is exited."""</span>
    <span class="n">current_trace_stack_ids</span> <span class="o">=</span> <span class="n">global_stack_trace_ids</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">trace_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">current_trace_stack_ids</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">handlers</span><span class="p">:</span>
                <span class="n">handler</span><span class="o">.</span><span class="n">end_trace</span><span class="p">(</span><span class="n">trace_id</span><span class="o">=</span><span class="n">trace_id</span><span class="p">,</span> <span class="n">trace_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">)</span>
            <span class="n">current_trace_stack_ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">global_stack_trace_ids</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">current_trace_stack_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BaseCallbackHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Base callback handler that can be used to track event starts and ends.

Source code in `llama-index-core/llama_index/core/callbacks/base_handler.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
<span class="normal">13</span>
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
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseCallbackHandler</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base callback handler that can be used to track event starts and ends."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_starts_to_ignore</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">],</span>
        <span class="n">event_ends_to_ignore</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the base callback handler."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_starts_to_ignore</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">event_starts_to_ignore</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_ends_to_ignore</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">event_ends_to_ignore</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run when an event starts and return id of event."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run when an event ends."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run when an overall trace is launched."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run when an overall trace is exited."""</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_start `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler.on_event_start "Permanent link")

```
on_event_start(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', parent_id: str = '', **kwargs: Any) -> str
```

Run when an event starts and return id of event.

Source code in `llama-index-core/llama_index/core/callbacks/base_handler.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run when an event starts and return id of event."""</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_end `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler.on_event_end "Permanent link")

```
on_event_end(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', **kwargs: Any) -> None
```

Run when an event ends.

Source code in `llama-index-core/llama_index/core/callbacks/base_handler.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run when an event ends."""</span>
</code></pre></div></td></tr></tbody></table>

### start\_trace `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler.start_trace "Permanent link")

```
start_trace(trace_id: Optional[str] = None) -> None
```

Run when an overall trace is launched.

Source code in `llama-index-core/llama_index/core/callbacks/base_handler.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run when an overall trace is launched."""</span>
</code></pre></div></td></tr></tbody></table>

### end\_trace `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler.end_trace "Permanent link")

```
end_trace(trace_id: Optional[str] = None, trace_map: Optional[Dict[str, List[str]]] = None) -> None
```

Run when an overall trace is exited.

Source code in `llama-index-core/llama_index/core/callbacks/base_handler.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run when an overall trace is exited."""</span>
</code></pre></div></td></tr></tbody></table>

Base schema for callback managers.

CBEvent `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Generic class to store event information.

Source code in `llama-index-core/llama_index/core/callbacks/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">75</span>
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
<span class="k">class</span> <span class="nc">CBEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generic class to store event information."""</span>

    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">time</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="k">def</span> <span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init time and id if needed."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">time</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="n">TIMESTAMP_FORMAT</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

CBEventType [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Callback manager event types.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `CHUNKING` |  | 
Logs for the before and after of text splitting.



 |
| `NODE_PARSING` |  | 

Logs for the documents and the nodes that they are parsed into.



 |
| `EMBEDDING` |  | 

Logs for the number of texts embedded.



 |
| `LLM` |  | 

Logs for the template and response of LLM calls.



 |
| `QUERY` |  | 

Keeps track of the start and end of each query.



 |
| `RETRIEVE` |  | 

Logs for the nodes retrieved for a query.



 |
| `SYNTHESIZE` |  | 

Logs for the result for synthesize calls.



 |
| `TREE` |  | 

Logs for the summary and level of summaries generated.



 |
| `SUB_QUESTION` |  | 

Logs for a generated sub question and answer.



 |

Source code in `llama-index-core/llama_index/core/callbacks/schema.py`

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
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CBEventType</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback manager event types.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        CHUNKING: Logs for the before and after of text splitting.</span>
<span class="sd">        NODE_PARSING: Logs for the documents and the nodes that they are parsed into.</span>
<span class="sd">        EMBEDDING: Logs for the number of texts embedded.</span>
<span class="sd">        LLM: Logs for the template and response of LLM calls.</span>
<span class="sd">        QUERY: Keeps track of the start and end of each query.</span>
<span class="sd">        RETRIEVE: Logs for the nodes retrieved for a query.</span>
<span class="sd">        SYNTHESIZE: Logs for the result for synthesize calls.</span>
<span class="sd">        TREE: Logs for the summary and level of summaries generated.</span>
<span class="sd">        SUB_QUESTION: Logs for a generated sub question and answer.</span>
<span class="sd">    """</span>

    <span class="n">CHUNKING</span> <span class="o">=</span> <span class="s2">"chunking"</span>
    <span class="n">NODE_PARSING</span> <span class="o">=</span> <span class="s2">"node_parsing"</span>
    <span class="n">EMBEDDING</span> <span class="o">=</span> <span class="s2">"embedding"</span>
    <span class="n">LLM</span> <span class="o">=</span> <span class="s2">"llm"</span>
    <span class="n">QUERY</span> <span class="o">=</span> <span class="s2">"query"</span>
    <span class="n">RETRIEVE</span> <span class="o">=</span> <span class="s2">"retrieve"</span>
    <span class="n">SYNTHESIZE</span> <span class="o">=</span> <span class="s2">"synthesize"</span>
    <span class="n">TREE</span> <span class="o">=</span> <span class="s2">"tree"</span>
    <span class="n">SUB_QUESTION</span> <span class="o">=</span> <span class="s2">"sub_question"</span>
    <span class="n">TEMPLATING</span> <span class="o">=</span> <span class="s2">"templating"</span>
    <span class="n">FUNCTION_CALL</span> <span class="o">=</span> <span class="s2">"function_call"</span>
    <span class="n">RERANKING</span> <span class="o">=</span> <span class="s2">"reranking"</span>
    <span class="n">EXCEPTION</span> <span class="o">=</span> <span class="s2">"exception"</span>
    <span class="n">AGENT_STEP</span> <span class="o">=</span> <span class="s2">"agent_step"</span>
</code></pre></div></td></tr></tbody></table>

EventPayload [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.EventPayload "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Source code in `llama-index-core/llama_index/core/callbacks/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">46</span>
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
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EventPayload</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
    <span class="n">DOCUMENTS</span> <span class="o">=</span> <span class="s2">"documents"</span>  <span class="c1"># list of documents before parsing</span>
    <span class="n">CHUNKS</span> <span class="o">=</span> <span class="s2">"chunks"</span>  <span class="c1"># list of text chunks</span>
    <span class="n">NODES</span> <span class="o">=</span> <span class="s2">"nodes"</span>  <span class="c1"># list of nodes</span>
    <span class="n">PROMPT</span> <span class="o">=</span> <span class="s2">"formatted_prompt"</span>  <span class="c1"># formatted prompt sent to LLM</span>
    <span class="n">MESSAGES</span> <span class="o">=</span> <span class="s2">"messages"</span>  <span class="c1"># list of messages sent to LLM</span>
    <span class="n">COMPLETION</span> <span class="o">=</span> <span class="s2">"completion"</span>  <span class="c1"># completion from LLM</span>
    <span class="n">RESPONSE</span> <span class="o">=</span> <span class="s2">"response"</span>  <span class="c1"># message response from LLM</span>
    <span class="n">QUERY_STR</span> <span class="o">=</span> <span class="s2">"query_str"</span>  <span class="c1"># query used for query engine</span>
    <span class="n">SUB_QUESTION</span> <span class="o">=</span> <span class="s2">"sub_question"</span>  <span class="c1"># a sub question &amp; answer + sources</span>
    <span class="n">EMBEDDINGS</span> <span class="o">=</span> <span class="s2">"embeddings"</span>  <span class="c1"># list of embeddings</span>
    <span class="n">TOP_K</span> <span class="o">=</span> <span class="s2">"top_k"</span>  <span class="c1"># top k nodes retrieved</span>
    <span class="n">ADDITIONAL_KWARGS</span> <span class="o">=</span> <span class="s2">"additional_kwargs"</span>  <span class="c1"># additional kwargs for event call</span>
    <span class="n">SERIALIZED</span> <span class="o">=</span> <span class="s2">"serialized"</span>  <span class="c1"># serialized object for event caller</span>
    <span class="n">FUNCTION_CALL</span> <span class="o">=</span> <span class="s2">"function_call"</span>  <span class="c1"># function call for the LLM</span>
    <span class="n">FUNCTION_OUTPUT</span> <span class="o">=</span> <span class="s2">"function_call_response"</span>  <span class="c1"># function call output</span>
    <span class="n">TOOL</span> <span class="o">=</span> <span class="s2">"tool"</span>  <span class="c1"># tool used in LLM call</span>
    <span class="n">MODEL_NAME</span> <span class="o">=</span> <span class="s2">"model_name"</span>  <span class="c1"># model name used in an event</span>
    <span class="n">TEMPLATE</span> <span class="o">=</span> <span class="s2">"template"</span>  <span class="c1"># template used in LLM call</span>
    <span class="n">TEMPLATE_VARS</span> <span class="o">=</span> <span class="s2">"template_vars"</span>  <span class="c1"># template variables used in LLM call</span>
    <span class="n">SYSTEM_PROMPT</span> <span class="o">=</span> <span class="s2">"system_prompt"</span>  <span class="c1"># system prompt used in LLM call</span>
    <span class="n">QUERY_WRAPPER_PROMPT</span> <span class="o">=</span> <span class="s2">"query_wrapper_prompt"</span>  <span class="c1"># query wrapper prompt used in LLM</span>
    <span class="n">EXCEPTION</span> <span class="o">=</span> <span class="s2">"exception"</span>  <span class="c1"># exception raised in an event</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Honeyhive](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/)[Next Langfuse](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/langfuse/)
