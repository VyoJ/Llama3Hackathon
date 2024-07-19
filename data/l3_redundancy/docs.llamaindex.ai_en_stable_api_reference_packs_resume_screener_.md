Title: Resume screener - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/

Markdown Content:
Resume screener - LlamaIndex


ResumeScreenerPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/#llama_index.packs.resume_screener.ResumeScreenerPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-resume-screener/llama_index/packs/resume_screener/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ResumeScreenerPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">job_description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">criteria</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reader</span> <span class="o">=</span> <span class="n">PDFReader</span><span class="p">()</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span> <span class="o">=</span> <span class="n">TreeSummarize</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">ResumeScreenerDecision</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>
        <span class="n">criteria_str</span> <span class="o">=</span> <span class="n">_format_criteria_str</span><span class="p">(</span><span class="n">criteria</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query</span> <span class="o">=</span> <span class="n">QUERY_TEMPLATE</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">job_description</span><span class="o">=</span><span class="n">job_description</span><span class="p">,</span> <span class="n">criteria_str</span><span class="o">=</span><span class="n">criteria_str</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"reader"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="p">,</span> <span class="s2">"synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resume_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run pack."""</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">resume_path</span><span class="p">))</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">doc</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">)</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">output</span><span class="o">.</span><span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/#llama_index.packs.resume_screener.ResumeScreenerPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-resume-screener/llama_index/packs/resume_screener/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"reader"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="p">,</span> <span class="s2">"synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/#llama_index.packs.resume_screener.ResumeScreenerPack.run "Permanent link")

```
run(resume_path: str, *args: Any, **kwargs: Any) -> Any
```

Run pack.

Source code in `llama-index-packs/llama-index-packs-resume-screener/llama_index/packs/resume_screener/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resume_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run pack."""</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">resume_path</span><span class="p">))</span>
    <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
        <span class="n">nodes</span><span class="o">=</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">doc</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">)</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">],</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">output</span><span class="o">.</span><span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Redis ingestion pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/)[Next Retry engine weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/retry_engine_weaviate/)
