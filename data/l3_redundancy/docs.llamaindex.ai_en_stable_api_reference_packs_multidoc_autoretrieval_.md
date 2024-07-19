Title: Multidoc autoretrieval - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/

Markdown Content:
Multidoc autoretrieval - LlamaIndex


MultiDocAutoRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/#llama_index.packs.multidoc_autoretrieval.MultiDocAutoRetrieverPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Multi-doc auto-retriever pack.

Uses weaviate as the underlying storage.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `docs` | `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
A list of documents to index.



 | _required_ |
| `**kwargs` |  | 

Keyword arguments to pass to the underlying index.



 | _required_ |

Source code in `llama-index-packs/llama-index-packs-multidoc-autoretrieval/llama_index/packs/multidoc_autoretrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 53</span>
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
<span class="normal">178</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiDocAutoRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Multi-doc auto-retriever pack.</span>

<span class="sd">    Uses weaviate as the underlying storage.</span>

<span class="sd">    Args:</span>
<span class="sd">        docs (List[Document]): A list of documents to index.</span>
<span class="sd">        **kwargs: Keyword arguments to pass to the underlying index.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">weaviate_client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">doc_metadata_index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">doc_chunks_index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">metadata_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">doc_metadata_schema</span><span class="p">:</span> <span class="n">VectorStoreInfo</span><span class="p">,</span>
        <span class="n">auto_retriever_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="kn">import</span> <span class="nn">weaviate</span>

        <span class="c1"># do some validation</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">metadata_nodes</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"The number of metadata nodes must match the number of documents."</span>
            <span class="p">)</span>

        <span class="c1"># authenticate</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">weaviate</span><span class="o">.</span><span class="n">Client</span><span class="p">,</span> <span class="n">weaviate_client</span><span class="p">)</span>
        <span class="c1"># auth_config = weaviate.AuthApiKey(api_key="")</span>
        <span class="c1"># client = weaviate.Client(</span>
        <span class="c1">#     "https://&lt;weaviate-cluster&gt;.weaviate.network",</span>
        <span class="c1">#     auth_client_secret=auth_config,</span>
        <span class="c1"># )</span>

        <span class="c1"># initialize two vector store classes corresponding to the two index names</span>
        <span class="n">metadata_store</span> <span class="o">=</span> <span class="n">WeaviateVectorStore</span><span class="p">(</span>
            <span class="n">weaviate_client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span> <span class="n">index_name</span><span class="o">=</span><span class="n">doc_metadata_index_name</span>
        <span class="p">)</span>
        <span class="n">metadata_sc</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">vector_store</span><span class="o">=</span><span class="n">metadata_store</span><span class="p">)</span>
        <span class="c1"># index VectorStoreIndex</span>
        <span class="c1"># Since "new_docs" are concise summaries, we can directly feed them as nodes into VectorStoreIndex</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">metadata_nodes</span><span class="p">,</span> <span class="n">storage_context</span><span class="o">=</span><span class="n">metadata_sc</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Indexed metadata nodes."</span><span class="p">)</span>

        <span class="c1"># construct separate Weaviate Index with original docs. Define a separate query engine with query engine mapping to each doc id.</span>
        <span class="n">chunks_store</span> <span class="o">=</span> <span class="n">WeaviateVectorStore</span><span class="p">(</span>
            <span class="n">weaviate_client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span> <span class="n">index_name</span><span class="o">=</span><span class="n">doc_chunks_index_name</span>
        <span class="p">)</span>
        <span class="n">chunks_sc</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">vector_store</span><span class="o">=</span><span class="n">chunks_store</span><span class="p">)</span>
        <span class="n">doc_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="n">storage_context</span><span class="o">=</span><span class="n">chunks_sc</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Indexed source document nodes."</span><span class="p">)</span>

        <span class="c1"># setup auto retriever</span>
        <span class="n">auto_retriever</span> <span class="o">=</span> <span class="n">VectorIndexAutoRetriever</span><span class="p">(</span>
            <span class="n">index</span><span class="p">,</span>
            <span class="n">vector_store_info</span><span class="o">=</span><span class="n">doc_metadata_schema</span><span class="p">,</span>
            <span class="o">**</span><span class="p">(</span><span class="n">auto_retriever_kwargs</span> <span class="ow">or</span> <span class="p">{}),</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index_auto_retriever</span> <span class="o">=</span> <span class="n">IndexAutoRetriever</span><span class="p">(</span><span class="n">retriever</span><span class="o">=</span><span class="n">auto_retriever</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Setup autoretriever over metadata."</span><span class="p">)</span>

        <span class="c1"># define per-document retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">retriever_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">index_id</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"index_id"</span><span class="p">]</span>
            <span class="c1"># filter for the specific doc id</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">MetadataFilters</span><span class="p">(</span>
                <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">MetadataFilter</span><span class="p">(</span>
                        <span class="n">key</span><span class="o">=</span><span class="s2">"index_id"</span><span class="p">,</span> <span class="n">operator</span><span class="o">=</span><span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="n">index_id</span>
                    <span class="p">),</span>
                <span class="p">]</span>
            <span class="p">)</span>
            <span class="n">retriever</span> <span class="o">=</span> <span class="n">doc_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">retriever_dict</span><span class="p">[</span><span class="n">index_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">retriever</span>

        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Setup per-document retriever."</span><span class="p">)</span>

        <span class="c1"># setup recursive retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span> <span class="o">=</span> <span class="n">RecursiveRetriever</span><span class="p">(</span>
            <span class="s2">"vector"</span><span class="p">,</span>
            <span class="n">retriever_dict</span><span class="o">=</span><span class="p">{</span><span class="s2">"vector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_auto_retriever</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">retriever_dict</span><span class="p">},</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Setup recursive retriever."</span><span class="p">)</span>

        <span class="c1"># plug into query engine</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">            LlamaPack.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"index_auto_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_auto_retriever</span><span class="p">,</span>
            <span class="s2">"retriever_dict"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever_dict</span><span class="p">,</span>
            <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Runs queries against the index.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Any: A response from the query engine.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/#llama_index.packs.multidoc_autoretrieval.MultiDocAutoRetrieverPack.get_modules "Permanent link")

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

Source code in `llama-index-packs/llama-index-packs-multidoc-autoretrieval/llama_index/packs/multidoc_autoretrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">156</span>
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
<span class="normal">169</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Returns a dictionary containing the internals of the LlamaPack.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Dict[str, Any]: A dictionary containing the internals of the</span>
<span class="sd">        LlamaPack.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"index_auto_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_auto_retriever</span><span class="p">,</span>
        <span class="s2">"retriever_dict"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever_dict</span><span class="p">,</span>
        <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/#llama_index.packs.multidoc_autoretrieval.MultiDocAutoRetrieverPack.run "Permanent link")

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

Source code in `llama-index-packs/llama-index-packs-multidoc-autoretrieval/llama_index/packs/multidoc_autoretrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Runs queries against the index.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Any: A response from the query engine.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multi tenancy rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/)[Next Nebulagraph query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/)
