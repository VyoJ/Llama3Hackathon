Title: Node parser semantic chunking - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/

Markdown Content:
Node parser semantic chunking - LlamaIndex


SemanticChunkingQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/#llama_index.packs.node_parser_semantic_chunking.SemanticChunkingQueryEnginePack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Semantic Chunking Query Engine Pack.

Takes in a list of documents, parses it with semantic embedding chunker, and runs a query engine on the resulting chunks.

Source code in `llama-index-packs/llama-index-packs-node-parser-semantic-chunking/llama_index/packs/node_parser_semantic_chunking/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">202</span>
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
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SemanticChunkingQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Semantic Chunking Query Engine Pack.</span>

<span class="sd">    Takes in a list of documents, parses it with semantic embedding chunker,</span>
<span class="sd">    and runs a query engine on the resulting chunks.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">buffer_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">breakpoint_percentile_threshold</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">95.0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span> <span class="o">=</span> <span class="n">OpenAIEmbedding</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">splitter</span> <span class="o">=</span> <span class="n">SemanticChunker</span><span class="p">(</span>
            <span class="n">buffer_size</span><span class="o">=</span><span class="n">buffer_size</span><span class="p">,</span>
            <span class="n">breakpoint_percentile_threshold</span><span class="o">=</span><span class="n">breakpoint_percentile_threshold</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"splitter"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">splitter</span><span class="p">,</span>
            <span class="s2">"embed_model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/#llama_index.packs.node_parser_semantic_chunking.SemanticChunkingQueryEnginePack.run "Permanent link")

```
run(query: str) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-node-parser-semantic-chunking/llama_index/packs/node_parser_semantic_chunking/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Neo4j query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/neo4j_query_engine/)[Next Ollama query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/)
