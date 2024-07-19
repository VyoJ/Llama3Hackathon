Title: Keyword - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/

Markdown Content:
Keyword - LlamaIndex


Node PostProcessor module.

KeywordNodePostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/#llama_index.core.postprocessor.KeywordNodePostprocessor "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Keyword-based Node processor.

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
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
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordNodePostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword-based Node processor."""</span>

    <span class="n">required_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">exclude_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">lang</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">"en"</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"KeywordNodePostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">spacy</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Spacy is not installed, please install it with `pip install spacy`."</span>
            <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">spacy.matcher</span> <span class="kn">import</span> <span class="n">PhraseMatcher</span>

        <span class="n">nlp</span> <span class="o">=</span> <span class="n">spacy</span><span class="o">.</span><span class="n">blank</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lang</span><span class="p">)</span>
        <span class="n">required_matcher</span> <span class="o">=</span> <span class="n">PhraseMatcher</span><span class="p">(</span><span class="n">nlp</span><span class="o">.</span><span class="n">vocab</span><span class="p">)</span>
        <span class="n">exclude_matcher</span> <span class="o">=</span> <span class="n">PhraseMatcher</span><span class="p">(</span><span class="n">nlp</span><span class="o">.</span><span class="n">vocab</span><span class="p">)</span>
        <span class="n">required_matcher</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="s2">"RequiredKeywords"</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">nlp</span><span class="o">.</span><span class="n">pipe</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keywords</span><span class="p">)))</span>
        <span class="n">exclude_matcher</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="s2">"ExcludeKeywords"</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">nlp</span><span class="o">.</span><span class="n">pipe</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">exclude_keywords</span><span class="p">)))</span>

        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
            <span class="n">doc</span> <span class="o">=</span> <span class="n">nlp</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">())</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keywords</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">required_matcher</span><span class="p">(</span><span class="n">doc</span><span class="p">):</span>
                <span class="k">continue</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude_keywords</span> <span class="ow">and</span> <span class="n">exclude_matcher</span><span class="p">(</span><span class="n">doc</span><span class="p">):</span>
                <span class="k">continue</span>
            <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_score</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Jinaai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/)[Next Llm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/)
