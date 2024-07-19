Title: Ragatouille retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/

Markdown Content:
Ragatouille retriever - LlamaIndex


RAGatouilleRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/#llama_index.packs.ragatouille_retriever.RAGatouilleRetrieverPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

RAGatouille Retriever pack.

Source code in `llama-index-packs/llama-index-packs-ragatouille-retriever/llama_index/packs/ragatouille_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">128</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RAGatouilleRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAGatouille Retriever pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"colbert-ir/colbertv2.0"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"my_index"</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span> <span class="o">=</span> <span class="n">model_name</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">ragatouille</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">ragatouille</span> <span class="kn">import</span> <span class="n">RAGPretrainedModel</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"RAGatouille is not installed. Please install it with `pip install ragatouille`."</span>
            <span class="p">)</span>

        <span class="n">doc_txts</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">doc_id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">doc_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>

        <span class="c1"># index the documents</span>
        <span class="k">if</span> <span class="n">index_path</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">RAG</span> <span class="o">=</span> <span class="n">RAGPretrainedModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"colbert-ir/colbertv2.0"</span><span class="p">)</span>
            <span class="n">index_path</span> <span class="o">=</span> <span class="n">RAG</span><span class="o">.</span><span class="n">index</span><span class="p">(</span>
                <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
                <span class="n">collection</span><span class="o">=</span><span class="n">doc_txts</span><span class="p">,</span>
                <span class="n">document_ids</span><span class="o">=</span><span class="n">doc_ids</span><span class="p">,</span>
                <span class="n">document_metadatas</span><span class="o">=</span><span class="n">doc_metadatas</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">RAG</span> <span class="o">=</span> <span class="n">RAGPretrainedModel</span><span class="o">.</span><span class="n">from_index</span><span class="p">(</span><span class="n">index_path</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">index_path</span> <span class="o">=</span> <span class="n">index_path</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">custom_retriever</span> <span class="o">=</span> <span class="n">CustomRetriever</span><span class="p">(</span><span class="n">RAG</span><span class="p">,</span> <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span> <span class="n">top_k</span><span class="o">=</span><span class="n">top_k</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span> <span class="o">=</span> <span class="n">RAG</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">documents</span> <span class="o">=</span> <span class="n">documents</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">custom_retriever</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add documents."""</span>
        <span class="n">doc_txts</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">doc_id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">doc_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="o">.</span><span class="n">add_to_index</span><span class="p">(</span>
            <span class="n">new_collection</span><span class="o">=</span><span class="n">doc_txts</span><span class="p">,</span>
            <span class="n">new_document_ids</span><span class="o">=</span><span class="n">doc_ids</span><span class="p">,</span>
            <span class="n">new_document_metadatas</span><span class="o">=</span><span class="n">doc_metadatas</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete documents."""</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">doc_id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="o">.</span><span class="n">delete_from_index</span><span class="p">(</span><span class="n">document_ids</span><span class="o">=</span><span class="n">doc_ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"RAG"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="p">,</span>
            <span class="s2">"documents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">documents</span><span class="p">,</span>
            <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_retriever</span><span class="p">,</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"index_path"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_path</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/#llama_index.packs.ragatouille_retriever.RAGatouilleRetrieverPack.add_documents "Permanent link")

```
add_documents(documents: List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]) -> None
```

Add documents.

Source code in `llama-index-packs/llama-index-packs-ragatouille-retriever/llama_index/packs/ragatouille_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add documents."""</span>
    <span class="n">doc_txts</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
    <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">doc_id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
    <span class="n">doc_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="o">.</span><span class="n">add_to_index</span><span class="p">(</span>
        <span class="n">new_collection</span><span class="o">=</span><span class="n">doc_txts</span><span class="p">,</span>
        <span class="n">new_document_ids</span><span class="o">=</span><span class="n">doc_ids</span><span class="p">,</span>
        <span class="n">new_document_metadatas</span><span class="o">=</span><span class="n">doc_metadatas</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/#llama_index.packs.ragatouille_retriever.RAGatouilleRetrieverPack.delete_documents "Permanent link")

```
delete_documents(documents: List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]) -> None
```

Delete documents.

Source code in `llama-index-packs/llama-index-packs-ragatouille-retriever/llama_index/packs/ragatouille_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete documents."""</span>
    <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">doc_id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="o">.</span><span class="n">delete_from_index</span><span class="p">(</span><span class="n">document_ids</span><span class="o">=</span><span class="n">doc_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/#llama_index.packs.ragatouille_retriever.RAGatouilleRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-ragatouille-retriever/llama_index/packs/ragatouille_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"RAG"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">RAG</span><span class="p">,</span>
        <span class="s2">"documents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">documents</span><span class="p">,</span>
        <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_retriever</span><span class="p">,</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="s2">"index_path"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_path</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/#llama_index.packs.ragatouille_retriever.RAGatouilleRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-ragatouille-retriever/llama_index/packs/ragatouille_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Rag fusion query pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/)[Next Raptor](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/)
