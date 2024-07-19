Title: Pathway - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/

Markdown Content:
Pathway - LlamaIndex


PathwayRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/#llama_index.retrievers.pathway.PathwayRetriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Pathway retriever.

Pathway is an open data processing framework. It allows you to easily develop data transformation pipelines that work with live data sources and changing data.

This is the client that implements Retriever API for PathwayVectorServer.

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-pathway/llama_index/retrievers/pathway/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PathwayRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pathway retriever.</span>

<span class="sd">    Pathway is an open data processing framework.</span>
<span class="sd">    It allows you to easily develop data transformation pipelines</span>
<span class="sd">    that work with live data sources and changing data.</span>

<span class="sd">    This is the client that implements Retriever API for PathwayVectorServer.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initializing the Pathway retriever client."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">_VectorStoreClient</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="n">rets</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">)</span>
        <span class="n">items</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">NodeWithScore</span><span class="p">(</span>
                <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">ret</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">ret</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]),</span>
                <span class="c1"># Transform cosine distance into a similairty score</span>
                <span class="c1"># (higher is more similar)</span>
                <span class="n">score</span><span class="o">=</span><span class="mi">1</span> <span class="o">-</span> <span class="n">ret</span><span class="p">[</span><span class="s2">"dist"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">ret</span> <span class="ow">in</span> <span class="n">rets</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">items</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="ow">or</span> <span class="mf">0.0</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mongodb atlas bm25 retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/)[Next Query fusion](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/)
