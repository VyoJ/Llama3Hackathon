Title: Rag fusion query pipeline - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/

Markdown Content:
Rag fusion query pipeline - LlamaIndex


RAGFusionPipelinePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/#llama_index.packs.rag_fusion_query_pipeline.RAGFusionPipelinePack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

RAG Fusion pipeline.

Create a bunch of vector indexes of different chunk sizes.

Source code in `llama-index-packs/llama-index-packs-rag-fusion-query-pipeline/llama_index/packs/rag_fusion_query_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 56</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RAGFusionPipelinePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAG Fusion pipeline.</span>

<span class="sd">    Create a bunch of vector indexes of different chunk sizes.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">chunk_sizes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">documents</span> <span class="o">=</span> <span class="n">documents</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chunk_sizes</span> <span class="o">=</span> <span class="n">chunk_sizes</span> <span class="ow">or</span> <span class="n">DEFAULT_CHUNK_SIZES</span>

        <span class="c1"># construct index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engines</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">retrievers</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">chunk_size</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_sizes</span><span class="p">:</span>
            <span class="n">splitter</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

            <span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_engines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">))</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">retrievers</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk_size</span><span class="p">)]</span> <span class="o">=</span> <span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">()</span>

        <span class="c1"># define rerank component</span>
        <span class="n">rerank_component</span> <span class="o">=</span> <span class="n">FnComponent</span><span class="p">(</span><span class="n">fn</span><span class="o">=</span><span class="n">reciprocal_rank_fusion</span><span class="p">)</span>

        <span class="c1"># construct query pipeline</span>
        <span class="n">p</span> <span class="o">=</span> <span class="n">QueryPipeline</span><span class="p">()</span>
        <span class="n">module_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">retrievers</span><span class="p">,</span>
            <span class="s2">"input"</span><span class="p">:</span> <span class="n">InputComponent</span><span class="p">(),</span>
            <span class="s2">"summarizer"</span><span class="p">:</span> <span class="n">TreeSummarize</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">),</span>
            <span class="c1"># NOTE: Join args</span>
            <span class="s2">"join"</span><span class="p">:</span> <span class="n">ArgPackComponent</span><span class="p">(),</span>
            <span class="s2">"reranker"</span><span class="p">:</span> <span class="n">rerank_component</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">p</span><span class="o">.</span><span class="n">add_modules</span><span class="p">(</span><span class="n">module_dict</span><span class="p">)</span>
        <span class="c1"># add links from input to retriever (id'ed by chunk_size)</span>
        <span class="k">for</span> <span class="n">chunk_size</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_sizes</span><span class="p">:</span>
            <span class="n">p</span><span class="o">.</span><span class="n">add_link</span><span class="p">(</span><span class="s2">"input"</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">chunk_size</span><span class="p">))</span>
            <span class="n">p</span><span class="o">.</span><span class="n">add_link</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk_size</span><span class="p">),</span> <span class="s2">"join"</span><span class="p">,</span> <span class="n">dest_key</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk_size</span><span class="p">))</span>
        <span class="n">p</span><span class="o">.</span><span class="n">add_link</span><span class="p">(</span><span class="s2">"join"</span><span class="p">,</span> <span class="s2">"reranker"</span><span class="p">)</span>
        <span class="n">p</span><span class="o">.</span><span class="n">add_link</span><span class="p">(</span><span class="s2">"input"</span><span class="p">,</span> <span class="s2">"summarizer"</span><span class="p">,</span> <span class="n">dest_key</span><span class="o">=</span><span class="s2">"query_str"</span><span class="p">)</span>
        <span class="n">p</span><span class="o">.</span><span class="n">add_link</span><span class="p">(</span><span class="s2">"reranker"</span><span class="p">,</span> <span class="s2">"summarizer"</span><span class="p">,</span> <span class="n">dest_key</span><span class="o">=</span><span class="s2">"nodes"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_pipeline</span> <span class="o">=</span> <span class="n">p</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"retrievers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrievers</span><span class="p">,</span>
            <span class="s2">"query_engines"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engines</span><span class="p">,</span>
            <span class="s2">"query_pipeline"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_pipeline</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/#llama_index.packs.rag_fusion_query_pipeline.RAGFusionPipelinePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-rag-fusion-query-pipeline/llama_index/packs/rag_fusion_query_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"retrievers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrievers</span><span class="p">,</span>
        <span class="s2">"query_engines"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engines</span><span class="p">,</span>
        <span class="s2">"query_pipeline"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_pipeline</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/#llama_index.packs.rag_fusion_query_pipeline.RAGFusionPipelinePack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-rag-fusion-query-pipeline/llama_index/packs/rag_fusion_query_pipeline/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Rag evaluator](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/)[Next Ragatouille retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/)
