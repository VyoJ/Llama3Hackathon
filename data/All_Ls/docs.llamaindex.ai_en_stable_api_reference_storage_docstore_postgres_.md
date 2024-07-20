Title: Postgres - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/

Markdown Content:
Postgres - LlamaIndex


PostgresDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/#llama_index.storage.docstore.postgres.PostgresDocumentStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVDocumentStore`

Postgres Document (Node) store.

A Postgres store for Document and Node objects.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `postgres_kvstore` | `[PostgresKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/#llama_index.storage.kvstore.postgres.PostgresKVStore "llama_index.storage.kvstore.postgres.PostgresKVStore")` | 
Postgres key-value store



 | _required_ |
| `namespace` | `str` | 

namespace for the docstore



 | `None` |
| `batch_size` | `int` | 

batch size for bulk operations



 | `DEFAULT_BATCH_SIZE` |

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-postgres/llama_index/storage/docstore/postgres/base.py`

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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PostgresDocumentStore</span><span class="p">(</span><span class="n">KVDocumentStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Postgres Document (Node) store.</span>

<span class="sd">    A Postgres store for Document and Node objects.</span>

<span class="sd">    Args:</span>
<span class="sd">        postgres_kvstore (PostgresKVStore): Postgres key-value store</span>
<span class="sd">        namespace (str): namespace for the docstore</span>
<span class="sd">        batch_size (int): batch size for bulk operations</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">postgres_kvstore</span><span class="p">:</span> <span class="n">PostgresKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a PostgresDocumentStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">postgres_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"docstore"</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a PostgresDocumentStore from a Postgres URI."""</span>
        <span class="n">postgres_kvstore</span> <span class="o">=</span> <span class="n">PostgresKVStore</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span>
            <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">postgres_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"docstore"</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a PostgresDocumentStore from a Postgres host and port."""</span>
        <span class="n">postgres_kvstore</span> <span class="o">=</span> <span class="n">PostgresKVStore</span><span class="o">.</span><span class="n">from_params</span><span class="p">(</span>
            <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">user</span><span class="o">=</span><span class="n">user</span><span class="p">,</span>
            <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
            <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
            <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
            <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">postgres_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_uri `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/#llama_index.storage.docstore.postgres.PostgresDocumentStore.from_uri "Permanent link")

```
from_uri(uri: str, namespace: Optional[str] = None, table_name: str = 'docstore', schema_name: str = 'public', perform_setup: bool = True, debug: bool = False, use_jsonb: bool = False) -> [PostgresDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/#llama_index.storage.docstore.postgres.PostgresDocumentStore "llama_index.storage.docstore.postgres.base.PostgresDocumentStore")
```

Load a PostgresDocumentStore from a Postgres URI.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-postgres/llama_index/storage/docstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
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
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_uri</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"docstore"</span><span class="p">,</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a PostgresDocumentStore from a Postgres URI."""</span>
    <span class="n">postgres_kvstore</span> <span class="o">=</span> <span class="n">PostgresKVStore</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span>
        <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span>
        <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
        <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">postgres_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_params `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/#llama_index.storage.docstore.postgres.PostgresDocumentStore.from_params "Permanent link")

```
from_params(host: Optional[str] = None, port: Optional[str] = None, database: Optional[str] = None, user: Optional[str] = None, password: Optional[str] = None, namespace: Optional[str] = None, table_name: str = 'docstore', schema_name: str = 'public', perform_setup: bool = True, debug: bool = False, use_jsonb: bool = False) -> [PostgresDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/#llama_index.storage.docstore.postgres.PostgresDocumentStore "llama_index.storage.docstore.postgres.base.PostgresDocumentStore")
```

Load a PostgresDocumentStore from a Postgres host and port.

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-postgres/llama_index/storage/docstore/postgres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"docstore"</span><span class="p">,</span>
    <span class="n">schema_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"public"</span><span class="p">,</span>
    <span class="n">perform_setup</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">use_jsonb</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PostgresDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a PostgresDocumentStore from a Postgres host and port."""</span>
    <span class="n">postgres_kvstore</span> <span class="o">=</span> <span class="n">PostgresKVStore</span><span class="o">.</span><span class="n">from_params</span><span class="p">(</span>
        <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
        <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
        <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
        <span class="n">user</span><span class="o">=</span><span class="n">user</span><span class="p">,</span>
        <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">,</span>
        <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
        <span class="n">schema_name</span><span class="o">=</span><span class="n">schema_name</span><span class="p">,</span>
        <span class="n">perform_setup</span><span class="o">=</span><span class="n">perform_setup</span><span class="p">,</span>
        <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">,</span>
        <span class="n">use_jsonb</span><span class="o">=</span><span class="n">use_jsonb</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">postgres_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/mongodb/)[Next Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/redis/)
