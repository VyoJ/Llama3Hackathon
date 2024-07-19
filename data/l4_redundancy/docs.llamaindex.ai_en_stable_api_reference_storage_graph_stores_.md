Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/

Markdown Content:
Index - LlamaIndex


DEFAULT\_PERSIST\_DIR `module-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.DEFAULT_PERSIST_DIR "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
DEFAULT_PERSIST_DIR = './storage'
```

DEFAULT\_PERSIST\_FNAME `module-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.DEFAULT_PERSIST_FNAME "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
DEFAULT_PERSIST_FNAME = 'graph_store.json'
```

GraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `Protocol`

Abstract graph store protocol.

This protocol defines the interface for a graph store, which is responsible for storing and retrieving knowledge graph data.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `[client](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.client "llama_index.core.graph_stores.types.GraphStore.client")` | `Any` | 
Any: The client used to connect to the graph store.



 |
| `[get](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get "llama_index.core.graph_stores.types.GraphStore.get")` | `List[List[str]]` | 

Callable\[\[str\], List\[List\[str\]\]\]: Get triplets for a given subject.



 |
| `[get_rel_map](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get_rel_map "llama_index.core.graph_stores.types.GraphStore.get_rel_map")` | `Dict[str, List[List[str]]]` | 

Callable\[\[Optional\[List\[str\]\], int\], Dict\[str, List\[List\[str\]\]\]\]: Get subjects' rel map in max depth.



 |
| `[upsert_triplet](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.upsert_triplet "llama_index.core.graph_stores.types.GraphStore.upsert_triplet")` | `None` | 

Callable\[\[str, str, str\], None\]: Upsert a triplet.



 |
| `[delete](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.delete "llama_index.core.graph_stores.types.GraphStore.delete")` | `None` | 

Callable\[\[str, str, str\], None\]: Delete a triplet.



 |
| `[persist](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.persist "llama_index.core.graph_stores.types.GraphStore.persist")` | `None` | 

Callable\[\[str, Optional\[fsspec.AbstractFileSystem\]\], None\]: Persist the graph store to a file.



 |
| `[get_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get_schema "llama_index.core.graph_stores.types.GraphStore.get_schema")` | `str` | 

Callable\[\[bool\], str\]: Get the schema of the graph store.



 |

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">201</span>
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
<span class="normal">257</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@runtime_checkable</span>
<span class="k">class</span> <span class="nc">GraphStore</span><span class="p">(</span><span class="n">Protocol</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Abstract graph store protocol.</span>

<span class="sd">    This protocol defines the interface for a graph store, which is responsible</span>
<span class="sd">    for storing and retrieving knowledge graph data.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        client: Any: The client used to connect to the graph store.</span>
<span class="sd">        get: Callable[[str], List[List[str]]]: Get triplets for a given subject.</span>
<span class="sd">        get_rel_map: Callable[[Optional[List[str]], int], Dict[str, List[List[str]]]]:</span>
<span class="sd">            Get subjects' rel map in max depth.</span>
<span class="sd">        upsert_triplet: Callable[[str, str, str], None]: Upsert a triplet.</span>
<span class="sd">        delete: Callable[[str, str, str], None]: Delete a triplet.</span>
<span class="sd">        persist: Callable[[str, Optional[fsspec.AbstractFileSystem]], None]:</span>
<span class="sd">            Persist the graph store to a file.</span>
<span class="sd">        get_schema: Callable[[bool], str]: Get the schema of the graph store.</span>
<span class="sd">    """</span>

    <span class="n">schema</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get triplets."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">subjs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Get depth-aware rel map."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add triplet."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete triplet."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the graph store to a file."""</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the schema of the graph store."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">param_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query the graph store with statement and parameters."""</span>
        <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.client "Permanent link")

```
client: Any
```

Get client.

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get "Permanent link")

```
get(subj: str) -> List[List[str]]
```

Get triplets.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Get triplets."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### get\_rel\_map [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get_rel_map "Permanent link")

```
get_rel_map(subjs: Optional[List[str]] = None, depth: int = 2, limit: int = 30) -> Dict[str, List[List[str]]]
```

Get depth-aware rel map.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">subjs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Get depth-aware rel map."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_triplet [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.upsert_triplet "Permanent link")

```
upsert_triplet(subj: str, rel: str, obj: str) -> None
```

Add triplet.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add triplet."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.delete "Permanent link")

```
delete(subj: str, rel: str, obj: str) -> None
```

Delete triplet.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete triplet."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.persist "Permanent link")

```
persist(persist_path: str, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the graph store to a file.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the graph store to a file."""</span>
    <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

### get\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.get_schema "Permanent link")

```
get_schema(refresh: bool = False) -> str
```

Get the schema of the graph store.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the schema of the graph store."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore.query "Permanent link")

```
query(query: str, param_map: Optional[Dict[str, Any]] = {}) -> Any
```

Query the graph store with statement and parameters.

Source code in `llama-index-core/llama_index/core/graph_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">param_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query the graph store with statement and parameters."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Falkordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/falkordb/)[Next Kuzu](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/kuzu/)
