Title: Mongodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/

Markdown Content:
Mongodb - LlamaIndex


MongoIndexStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/#llama_index.storage.index_store.mongodb.MongoIndexStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVIndexStore`

Mongo Index store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mongo_kvstore` | `[MongoDBKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/#llama_index.storage.kvstore.mongodb.MongoDBKVStore "llama_index.storage.kvstore.mongodb.MongoDBKVStore")` | 
MongoDB key-value store



 | _required_ |
| `namespace` | `str` | 

namespace for the index store



 | `None` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-mongodb/llama_index/storage/index_store/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
<span class="normal"> 8</span>
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
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MongoIndexStore</span><span class="p">(</span><span class="n">KVIndexStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Mongo Index store.</span>

<span class="sd">    Args:</span>
<span class="sd">        mongo_kvstore (MongoDBKVStore): MongoDB key-value store</span>
<span class="sd">        namespace (str): namespace for the index store</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">mongo_kvstore</span><span class="p">:</span> <span class="n">MongoDBKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a MongoIndexStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">mongo_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a MongoIndexStore from a MongoDB URI."""</span>
        <span class="n">mongo_kvstore</span> <span class="o">=</span> <span class="n">MongoDBKVStore</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">,</span> <span class="n">db_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">mongo_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_host_and_port</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a MongoIndexStore from a MongoDB host and port."""</span>
        <span class="n">mongo_kvstore</span> <span class="o">=</span> <span class="n">MongoDBKVStore</span><span class="o">.</span><span class="n">from_host_and_port</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">db_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">mongo_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_uri `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/#llama_index.storage.index_store.mongodb.MongoIndexStore.from_uri "Permanent link")

```
from_uri(uri: str, db_name: Optional[str] = None, namespace: Optional[str] = None) -> [MongoIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/#llama_index.storage.index_store.mongodb.MongoIndexStore "llama_index.storage.index_store.mongodb.base.MongoIndexStore")
```

Load a MongoIndexStore from a MongoDB URI.

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-mongodb/llama_index/storage/index_store/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a MongoIndexStore from a MongoDB URI."""</span>
    <span class="n">mongo_kvstore</span> <span class="o">=</span> <span class="n">MongoDBKVStore</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">,</span> <span class="n">db_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">mongo_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_host\_and\_port `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/#llama_index.storage.index_store.mongodb.MongoIndexStore.from_host_and_port "Permanent link")

```
from_host_and_port(host: str, port: int, db_name: Optional[str] = None, namespace: Optional[str] = None) -> [MongoIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/#llama_index.storage.index_store.mongodb.MongoIndexStore "llama_index.storage.index_store.mongodb.base.MongoIndexStore")
```

Load a MongoIndexStore from a MongoDB host and port.

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-mongodb/llama_index/storage/index_store/mongodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_host_and_port</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="n">db_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MongoIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a MongoIndexStore from a MongoDB host and port."""</span>
    <span class="n">mongo_kvstore</span> <span class="o">=</span> <span class="n">MongoDBKVStore</span><span class="o">.</span><span class="n">from_host_and_port</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">db_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">mongo_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/)[Next Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/postgres/)
