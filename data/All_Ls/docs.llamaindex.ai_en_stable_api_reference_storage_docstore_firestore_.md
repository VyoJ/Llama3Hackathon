Title: Firestore - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/

Markdown Content:
Firestore - LlamaIndex


FirestoreDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/#llama_index.storage.docstore.firestore.FirestoreDocumentStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVDocumentStore`

Firestore Document (Node) store.

A Firestore store for Document and Node objects.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `firestore_kvstore` | `[FirestoreKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore "llama_index.storage.kvstore.firestore.FirestoreKVStore")` | 
Firestore key-value store



 | _required_ |
| `namespace` | `str` | 

namespace for the docstore



 | `None` |

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-firestore/llama_index/storage/docstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
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
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FirestoreDocumentStore</span><span class="p">(</span><span class="n">KVDocumentStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Firestore Document (Node) store.</span>

<span class="sd">    A Firestore store for Document and Node objects.</span>

<span class="sd">    Args:</span>
<span class="sd">        firestore_kvstore (FirestoreKVStore): Firestore key-value store</span>
<span class="sd">        namespace (str): namespace for the docstore</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">firestore_kvstore</span><span class="p">:</span> <span class="n">FirestoreKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a FirestoreDocumentStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">firestore_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_database</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">project</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"FirestoreDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Args:</span>
<span class="sd">            project (str): The project which the client acts on behalf of.</span>
<span class="sd">            database (str): The database name that the client targets.</span>
<span class="sd">            namespace (str): namespace for the docstore.</span>
<span class="sd">        """</span>
        <span class="n">firestore_kvstore</span> <span class="o">=</span> <span class="n">FirestoreKVStore</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">project</span><span class="p">,</span> <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">firestore_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_database `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/#llama_index.storage.docstore.firestore.FirestoreDocumentStore.from_database "Permanent link")

```
from_database(project: str, database: str, namespace: Optional[str] = None) -> [FirestoreDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/#llama_index.storage.docstore.firestore.FirestoreDocumentStore "llama_index.storage.docstore.firestore.base.FirestoreDocumentStore")
```

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `project` | `str` | 
The project which the client acts on behalf of.



 | _required_ |
| `database` | `str` | 

The database name that the client targets.



 | _required_ |
| `namespace` | `str` | 

namespace for the docstore.



 | `None` |

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-firestore/llama_index/storage/docstore/firestore/base.py`

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
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_database</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">project</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">database</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"FirestoreDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Args:</span>
<span class="sd">        project (str): The project which the client acts on behalf of.</span>
<span class="sd">        database (str): The database name that the client targets.</span>
<span class="sd">        namespace (str): namespace for the docstore.</span>
<span class="sd">    """</span>
    <span class="n">firestore_kvstore</span> <span class="o">=</span> <span class="n">FirestoreKVStore</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">project</span><span class="p">,</span> <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">firestore_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/elasticsearch/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/)
