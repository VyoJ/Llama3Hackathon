Title: Openinference - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/

Markdown Content:
Openinference - LlamaIndex


OpenInferenceCallbackHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/#llama_index.callbacks.openinference.OpenInferenceCallbackHandler "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`

Callback handler for storing generation data in OpenInference format. OpenInference is an open standard for capturing and storing AI model inferences. It enables production LLMapp servers to seamlessly integrate with LLM observability solutions such as Arize and Phoenix.

For more information on the specification, see https://github.com/Arize-ai/open-inference-spec

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-openinference/llama_index/callbacks/openinference/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">159</span>
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
<span class="normal">287</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenInferenceCallbackHandler</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback handler for storing generation data in OpenInference format.</span>
<span class="sd">    OpenInference is an open standard for capturing and storing AI model</span>
<span class="sd">    inferences. It enables production LLMapp servers to seamlessly integrate</span>
<span class="sd">    with LLM observability solutions such as Arize and Phoenix.</span>

<span class="sd">    For more information on the specification, see</span>
<span class="sd">    https://github.com/Arize-ai/open-inference-spec</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">callback</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">List</span><span class="p">[</span><span class="n">QueryData</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeData</span><span class="p">]],</span> <span class="kc">None</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initializes the OpenInferenceCallbackHandler.</span>

<span class="sd">        Args:</span>
<span class="sd">            callback (Optional[Callable[[List[QueryData], List[NodeData]], None]], optional): A</span>
<span class="sd">            callback function that will be called when a query trace is</span>
<span class="sd">            completed, often used for logging or persisting query data.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="p">[],</span> <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="p">[])</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback</span> <span class="o">=</span> <span class="n">callback</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span> <span class="o">=</span> <span class="n">TraceData</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">QueryData</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeData</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">trace_id</span> <span class="o"></span> <span class="s2">"chat"</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span> <span class="o">=</span> <span class="n">TraceData</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">isoformat</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">_generate_random_id</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">trace_id</span> <span class="o"></span> <span class="s2">"chat"</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">node_datas</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span> <span class="o">=</span> <span class="n">TraceData</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_callback</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">payload</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">:</span>
                <span class="n">query_text</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">]</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">query_text</span> <span class="o">=</span> <span class="n">query_text</span>
            <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">prompt</span> <span class="o">:=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">llm_prompt</span> <span class="o">=</span> <span class="n">prompt</span>
                <span class="k">if</span> <span class="n">messages</span> <span class="o">:=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">llm_messages</span> <span class="o">=</span> <span class="p">[</span>
                        <span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">role</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">m</span><span class="o">.</span><span class="n">content</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">messages</span>
                    <span class="p">]</span>
                    <span class="c1"># For chat engines there is no query event and thus the</span>
                    <span class="c1"># query text will be None, in this case we set the query</span>
                    <span class="c1"># text to the last message passed to the LLM</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">query_text</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">query_text</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">content</span>
        <span class="k">return</span> <span class="n">event_id</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">payload</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span>
        <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">]:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
                <span class="n">score</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">score</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">node_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">node_datas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">NodeData</span><span class="p">(</span>
                        <span class="nb">id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">hash</span><span class="p">,</span>
                        <span class="n">node_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">response_text</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">response</span> <span class="o">:=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">ChatResponse</span><span class="p">):</span>
                        <span class="c1"># If the response is of class ChatResponse the string</span>
                        <span class="c1"># representation has the format "&lt;role&gt;: &lt;message&gt;",</span>
                        <span class="c1"># but we want just the message</span>
                        <span class="n">response_text</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">response_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">response_text</span> <span class="o">=</span> <span class="n">response_text</span>
                <span class="k">elif</span> <span class="n">completion</span> <span class="o">:=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">COMPLETION</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">response_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">completion</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_trace_data</span><span class="o">.</span><span class="n">query_data</span><span class="o">.</span><span class="n">query_embedding</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">EMBEDDINGS</span>
            <span class="p">][</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">flush_query_data_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">QueryData</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Clears the query data buffer and returns the data.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[QueryData]: The query data.</span>
<span class="sd">        """</span>
        <span class="n">query_data_buffer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">return</span> <span class="n">query_data_buffer</span>

    <span class="k">def</span> <span class="nf">flush_node_data_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeData</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Clears the node data buffer and returns the data.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[NodeData]: The node data.</span>
<span class="sd">        """</span>
        <span class="n">node_data_buffer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">return</span> <span class="n">node_data_buffer</span>
</code></pre></div></td></tr></tbody></table>

### flush\_query\_data\_buffer [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/#llama_index.callbacks.openinference.OpenInferenceCallbackHandler.flush_query_data_buffer "Permanent link")

```
flush_query_data_buffer() -> List[QueryData]
```

Clears the query data buffer and returns the data.

**Returns:**

| Type | Description |
| --- | --- |
| `List[QueryData]` | 
List\[QueryData\]: The query data.



 |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-openinference/llama_index/callbacks/openinference/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">flush_query_data_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">QueryData</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Clears the query data buffer and returns the data.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[QueryData]: The query data.</span>
<span class="sd">    """</span>
    <span class="n">query_data_buffer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_query_data_buffer</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">return</span> <span class="n">query_data_buffer</span>
</code></pre></div></td></tr></tbody></table>

### flush\_node\_data\_buffer [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/#llama_index.callbacks.openinference.OpenInferenceCallbackHandler.flush_node_data_buffer "Permanent link")

```
flush_node_data_buffer() -> List[NodeData]
```

Clears the node data buffer and returns the data.

**Returns:**

| Type | Description |
| --- | --- |
| `List[NodeData]` | 
List\[NodeData\]: The node data.



 |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-openinference/llama_index/callbacks/openinference/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">flush_node_data_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeData</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Clears the node data buffer and returns the data.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[NodeData]: The node data.</span>
<span class="sd">    """</span>
    <span class="n">node_data_buffer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_node_data_buffer</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">return</span> <span class="n">node_data_buffer</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llama debug](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/)[Next Promptlayer](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/)
