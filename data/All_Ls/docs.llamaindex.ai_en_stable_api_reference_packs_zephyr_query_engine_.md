Title: Zephyr query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/

Markdown Content:
Zephyr query engine - LlamaIndex


ZephyrQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/#llama_index.packs.zephyr_query_engine.ZephyrQueryEnginePack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-zephyr-query-engine/llama_index/packs/zephyr_query_engine/base.py`

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
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ZephyrQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">torch</span>
            <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">BitsAndBytesConfig</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Dependencies missing, run "</span>
                <span class="s2">"`pip install torch transformers accelerate bitsandbytes`"</span>
            <span class="p">)</span>

        <span class="n">quantization_config</span> <span class="o">=</span> <span class="n">BitsAndBytesConfig</span><span class="p">(</span>
            <span class="n">load_in_4bit</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">bnb_4bit_compute_dtype</span><span class="o">=</span><span class="n">torch</span><span class="o">.</span><span class="n">float16</span><span class="p">,</span>
            <span class="n">bnb_4bit_quant_type</span><span class="o">=</span><span class="s2">"nf4"</span><span class="p">,</span>
            <span class="n">bnb_4bit_use_double_quant</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">HuggingFaceLLM</span><span class="p">(</span>
                <span class="n">model_name</span><span class="o">=</span><span class="s2">"HuggingFaceH4/zephyr-7b-beta"</span><span class="p">,</span>
                <span class="n">tokenizer_name</span><span class="o">=</span><span class="s2">"HuggingFaceH4/zephyr-7b-beta"</span><span class="p">,</span>
                <span class="n">query_wrapper_prompt</span><span class="o">=</span><span class="n">PromptTemplate</span><span class="p">(</span>
                    <span class="s2">"&lt;|system|&gt;</span><span class="se">\n</span><span class="s2">&lt;/s&gt;</span><span class="se">\n</span><span class="s2">&lt;|user|&gt;</span><span class="se">\n</span><span class="si">{query_str}</span><span class="s2">&lt;/s&gt;</span><span class="se">\n</span><span class="s2">&lt;|assistant|&gt;</span><span class="se">\n</span><span class="s2">"</span>
                <span class="p">),</span>
                <span class="n">context_window</span><span class="o">=</span><span class="mi">3900</span><span class="p">,</span>
                <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">256</span><span class="p">,</span>
                <span class="n">model_kwargs</span><span class="o">=</span><span class="p">{</span><span class="s2">"quantization_config"</span><span class="p">:</span> <span class="n">quantization_config</span><span class="p">},</span>
                <span class="n">generate_kwargs</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"do_sample"</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                    <span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">0.7</span><span class="p">,</span>
                    <span class="s2">"top_k"</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
                    <span class="s2">"top_p"</span><span class="p">:</span> <span class="mf">0.95</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="n">device_map</span><span class="o">=</span><span class="s2">"auto"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span>
                <span class="s2">"Failed to load and quantize model, likely due to CUDA being missing. "</span>
                <span class="s2">"Loading full precision model instead."</span>
            <span class="p">)</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">HuggingFaceLLM</span><span class="p">(</span>
                <span class="n">model_name</span><span class="o">=</span><span class="s2">"HuggingFaceH4/zephyr-7b-beta"</span><span class="p">,</span>
                <span class="n">tokenizer_name</span><span class="o">=</span><span class="s2">"HuggingFaceH4/zephyr-7b-beta"</span><span class="p">,</span>
                <span class="n">query_wrapper_prompt</span><span class="o">=</span><span class="n">PromptTemplate</span><span class="p">(</span>
                    <span class="s2">"&lt;|system|&gt;</span><span class="se">\n</span><span class="s2">&lt;/s&gt;</span><span class="se">\n</span><span class="s2">&lt;|user|&gt;</span><span class="se">\n</span><span class="si">{query_str}</span><span class="s2">&lt;/s&gt;</span><span class="se">\n</span><span class="s2">&lt;|assistant|&gt;</span><span class="se">\n</span><span class="s2">"</span>
                <span class="p">),</span>
                <span class="n">context_window</span><span class="o">=</span><span class="mi">3900</span><span class="p">,</span>
                <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">256</span><span class="p">,</span>
                <span class="n">generate_kwargs</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"do_sample"</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                    <span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">0.7</span><span class="p">,</span>
                    <span class="s2">"top_k"</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
                    <span class="s2">"top_p"</span><span class="p">:</span> <span class="mf">0.95</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="n">device_map</span><span class="o">=</span><span class="s2">"auto"</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="c1"># set tokenizer for proper token counting</span>
        <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">AutoTokenizer</span>

        <span class="n">tokenizer</span> <span class="o">=</span> <span class="n">AutoTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"HuggingFaceH4/zephyr-7b-beta"</span><span class="p">)</span>
        <span class="n">set_global_tokenizer</span><span class="p">(</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">encode</span><span class="p">)</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="s2">"local:BAAI/bge-base-en-v1.5"</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/#llama_index.packs.zephyr_query_engine.ZephyrQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-zephyr-query-engine/llama_index/packs/zephyr_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/#llama_index.packs.zephyr_query_engine.ZephyrQueryEnginePack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-zephyr-query-engine/llama_index/packs/zephyr_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Zenguard](https://docs.llamaindex.ai/en/stable/api_reference/packs/zenguard/)[Next Chat memory buffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/)
