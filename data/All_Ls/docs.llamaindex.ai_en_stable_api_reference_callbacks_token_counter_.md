Title: Token counter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/

Markdown Content:
Token counter - LlamaIndex


TokenCountingHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PythonicallyPrintingBaseHandler`

Callback handler for counting tokens in LLM and Embedding events.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tokenizer` | `Optional[Callable[[str], List]]` | 
Tokenizer to use. Defaults to the global tokenizer (see llama\_index.core.utils.globals\_helper).



 | `None` |
| `event_starts_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

List of event types to ignore at the start of a trace.



 | `None` |
| `event_ends_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

List of event types to ignore at the end of a trace.



 | `None` |

Source code in `llama-index-core/llama_index/core/callbacks/token_counting.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 96</span>
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
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
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
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TokenCountingHandler</span><span class="p">(</span><span class="n">PythonicallyPrintingBaseHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback handler for counting tokens in LLM and Embedding events.</span>

<span class="sd">    Args:</span>
<span class="sd">        tokenizer:</span>
<span class="sd">            Tokenizer to use. Defaults to the global tokenizer</span>
<span class="sd">            (see llama_index.core.utils.globals_helper).</span>
<span class="sd">        event_starts_to_ignore: List of event types to ignore at the start of a trace.</span>
<span class="sd">        event_ends_to_ignore: List of event types to ignore at the end of a trace.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_starts_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_ends_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">logger</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TokenCountingEvent</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TokenCountingEvent</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_token_counter</span> <span class="o">=</span> <span class="n">TokenCounter</span><span class="p">(</span><span class="n">tokenizer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="n">event_starts_to_ignore</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="n">event_ends_to_ignore</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">logger</span><span class="o">=</span><span class="n">logger</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">event_id</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Count the LLM or Embedding tokens as needed."""</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span>
            <span class="ow">and</span> <span class="n">event_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">event_ends_to_ignore</span>
            <span class="ow">and</span> <span class="n">payload</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="n">total_chunk_tokens</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">,</span> <span class="p">[]):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">TokenCountingEvent</span><span class="p">(</span>
                        <span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">,</span>
                        <span class="n">prompt</span><span class="o">=</span><span class="n">chunk</span><span class="p">,</span>
                        <span class="n">prompt_token_count</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_token_counter</span><span class="o">.</span><span class="n">get_string_tokens</span><span class="p">(</span><span class="n">chunk</span><span class="p">),</span>
                        <span class="n">completion</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                        <span class="n">completion_token_count</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
                <span class="n">total_chunk_tokens</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">total_token_count</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Embedding Token Usage: </span><span class="si">{</span><span class="n">total_chunk_tokens</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">total_llm_token_count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the current total LLM token count."""</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">x</span><span class="o">.</span><span class="n">total_token_count</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span><span class="p">])</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">prompt_llm_token_count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the current total LLM prompt token count."""</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">x</span><span class="o">.</span><span class="n">prompt_token_count</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span><span class="p">])</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">completion_llm_token_count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the current total LLM completion token count."""</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">x</span><span class="o">.</span><span class="n">completion_token_count</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span><span class="p">])</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">total_embedding_token_count</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the current total Embedding token count."""</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">x</span><span class="o">.</span><span class="n">total_token_count</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">reset_counts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset the token counts."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span> <span class="o">=</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

### total\_llm\_token\_count `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.total_llm_token_count "Permanent link")

```
total_llm_token_count: int
```

Get the current total LLM token count.

### prompt\_llm\_token\_count `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.prompt_llm_token_count "Permanent link")

```
prompt_llm_token_count: int
```

Get the current total LLM prompt token count.

### completion\_llm\_token\_count `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.completion_llm_token_count "Permanent link")

```
completion_llm_token_count: int
```

Get the current total LLM completion token count.

### total\_embedding\_token\_count `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.total_embedding_token_count "Permanent link")

```
total_embedding_token_count: int
```

Get the current total Embedding token count.

### on\_event\_end [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.on_event_end "Permanent link")

```
on_event_end(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', **kwargs: Any) -> None
```

Count the LLM or Embedding tokens as needed.

Source code in `llama-index-core/llama_index/core/callbacks/token_counting.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
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
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Count the LLM or Embedding tokens as needed."""</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">event_type</span> <span class="o"></span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">EMBEDDING</span>
        <span class="ow">and</span> <span class="n">event_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">event_ends_to_ignore</span>
        <span class="ow">and</span> <span class="n">payload</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="n">total_chunk_tokens</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">TokenCountingEvent</span><span class="p">(</span>
                    <span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">,</span>
                    <span class="n">prompt</span><span class="o">=</span><span class="n">chunk</span><span class="p">,</span>
                    <span class="n">prompt_token_count</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_token_counter</span><span class="o">.</span><span class="n">get_string_tokens</span><span class="p">(</span><span class="n">chunk</span><span class="p">),</span>
                    <span class="n">completion</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                    <span class="n">completion_token_count</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="n">total_chunk_tokens</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">total_token_count</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Embedding Token Usage: </span><span class="si">{</span><span class="n">total_chunk_tokens</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### reset\_counts [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/#llama_index.core.callbacks.token_counting.TokenCountingHandler.reset_counts "Permanent link")

```
reset_counts() -> None
```

Reset the token counts.

Source code in `llama-index-core/llama_index/core/callbacks/token_counting.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">reset_counts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset the token counts."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">llm_token_counts</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">embedding_token_counts</span> <span class="o">=</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Promptlayer](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/)[Next Uptrain](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/)
