Title: Redis ingestion pipeline - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/

Markdown Content:
Redis ingestion pipeline - LlamaIndex


RedisIngestionPipelinePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/#llama_index.packs.redis_ingestion_pipeline.RedisIngestionPipelinePack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Redis Ingestion Pipeline Completion pack.

Source code in `llama-index-packs/llama-index-packs-redis-ingestion-pipeline/llama_index/packs/redis_ingestion_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RedisIngestionPipelinePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Redis Ingestion Pipeline Completion pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">],</span>
        <span class="n">hostname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"localhost"</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">6379</span><span class="p">,</span>
        <span class="n">cache_collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ingest_cache"</span><span class="p">,</span>
        <span class="n">vector_collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"vector_store"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span> <span class="o">=</span> <span class="n">RedisVectorStore</span><span class="p">(</span>
            <span class="n">hostname</span><span class="o">=</span><span class="n">hostname</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">vector_collection_name</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">ingest_cache</span> <span class="o">=</span> <span class="n">IngestionCache</span><span class="p">(</span>
            <span class="n">cache</span><span class="o">=</span><span class="n">RedisCache</span><span class="p">(</span>
                <span class="n">hostname</span><span class="o">=</span><span class="n">hostname</span><span class="p">,</span>
                <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">cache_collection_name</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">pipeline</span> <span class="o">=</span> <span class="n">IngestionPipeline</span><span class="p">(</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="n">cache</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ingest_cache</span><span class="p">,</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"pipeline"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipeline</span><span class="p">,</span>
            <span class="s2">"vector_store"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="p">,</span>
            <span class="s2">"ingest_cache"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">ingest_cache</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">inputs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">inputs</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/#llama_index.packs.redis_ingestion_pipeline.RedisIngestionPipelinePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-redis-ingestion-pipeline/llama_index/packs/redis_ingestion_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"pipeline"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipeline</span><span class="p">,</span>
        <span class="s2">"vector_store"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_store</span><span class="p">,</span>
        <span class="s2">"ingest_cache"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">ingest_cache</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/#llama_index.packs.redis_ingestion_pipeline.RedisIngestionPipelinePack.run "Permanent link")

```
run(inputs: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-redis-ingestion-pipeline/llama_index/packs/redis_ingestion_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">inputs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">inputs</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Recursive retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/)[Next Resume screener](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/)
