Title: Opensearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/

Markdown Content:
Opensearch - LlamaIndex


OpensearchVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Elasticsearch/Opensearch vector store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `client` | `OpensearchVectorClient` | 
Vector index client to use for data insertion/querying.



 | _required_ |

**Examples:**

`pip install llama-index-vector-stores-opensearch`

```
from llama_index.vector_stores.opensearch import (
    OpensearchVectorStore,
    OpensearchVectorClient,
)

# http endpoint for your cluster (opensearch required for vector index usage)
endpoint = "http://localhost:9200"
# index to demonstrate the VectorStore impl
idx = "gpt-index-demo"

# OpensearchVectorClient stores text in this field by default
text_field = "content"
# OpensearchVectorClient stores embeddings in this field by default
embedding_field = "embedding"

# OpensearchVectorClient encapsulates logic for a
# single opensearch index with vector search enabled
client = OpensearchVectorClient(
    endpoint, idx, 1536, embedding_field=embedding_field, text_field=text_field
)

# initialize vector store
vector_store = OpensearchVectorStore(client)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpensearchVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Elasticsearch/Opensearch vector store.</span>

<span class="sd">    Args:</span>
<span class="sd">        client (OpensearchVectorClient): Vector index client to use</span>
<span class="sd">            for data insertion/querying.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-opensearch`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.opensearch import (</span>
<span class="sd">            OpensearchVectorStore,</span>
<span class="sd">            OpensearchVectorClient,</span>
<span class="sd">        )</span>

<span class="sd">        # http endpoint for your cluster (opensearch required for vector index usage)</span>
<span class="sd">        endpoint = "http://localhost:9200"</span>
<span class="sd">        # index to demonstrate the VectorStore impl</span>
<span class="sd">        idx = "gpt-index-demo"</span>

<span class="sd">        # OpensearchVectorClient stores text in this field by default</span>
<span class="sd">        text_field = "content"</span>
<span class="sd">        # OpensearchVectorClient stores embeddings in this field by default</span>
<span class="sd">        embedding_field = "embedding"</span>

<span class="sd">        # OpensearchVectorClient encapsulates logic for a</span>
<span class="sd">        # single opensearch index with vector search enabled</span>
<span class="sd">        client = OpensearchVectorClient(</span>
<span class="sd">            endpoint, idx, 1536, embedding_field=embedding_field, text_field=text_field</span>
<span class="sd">        )</span>

<span class="sd">        # initialize vector store</span>
<span class="sd">        vector_store = OpensearchVectorStore(client)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">_client</span><span class="p">:</span> <span class="n">OpensearchVectorClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">OpensearchVectorClient</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">async_add</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Async add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings.</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">index_results</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using a ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document whose nodes should be deleted.</span>

<span class="sd">        """</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">adelete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Async delete nodes using a ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document whose nodes should be deleted.</span>

<span class="sd">        """</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">delete_by_doc_id</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): Store query object.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Async query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): Store query object.</span>

<span class="sd">        """</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="p">,</span>
            <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">async_add</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### async\_add `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.async_add "Permanent link")

```
async_add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Async add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Async add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings.</span>

<span class="sd">    """</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">index_results</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using a ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document whose nodes should be deleted.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using a ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document whose nodes should be deleted.</span>

<span class="sd">    """</span>
    <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">adelete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.adelete "Permanent link")

```
adelete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Async delete nodes using a ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document whose nodes should be deleted.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Async delete nodes using a ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document whose nodes should be deleted.</span>

<span class="sd">    """</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">delete_by_doc_id</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Store query object.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): Store query object.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### aquery `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/#llama_index.vector_stores.opensearch.OpensearchVectorStore.aquery "Permanent link")

```
aquery(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Async query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Store query object.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-opensearch/llama_index/vector_stores/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Async query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): Store query object.</span>

<span class="sd">    """</span>
    <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>

    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="p">,</span>
        <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/)[Next Pgvecto rs](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/)
