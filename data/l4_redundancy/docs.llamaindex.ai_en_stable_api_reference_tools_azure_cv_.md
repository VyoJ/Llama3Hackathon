Title: Azure cv - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/

Markdown Content:
Azure cv - LlamaIndex


AzureCVToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/#llama_index.tools.azure_cv.AzureCVToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Azure Cognitive Vision tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-azure-cv/llama_index/tools/azure_cv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureCVToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure Cognitive Vision tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"process_image"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">resource</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">language</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span>
        <span class="n">api_version</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"2023-04-01-preview"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cv_url</span> <span class="o">=</span> <span class="n">CV_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">resource</span><span class="o">=</span><span class="n">resource</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">language</span> <span class="o">=</span> <span class="n">language</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_version</span> <span class="o">=</span> <span class="n">api_version</span>

    <span class="k">def</span> <span class="nf">process_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">features</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This tool accepts an image url or file and can process and return a variety of text depending on the use case.</span>
<span class="sd">        You can use the features argument to configure what text you want returned.</span>

<span class="sd">        Args:</span>
<span class="sd">            url (str): The url for the image to caption</span>
<span class="sd">            features (List[str]): Instructions on how to process the image. Valid keys are tags, objects, read, caption</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">cv_url</span><span class="si">}</span><span class="s1">?features=</span><span class="si">{</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">features</span><span class="p">)</span><span class="si">}</span><span class="s1">&amp;language=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">language</span><span class="si">}</span><span class="s1">&amp;api-version=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">api_version</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"Ocp-Apim-Subscription-Key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">},</span>
            <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"url"</span><span class="p">:</span> <span class="n">url</span><span class="p">},</span>
        <span class="p">)</span>
        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">if</span> <span class="s2">"read"</span> <span class="ow">in</span> <span class="n">features</span><span class="p">:</span>
            <span class="n">response_json</span><span class="p">[</span><span class="s2">"readResult"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"readResult"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">response_json</span>
</code></pre></div></td></tr></tbody></table>

### process\_image [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/#llama_index.tools.azure_cv.AzureCVToolSpec.process_image "Permanent link")

```
process_image(url: str, features: List[str])
```

This tool accepts an image url or file and can process and return a variety of text depending on the use case. You can use the features argument to configure what text you want returned.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `str` | 
The url for the image to caption



 | _required_ |
| `features` | `List[str]` | 

Instructions on how to process the image. Valid keys are tags, objects, read, caption



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-cv/llama_index/tools/azure_cv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
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
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">process_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">features</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This tool accepts an image url or file and can process and return a variety of text depending on the use case.</span>
<span class="sd">    You can use the features argument to configure what text you want returned.</span>

<span class="sd">    Args:</span>
<span class="sd">        url (str): The url for the image to caption</span>
<span class="sd">        features (List[str]): Instructions on how to process the image. Valid keys are tags, objects, read, caption</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">cv_url</span><span class="si">}</span><span class="s1">?features=</span><span class="si">{</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">features</span><span class="p">)</span><span class="si">}</span><span class="s1">&amp;language=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">language</span><span class="si">}</span><span class="s1">&amp;api-version=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">api_version</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
        <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"Ocp-Apim-Subscription-Key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">},</span>
        <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"url"</span><span class="p">:</span> <span class="n">url</span><span class="p">},</span>
    <span class="p">)</span>
    <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">if</span> <span class="s2">"read"</span> <span class="ow">in</span> <span class="n">features</span><span class="p">:</span>
        <span class="n">response_json</span><span class="p">[</span><span class="s2">"readResult"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"readResult"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">]</span>

    <span class="k">return</span> <span class="n">response_json</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/)[Next Azure speech](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/)
