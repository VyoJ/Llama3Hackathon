Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/

Markdown Content:
Index - LlamaIndex


AsyncBaseTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")`

Base-level tool class that is backwards compatible with the old tool spec but also supports async.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">158</span>
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
<span class="normal">179</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AsyncBaseTool</span><span class="p">(</span><span class="n">BaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Base-level tool class that is backwards compatible with the old tool spec but also</span>
<span class="sd">    supports async.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This is the method that should be implemented by the tool developer.</span>
<span class="sd">        """</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This is the async version of the call method.</span>
<span class="sd">        Should also be implemented by the tool developer as an</span>
<span class="sd">        async-compatible implementation.</span>
<span class="sd">        """</span>
</code></pre></div></td></tr></tbody></table>

### call `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool.call "Permanent link")

```
call(input: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

This is the method that should be implemented by the tool developer.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This is the method that should be implemented by the tool developer.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

### acall `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool.acall "Permanent link")

```
acall(input: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

This is the async version of the call method. Should also be implemented by the tool developer as an async-compatible implementation.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This is the async version of the call method.</span>
<span class="sd">    Should also be implemented by the tool developer as an</span>
<span class="sd">    async-compatible implementation.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table>

BaseToolAsyncAdapter [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseToolAsyncAdapter "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")`

Adapter class that allows a synchronous tool to be used as an async tool.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseToolAsyncAdapter</span><span class="p">(</span><span class="n">AsyncBaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Adapter class that allows a synchronous tool to be used as an async tool.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">BaseTool</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">base_tool</span> <span class="o">=</span> <span class="n">tool</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_tool</span><span class="o">.</span><span class="n">metadata</span>

    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_tool</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BaseTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "Permanent link")
------------------------------------------------------------------------------------------------------------------------------

Bases: `DispatcherSpanMixin`

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
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
<span class="normal">155</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseTool</span><span class="p">(</span><span class="n">DispatcherSpanMixin</span><span class="p">):</span>
    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">_process_langchain_tool_kwargs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Process langchain tool kwargs."""</span>
        <span class="k">if</span> <span class="s2">"name"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">langchain_tool_kwargs</span><span class="p">:</span>
            <span class="n">langchain_tool_kwargs</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span> <span class="ow">or</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="s2">"description"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">langchain_tool_kwargs</span><span class="p">:</span>
            <span class="n">langchain_tool_kwargs</span><span class="p">[</span><span class="s2">"description"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span>
        <span class="k">if</span> <span class="s2">"fn_schema"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">langchain_tool_kwargs</span><span class="p">:</span>
            <span class="n">langchain_tool_kwargs</span><span class="p">[</span><span class="s2">"args_schema"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">fn_schema</span>
        <span class="k">return</span> <span class="n">langchain_tool_kwargs</span>

    <span class="k">def</span> <span class="nf">to_langchain_tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Tool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To langchain tool."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Tool</span>

        <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
            <span class="n">langchain_tool_kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">Tool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
            <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">,</span>
            <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_langchain_structured_tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StructuredTool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To langchain structured tool."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">StructuredTool</span>

        <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
            <span class="n">langchain_tool_kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">StructuredTool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
            <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">,</span>
            <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_langchain\_tool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool.to_langchain_tool "Permanent link")

```
to_langchain_tool(**langchain_tool_kwargs: Any) -> Tool
```

To langchain tool.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
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
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_langchain_tool</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Tool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To langchain tool."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Tool</span>

    <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
        <span class="n">langchain_tool_kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">Tool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
        <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_langchain\_structured\_tool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool.to_langchain_structured_tool "Permanent link")

```
to_langchain_structured_tool(**langchain_tool_kwargs: Any) -> StructuredTool
```

To langchain structured tool.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">142</span>
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
<span class="normal">155</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_langchain_structured_tool</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StructuredTool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To langchain structured tool."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">StructuredTool</span>

    <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
        <span class="n">langchain_tool_kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">StructuredTool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
        <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ToolMetadata `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">ToolMetadata</span><span class="p">:</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="n">DefaultToolFnSchema</span>
    <span class="n">return_direct</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">get_parameters_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"object"</span><span class="p">,</span>
                <span class="s2">"properties"</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">"input"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="s2">"input query string"</span><span class="p">,</span> <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"string"</span><span class="p">},</span>
                <span class="p">},</span>
                <span class="s2">"required"</span><span class="p">:</span> <span class="p">[</span><span class="s2">"input"</span><span class="p">],</span>
            <span class="p">}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">parameters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn_schema</span><span class="o">.</span><span class="n">schema</span><span class="p">()</span>
            <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
                <span class="n">k</span><span class="p">:</span> <span class="n">v</span>
                <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">parameters</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"type"</span><span class="p">,</span> <span class="s2">"properties"</span><span class="p">,</span> <span class="s2">"required"</span><span class="p">,</span> <span class="s2">"definitions"</span><span class="p">]</span>
            <span class="p">}</span>
        <span class="k">return</span> <span class="n">parameters</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">fn_schema_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get fn schema as string."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"fn_schema is None."</span><span class="p">)</span>
        <span class="n">parameters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_parameters_dict</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">parameters</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get name."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"name is None."</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>

    <span class="nd">@deprecated</span><span class="p">(</span>
        <span class="s2">"Deprecated in favor of `to_openai_tool`, which should be used instead."</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">to_openai_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Deprecated and replaced by `to_openai_tool`.</span>
<span class="sd">        The name and arguments of a function that should be called, as generated by the</span>
<span class="sd">        model.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="s2">"description"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
            <span class="s2">"parameters"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_parameters_dict</span><span class="p">(),</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">to_openai_tool</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">skip_length_check</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""To OpenAI tool."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">skip_length_check</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1024</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Tool description exceeds maximum length of 1024 characters. "</span>
                <span class="s2">"Please shorten your description or move it to the prompt."</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"function"</span><span class="p">,</span>
            <span class="s2">"function"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                <span class="s2">"description"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
                <span class="s2">"parameters"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_parameters_dict</span><span class="p">(),</span>
            <span class="p">},</span>
        <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### fn\_schema\_str `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata.fn_schema_str "Permanent link")

```
fn_schema_str: str
```

Get fn schema as string.

### get\_name [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata.get_name "Permanent link")

```
get_name() -> str
```

Get name.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get name."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"name is None."</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
</code></pre></div></td></tr></tbody></table>

### to\_openai\_function [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata.to_openai_function "Permanent link")

```
to_openai_function() -> Dict[str, Any]
```

Deprecated and replaced by `to_openai_tool`. The name and arguments of a function that should be called, as generated by the model.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="p">(</span>
    <span class="s2">"Deprecated in favor of `to_openai_tool`, which should be used instead."</span>
<span class="p">)</span>
<span class="k">def</span> <span class="nf">to_openai_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Deprecated and replaced by `to_openai_tool`.</span>
<span class="sd">    The name and arguments of a function that should be called, as generated by the</span>
<span class="sd">    model.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="s2">"description"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
        <span class="s2">"parameters"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_parameters_dict</span><span class="p">(),</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### to\_openai\_tool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata.to_openai_tool "Permanent link")

```
to_openai_tool(skip_length_check: bool = False) -> Dict[str, Any]
```

To OpenAI tool.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_openai_tool</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">skip_length_check</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""To OpenAI tool."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">skip_length_check</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1024</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Tool description exceeds maximum length of 1024 characters. "</span>
            <span class="s2">"Please shorten your description or move it to the prompt."</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"function"</span><span class="p">,</span>
        <span class="s2">"function"</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">"name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="s2">"description"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
            <span class="s2">"parameters"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_parameters_dict</span><span class="p">(),</span>
        <span class="p">},</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

ToolOutput [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Tool output.

Source code in `llama-index-core/llama_index/core/tools/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 90</span>
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
<span class="normal">101</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ToolOutput</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tool output."""</span>

    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">raw_input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
    <span class="n">raw_output</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">is_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""String."""</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Graphql](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/)[Next Ionic shopping](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/)
