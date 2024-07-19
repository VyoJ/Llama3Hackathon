Title: Keyword - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/

Markdown Content:
Keyword - LlamaIndex


LlamaIndex data structures.

KeywordTableIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/#llama_index.core.indices.KeywordTableIndex "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseKeywordTableIndex`

Keyword Table Index.

This index uses a GPT model to extract keywords from the text.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordTableIndex</span><span class="p">(</span><span class="n">BaseKeywordTableIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword Table Index.</span>

<span class="sd">    This index uses a GPT model to extract keywords from the text.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">_extract_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from text."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">keyword_extract_template</span><span class="p">,</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">extract_keywords_given_response</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">start_token</span><span class="o">=</span><span class="s2">"KEYWORDS:"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_extract_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from text."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">keyword_extract_template</span><span class="p">,</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">extract_keywords_given_response</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">start_token</span><span class="o">=</span><span class="s2">"KEYWORDS:"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

SimpleKeywordTableIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/#llama_index.core.indices.SimpleKeywordTableIndex "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseKeywordTableIndex`

Simple Keyword Table Index.

This index uses a simple regex extractor to extract keywords from the text.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/simple_base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
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
<span class="normal">41</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleKeywordTableIndex</span><span class="p">(</span><span class="n">BaseKeywordTableIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Keyword Table Index.</span>

<span class="sd">    This index uses a simple regex extractor to extract keywords from the text.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">_extract_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from text."""</span>
        <span class="k">return</span> <span class="n">simple_extract_keywords</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_chunk</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
            <span class="nb">str</span><span class="p">,</span> <span class="n">KeywordTableRetrieverMode</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">KeywordTableRetrieverMode</span><span class="o">.</span><span class="n">SIMPLE</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">retriever_mode</span><span class="o">=</span><span class="n">retriever_mode</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RAKEKeywordTableIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/#llama_index.core.indices.RAKEKeywordTableIndex "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseKeywordTableIndex`

RAKE Keyword Table Index.

This index uses a RAKE keyword extractor to extract keywords from the text.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/rake_base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
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
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RAKEKeywordTableIndex</span><span class="p">(</span><span class="n">BaseKeywordTableIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAKE Keyword Table Index.</span>

<span class="sd">    This index uses a RAKE keyword extractor to extract keywords from the text.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">_extract_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from text."""</span>
        <span class="k">return</span> <span class="n">rake_extract_keywords</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">max_keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_chunk</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
            <span class="nb">str</span><span class="p">,</span> <span class="n">KeywordTableRetrieverMode</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">KeywordTableRetrieverMode</span><span class="o">.</span><span class="n">RAKE</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">retriever_mode</span><span class="o">=</span><span class="n">retriever_mode</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/indices/)[Next Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/)
