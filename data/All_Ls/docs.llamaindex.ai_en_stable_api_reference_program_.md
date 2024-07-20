Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/

Markdown Content:
Index - LlamaIndex


BasePydanticProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/#llama_index.core.types.BasePydanticProgram "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `DispatcherSpanMixin`, `ABC`, `Generic[Model]`

A base class for LLM-powered function that return a pydantic model.

Note: this interface is not yet stable.

Source code in `llama-index-core/llama_index/core/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">60</span>
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
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BasePydanticProgram</span><span class="p">(</span><span class="n">DispatcherSpanMixin</span><span class="p">,</span> <span class="n">ABC</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">Model</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""A base class for LLM-powered function that return a pydantic model.</span>

<span class="sd">    Note: this interface is not yet stable.</span>
<span class="sd">    """</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Model</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Model</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Guidance](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/)[Next Llm text completion](https://docs.llamaindex.ai/en/stable/api_reference/program/llm_text_completion/)
