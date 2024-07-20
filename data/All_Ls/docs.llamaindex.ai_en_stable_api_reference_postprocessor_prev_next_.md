Title: Prev next - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/

Markdown Content:
Prev next - LlamaIndex


Node PostProcessor module.

PrevNextNodePostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/#llama_index.core.postprocessor.PrevNextNodePostprocessor "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Previous/Next Node post-processor.

Allows users to fetch additional nodes from the document store, based on the relationships of the nodes.

NOTE: this is a beta feature.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `docstore` | `[BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.BaseDocumentStore")` | 
The document store.



 | _required_ |
| `num_nodes` | `int` | 

The number of nodes to return (default: 1)



 | _required_ |
| `mode` | `str` | 

The mode of the post-processor. Can be "previous", "next", or "both.



 | _required_ |

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
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
<span class="normal">222</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PrevNextNodePostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Previous/Next Node post-processor.</span>

<span class="sd">    Allows users to fetch additional nodes from the document store,</span>
<span class="sd">    based on the relationships of the nodes.</span>

<span class="sd">    NOTE: this is a beta feature.</span>

<span class="sd">    Args:</span>
<span class="sd">        docstore (BaseDocumentStore): The document store.</span>
<span class="sd">        num_nodes (int): The number of nodes to return (default: 1)</span>
<span class="sd">        mode (str): The mode of the post-processor.</span>
<span class="sd">            Can be "previous", "next", or "both.</span>

<span class="sd">    """</span>

    <span class="n">docstore</span><span class="p">:</span> <span class="n">BaseDocumentStore</span>
    <span class="n">num_nodes</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">"next"</span><span class="p">)</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"mode"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_validate_mode</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate mode."""</span>
        <span class="k">if</span> <span class="n">v</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"next"</span><span class="p">,</span> <span class="s2">"previous"</span><span class="p">,</span> <span class="s2">"both"</span><span class="p">]:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid mode: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PrevNextNodePostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">all_nodes</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="s2">"previous"</span><span class="p">:</span>
                <span class="n">all_nodes</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
                    <span class="n">get_backward_nodes</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">prev_node_info</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span>
                    <span class="n">node_inserted</span> <span class="o">=</span> <span class="kc">True</span>
                    <span class="n">sorted_nodes</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
                    <span class="k">break</span>
                <span class="c1"># append to current candidate</span>
                <span class="k">elif</span> <span class="n">next_node_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">node_id</span> <span class="o">==</span> <span class="n">next_node_info</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span>
                    <span class="n">node_inserted</span> <span class="o">=</span> <span class="kc">True</span>
                    <span class="n">sorted_nodes</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
                    <span class="k">break</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">node_inserted</span><span class="p">:</span>
                <span class="n">sorted_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">sorted_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Presidio](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/)[Next Rankgpt rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/)
