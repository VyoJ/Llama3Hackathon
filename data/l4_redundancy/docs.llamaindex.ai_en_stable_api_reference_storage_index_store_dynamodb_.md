Title: Dynamodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/

Markdown Content:
Dynamodb - LlamaIndex


DynamoDBIndexStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/#llama_index.storage.index_store.dynamodb.DynamoDBIndexStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVIndexStore`

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-dynamodb/llama_index/storage/index_store/dynamodb/base.py`

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
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DynamoDBIndexStore</span><span class="p">(</span><span class="n">KVIndexStore</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dynamodb_kvstore</span><span class="p">:</span> <span class="n">DynamoDBKVStore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init a DynamoDBIndexStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kvstore</span><span class="o">=</span><span class="n">dynamodb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBIndexStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load DynamoDBIndexStore from a DynamoDB table name."""</span>
        <span class="n">ddb_kvstore</span> <span class="o">=</span> <span class="n">DynamoDBKVStore</span><span class="o">.</span><span class="n">from_table_name</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dynamodb_kvstore</span><span class="o">=</span><span class="n">ddb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_table\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/#llama_index.storage.index_store.dynamodb.DynamoDBIndexStore.from_table_name "Permanent link")

```
from_table_name(table_name: str, namespace: str | None = None) -> [DynamoDBIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/#llama_index.storage.index_store.dynamodb.DynamoDBIndexStore "llama_index.storage.index_store.dynamodb.base.DynamoDBIndexStore")
```

Load DynamoDBIndexStore from a DynamoDB table name.

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-dynamodb/llama_index/storage/index_store/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBIndexStore</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load DynamoDBIndexStore from a DynamoDB table name."""</span>
    <span class="n">ddb_kvstore</span> <span class="o">=</span> <span class="n">DynamoDBKVStore</span><span class="o">.</span><span class="n">from_table_name</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dynamodb_kvstore</span><span class="o">=</span><span class="n">ddb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/)[Next Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/elasticsearch/)
