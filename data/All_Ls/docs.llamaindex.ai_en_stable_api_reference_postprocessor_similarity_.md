Title: Similarity - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/

Markdown Content:
Similarity - LlamaIndex


Node PostProcessor module.

SimilarityPostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/#llama_index.core.postprocessor.SimilarityPostprocessor "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Similarity-based Node processor.

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
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
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimilarityPostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Similarity-based Node processor."""</span>

    <span class="n">similarity_cutoff</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SimilarityPostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="n">sim_cutoff_exists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_cutoff</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">should_use_node</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">if</span> <span class="n">sim_cutoff_exists</span><span class="p">:</span>
                <span class="n">similarity</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">score</span>
                <span class="k">if</span> <span class="n">similarity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">should_use_node</span> <span class="o">=</span> <span class="kc">False</span>
                <span class="k">elif</span> <span class="n">cast</span><span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">similarity</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">cast</span><span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_cutoff</span><span class="p">):</span>
                    <span class="n">should_use_node</span> <span class="o">=</span> <span class="kc">False</span>

            <span class="k">if</span> <span class="n">should_use_node</span><span class="p">:</span>
                <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sentence optimizer](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/)[Next Time weighted](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/time_weighted/)
