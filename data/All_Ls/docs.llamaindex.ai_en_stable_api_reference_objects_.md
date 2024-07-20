Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/objects/

Markdown Content:
Index - LlamaIndex


LlamaIndex objects.

ObjectIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectIndex "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

Bases: `Generic[OT]`

Object index.

Source code in `llama-index-core/llama_index/core/objects/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
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
<span class="normal">262</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ObjectIndex</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">OT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Object index."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="n">BaseIndex</span><span class="p">,</span> <span class="n">object_node_mapping</span><span class="p">:</span> <span class="n">BaseObjectNodeMapping</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span> <span class="o">=</span> <span class="n">object_node_mapping</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseIndex</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Index."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">object_node_mapping</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseObjectNodeMapping</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Object node mapping."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">OT</span><span class="p">],</span>
        <span class="n">object_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseObjectNodeMapping</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">from_node_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">TextNode</span><span class="p">],</span> <span class="n">OT</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">to_node_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">OT</span><span class="p">],</span> <span class="n">TextNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">,</span>
        <span class="o">**</span><span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ObjectIndex"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.objects.utils</span> <span class="kn">import</span> <span class="n">get_object_mapping</span>

        <span class="c1"># pick the best mapping if not provided</span>
        <span class="k">if</span> <span class="n">object_mapping</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">object_mapping</span> <span class="o">=</span> <span class="n">get_object_mapping</span><span class="p">(</span>
                <span class="n">objects</span><span class="p">,</span>
                <span class="n">from_node_fn</span><span class="o">=</span><span class="n">from_node_fn</span><span class="p">,</span>
                <span class="n">to_node_fn</span><span class="o">=</span><span class="n">to_node_fn</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="n">object_mapping</span><span class="o">.</span><span class="n">to_nodes</span><span class="p">(</span><span class="n">objects</span><span class="p">)</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">index_cls</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">index_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">object_mapping</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects_and_index</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">OT</span><span class="p">],</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseIndex</span><span class="p">,</span>
        <span class="n">object_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseObjectNodeMapping</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">from_node_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">TextNode</span><span class="p">],</span> <span class="n">OT</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">to_node_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">OT</span><span class="p">],</span> <span class="n">TextNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ObjectIndex"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.objects.utils</span> <span class="kn">import</span> <span class="n">get_object_mapping</span>

        <span class="c1"># pick the best mapping if not provided</span>
        <span class="k">if</span> <span class="n">object_mapping</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">object_mapping</span> <span class="o">=</span> <span class="n">get_object_mapping</span><span class="p">(</span>
                <span class="n">objects</span><span class="p">,</span>
                <span class="n">from_node_fn</span><span class="o">=</span><span class="n">from_node_fn</span><span class="p">,</span>
                <span class="n">to_node_fn</span><span class="o">=</span><span class="n">to_node_fn</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">object_mapping</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">insert_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="o">.</span><span class="n">add_object</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
        <span class="n">node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="o">.</span><span class="n">to_node</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">([</span><span class="n">node</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ObjectRetriever</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ObjectRetriever</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
            <span class="n">object_node_mapping</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_node_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># try to persist object node mapping</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span>
                <span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="o">=</span><span class="n">obj_node_mapping_fname</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="p">(</span><span class="ne">NotImplementedError</span><span class="p">,</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PickleError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="s2">"Unable to persist ObjectNodeMapping. You will need to "</span>
                    <span class="s2">"reconstruct the same object node mapping to build this ObjectIndex"</span>
                <span class="p">),</span>
                <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">object_node_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseObjectNodeMapping</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ObjectIndex"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices</span> <span class="kn">import</span> <span class="n">load_index_from_storage</span>

        <span class="n">storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">)</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">load_index_from_storage</span><span class="p">(</span><span class="n">storage_context</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">object_node_mapping</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">object_node_mapping</span><span class="o">=</span><span class="n">object_node_mapping</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># try to load object_node_mapping</span>
            <span class="c1"># assume SimpleObjectNodeMapping for simplicity as its only subclass</span>
            <span class="c1"># that supports this method</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">object_node_mapping</span> <span class="o">=</span> <span class="n">SimpleObjectNodeMapping</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
                    <span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span>
                    <span class="s2">"Unable to load from persist dir. The object_node_mapping cannot be loaded."</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">object_node_mapping</span><span class="o">=</span><span class="n">object_node_mapping</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### index `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectIndex.index "Permanent link")

```
index: [BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")
```

Index.

### object\_node\_mapping `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectIndex.object_node_mapping "Permanent link")

```
object_node_mapping: BaseObjectNodeMapping
```

Object node mapping.

ObjectRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[ChainableMixin](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "llama_index.core.base.query_pipeline.query.ChainableMixin")`, `Generic[OT]`

Object retriever.

Source code in `llama-index-core/llama_index/core/objects/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
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
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ObjectRetriever</span><span class="p">(</span><span class="n">ChainableMixin</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">OT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Object retriever."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">object_node_mapping</span><span class="p">:</span> <span class="n">BaseObjectNodeMapping</span><span class="p">[</span><span class="n">OT</span><span class="p">],</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span> <span class="o">=</span> <span class="n">object_node_mapping</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Retriever."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">object_node_mapping</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseObjectNodeMapping</span><span class="p">[</span><span class="n">OT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Object node mapping."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">node_postprocessors</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Node postprocessors."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">OT</span><span class="p">]:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="o">.</span><span class="n">from_node</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">OT</span><span class="p">]:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">str_or_query_bundle</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">str_or_query_bundle</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_bundle</span> <span class="o">=</span> <span class="n">str_or_query_bundle</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_node_mapping</span><span class="o">.</span><span class="n">from_node</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""As query component."""</span>
        <span class="k">return</span> <span class="n">ObjectRetrieverComponent</span><span class="p">(</span><span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever.retriever "Permanent link")

```
retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Retriever.

### object\_node\_mapping `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever.object_node_mapping "Permanent link")

```
object_node_mapping: BaseObjectNodeMapping[OT]
```

Object node mapping.

### node\_postprocessors `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever.node_postprocessors "Permanent link")

```
node_postprocessors: List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]
```

Node postprocessors.

SimpleObjectNodeMapping [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleObjectNodeMapping "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseObjectNodeMapping[Any]`

General node mapping that works for any obj.

More specifically, any object with a meaningful string representation.

Source code in `llama-index-core/llama_index/core/objects/base_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
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
<span class="normal">176</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleObjectNodeMapping</span><span class="p">(</span><span class="n">BaseObjectNodeMapping</span><span class="p">[</span><span class="n">Any</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""General node mapping that works for any obj.</span>

<span class="sd">    More specifically, any object with a meaningful string representation.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">objs</span> <span class="o">=</span> <span class="n">objs</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">objs</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">validate_object</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_objs</span> <span class="o">=</span> <span class="p">{</span><span class="nb">hash</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">obj</span><span class="p">)):</span> <span class="n">obj</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">objs</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleObjectNodeMapping"</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">objs</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">obj_node_mapping</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_objs</span>

    <span class="nd">@obj_node_mapping</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">obj_node_mapping</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mapping</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_objs</span> <span class="o">=</span> <span class="n">mapping</span>

    <span class="k">def</span> <span class="nf">_add_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_objs</span><span class="p">[</span><span class="nb">hash</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">obj</span><span class="p">))]</span> <span class="o">=</span> <span class="n">obj</span>

    <span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">obj</span><span class="p">))),</span> <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">obj</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_objs</span><span class="p">[</span><span class="nb">hash</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">))]</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist object node mapping.</span>

<span class="sd">        NOTE: This may fail depending on whether the object types are</span>
<span class="sd">        pickle-able.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
        <span class="n">obj_node_mapping_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">obj_node_mapping_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PickleError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Objs is not pickleable"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleObjectNodeMapping"</span><span class="p">:</span>
        <span class="n">obj_node_mapping_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">obj_node_mapping_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">simple_object_node_mapping</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PickleError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Objs cannot be loaded."</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
        <span class="k">return</span> <span class="n">simple_object_node_mapping</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleObjectNodeMapping.persist "Permanent link")

```
persist(persist_dir: str = DEFAULT_PERSIST_DIR, obj_node_mapping_fname: str = DEFAULT_PERSIST_FNAME) -> None
```

Persist object node mapping.

NOTE: This may fail depending on whether the object types are pickle-able.

Source code in `llama-index-core/llama_index/core/objects/base_node_mapping.py`

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
<span class="normal">162</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
    <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist object node mapping.</span>

<span class="sd">    NOTE: This may fail depending on whether the object types are</span>
<span class="sd">    pickle-able.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">):</span>
        <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
    <span class="n">obj_node_mapping_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">obj_node_mapping_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PickleError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Objs is not pickleable"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
</code></pre></div></td></tr></tbody></table>

SQLTableNodeMapping [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableNodeMapping "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseObjectNodeMapping[[SQLTableSchema](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableSchema "llama_index.core.objects.table_node_mapping.SQLTableSchema")]`

SQL Table node mapping.

Source code in `llama-index-core/llama_index/core/objects/table_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
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
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLTableNodeMapping</span><span class="p">(</span><span class="n">BaseObjectNodeMapping</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""SQL Table node mapping."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sql_database</span><span class="p">:</span> <span class="n">SQLDatabase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span> <span class="o">=</span> <span class="n">sql_database</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">objs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">],</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SQLDatabase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseObjectNodeMapping"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize node mapping."""</span>
        <span class="k">if</span> <span class="n">sql_database</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide sql_database"</span><span class="p">)</span>
        <span class="c1"># ignore objs, since we are building from sql_database</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">sql_database</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_add_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">SQLTableSchema</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">SQLTableSchema</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To node."""</span>
        <span class="c1"># taken from existing schema logic</span>
        <span class="n">table_text</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Schema of table </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="s2">"</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">get_single_table_info</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"name"</span><span class="p">:</span> <span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="p">}</span>

        <span class="k">if</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">table_text</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Context of table </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">table_text</span> <span class="o">+=</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span>
            <span class="n">metadata</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span>

        <span class="n">table_identity</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}{</span><span class="n">obj</span><span class="o">.</span><span class="n">context_str</span><span class="si">}</span><span class="s2">"</span>

        <span class="k">return</span> <span class="n">TextNode</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="n">table_identity</span><span class="p">)),</span>
            <span class="n">text</span><span class="o">=</span><span class="n">table_text</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"context"</span><span class="p">],</span>
            <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"context"</span><span class="p">],</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SQLTableSchema</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From node."""</span>
        <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Metadata must be set"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">SQLTableSchema</span><span class="p">(</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">context_str</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"context"</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">obj_node_mapping</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""The mapping data structure between node and object."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Subclasses should implement this!"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="o">...</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist objs."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Subclasses should implement this!"</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SQLTableNodeMapping"</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"This object node mapping does not support persist method."</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### obj\_node\_mapping `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableNodeMapping.obj_node_mapping "Permanent link")

```
obj_node_mapping: Dict[int, Any]
```

The mapping data structure between node and object.

### from\_objects `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableNodeMapping.from_objects "Permanent link")

```
from_objects(objs: Sequence[[SQLTableSchema](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableSchema "llama_index.core.objects.table_node_mapping.SQLTableSchema")], *args: Any, sql_database: Optional[SQLDatabase] = None, **kwargs: Any) -> BaseObjectNodeMapping
```

Initialize node mapping.

Source code in `llama-index-core/llama_index/core/objects/table_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">objs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">SQLTableSchema</span><span class="p">],</span>
    <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="n">sql_database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SQLDatabase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseObjectNodeMapping"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize node mapping."""</span>
    <span class="k">if</span> <span class="n">sql_database</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide sql_database"</span><span class="p">)</span>
    <span class="c1"># ignore objs, since we are building from sql_database</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">sql_database</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableNodeMapping.to_node "Permanent link")

```
to_node(obj: [SQLTableSchema](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableSchema "llama_index.core.objects.table_node_mapping.SQLTableSchema")) -> [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")
```

To node.

Source code in `llama-index-core/llama_index/core/objects/table_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
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
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">SQLTableSchema</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To node."""</span>
    <span class="c1"># taken from existing schema logic</span>
    <span class="n">table_text</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">"Schema of table </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="s2">"</span>
        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_sql_database</span><span class="o">.</span><span class="n">get_single_table_info</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
    <span class="p">)</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"name"</span><span class="p">:</span> <span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="p">}</span>

    <span class="k">if</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">table_text</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Context of table </span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="s2">"</span>
        <span class="n">table_text</span> <span class="o">+=</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">context_str</span>

    <span class="n">table_identity</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">obj</span><span class="o">.</span><span class="n">table_name</span><span class="si">}{</span><span class="n">obj</span><span class="o">.</span><span class="n">context_str</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">return</span> <span class="n">TextNode</span><span class="p">(</span>
        <span class="n">id_</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="n">table_identity</span><span class="p">)),</span>
        <span class="n">text</span><span class="o">=</span><span class="n">table_text</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"context"</span><span class="p">],</span>
        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"context"</span><span class="p">],</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableNodeMapping.persist "Permanent link")

```
persist(persist_dir: str = ..., obj_node_mapping_fname: str = ...) -> None
```

Persist objs.

Source code in `llama-index-core/llama_index/core/objects/table_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span> <span class="n">obj_node_mapping_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="o">...</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist objs."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Subclasses should implement this!"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

SQLTableSchema [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SQLTableSchema "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Lightweight representation of a SQL table.

Source code in `llama-index-core/llama_index/core/objects/table_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SQLTableSchema</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Lightweight representation of a SQL table."""</span>

    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">context_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

SimpleQueryToolNodeMapping [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleQueryToolNodeMapping "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseQueryToolNodeMapping`

Simple query tool mapping.

Source code in `llama-index-core/llama_index/core/objects/tool_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">123</span>
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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleQueryToolNodeMapping</span><span class="p">(</span><span class="n">BaseQueryToolNodeMapping</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple query tool mapping."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">objs</span> <span class="o">=</span> <span class="n">objs</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span> <span class="o">=</span> <span class="p">{</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">tool</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">objs</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">validate_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">QueryEngineTool</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Object must be of type </span><span class="si">{</span><span class="n">QueryEngineTool</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseObjectNodeMapping"</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">objs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_add_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Tool name must be set"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">[</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool</span>

    <span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To node."""</span>
        <span class="k">return</span> <span class="n">convert_tool_to_node</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryEngineTool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From node."""</span>
        <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Metadata must be set"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]]</span>
</code></pre></div></td></tr></tbody></table>

### to\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleQueryToolNodeMapping.to_node "Permanent link")

```
to_node(obj: [QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")) -> [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")
```

To node.

Source code in `llama-index-core/llama_index/core/objects/tool_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">QueryEngineTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To node."""</span>
    <span class="k">return</span> <span class="n">convert_tool_to_node</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

SimpleToolNodeMapping [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleToolNodeMapping "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseToolNodeMapping`

Simple Tool mapping.

In this setup, we assume that the tool name is unique, and that the list of all tools are stored in memory.

Source code in `llama-index-core/llama_index/core/objects/tool_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
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
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleToolNodeMapping</span><span class="p">(</span><span class="n">BaseToolNodeMapping</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Tool mapping.</span>

<span class="sd">    In this setup, we assume that the tool name is unique, and</span>
<span class="sd">    that the list of all tools are stored in memory.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">objs</span> <span class="o">=</span> <span class="n">objs</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span> <span class="o">=</span> <span class="p">{</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">tool</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">objs</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_objects</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">objs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseObjectNodeMapping"</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">objs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_add_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">BaseTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">[</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool</span>

    <span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">BaseTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To node."""</span>
        <span class="k">return</span> <span class="n">convert_tool_to_node</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseTool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From node."""</span>
        <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Metadata must be set"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]]</span>
</code></pre></div></td></tr></tbody></table>

### to\_node [#](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.SimpleToolNodeMapping.to_node "Permanent link")

```
to_node(tool: [BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")) -> [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")
```

To node.

Source code in `llama-index-core/llama_index/core/objects/tool_node_mapping.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">BaseTool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To node."""</span>
    <span class="k">return</span> <span class="n">convert_tool_to_node</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Voyageai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/voyageai_rerank/)[Next Guardrails](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/)
