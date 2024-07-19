Title: Dataset generation - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/

Markdown Content:
Dataset generation - LlamaIndex


Evaluation modules.

DatasetGenerator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PromptMixin`

Generate dataset (question/ question-answer pairs) based on the given documents.

NOTE: this is a beta feature, subject to change!

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[Node]` | 
List of nodes. (Optional)



 | _required_ |
| `llm` | `[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")` | 

Language model.



 | `None` |
| `callback_manager` | `[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")` | 

Callback manager.



 | `None` |
| `num_questions_per_chunk` | `int` | 

number of question to be generated per chunk. Each document is chunked of size 512 words.



 | `10` |
| `text_question_template` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate") | None` | 

Question generation template.



 | `None` |
| `question_gen_query` | `str | None` | 

Question generation query.



 | `None` |

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

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
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="p">(</span>
    <span class="s2">"Deprecated in favor of `RagDatasetGenerator` which should be used instead."</span><span class="p">,</span>
    <span class="n">action</span><span class="o">=</span><span class="s2">"always"</span><span class="p">,</span>
<span class="p">)</span>
<span class="k">class</span> <span class="nc">DatasetGenerator</span><span class="p">(</span><span class="n">PromptMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Generate dataset (question/ question-answer pairs) \</span>
<span class="sd">    based on the given documents.</span>

<span class="sd">    NOTE: this is a beta feature, subject to change!</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[Node]): List of nodes. (Optional)</span>
<span class="sd">        llm (LLM): Language model.</span>
<span class="sd">        callback_manager (CallbackManager): Callback manager.</span>
<span class="sd">        num_questions_per_chunk: number of question to be \</span>
<span class="sd">        generated per chunk. Each document is chunked of size 512 words.</span>
<span class="sd">        text_question_template: Question generation template.</span>
<span class="sd">        question_gen_query: Question generation query.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_questions_per_chunk</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">text_question_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">question_gen_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">ServiceContext</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">text_question_template</span> <span class="o">=</span> <span class="n">text_question_template</span> <span class="ow">or</span> <span class="n">PromptTemplate</span><span class="p">(</span>
            <span class="n">DEFAULT_QUESTION_GENERATION_PROMPT</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">text_qa_template</span> <span class="o">=</span> <span class="n">text_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">question_gen_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">question_gen_query</span>
            <span class="ow">or</span> <span class="sa">f</span><span class="s2">"You are a Teacher/Professor. Your task is to setup </span><span class="se">\</span>
<span class="s2">                        </span><span class="si">{</span><span class="n">num_questions_per_chunk</span><span class="si">}</span><span class="s2"> questions for an upcoming </span><span class="se">\</span>
<span class="s2">                        quiz/examination. The questions should be diverse in nature </span><span class="se">\</span>
<span class="s2">                            across the document. Restrict the questions to the </span><span class="se">\</span>
<span class="s2">                                context information provided."</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span> <span class="o">=</span> <span class="n">nodes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_mode</span> <span class="o">=</span> <span class="n">metadata_mode</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_questions_per_chunk</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">text_question_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">question_gen_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">required_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">exclude_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">ServiceContext</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DatasetGenerator</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate dataset from documents."""</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="n">transformations_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span> <span class="n">transformations</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span>
        <span class="p">)</span>

        <span class="c1"># use node postprocessor to filter nodes</span>
        <span class="n">required_keywords</span> <span class="o">=</span> <span class="n">required_keywords</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">exclude_keywords</span> <span class="o">=</span> <span class="n">exclude_keywords</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">node_postprocessor</span> <span class="o">=</span> <span class="n">KeywordNodePostprocessor</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">required_keywords</span><span class="o">=</span><span class="n">required_keywords</span><span class="p">,</span>
            <span class="n">exclude_keywords</span><span class="o">=</span><span class="n">exclude_keywords</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">node_with_scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="n">node_with_scores</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span><span class="n">node_with_scores</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">node_with_scores</span><span class="p">]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">num_questions_per_chunk</span><span class="o">=</span><span class="n">num_questions_per_chunk</span><span class="p">,</span>
            <span class="n">text_question_template</span><span class="o">=</span><span class="n">text_question_template</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">question_gen_query</span><span class="o">=</span><span class="n">question_gen_query</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_agenerate_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">generate_response</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Node question generator."""</span>
        <span class="n">query_tasks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Coroutine</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">responses_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">tqdm.asyncio</span> <span class="kn">import</span> <span class="n">tqdm_asyncio</span>

            <span class="n">async_module</span> <span class="o">=</span> <span class="n">tqdm_asyncio</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">async_module</span> <span class="o">=</span> <span class="n">asyncio</span>

        <span class="n">summary_indices</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SummaryIndex</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">num</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_tasks</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">num</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_mode</span><span class="p">),</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">],</span>
                <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
                <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
                <span class="n">text_qa_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_question_template</span><span class="p">,</span>
                <span class="n">use_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">task</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">question_gen_query</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">query_tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">task</span><span class="p">)</span>
            <span class="n">summary_indices</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>

        <span class="n">responses</span> <span class="o">=</span> <span class="k">await</span> <span class="n">async_module</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">query_tasks</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">response</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">responses</span><span class="p">):</span>
            <span class="n">result</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">cleaned_questions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^\d+[\).\s]"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">question</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">question</span> <span class="ow">in</span> <span class="n">result</span>
            <span class="p">]</span>
            <span class="n">cleaned_questions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">question</span> <span class="k">for</span> <span class="n">question</span> <span class="ow">in</span> <span class="n">cleaned_questions</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">question</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
            <span class="p">]</span>
            <span class="n">cur_queries</span> <span class="o">=</span> <span class="p">{</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()):</span> <span class="n">question</span> <span class="k">for</span> <span class="n">question</span> <span class="ow">in</span> <span class="n">cleaned_questions</span>
            <span class="p">}</span>
            <span class="n">queries</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cur_queries</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">generate_response</span><span class="p">:</span>
                <span class="n">index</span> <span class="o">=</span> <span class="n">summary_indices</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
                <span class="n">qr_tasks</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="n">cur_query_items</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">cur_queries</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
                <span class="n">cur_query_keys</span> <span class="o">=</span> <span class="p">[</span><span class="n">query_id</span> <span class="k">for</span> <span class="n">query_id</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">cur_query_items</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">query_id</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">cur_query_items</span><span class="p">:</span>
                    <span class="n">qa_query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
                        <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
                        <span class="n">text_qa_template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_qa_template</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="n">qr_task</span> <span class="o">=</span> <span class="n">qa_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
                    <span class="n">qr_tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">qr_task</span><span class="p">)</span>
                <span class="n">qr_responses</span> <span class="o">=</span> <span class="k">await</span> <span class="n">async_module</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">qr_tasks</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">query_id</span><span class="p">,</span> <span class="n">qa_response</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">cur_query_keys</span><span class="p">,</span> <span class="n">qr_responses</span><span class="p">):</span>
                    <span class="n">responses_dict</span><span class="p">[</span><span class="n">query_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">qa_response</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">pass</span>

        <span class="n">query_ids</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">queries</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">num</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_ids</span> <span class="o">=</span> <span class="n">query_ids</span><span class="p">[:</span><span class="n">num</span><span class="p">]</span>
            <span class="c1"># truncate queries, responses to the subset of query ids</span>
            <span class="n">queries</span> <span class="o">=</span> <span class="p">{</span><span class="n">query_id</span><span class="p">:</span> <span class="n">queries</span><span class="p">[</span><span class="n">query_id</span><span class="p">]</span> <span class="k">for</span> <span class="n">query_id</span> <span class="ow">in</span> <span class="n">query_ids</span><span class="p">}</span>
            <span class="k">if</span> <span class="n">generate_response</span><span class="p">:</span>
                <span class="n">responses_dict</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="n">query_id</span><span class="p">:</span> <span class="n">responses_dict</span><span class="p">[</span><span class="n">query_id</span><span class="p">]</span> <span class="k">for</span> <span class="n">query_id</span> <span class="ow">in</span> <span class="n">query_ids</span>
                <span class="p">}</span>

        <span class="k">return</span> <span class="n">QueryResponseDataset</span><span class="p">(</span><span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="o">=</span><span class="n">responses_dict</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_questions_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Generates questions for each document."""</span>
        <span class="n">dataset</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_dataset</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">,</span> <span class="n">generate_response</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">dataset</span><span class="o">.</span><span class="n">questions</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_dataset_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generates questions for each document."""</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_dataset</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">,</span> <span class="n">generate_response</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate_questions_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Generates questions for each document."""</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agenerate_questions_from_nodes</span><span class="p">(</span><span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">generate_dataset_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generates questions for each document."""</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agenerate_dataset_from_nodes</span><span class="p">(</span><span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"text_question_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_question_template</span><span class="p">,</span>
            <span class="s2">"text_qa_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_qa_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"text_question_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">text_question_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"text_question_template"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"text_qa_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">text_qa_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"text_qa_template"</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### from\_documents `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator.from_documents "Permanent link")

```
from_documents(documents: List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, transformations: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, num_questions_per_chunk: int = 10, text_question_template: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate") | None = None, text_qa_template: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate") | None = None, question_gen_query: str | None = None, required_keywords: List[str] | None = None, exclude_keywords: List[str] | None = None, show_progress: bool = False, service_context: ServiceContext | None = None) -> [DatasetGenerator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator "llama_index.core.evaluation.dataset_generation.DatasetGenerator")
```

Generate dataset from documents.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">172</span>
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
<span class="normal">225</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">num_questions_per_chunk</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">text_question_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">question_gen_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">required_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">exclude_keywords</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="c1"># deprecated</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">ServiceContext</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DatasetGenerator</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate dataset from documents."""</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
    <span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="n">transformations_from_settings_or_context</span><span class="p">(</span>
        <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
    <span class="p">)</span>
    <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">callback_manager</span>
        <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="n">run_transformations</span><span class="p">(</span>
        <span class="n">documents</span><span class="p">,</span> <span class="n">transformations</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span>
    <span class="p">)</span>

    <span class="c1"># use node postprocessor to filter nodes</span>
    <span class="n">required_keywords</span> <span class="o">=</span> <span class="n">required_keywords</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">exclude_keywords</span> <span class="o">=</span> <span class="n">exclude_keywords</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">node_postprocessor</span> <span class="o">=</span> <span class="n">KeywordNodePostprocessor</span><span class="p">(</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">required_keywords</span><span class="o">=</span><span class="n">required_keywords</span><span class="p">,</span>
        <span class="n">exclude_keywords</span><span class="o">=</span><span class="n">exclude_keywords</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">node_with_scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
    <span class="n">node_with_scores</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span><span class="n">node_with_scores</span><span class="p">)</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">node_with_scores</span><span class="p">]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">num_questions_per_chunk</span><span class="o">=</span><span class="n">num_questions_per_chunk</span><span class="p">,</span>
        <span class="n">text_question_template</span><span class="o">=</span><span class="n">text_question_template</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
        <span class="n">question_gen_query</span><span class="o">=</span><span class="n">question_gen_query</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### agenerate\_questions\_from\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator.agenerate_questions_from_nodes "Permanent link")

```
agenerate_questions_from_nodes(num: int | None = None) -> List[str]
```

Generates questions for each document.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_questions_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Generates questions for each document."""</span>
    <span class="n">dataset</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">,</span> <span class="n">generate_response</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">dataset</span><span class="o">.</span><span class="n">questions</span>
</code></pre></div></td></tr></tbody></table>

### agenerate\_dataset\_from\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator.agenerate_dataset_from_nodes "Permanent link")

```
agenerate_dataset_from_nodes(num: int | None = None) -> [QueryResponseDataset](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset "llama_index.core.evaluation.dataset_generation.QueryResponseDataset")
```

Generates questions for each document.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_dataset_from_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generates questions for each document."""</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agenerate_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">,</span> <span class="n">generate_response</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### generate\_questions\_from\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator.generate_questions_from_nodes "Permanent link")

```
generate_questions_from_nodes(num: int | None = None) -> List[str]
```

Generates questions for each document.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_questions_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Generates questions for each document."""</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agenerate_questions_from_nodes</span><span class="p">(</span><span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### generate\_dataset\_from\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.DatasetGenerator.generate_dataset_from_nodes "Permanent link")

```
generate_dataset_from_nodes(num: int | None = None) -> [QueryResponseDataset](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset "llama_index.core.evaluation.dataset_generation.QueryResponseDataset")
```

Generates questions for each document.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_dataset_from_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generates questions for each document."""</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agenerate_dataset_from_nodes</span><span class="p">(</span><span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

QueryResponseDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Query Response Dataset.

The response can be empty if the dataset is generated from documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `queries` | `Dict[str, str]` | 
Query id -> query.



 | _required_ |
| `responses` | `Dict[str, str]` | 

Query id -> response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 51</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="p">(</span>
    <span class="s2">"Deprecated in favor of `LabelledRagDataset` which should be used instead."</span><span class="p">,</span>
    <span class="n">action</span><span class="o">=</span><span class="s2">"always"</span><span class="p">,</span>
<span class="p">)</span>
<span class="k">class</span> <span class="nc">QueryResponseDataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Query Response Dataset.</span>

<span class="sd">    The response can be empty if the dataset is generated from documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        queries (Dict[str, str]): Query id -&gt; query.</span>
<span class="sd">        responses (Dict[str, str]): Query id -&gt; response.</span>

<span class="sd">    """</span>

    <span class="n">queries</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Query id -&gt; query"</span>
    <span class="p">)</span>
    <span class="n">responses</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Query id -&gt; response"</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_qr_pairs</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">qr_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create from qr pairs."""</span>
        <span class="c1"># define ids as simple integers</span>
        <span class="n">queries</span> <span class="o">=</span> <span class="p">{</span><span class="nb">str</span><span class="p">(</span><span class="n">idx</span><span class="p">):</span> <span class="n">query</span> <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">_</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">qr_pairs</span><span class="p">)}</span>
        <span class="n">responses</span> <span class="o">=</span> <span class="p">{</span><span class="nb">str</span><span class="p">(</span><span class="n">idx</span><span class="p">):</span> <span class="n">response</span> <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">qr_pairs</span><span class="p">)}</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">qr_pairs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get pairs."""</span>
        <span class="c1"># if query_id not in response, throw error</span>
        <span class="k">for</span> <span class="n">query_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">queries</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">query_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">responses</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query id </span><span class="si">{</span><span class="n">query_id</span><span class="si">}</span><span class="s2"> not in responses"</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">queries</span><span class="p">[</span><span class="n">query_id</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">responses</span><span class="p">[</span><span class="n">query_id</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">query_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">queries</span>
        <span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">questions</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get questions."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">queries</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Save json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### qr\_pairs `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset.qr_pairs "Permanent link")

```
qr_pairs: List[Tuple[str, str]]
```

Get pairs.

### questions `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset.questions "Permanent link")

```
questions: List[str]
```

Get questions.

### from\_qr\_pairs `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset.from_qr_pairs "Permanent link")

```
from_qr_pairs(qr_pairs: List[Tuple[str, str]]) -> [QueryResponseDataset](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset "llama_index.core.evaluation.dataset_generation.QueryResponseDataset")
```

Create from qr pairs.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_qr_pairs</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">qr_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create from qr pairs."""</span>
    <span class="c1"># define ids as simple integers</span>
    <span class="n">queries</span> <span class="o">=</span> <span class="p">{</span><span class="nb">str</span><span class="p">(</span><span class="n">idx</span><span class="p">):</span> <span class="n">query</span> <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">_</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">qr_pairs</span><span class="p">)}</span>
    <span class="n">responses</span> <span class="o">=</span> <span class="p">{</span><span class="nb">str</span><span class="p">(</span><span class="n">idx</span><span class="p">):</span> <span class="n">response</span> <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">qr_pairs</span><span class="p">)}</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### save\_json [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset.save_json "Permanent link")

```
save_json(path: str) -> None
```

Save json.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Save json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_json `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset.from_json "Permanent link")

```
from_json(path: str) -> [QueryResponseDataset](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/#llama_index.core.evaluation.QueryResponseDataset "llama_index.core.evaluation.dataset_generation.QueryResponseDataset")
```

Load json.

Source code in `llama-index-core/llama_index/core/evaluation/dataset_generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryResponseDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Correctness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/)[Next Faithfullness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/)
