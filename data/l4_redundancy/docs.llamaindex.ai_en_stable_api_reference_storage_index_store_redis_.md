Title: Redis - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/

Markdown Content:
Redis - LlamaIndex


RedisIndexStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/#llama_index.storage.index_store.redis.RedisIndexStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVIndexStore`

Redis Index store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `redis_kvstore` | `[RedisKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/redis/#llama_index.storage.kvstore.redis.RedisKVStore "llama_index.storage.kvstore.redis.RedisKVStore")` | 
Redis key-value store



 | _required_ |
| `namespace` | `str` | 

namespace for the index store



 | `None` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-redis/llama_index/storage/index_store/redis/base.py`

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
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RedisIndexStore</span><span class="p">(</span><span class="n">KVIndexStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Redis Index store.</span>

<span class="sd">    Args:</span>
<span class="sd">        redis_kvstore (RedisKVStore): Redis key-value store</span>
<span class="sd">        namespace (str): namespace for the index store</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">redis_kvstore</span><span class="p">:</span> <span class="n">RedisKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a RedisIndexStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">redis_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
        <span class="c1"># avoid conflicts with redis docstore</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_namespace</span><span class="si">}</span><span class="s2">/index"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_redis_client</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">redis_client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RedisIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a RedisIndexStore from a Redis Client."""</span>
        <span class="n">redis_kvstore</span> <span class="o">=</span> <span class="n">RedisKVStore</span><span class="o">.</span><span class="n">from_redis_client</span><span class="p">(</span><span class="n">redis_client</span><span class="o">=</span><span class="n">redis_client</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">redis_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_host_and_port</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RedisIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a RedisIndexStore from a Redis host and port."""</span>
        <span class="n">redis_kvstore</span> <span class="o">=</span> <span class="n">RedisKVStore</span><span class="o">.</span><span class="n">from_host_and_port</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">redis_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_redis\_client `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/#llama_index.storage.index_store.redis.RedisIndexStore.from_redis_client "Permanent link")

```
from_redis_client(redis_client: Any, namespace: Optional[str] = None) -> [RedisIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/#llama_index.storage.index_store.redis.RedisIndexStore "llama_index.storage.index_store.redis.base.RedisIndexStore")
```

Load a RedisIndexStore from a Redis Client.

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-redis/llama_index/storage/index_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_redis_client</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">redis_client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RedisIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a RedisIndexStore from a Redis Client."""</span>
    <span class="n">redis_kvstore</span> <span class="o">=</span> <span class="n">RedisKVStore</span><span class="o">.</span><span class="n">from_redis_client</span><span class="p">(</span><span class="n">redis_client</span><span class="o">=</span><span class="n">redis_client</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">redis_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_host\_and\_port `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/#llama_index.storage.index_store.redis.RedisIndexStore.from_host_and_port "Permanent link")

```
from_host_and_port(host: str, port: int, namespace: Optional[str] = None) -> [RedisIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/#llama_index.storage.index_store.redis.RedisIndexStore "llama_index.storage.index_store.redis.base.RedisIndexStore")
```

Load a RedisIndexStore from a Redis host and port.

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-redis/llama_index/storage/index_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
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
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RedisIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a RedisIndexStore from a Redis host and port."""</span>
    <span class="n">redis_kvstore</span> <span class="o">=</span> <span class="n">RedisKVStore</span><span class="o">.</span><span class="n">from_host_and_port</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">redis_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/postgres/)[Next Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/simple/)
