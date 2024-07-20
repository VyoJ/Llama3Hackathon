Title: Multi tenancy rag - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/

Markdown Content:
Multi tenancy rag - LlamaIndex


MultiTenancyRAGPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/#llama_index.packs.multi_tenancy_rag.MultiTenancyRAGPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-multi-tenancy-rag/llama_index/packs/multi_tenancy_rag/base.py`

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
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiTenancyRAGPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">,</span> <span class="n">temperature</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="o">=</span><span class="p">[],</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">user</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert Documents of a user into index."""</span>
        <span class="c1"># Add metadata to documents</span>
        <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"user"</span><span class="p">]</span> <span class="o">=</span> <span class="n">user</span>
        <span class="c1"># Create Nodes using IngestionPipeline</span>
        <span class="n">pipeline</span> <span class="o">=</span> <span class="n">IngestionPipeline</span><span class="p">(</span>
            <span class="n">transformations</span><span class="o">=</span><span class="p">[</span>
                <span class="n">SentenceSplitter</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="mi">512</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="mi">20</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span> <span class="n">num_workers</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
        <span class="c1"># Insert nodes into the index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">user</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="c1"># Define retriever to filter out nodes for user and query</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">MetadataFilters</span><span class="p">(</span>
                <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">ExactMatchFilter</span><span class="p">(</span>
                        <span class="n">key</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                        <span class="n">value</span><span class="o">=</span><span class="n">user</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">]</span>
            <span class="p">),</span>
            <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
        <span class="c1"># Define response synthesizer</span>
        <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span><span class="n">response_mode</span><span class="o">=</span><span class="s2">"compact"</span><span class="p">)</span>
        <span class="c1"># Define Query Engine</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span> <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/#llama_index.packs.multi_tenancy_rag.MultiTenancyRAGPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-multi-tenancy-rag/llama_index/packs/multi_tenancy_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/#llama_index.packs.multi_tenancy_rag.MultiTenancyRAGPack.add "Permanent link")

```
add(documents: List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], user: Any) -> None
```

Insert Documents of a user into index.

Source code in `llama-index-packs/llama-index-packs-multi-tenancy-rag/llama_index/packs/multi_tenancy_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">27</span>
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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">user</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Insert Documents of a user into index."""</span>
    <span class="c1"># Add metadata to documents</span>
    <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
        <span class="n">document</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"user"</span><span class="p">]</span> <span class="o">=</span> <span class="n">user</span>
    <span class="c1"># Create Nodes using IngestionPipeline</span>
    <span class="n">pipeline</span> <span class="o">=</span> <span class="n">IngestionPipeline</span><span class="p">(</span>
        <span class="n">transformations</span><span class="o">=</span><span class="p">[</span>
            <span class="n">SentenceSplitter</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="mi">512</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="mi">20</span><span class="p">),</span>
        <span class="p">]</span>
    <span class="p">)</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span> <span class="n">num_workers</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
    <span class="c1"># Insert nodes into the index</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/#llama_index.packs.multi_tenancy_rag.MultiTenancyRAGPack.run "Permanent link")

```
run(query_str: str, user: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-multi-tenancy-rag/llama_index/packs/multi_tenancy_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
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
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">user</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="c1"># Define retriever to filter out nodes for user and query</span>
    <span class="n">retriever</span> <span class="o">=</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span>
        <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="n">MetadataFilters</span><span class="p">(</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ExactMatchFilter</span><span class="p">(</span>
                    <span class="n">key</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                    <span class="n">value</span><span class="o">=</span><span class="n">user</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="p">),</span>
        <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
    <span class="c1"># Define response synthesizer</span>
    <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span><span class="n">response_mode</span><span class="o">=</span><span class="s2">"compact"</span><span class="p">)</span>
    <span class="c1"># Define Query Engine</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="p">(</span>
        <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span> <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multi document agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/)[Next Multidoc autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/)
