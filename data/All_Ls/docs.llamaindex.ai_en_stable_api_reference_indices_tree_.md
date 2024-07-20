Title: Tree - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/

Markdown Content:
Tree - LlamaIndex


LlamaIndex data structures.

TreeIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/#llama_index.core.indices.TreeIndex "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexGraph]`

Tree Index.

The tree index is a tree-structured index, where each node is a summary of the children nodes. During index construction, the tree is constructed in a bottoms-up fashion until we end up with a set of root\_nodes.

There are a few different options during query time (see :ref:`Ref-Query`). The main option is to traverse down the tree from the root nodes. A secondary answer is to directly synthesize the answer from the root nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `summary_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
A Summarization Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `insert_prompt` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

An Tree Insertion Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `num_children` | `int` | 

The number of children each node should have.



 | `10` |
| `build_tree` | `bool` | 

Whether to build the tree during index construction.



 | `True` |
| `show_progress` | `bool` | 

Whether to show progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/tree/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 44</span>
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
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TreeIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexGraph</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Tree Index.</span>

<span class="sd">    The tree index is a tree-structured index, where each node is a summary of</span>
<span class="sd">    the children nodes. During index construction, the tree is constructed</span>
<span class="sd">    in a bottoms-up fashion until we end up with a set of root_nodes.</span>

<span class="sd">    There are a few different options during query time (see :ref:`Ref-Query`).</span>
<span class="sd">    The main option is to traverse down the tree from the root nodes.</span>
<span class="sd">    A secondary answer is to directly synthesize the answer from the root nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        summary_template (Optional[BasePromptTemplate]): A Summarization Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        insert_prompt (Optional[BasePromptTemplate]): An Tree Insertion Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        num_children (int): The number of children each node should have.</span>
<span class="sd">        build_tree (bool): Whether to build the tree during index construction.</span>
<span class="sd">        show_progress (bool): Whether to show progress bars. Defaults to False.</span>

<span class="sd">    """</span>

    <span class="n">index_struct_cls</span> <span class="o">=</span> <span class="n">IndexGraph</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexGraph</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summary_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_children</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">build_tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="c1"># need to set parameters before building index in base class.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_children</span> <span class="o">=</span> <span class="n">num_children</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">summary_template</span> <span class="o">=</span> <span class="n">summary_template</span> <span class="ow">or</span> <span class="n">DEFAULT_SUMMARY_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">insert_prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">insert_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_INSERT_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">build_tree</span> <span class="o">=</span> <span class="n">build_tree</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span> <span class="o">=</span> <span class="n">use_async</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
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
        <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">TreeRetrieverMode</span><span class="p">]</span> <span class="o">=</span> <span class="n">TreeRetrieverMode</span><span class="o">.</span><span class="n">SELECT_LEAF</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="c1"># NOTE: lazy import</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.tree.all_leaf_retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">TreeAllLeafRetriever</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.tree.select_leaf_embedding_retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">TreeSelectLeafEmbeddingRetriever</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.tree.select_leaf_retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">TreeSelectLeafRetriever</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.tree.tree_root_retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">TreeRootRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_validate_build_tree_required</span><span class="p">(</span><span class="n">TreeRetrieverMode</span><span class="p">(</span><span class="n">retriever_mode</span><span class="p">))</span>

        <span class="k">if</span> <span class="n">retriever_mode</span> <span class="o"></span> <span class="n">TreeRetrieverMode</span><span class="o">.</span><span class="n">SELECT_LEAF_EMBEDDING</span><span class="p">:</span>
            <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">TreeSelectLeafEmbeddingRetriever</span><span class="p">(</span>
                <span class="bp">self</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">retriever_mode</span> <span class="o"></span> <span class="n">TreeRetrieverMode</span><span class="o">.</span><span class="n">ALL_LEAF</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">TreeAllLeafRetriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown retriever mode: </span><span class="si">{</span><span class="n">retriever_mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_validate_build_tree_required</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">retriever_mode</span><span class="p">:</span> <span class="n">TreeRetrieverMode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if index supports modes that require trees."""</span>
        <span class="k">if</span> <span class="n">retriever_mode</span> <span class="ow">in</span> <span class="n">REQUIRE_TREE_MODES</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_tree</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Index was constructed without building trees, "</span>
                <span class="sa">f</span><span class="s2">"but retriever mode </span><span class="si">{</span><span class="n">retriever_mode</span><span class="si">}</span><span class="s2"> requires trees."</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">IndexGraph</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes."""</span>
        <span class="n">index_builder</span> <span class="o">=</span> <span class="n">GPTTreeIndexBuilder</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">num_children</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">summary_template</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span><span class="p">,</span>
            <span class="n">docstore</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">index_builder</span><span class="o">.</span><span class="n">build_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">build_tree</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">build_tree</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a document."""</span>
        <span class="c1"># TODO: allow to customize insert prompt</span>
        <span class="n">inserter</span> <span class="o">=</span> <span class="n">TreeIndexInserter</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">num_children</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_children</span><span class="p">,</span>
            <span class="n">insert_prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">insert_prompt</span><span class="p">,</span>
            <span class="n">summary_prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">summary_template</span><span class="p">,</span>
            <span class="n">docstore</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">inserter</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a node."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Delete not implemented for tree index."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve a dict mapping of ingested documents and their nodes+metadata."""</span>
        <span class="n">node_doc_ids</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">all_nodes</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
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

### ref\_doc\_info `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/#llama_index.core.indices.TreeIndex.ref_doc_info "Permanent link")

```
ref_doc_info: Dict[str, [RefDocInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.RefDocInfo "llama_index.core.storage.docstore.types.RefDocInfo")]
```

Retrieve a dict mapping of ingested documents and their nodes+metadata.

Back to top

[Previous Summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/)[Next Vectara](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/)
