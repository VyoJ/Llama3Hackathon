Title: Keyword - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/

Markdown Content:
Keyword - LlamaIndex


KeywordExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/#llama_index.core.extractors.KeywordExtractor "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Keyword extractor. Node-level extractor. Extracts `excerpt_keywords` metadata field.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 
LLM



 | `None` |
| `keywords` | `int` | 

number of keywords to extract



 | `5` |
| `prompt_template` | `str` | 

template for keyword extraction



 | `DEFAULT_KEYWORD_EXTRACT_TEMPLATE` |

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
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
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword extractor. Node-level extractor. Extracts</span>
<span class="sd">    `excerpt_keywords` metadata field.</span>

<span class="sd">    Args:</span>
<span class="sd">        llm (Optional[LLM]): LLM</span>
<span class="sd">        keywords (int): number of keywords to extract</span>
<span class="sd">        prompt_template (str): template for keyword extraction</span>
<span class="sd">    """</span>

    <span class="n">llm</span><span class="p">:</span> <span class="n">LLMPredictorType</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The LLM to use for generation."</span><span class="p">)</span>
    <span class="n">keywords</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The number of keywords to extract."</span><span class="p">,</span> <span class="n">gt</span><span class="o">=</span><span class="mi">0</span>
    <span class="p">)</span>

    <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_KEYWORD_EXTRACT_TEMPLATE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Prompt template to use when generating keywords."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># TODO: llm_predictor arg is deprecated</span>
        <span class="n">llm_predictor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keywords</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_KEYWORD_EXTRACT_TEMPLATE</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_NUM_WORKERS</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">keywords</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"num_keywords must be &gt;= 1"</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_predictor</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">keywords</span><span class="o">=</span><span class="n">keywords</span><span class="p">,</span>
            <span class="n">prompt_template</span><span class="o">=</span><span class="n">prompt_template</span><span class="p">,</span>
            <span class="n">num_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"KeywordExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aextract_keywords_from_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords from a node and return it's metadata dict."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{}</span>

        <span class="n">context_str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">)</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">prompt_template</span><span class="p">),</span>
            <span class="n">keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">keywords</span><span class="p">,</span>
            <span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"excerpt_keywords"</span><span class="p">:</span> <span class="n">keywords</span><span class="o">.</span><span class="n">strip</span><span class="p">()}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="n">keyword_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">keyword_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_aextract_keywords_from_node</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>

        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">keyword_jobs</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/extractors/)[Next Marvin](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/)
