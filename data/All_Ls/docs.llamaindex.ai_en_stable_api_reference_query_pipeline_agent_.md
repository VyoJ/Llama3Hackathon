Title: Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/

Markdown Content:
Agent - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Agent component.

Abstract class used for type checking.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseAgentComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Agent component.</span>

<span class="sd">    Abstract class used for type checking.</span>

<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

Bases: `BaseAgentComponent`

Function component for agents.

Designed to let users easily modify state.

NOTE: this is now deprecated in favor of using `StatefulFnComponent`.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">151</span>
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
<span class="normal">258</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentFnComponent</span><span class="p">(</span><span class="n">BaseAgentComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Function component for agents.</span>

<span class="sd">    Designed to let users easily modify state.</span>

<span class="sd">    NOTE: this is now deprecated in favor of using `StatefulFnComponent`.</span>

<span class="sd">    """</span>

    <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Function to run."</span><span class="p">)</span>
    <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Async function to run. If not provided, will run `fn`."</span>
    <span class="p">)</span>

    <span class="n">_req_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_opt_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span>
        <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">req_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">opt_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="c1"># determine parameters</span>
        <span class="n">default_req_params</span><span class="p">,</span> <span class="n">default_opt_params</span> <span class="o">=</span> <span class="n">get_parameters</span><span class="p">(</span><span class="n">fn</span><span class="p">)</span>
        <span class="c1"># make sure task and step are part of the list, and remove them from the list</span>
        <span class="k">if</span> <span class="s2">"task"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">default_req_params</span> <span class="ow">or</span> <span class="s2">"state"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">default_req_params</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"AgentFnComponent must have 'task' and 'state' as required parameters"</span>
            <span class="p">)</span>

        <span class="n">default_req_params</span> <span class="o">=</span> <span class="n">default_req_params</span> <span class="o">-</span> <span class="p">{</span><span class="s2">"task"</span><span class="p">,</span> <span class="s2">"state"</span><span class="p">}</span>
        <span class="n">default_opt_params</span> <span class="o">=</span> <span class="n">default_opt_params</span> <span class="o">-</span> <span class="p">{</span><span class="s2">"task"</span><span class="p">,</span> <span class="s2">"state"</span><span class="p">}</span>

        <span class="k">if</span> <span class="n">req_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">req_params</span> <span class="o">=</span> <span class="n">default_req_params</span>
        <span class="k">if</span> <span class="n">opt_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">opt_params</span> <span class="o">=</span> <span class="n">default_opt_params</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span> <span class="o">=</span> <span class="n">req_params</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span> <span class="o">=</span> <span class="n">opt_params</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">fn</span><span class="o">=</span><span class="n">fn</span><span class="p">,</span> <span class="n">async_fn</span><span class="o">=</span><span class="n">async_fn</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="c1"># TODO: implement</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.agent.types</span> <span class="kn">import</span> <span class="n">Task</span>

        <span class="k">if</span> <span class="s2">"task"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'task'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"task"</span><span class="p">],</span> <span class="n">Task</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'task' of type Task"</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"state"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'state'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"state"</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'state' of type dict"</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component outputs."""</span>
        <span class="c1"># NOTE: we override this to do nothing</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">_validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="c1"># if not isinstance(output, dict):</span>
        <span class="c1">#     raise ValueError("Output must be a dictionary")</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="c1"># if not isinstance(output, dict):</span>
            <span class="c1">#     raise ValueError("Output must be a dictionary")</span>
            <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="p">{</span><span class="s2">"task"</span><span class="p">,</span> <span class="s2">"state"</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span><span class="p">},</span>
            <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># output can be anything, overrode validate function</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentFnComponent.input_keys "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentFnComponent.output_keys "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentFnComponent.set_callback_manager "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
<span class="normal">201</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

validate\_component\_outputs [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentFnComponent.validate_component_outputs "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
validate_component_outputs(output: Dict[str, Any]) -> Dict[str, Any]
```

Validate component outputs.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Validate component outputs."""</span>
    <span class="c1"># NOTE: we override this to do nothing</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

Bases: `BaseAgentComponent`

Custom component for agents.

Designed to let users easily modify state.

NOTE: this is now deprecated in favor of using `StatefulFnComponent`.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">261</span>
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
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CustomAgentComponent</span><span class="p">(</span><span class="n">BaseAgentComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Custom component for agents.</span>

<span class="sd">    Designed to let users easily modify state.</span>

<span class="sd">    NOTE: this is now deprecated in favor of using `StatefulFnComponent`.</span>

<span class="sd">    """</span>

    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Callback manager"</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="c1"># TODO: refactor to put this on base class</span>
        <span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sub_query_components</span><span class="p">:</span>
            <span class="n">component</span><span class="o">.</span><span class="n">set_callback_manager</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># NOTE: user can override this method to validate inputs</span>
        <span class="c1"># but we do this by default for convenience</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"This component does not support async run."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Input keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_optional_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Optional input keys dict."""</span>
        <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Output keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>

        <span class="n">input_keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_input_keys</span><span class="o">.</span><span class="n">union</span><span class="p">({</span><span class="s2">"task"</span><span class="p">,</span> <span class="s2">"state"</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="n">input_keys</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_optional_input_keys</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.CustomAgentComponent.input_keys "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.CustomAgentComponent.output_keys "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.CustomAgentComponent.set_callback_manager "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
    <span class="c1"># TODO: refactor to put this on base class</span>
    <span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sub_query_components</span><span class="p">:</span>
        <span class="n">component</span><span class="o">.</span><span class="n">set_callback_manager</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Takes in agent inputs and transforms it into desired outputs.

NOTE: this is now deprecated in favor of using `StatefulFnComponent`.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 44</span>
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
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentInputComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Takes in agent inputs and transforms it into desired outputs.</span>

<span class="sd">    NOTE: this is now deprecated in favor of using `StatefulFnComponent`.</span>

<span class="sd">    """</span>

    <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Function to run."</span><span class="p">)</span>
    <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Async function to run. If not provided, will run `fn`."</span>
    <span class="p">)</span>

    <span class="n">_req_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_opt_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span>
        <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">req_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">opt_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="c1"># determine parameters</span>
        <span class="n">default_req_params</span><span class="p">,</span> <span class="n">default_opt_params</span> <span class="o">=</span> <span class="n">get_parameters</span><span class="p">(</span><span class="n">fn</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">req_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">req_params</span> <span class="o">=</span> <span class="n">default_req_params</span>
        <span class="k">if</span> <span class="n">opt_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">opt_params</span> <span class="o">=</span> <span class="n">default_opt_params</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span> <span class="o">=</span> <span class="n">req_params</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span> <span class="o">=</span> <span class="n">opt_params</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">fn</span><span class="o">=</span><span class="n">fn</span><span class="p">,</span> <span class="n">async_fn</span><span class="o">=</span><span class="n">async_fn</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="c1"># TODO: implement</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.agent.types</span> <span class="kn">import</span> <span class="n">Task</span>

        <span class="k">if</span> <span class="s2">"task"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'task'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"task"</span><span class="p">],</span> <span class="n">Task</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'task' of type Task"</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"state"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'state'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"state"</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'state' of type dict"</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component outputs."""</span>
        <span class="c1"># NOTE: we override this to do nothing</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">_validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Output must be a dictionary"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">output</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Output must be a dictionary"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">output</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="p">{</span><span class="s2">"task"</span><span class="p">,</span> <span class="s2">"state"</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span><span class="p">},</span>
            <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># output can be anything, overrode validate function</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span><span class="nb">set</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentInputComponent.input_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentInputComponent.output_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentInputComponent.set_callback_manager "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

validate\_component\_outputs [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/#llama_index.core.query_pipeline.components.agent.AgentInputComponent.validate_component_outputs "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
validate_component_outputs(output: Dict[str, Any]) -> Dict[str, Any]
```

Validate component outputs.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Validate component outputs."""</span>
    <span class="c1"># NOTE: we override this to do nothing</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Transform](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/)[Next Arg pack](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/arg_pack/)
