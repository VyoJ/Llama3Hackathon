Title: Passio nutrition ai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/

Markdown Content:
Passio nutrition ai - LlamaIndex


NutritionAIToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/#llama_index.tools.passio_nutrition_ai.NutritionAIToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Tool that queries the Passio Nutrition AI API.

Source code in `llama-index-integrations/tools/llama-index-tools-passio-nutrition-ai/llama_index/tools/passio_nutrition_ai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
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
<span class="normal">144</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NutritionAIToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tool that queries the Passio Nutrition AI API."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"nutrition_ai_search"</span><span class="p">]</span>
    <span class="n">auth_</span><span class="p">:</span> <span class="n">ManagedPassioLifeAuth</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">auth_</span> <span class="o">=</span> <span class="n">ManagedPassioLifeAuth</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span>

    <span class="nd">@retry</span><span class="p">(</span>
        <span class="n">retry</span><span class="o">=</span><span class="n">retry_if_result</span><span class="p">(</span><span class="n">is_http_retryable</span><span class="p">),</span>
        <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_attempt</span><span class="p">(</span><span class="mi">4</span><span class="p">),</span>
        <span class="n">wait</span><span class="o">=</span><span class="n">wait_random</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.3</span><span class="p">)</span> <span class="o">+</span> <span class="n">wait_exponential</span><span class="p">(</span><span class="n">multiplier</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="nb">min</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="nb">max</span><span class="o">=</span><span class="mi">2</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">_http_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">ENDPOINT_BASE_URL</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">auth_</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"term"</span><span class="p">:</span> <span class="n">query</span><span class="p">},</span>  <span class="c1"># type: ignore</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_nutrition_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_http_get</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No response from NutritionAI API."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">nutrition_ai_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieve nutrition facts for a given food item.</span>
<span class="sd">        Input should be a search query string for the food item.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The food item to look for.</span>

<span class="sd">        Returns a JSON result with the nutrition facts for the food item and, if available, alternative food items which sometimes are a better match.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_nutrition_request</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### nutrition\_ai\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/#llama_index.tools.passio_nutrition_ai.NutritionAIToolSpec.nutrition_ai_search "Permanent link")

```
nutrition_ai_search(query: str)
```

Retrieve nutrition facts for a given food item. Input should be a search query string for the food item.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The food item to look for.



 | _required_ |

Returns a JSON result with the nutrition facts for the food item and, if available, alternative food items which sometimes are a better match.

Source code in `llama-index-integrations/tools/llama-index-tools-passio-nutrition-ai/llama_index/tools/passio_nutrition_ai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">nutrition_ai_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieve nutrition facts for a given food item.</span>
<span class="sd">    Input should be a search query string for the food item.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The food item to look for.</span>

<span class="sd">    Returns a JSON result with the nutrition facts for the food item and, if available, alternative food items which sometimes are a better match.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_nutrition_request</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openapi](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/)[Next Playgrounds](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/)
