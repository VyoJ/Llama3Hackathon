Title: Summary - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/

Markdown Content:
Summary - LlamaIndex


LlamaIndex data structures.

SummaryIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/#llama_index.core.indices.SummaryIndex "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexList]`

Summary Index.

The summary index is a simple data structure where nodes are stored in a sequence. During index construction, the document texts are chunked up, converted to nodes, and stored in a list.

During query time, the summary index iterates through the nodes with some optional filter parameters, and synthesizes an answer from all the nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
A Question-Answer Prompt (see :ref:`Prompt-Templates`). NOTE: this is a deprecated field.



 | _required_ |
| `show_progress` | `bool` | 

Whether to show tqdm progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/list/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 33</span>
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
<span class="normal">152</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SummaryIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexList</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Summary Index.</span>

<span class="sd">    The summary index is a simple data structure where nodes are stored in</span>
<span class="sd">    a sequence. During index construction, the document texts are</span>
<span class="sd">    chunked up, converted to nodes, and stored in a list.</span>

<span class="sd">    During query time, the summary index iterates through the nodes</span>
<span class="sd">    with some optional filter parameters, and synthesizes an</span>
<span class="sd">    answer from all the nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): A Question-Answer Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">            NOTE: this is a deprecated field.</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>

<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">IndexList</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexList</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">ListRetrieverMode</span><span class="p">]</span> <span class="o">=</span> <span class="n">ListRetrieverMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.list.retrievers</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">SummaryIndexEmbeddingRetriever</span><span class="p">,</span>
            <span class="n">SummaryIndexLLMRetriever</span><span class="p">,</span>
            <span class="n">SummaryIndexRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">retriever_mode</span> <span class="o"></span> <span class="n">ListRetrieverMode</span><span class="o">.</span><span class="n">EMBEDDING</span><span class="p">:</span>
            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">SummaryIndexEmbeddingRetriever</span><span class="p">(</span>
                <span class="bp">self</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">retriever_mode</span> <span class="o">==</span> <span class="n">ListRetrieverMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">SummaryIndexLLMRetriever</span><span class="p">(</span>
                <span class="bp">self</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown retriever mode: </span><span class="si">{</span><span class="n">retriever_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexList</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            documents (List[BaseDocument]): A list of documents.</span>

<span class="sd">        Returns:</span>
<span class="sd">            IndexList: The created summary index.</span>
<span class="sd">        """</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="n">IndexList</span><span class="p">()</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Processing nodes"</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">index_struct</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a node."""</span>
        <span class="n">cur_node_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">nodes</span>
        <span class="n">cur_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">cur_node_ids</span><span class="p">)</span>
        <span class="n">nodes_to_keep</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">cur_nodes</span> <span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">node_id</span> <span class="o">!=</span> <span class="n">node_id</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes_to_keep</span><span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
        <span class="n">node_doc_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">nodes</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_doc_ids</span><span class="p">)</span>

        <span class="n">all_ref_doc_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">ref_node</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">source_node</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">ref_node</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">ref_doc_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_ref_doc_info</span><span class="p">(</span><span class="n">ref_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">ref_doc_info</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">all_ref_doc_info</span><span class="p">[</span><span class="n">ref_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref_doc_info</span>
        <span class="k">return</span> <span class="n">all_ref_doc_info</span>
</code></pre></div></td></tr></tbody></table>

### ref\_doc\_info `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/#llama_index.core.indices.SummaryIndex.ref_doc_info "Permanent link")

```
ref_doc_info: Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Retrieve a dict mapping of ingested documents and their nodes+metadata.

Back to top

[Previous Property graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/)[Next Tree](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/)
