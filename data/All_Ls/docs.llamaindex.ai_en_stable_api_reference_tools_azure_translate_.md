Title: Azure translate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/

Markdown Content:
Azure translate - LlamaIndex


AzureTranslateToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/#llama_index.tools.azure_translate.AzureTranslateToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Azure Translate tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-azure-translate/llama_index/tools/azure_translate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
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
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureTranslateToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure Translate tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"translate"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">region</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Ocp-Apim-Subscription-Key"</span><span class="p">:</span> <span class="n">api_key</span><span class="p">,</span>
            <span class="s2">"Ocp-Apim-Subscription-Region"</span><span class="p">:</span> <span class="n">region</span><span class="p">,</span>
            <span class="s2">"Content-type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">translate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this tool to translate text from one language to another.</span>
<span class="sd">        The source language will be automatically detected. You need to specify the target language</span>
<span class="sd">        using a two character language code.</span>

<span class="sd">        Args:</span>
<span class="sd">            language (str): Target translation language.</span>
<span class="sd">        """</span>
        <span class="n">request</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="n">ENDPOINT_BASE_URL</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"api-version"</span><span class="p">:</span> <span class="s2">"3.0"</span><span class="p">,</span> <span class="s2">"to"</span><span class="p">:</span> <span class="n">language</span><span class="p">},</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="p">[{</span><span class="s2">"text"</span><span class="p">:</span> <span class="n">text</span><span class="p">}],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">request</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### translate [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/#llama_index.tools.azure_translate.AzureTranslateToolSpec.translate "Permanent link")

```
translate(text: str, language: str)
```

Use this tool to translate text from one language to another. The source language will be automatically detected. You need to specify the target language using a two character language code.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `language` | `str` | 
Target translation language.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-translate/llama_index/tools/azure_translate/base.py`

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
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">translate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this tool to translate text from one language to another.</span>
<span class="sd">    The source language will be automatically detected. You need to specify the target language</span>
<span class="sd">    using a two character language code.</span>

<span class="sd">    Args:</span>
<span class="sd">        language (str): Target translation language.</span>
<span class="sd">    """</span>
    <span class="n">request</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="n">ENDPOINT_BASE_URL</span><span class="p">,</span>
        <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"api-version"</span><span class="p">:</span> <span class="s2">"3.0"</span><span class="p">,</span> <span class="s2">"to"</span><span class="p">:</span> <span class="n">language</span><span class="p">},</span>
        <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
        <span class="n">json</span><span class="o">=</span><span class="p">[{</span><span class="s2">"text"</span><span class="p">:</span> <span class="n">text</span><span class="p">}],</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">request</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure speech](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/)[Next Bing search](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/)
