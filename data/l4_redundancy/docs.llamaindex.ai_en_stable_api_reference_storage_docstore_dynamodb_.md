Title: Dynamodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/

Markdown Content:
Dynamodb - LlamaIndex


DynamoDBDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/#llama_index.storage.docstore.dynamodb.DynamoDBDocumentStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVDocumentStore`

Source code in `llama-index-integrations/storage/docstore/llama-index-storage-docstore-dynamodb/llama_index/storage/docstore/dynamodb/base.py`

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
<span class="normal">24</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DynamoDBDocumentStore</span><span class="p">(</span><span class="n">KVDocumentStore</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">dynamodb_kvstore</span><span class="p">:</span> <span class="n">DynamoDBKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">kvstore</span><span class="o">=</span><span class="n">dynamodb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"DynamoDBDocumentStore"</span><span class="p">:</span>
        <span class="n">dynamodb_kvstore</span> <span class="o">=</span> <span class="n">DynamoDBKVStore</span><span class="o">.</span><span class="n">from_table_name</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dynamodb_kvstore</span><span class="o">=</span><span class="n">dynamodb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/)[Next Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/elasticsearch/)
