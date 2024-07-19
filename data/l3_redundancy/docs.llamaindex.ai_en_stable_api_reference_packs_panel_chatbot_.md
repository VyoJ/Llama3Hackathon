Title: Panel chatbot - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/

Markdown Content:
Panel chatbot - LlamaIndex


PanelChatPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/#llama_index.packs.panel_chatbot.PanelChatPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Panel chatbot pack.

Source code in `llama-index-packs/llama-index-packs-panel-chatbot/llama_index/packs/panel_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PanelChatPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Panel chatbot pack."""</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">for</span> <span class="n">variable</span> <span class="ow">in</span> <span class="n">ENVIRONMENT_VARIABLES</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">variable</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"</span><span class="si">%s</span><span class="s2"> environment variable is not set"</span><span class="p">,</span> <span class="n">variable</span><span class="p">)</span>

        <span class="kn">import</span> <span class="nn">panel</span> <span class="k">as</span> <span class="nn">pn</span>

        <span class="k">if</span> <span class="vm">__name__</span> <span class="o"></span> <span class="s2">"__main__"</span><span class="p">:</span>
        <span class="c1"># 'pytest tests' will fail if app is imported elsewhere</span>
        <span class="kn">from</span> <span class="nn">app</span> <span class="kn">import</span> <span class="n">create_chat_ui</span>

        <span class="n">pn</span><span class="o">.</span><span class="n">serve</span><span class="p">(</span><span class="n">create_chat_ui</span><span class="p">)</span>
    <span class="k">elif</span> <span class="vm">__name__</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"bokeh"</span><span class="p">):</span>
        <span class="kn">from</span> <span class="nn">app</span> <span class="kn">import</span> <span class="n">create_chat_ui</span>

        <span class="n">create_chat_ui</span><span class="p">()</span><span class="o">.</span><span class="n">servable</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span>
            <span class="s2">"To serve the Panel ChatBot please run this file with 'panel serve' or 'python'"</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Ollama query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/)[Next Query understanding agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/query_understanding_agent/)
