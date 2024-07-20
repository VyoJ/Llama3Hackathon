Title: Cohere citation chat - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/

Markdown Content:
Cohere citation chat - LlamaIndex


CohereCitationChatEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/#llama_index.packs.cohere_citation_chat.CohereCitationChatEnginePack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-cohere-citation-chat/llama_index/packs/cohere_citation_chat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
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
<span class="normal">50</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CohereCitationChatEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">cohere_api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.llms.cohere</span> <span class="kn">import</span> <span class="n">Cohere</span>
            <span class="kn">from</span> <span class="nn">llama_index.embeddings.cohere</span> <span class="kn">import</span> <span class="n">CohereEmbedding</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please run `pip install llama-index-llms-cohere llama-index-embeddings-cohere` "</span>
                <span class="s2">"to use the Cohere."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">cohere_api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"COHERE_API_KEY"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">Cohere</span><span class="p">(</span>
            <span class="s2">"command"</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="p">{</span><span class="s2">"prompt_truncation"</span><span class="p">:</span> <span class="s2">"AUTO"</span><span class="p">},</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model_document</span> <span class="o">=</span> <span class="n">CohereEmbedding</span><span class="p">(</span>
            <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="s2">"embed-english-v3.0"</span><span class="p">,</span>
            <span class="n">input_type</span><span class="o">=</span><span class="s2">"search_document"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndexWithCitationsChat</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model_document</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">,</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseChatEngine</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="c1"># Change Cohere embed input type. See the documentation here https://docs.cohere.com/reference/embed</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">set_embed_model_input_type</span><span class="p">(</span><span class="s2">"search_query"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_chat_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/#llama_index.packs.cohere_citation_chat.CohereCitationChatEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-cohere-citation-chat/llama_index/packs/cohere_citation_chat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"vector_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">,</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/#llama_index.packs.cohere_citation_chat.CohereCitationChatEnginePack.run "Permanent link")

```
run(**kwargs: Any) -> [BaseChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "llama_index.core.chat_engine.types.BaseChatEngine")
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-cohere-citation-chat/llama_index/packs/cohere_citation_chat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseChatEngine</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="c1"># Change Cohere embed input type. See the documentation here https://docs.cohere.com/reference/embed</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">set_embed_model_input_type</span><span class="p">(</span><span class="s2">"search_query"</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_chat_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cogniswitch agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/)[Next Corrective rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/)
