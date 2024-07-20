Title: Trulens eval packs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/

Markdown Content:
Trulens eval packs - LlamaIndex


TruLensHarmlessPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHarmlessPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

The TruLens-Eval Harmless LlamaPack show how to instrument and evaluate your LlamaIndex query engine. It launches starts a logging database and launches a dashboard in the background, builds an index over an input list of nodes, and instantiates and instruments a query engine over that index. It also instantiates the a suite of Harmless evals so that query is logged and evaluated for harmlessness.

Note: Using this LlamaPack requires that your OpenAI and HuggingFace API keys are set via the OPENAI\_API\_KEY and HUGGINGFACE\_API\_KEY environment variable.

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">115</span>
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
<span class="normal">240</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TruLensHarmlessPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    The TruLens-Eval Harmless LlamaPack show how to instrument and evaluate your LlamaIndex query</span>
<span class="sd">    engine. It launches starts a logging database and launches a dashboard in the background,</span>
<span class="sd">    builds an index over an input list of nodes, and instantiates and instruments a query engine</span>
<span class="sd">    over that index. It also instantiates the a suite of Harmless evals so that query is logged</span>
<span class="sd">    and evaluated for harmlessness.</span>

<span class="sd">    Note: Using this LlamaPack requires that your OpenAI and HuggingFace API keys are set via the</span>
<span class="sd">    OPENAI_API_KEY and HUGGINGFACE_API_KEY environment variable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">],</span>
        <span class="n">app_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes a new instance of TruLensEvalPack.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[TextNode]): An input list of nodes over which the index</span>
<span class="sd">            will be built.</span>
<span class="sd">            app_id (str): The application ID for the TruLensEvalPack.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">trulens_eval</span> <span class="kn">import</span> <span class="n">Feedback</span><span class="p">,</span> <span class="n">Tru</span><span class="p">,</span> <span class="n">TruLlama</span>
            <span class="kn">from</span> <span class="nn">trulens_eval.feedback.provider.openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"The trulens-eval package could not be found. "</span>
                <span class="s2">"Please install with `pip install trulens-eval`."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">app_id</span> <span class="o">=</span> <span class="n">app_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span> <span class="o">=</span> <span class="n">Tru</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="o">.</span><span class="n">run_dashboard</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

        <span class="c1"># Initialize provider class</span>
        <span class="n">provider</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">()</span>

        <span class="c1"># LLM-based feedback functions</span>
        <span class="n">f_controversiality</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">controversiality_with_cot_reasons</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Criminality"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_criminality</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">criminality_with_cot_reasons</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Controversiality"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_insensitivity</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">insensitivity_with_cot_reasons</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Insensitivity"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_maliciousness</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">maliciousness_with_cot_reasons</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Maliciousness"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>

        <span class="c1"># Moderation feedback functions</span>
        <span class="n">f_hate</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">moderation_hate</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Hate"</span><span class="p">,</span> <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_hatethreatening</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">moderation_hatethreatening</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Hate/Threatening"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_violent</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">moderation_violence</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Violent"</span><span class="p">,</span> <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_violentgraphic</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">moderation_violencegraphic</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"Violent/Graphic"</span><span class="p">,</span>
            <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_selfharm</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">moderation_selfharm</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Self Harm"</span><span class="p">,</span> <span class="n">higher_is_better</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>

        <span class="n">harmless_feedbacks</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">f_controversiality</span><span class="p">,</span>
            <span class="n">f_criminality</span><span class="p">,</span>
            <span class="n">f_insensitivity</span><span class="p">,</span>
            <span class="n">f_maliciousness</span><span class="p">,</span>
            <span class="n">f_hate</span><span class="p">,</span>
            <span class="n">f_hatethreatening</span><span class="p">,</span>
            <span class="n">f_violent</span><span class="p">,</span>
            <span class="n">f_violentgraphic</span><span class="p">,</span>
            <span class="n">f_selfharm</span><span class="p">,</span>
        <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="o">=</span> <span class="n">TruLlama</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">app_id</span><span class="o">=</span><span class="n">app_id</span><span class="p">,</span> <span class="n">feedbacks</span><span class="o">=</span><span class="n">harmless_feedbacks</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">            LlamaPack.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Runs queries against the index.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Any: A response from the query engine.</span>
<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHarmlessPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Returns a dictionary containing the internals of the LlamaPack.

**Returns:**

| Type | Description |
| --- | --- |
| `Dict[str, Any]` | 
Dict\[str, Any\]: A dictionary containing the internals of the



 |
| `Dict[str, Any]` | 

LlamaPack.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">217</span>
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
<span class="normal">230</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">        LlamaPack.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
        <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHarmlessPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Runs queries against the index.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | 
A response from the query engine.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Runs queries against the index.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Any: A response from the query engine.</span>
<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

TruLensHelpfulPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHelpfulPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

The TruLens-Eval Helpful LlamaPack show how to instrument and evaluate your LlamaIndex query engine. It launches starts a logging database and launches a dashboard in the background, builds an index over an input list of nodes, and instantiates and instruments a query engine over that index. It also instantiates the a suite of Helpful evals so that query is logged and evaluated for helpfulness.

Note: Using this LlamaPack requires that your OpenAI and HuggingFace API keys are set via the OPENAI\_API\_KEY and HUGGINGFACE\_API\_KEY environment variable.

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">243</span>
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
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TruLensHelpfulPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    The TruLens-Eval Helpful LlamaPack show how to instrument and evaluate your LlamaIndex query</span>
<span class="sd">    engine. It launches starts a logging database and launches a dashboard in the background,</span>
<span class="sd">    builds an index over an input list of nodes, and instantiates and instruments a query engine</span>
<span class="sd">    over that index. It also instantiates the a suite of Helpful evals so that query is logged</span>
<span class="sd">    and evaluated for helpfulness.</span>

<span class="sd">    Note: Using this LlamaPack requires that your OpenAI and HuggingFace API keys are set via the</span>
<span class="sd">    OPENAI_API_KEY and HUGGINGFACE_API_KEY environment variable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">],</span>
        <span class="n">app_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes a new instance of TruLensEvalPack.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[TextNode]): An input list of nodes over which the index</span>
<span class="sd">            will be built.</span>
<span class="sd">            app_id (str): The application ID for the TruLensEvalPack.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">trulens_eval</span> <span class="kn">import</span> <span class="n">Feedback</span><span class="p">,</span> <span class="n">Tru</span><span class="p">,</span> <span class="n">TruLlama</span>
            <span class="kn">from</span> <span class="nn">trulens_eval.feedback.provider.hugs</span> <span class="kn">import</span> <span class="n">Huggingface</span>
            <span class="kn">from</span> <span class="nn">trulens_eval.feedback.provider.openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"The trulens-eval package could not be found. "</span>
                <span class="s2">"Please install with `pip install trulens-eval`."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">app_id</span> <span class="o">=</span> <span class="n">app_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span> <span class="o">=</span> <span class="n">Tru</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="o">.</span><span class="n">run_dashboard</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

        <span class="c1"># Initialize provider class</span>
        <span class="n">provider</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">()</span>

        <span class="n">hugs_provider</span> <span class="o">=</span> <span class="n">Huggingface</span><span class="p">()</span>

        <span class="c1"># LLM-based feedback functions</span>
        <span class="n">f_coherence</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">coherence_with_cot_reasons</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Coherence"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_input_sentiment</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">sentiment_with_cot_reasons</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Input Sentiment"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_input</span><span class="p">()</span>
        <span class="n">f_output_sentiment</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">sentiment_with_cot_reasons</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Output Sentiment"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
        <span class="n">f_langmatch</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">hugs_provider</span><span class="o">.</span><span class="n">language_match</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Language Match"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_input_output</span><span class="p">()</span>

        <span class="n">helpful_feedbacks</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">f_coherence</span><span class="p">,</span>
            <span class="n">f_input_sentiment</span><span class="p">,</span>
            <span class="n">f_output_sentiment</span><span class="p">,</span>
            <span class="n">f_langmatch</span><span class="p">,</span>
        <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="o">=</span> <span class="n">TruLlama</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">app_id</span><span class="o">=</span><span class="n">app_id</span><span class="p">,</span> <span class="n">feedbacks</span><span class="o">=</span><span class="n">helpful_feedbacks</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">            LlamaPack.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Runs queries against the index.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Any: A response from the query engine.</span>
<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHelpfulPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Returns a dictionary containing the internals of the LlamaPack.

**Returns:**

| Type | Description |
| --- | --- |
| `Dict[str, Any]` | 
Dict\[str, Any\]: A dictionary containing the internals of the



 |
| `Dict[str, Any]` | 

LlamaPack.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">        LlamaPack.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
        <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensHelpfulPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Runs queries against the index.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | 
A response from the query engine.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Runs queries against the index.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Any: A response from the query engine.</span>
<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

TruLensRAGTriadPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensRAGTriadPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

The TruLens-Eval RAG Triad LlamaPack show how to instrument and evaluate your LlamaIndex query engine. It launches starts a logging database and launches a dashboard in the background, builds an index over an input list of nodes, and instantiates and instruments a query engine over that index. It also instantiates the RAG triad (groundedness, context relevance, answer relevance)' so that query is logged and evaluated by this triad for detecting hallucination.

Note: Using this LlamaPack requires that your OpenAI API key is set via the OPENAI\_API\_KEY environment variable.

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TruLensRAGTriadPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    The TruLens-Eval RAG Triad LlamaPack show how to instrument and evaluate your LlamaIndex query</span>
<span class="sd">    engine. It launches starts a logging database and launches a dashboard in the background,</span>
<span class="sd">    builds an index over an input list of nodes, and instantiates and instruments a query engine</span>
<span class="sd">    over that index. It also instantiates the RAG triad (groundedness, context relevance, answer relevance)'</span>
<span class="sd">    so that query is logged and evaluated by this triad for detecting hallucination.</span>

<span class="sd">    Note: Using this LlamaPack requires that your OpenAI API key is set via the</span>
<span class="sd">    OPENAI_API_KEY environment variable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">],</span>
        <span class="n">app_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes a new instance of TruLensEvalPack.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[TextNode]): An input list of nodes over which the index</span>
<span class="sd">            will be built.</span>
<span class="sd">            app_id (str): The application ID for the TruLensEvalPack.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">trulens_eval</span> <span class="kn">import</span> <span class="n">Feedback</span><span class="p">,</span> <span class="n">Tru</span><span class="p">,</span> <span class="n">TruLlama</span>
            <span class="kn">from</span> <span class="nn">trulens_eval.feedback</span> <span class="kn">import</span> <span class="n">Groundedness</span>
            <span class="kn">from</span> <span class="nn">trulens_eval.feedback.provider.openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"The trulens-eval package could not be found. "</span>
                <span class="s2">"Please install with `pip install trulens-eval`."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">app_id</span> <span class="o">=</span> <span class="n">app_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span> <span class="o">=</span> <span class="n">Tru</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="o">.</span><span class="n">run_dashboard</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

        <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

        <span class="c1"># Initialize provider class</span>
        <span class="n">provider</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">()</span>

        <span class="n">grounded</span> <span class="o">=</span> <span class="n">Groundedness</span><span class="p">(</span><span class="n">groundedness_provider</span><span class="o">=</span><span class="n">provider</span><span class="p">)</span>

        <span class="c1"># Define a groundedness feedback function</span>
        <span class="n">f_groundedness</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">Feedback</span><span class="p">(</span>
                <span class="n">grounded</span><span class="o">.</span><span class="n">groundedness_measure_with_cot_reasons</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Groundedness"</span>
            <span class="p">)</span>
            <span class="o">.</span><span class="n">on</span><span class="p">(</span><span class="n">TruLlama</span><span class="o">.</span><span class="n">select_source_nodes</span><span class="p">()</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">collect</span><span class="p">())</span>
            <span class="o">.</span><span class="n">on_output</span><span class="p">()</span>
            <span class="o">.</span><span class="n">aggregate</span><span class="p">(</span><span class="n">grounded</span><span class="o">.</span><span class="n">grounded_statements_aggregator</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># Question/answer relevance between overall question and answer.</span>
        <span class="n">f_qa_relevance</span> <span class="o">=</span> <span class="n">Feedback</span><span class="p">(</span>
            <span class="n">provider</span><span class="o">.</span><span class="n">relevance</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Answer Relevance"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">on_input_output</span><span class="p">()</span>

        <span class="c1"># Question/statement relevance between question and each context chunk.</span>
        <span class="n">f_context_relevance</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">Feedback</span><span class="p">(</span><span class="n">provider</span><span class="o">.</span><span class="n">qs_relevance</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">"Context Relevance"</span><span class="p">)</span>
            <span class="o">.</span><span class="n">on_input</span><span class="p">()</span>
            <span class="o">.</span><span class="n">on</span><span class="p">(</span><span class="n">TruLlama</span><span class="o">.</span><span class="n">select_source_nodes</span><span class="p">()</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">collect</span><span class="p">())</span>
            <span class="o">.</span><span class="n">aggregate</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">feedbacks</span> <span class="o">=</span> <span class="p">[</span><span class="n">f_groundedness</span><span class="p">,</span> <span class="n">f_qa_relevance</span><span class="p">,</span> <span class="n">f_context_relevance</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="o">=</span> <span class="n">TruLlama</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">app_id</span><span class="o">=</span><span class="n">app_id</span><span class="p">,</span> <span class="n">feedbacks</span><span class="o">=</span><span class="n">feedbacks</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">            LlamaPack.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Runs queries against the index.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Any: A response from the query engine.</span>
<span class="sd">        """</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensRAGTriadPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Returns a dictionary containing the internals of the LlamaPack.

**Returns:**

| Type | Description |
| --- | --- |
| `Dict[str, Any]` | 
Dict\[str, Any\]: A dictionary containing the internals of the



 |
| `Dict[str, Any]` | 

LlamaPack.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 89</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">        LlamaPack.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"session"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru</span><span class="p">,</span>
        <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="s2">"tru_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/#llama_index.packs.trulens_eval_packs.TruLensRAGTriadPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Runs queries against the index.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | 
A response from the query engine.



 |

Source code in `llama-index-packs/llama-index-packs-trulens-eval-packs/llama_index/packs/trulens_eval_packs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Runs queries against the index.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Any: A response from the query engine.</span>
<span class="sd">    """</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tru_query_engine</span> <span class="k">as</span> <span class="n">_</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Timescale vector autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/timescale_vector_autoretrieval/)[Next Vanna](https://docs.llamaindex.ai/en/stable/api_reference/packs/vanna/)
