Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/

Markdown Content:
Index - LlamaIndex


MultiModalLLM [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[ChainableMixin](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "llama_index.core.base.query_pipeline.query.ChainableMixin")`, `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`, `DispatcherSpanMixin`

Multi-Modal LLM interface.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
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
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiModalLLM</span><span class="p">(</span><span class="n">ChainableMixin</span><span class="p">,</span> <span class="n">BaseComponent</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Multi-Modal LLM interface."""</span>

    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"callback_manager"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_validate_callback_manager</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CallbackManager</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">return</span> <span class="n">v</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Multi-Modal LLM metadata."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Completion endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Streaming completion endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Chat endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Stream chat endpoint for Multi-Modal LLM."""</span>

    <span class="c1"># </span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async completion endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async streaming completion endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async chat endpoint for Multi-Modal LLM."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async streaming chat endpoint for Multi-Modal LLM."""</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return query component."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">is_chat_model</span><span class="p">:</span>
            <span class="c1"># TODO: we don't have a separate chat component</span>
            <span class="k">return</span> <span class="n">MultiModalCompleteComponent</span><span class="p">(</span><span class="n">multi_modal_llm</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">MultiModalCompleteComponent</span><span class="p">(</span><span class="n">multi_modal_llm</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__init_subclass__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        The callback decorators installs events, so they must be applied before</span>
<span class="sd">        the span decorators, otherwise the spans wouldn't contain the events.</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">attr</span> <span class="ow">in</span> <span class="p">(</span>
            <span class="s2">"complete"</span><span class="p">,</span>
            <span class="s2">"acomplete"</span><span class="p">,</span>
            <span class="s2">"stream_complete"</span><span class="p">,</span>
            <span class="s2">"astream_complete"</span><span class="p">,</span>
            <span class="s2">"chat"</span><span class="p">,</span>
            <span class="s2">"achat"</span><span class="p">,</span>
            <span class="s2">"stream_chat"</span><span class="p">,</span>
            <span class="s2">"astream_chat"</span><span class="p">,</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="nb">callable</span><span class="p">(</span><span class="n">method</span> <span class="o">:=</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attr</span><span class="p">)):</span>
                <span class="k">if</span> <span class="n">attr</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">):</span>
                    <span class="nb">setattr</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">attr</span><span class="p">,</span> <span class="n">llm_chat_callback</span><span class="p">()(</span><span class="n">method</span><span class="p">))</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="nb">setattr</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">attr</span><span class="p">,</span> <span class="n">llm_completion_callback</span><span class="p">()(</span><span class="n">method</span><span class="p">))</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__init_subclass__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### metadata `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.metadata "Permanent link")

```
metadata: MultiModalLLMMetadata
```

Multi-Modal LLM metadata.

### complete `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.complete "Permanent link")

```
complete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], **kwargs: Any) -> CompletionResponse
```

Completion endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Completion endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### stream\_complete `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.stream_complete "Permanent link")

```
stream_complete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], **kwargs: Any) -> CompletionResponseGen
```

Streaming completion endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Streaming completion endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.chat "Permanent link")

```
chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponse
```

Chat endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Chat endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### stream\_chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.stream_chat "Permanent link")

```
stream_chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponseGen
```

Stream chat endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Stream chat endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### acomplete `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.acomplete "Permanent link")

```
acomplete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], **kwargs: Any) -> CompletionResponse
```

Async completion endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async completion endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### astream\_complete `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.astream_complete "Permanent link")

```
astream_complete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], **kwargs: Any) -> CompletionResponseAsyncGen
```

Async streaming completion endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async streaming completion endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### achat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.achat "Permanent link")

```
achat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponse
```

Async chat endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async chat endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

### astream\_chat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM.astream_chat "Permanent link")

```
astream_chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponseAsyncGen
```

Async streaming chat endpoint for Multi-Modal LLM.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async streaming chat endpoint for Multi-Modal LLM."""</span>
</code></pre></div></td></tr></tbody></table>

BaseMultiModalComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.BaseMultiModalComponent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Base LLM component.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseMultiModalComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base LLM component."""</span>

    <span class="n">multi_modal_llm</span><span class="p">:</span> <span class="n">MultiModalLLM</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"LLM"</span><span class="p">)</span>
    <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Streaming mode"</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

### set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.BaseMultiModalComponent.set_callback_manager "Permanent link")

```
set_callback_manager(callback_manager: Any) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">195</span>
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

MultiModalCompleteComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalCompleteComponent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseMultiModalComponent](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.BaseMultiModalComponent "llama_index.core.multi_modal_llms.base.BaseMultiModalComponent")`

Multi-modal completion component.

Source code in `llama-index-core/llama_index/core/multi_modal_llms/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
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
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiModalCompleteComponent</span><span class="p">(</span><span class="n">BaseMultiModalComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Multi-modal completion component."""</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="k">if</span> <span class="s2">"prompt"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Prompt must be in input dict."</span><span class="p">)</span>

        <span class="c1"># do special check to see if prompt is a list of chat messages</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">],</span> <span class="n">get_args</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])):</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                <span class="s2">"Chat messages not yet supported as input to multi-modal model."</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">])</span>

        <span class="c1"># make sure image documents are valid</span>
        <span class="k">if</span> <span class="s2">"image_documents"</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"image_documents"</span><span class="p">],</span> <span class="nb">list</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"image_documents must be a list."</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">[</span><span class="s2">"image_documents"</span><span class="p">]:</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">ImageDocument</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="s2">"image_documents must be a list of ImageDocument objects."</span>
                    <span class="p">)</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span>
        <span class="n">image_documents</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"image_documents"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">streaming</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">multi_modal_llm</span><span class="o">.</span><span class="n">stream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">multi_modal_llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="c1"># non-trivial to figure how to support chat/complete/etc.</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"prompt"</span><span class="p">]</span>
        <span class="n">image_documents</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"image_documents"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">streaming</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">multi_modal_llm</span><span class="o">.</span><span class="n">astream_complete</span><span class="p">(</span>
                <span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">multi_modal_llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">response</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># TODO: support only complete for now</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"prompt"</span><span class="p">,</span> <span class="s2">"image_documents"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

### input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalCompleteComponent.input_keys "Permanent link")

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

### output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalCompleteComponent.output_keys "Permanent link")

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

Back to top

[Previous Gemini](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/)[Next Ollama](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/)
