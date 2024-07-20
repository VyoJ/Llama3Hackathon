Title: Tree - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/

Markdown Content:
Tree - LlamaIndex


TreeAllLeafRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/#llama_index.core.retrievers.TreeAllLeafRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

GPT all leaf retriever.

This class builds a query-specific tree from leaf nodes to return a response. Using this query mode means that the tree index doesn't need to be built when initialized, since we rebuild the tree for each query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
Question-Answer Prompt (see :ref:`Prompt-Templates`).



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/tree/all_leaf_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
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
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TreeAllLeafRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GPT all leaf retriever.</span>

<span class="sd">    This class builds a query-specific tree from leaf nodes to return a response.</span>
<span class="sd">    Using this query mode means that the tree index doesn't need to be built</span>
<span class="sd">    when initialized, since we rebuild the tree for each query.</span>

<span class="sd">    Args:</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): Question-Answer Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">TreeIndex</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">index_struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">docstore</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Starting query: </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">index_struct</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">IndexGraph</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="p">)</span>
        <span class="n">all_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node_dict</span><span class="p">(</span><span class="n">index_struct</span><span class="o">.</span><span class="n">all_nodes</span><span class="p">)</span>
        <span class="n">sorted_node_list</span> <span class="o">=</span> <span class="n">get_sorted_node_list</span><span class="p">(</span><span class="n">all_nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">sorted_node_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

TreeSelectLeafEmbeddingRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/#llama_index.core.retrievers.TreeSelectLeafEmbeddingRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[TreeSelectLeafRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/#llama_index.core.retrievers.TreeSelectLeafRetriever "llama_index.core.indices.tree.select_leaf_retriever.TreeSelectLeafRetriever")`

Tree select leaf embedding retriever.

This class traverses the index graph using the embedding similarity between the query and the node text.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
Tree Select Query Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `query_template_multiple` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Tree Select Query Prompt (Multiple) (see :ref:`Prompt-Templates`).



 | `None` |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Question-Answer Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `refine_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Refinement Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `child_branch_factor` | `int` | 

Number of child nodes to consider at each level. If child\_branch\_factor is 1, then the query will only choose one child node to traverse for any given parent node. If child\_branch\_factor is 2, then the query will choose two child nodes.



 | `1` |
| `embed_model` | `Optional[[BaseEmbedding](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "llama_index.core.base.embeddings.base.BaseEmbedding")]` | 

Embedding model to use for embedding similarity.



 | `None` |

Source code in `llama-index-core/llama_index/core/indices/tree/select_leaf_embedding_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
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
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TreeSelectLeafEmbeddingRetriever</span><span class="p">(</span><span class="n">TreeSelectLeafRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tree select leaf embedding retriever.</span>

<span class="sd">    This class traverses the index graph using the embedding similarity between the</span>
<span class="sd">    query and the node text.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_template (Optional[BasePromptTemplate]): Tree Select Query Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        query_template_multiple (Optional[BasePromptTemplate]): Tree Select</span>
<span class="sd">            Query Prompt (Multiple)</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): Question-Answer Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        refine_template (Optional[BasePromptTemplate]): Refinement Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        child_branch_factor (int): Number of child nodes to consider at each level.</span>
<span class="sd">            If child_branch_factor is 1, then the query will only choose one child node</span>
<span class="sd">            to traverse for any given parent node.</span>
<span class="sd">            If child_branch_factor is 2, then the query will choose two child nodes.</span>
<span class="sd">        embed_model (Optional[BaseEmbedding]): Embedding model to use for</span>
<span class="sd">            embedding similarity.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">TreeIndex</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_template_multiple</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">child_branch_factor</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">index</span><span class="p">,</span>
            <span class="n">query_template</span><span class="o">=</span><span class="n">query_template</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">refine_template</span><span class="o">=</span><span class="n">refine_template</span><span class="p">,</span>
            <span class="n">query_template_multiple</span><span class="o">=</span><span class="n">query_template_multiple</span><span class="p">,</span>
            <span class="n">child_branch_factor</span><span class="o">=</span><span class="n">child_branch_factor</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query_level</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_node_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query recursively."""</span>
        <span class="n">cur_nodes</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">index</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">cur_node_ids</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">}</span>
        <span class="n">cur_node_list</span> <span class="o">=</span> <span class="n">get_sorted_node_list</span><span class="p">(</span><span class="n">cur_nodes</span><span class="p">)</span>

        <span class="c1"># Get the node with the highest similarity to the query</span>
        <span class="n">selected_nodes</span><span class="p">,</span> <span class="n">selected_indices</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_most_similar_nodes</span><span class="p">(</span>
            <span class="n">cur_node_list</span><span class="p">,</span> <span class="n">query_bundle</span>
        <span class="p">)</span>

        <span class="n">result_response</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">selected_nodes</span><span class="p">,</span> <span class="n">selected_indices</span><span class="p">):</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Node [</span><span class="si">{</span><span class="n">index</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">] Summary text: "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="s1">' '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

            <span class="c1"># Get the response for the selected node</span>
            <span class="n">result_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_with_selected_node</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">level</span><span class="p">,</span> <span class="n">prev_response</span><span class="o">=</span><span class="n">result_response</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">result_response</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_query_text_embedding_similarities</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get query text embedding similarity.</span>

<span class="sd">        Cache the query embedding and the node text embedding.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_agg_embedding_from_queries</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span>
            <span class="p">)</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_text_embedding</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span>
                <span class="p">)</span>

            <span class="n">similarity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">similarity</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span>
            <span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">similarity</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">similarities</span>

    <span class="k">def</span> <span class="nf">_get_most_similar_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get the node with the highest similarity to the query."""</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_query_text_embedding_similarities</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span><span class="p">)</span>

        <span class="n">selected_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">selected_indices</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span>
            <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="p">),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">selected_nodes</span><span class="p">)</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span><span class="p">:</span>
                <span class="n">selected_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">selected_indices</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nodes</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">selected_nodes</span><span class="p">,</span> <span class="n">selected_indices</span>

    <span class="k">def</span> <span class="nf">_select_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_node_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">selected_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_most_similar_nodes</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">selected_nodes</span>
</code></pre></div></td></tr></tbody></table>

TreeSelectLeafRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/#llama_index.core.retrievers.TreeSelectLeafRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Tree select leaf retriever.

This class traverses the index graph and searches for a leaf node that can best answer the query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
Tree Select Query Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `query_template_multiple` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Tree Select Query Prompt (Multiple) (see :ref:`Prompt-Templates`).



 | `None` |
| `child_branch_factor` | `int` | 

Number of child nodes to consider at each level. If child\_branch\_factor is 1, then the query will only choose one child node to traverse for any given parent node. If child\_branch\_factor is 2, then the query will choose two child nodes.



 | `1` |

Source code in `llama-index-core/llama_index/core/indices/tree/select_leaf_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 59</span>
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
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TreeSelectLeafRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tree select leaf retriever.</span>

<span class="sd">    This class traverses the index graph and searches for a leaf node that can best</span>
<span class="sd">    answer the query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_template (Optional[BasePromptTemplate]): Tree Select Query Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        query_template_multiple (Optional[BasePromptTemplate]): Tree Select</span>
<span class="sd">            Query Prompt (Multiple)</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        child_branch_factor (int): Number of child nodes to consider at each level.</span>
<span class="sd">            If child_branch_factor is 1, then the query will only choose one child node</span>
<span class="sd">            to traverse for any given parent node.</span>
<span class="sd">            If child_branch_factor is 2, then the query will choose two child nodes.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">TreeIndex</span><span class="p">,</span>
        <span class="n">query_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_template_multiple</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">child_branch_factor</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">_llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">index_struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">docstore</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span> <span class="o">=</span> <span class="n">Settings</span><span class="o">.</span><span class="n">_prompt_helper</span> <span class="ow">or</span> <span class="n">PromptHelper</span><span class="o">.</span><span class="n">from_llm_metadata</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span> <span class="o">=</span> <span class="n">text_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_refine_template</span> <span class="o">=</span> <span class="n">refine_template</span> <span class="ow">or</span> <span class="n">DEFAULT_REFINE_PROMPT_SEL</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_template</span> <span class="o">=</span> <span class="n">query_template</span> <span class="ow">or</span> <span class="n">DEFAULT_QUERY_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_template_multiple</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">query_template_multiple</span> <span class="ow">or</span> <span class="n">DEFAULT_QUERY_PROMPT_MULTIPLE</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span> <span class="o">=</span> <span class="n">child_branch_factor</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">index</span><span class="o">.</span><span class="n">service_context</span>
            <span class="p">),</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query_with_selected_node</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">selected_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">prev_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get response for selected node.</span>

<span class="sd">        If not leaf node, it will recursively call _query on the child nodes.</span>
<span class="sd">        If prev_response is provided, we will update prev_response with the answer.</span>

<span class="sd">        """</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">get_children</span><span class="p">(</span><span class="n">selected_node</span><span class="p">))</span> <span class="o"></span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Only one node left. Querying node."</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_with_selected_node</span><span class="p">(</span>
                <span class="n">cur_node_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">query_bundle</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">level</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span> <span class="o"></span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">query_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                <span class="n">num_chunks</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">),</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span>
            <span class="p">)</span>
            <span class="n">text_splitter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">get_text_splitter_given_prompt</span><span class="p">(</span>
                <span class="n">prompt</span><span class="o">=</span><span class="n">query_template</span><span class="p">,</span>
                <span class="n">num_chunks</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="n">numbered_node_text</span> <span class="o">=</span> <span class="n">get_numbered_text_from_nodes</span><span class="p">(</span>
                <span class="n">cur_node_list</span><span class="p">,</span> <span class="n">text_splitter</span><span class="o">=</span><span class="n">text_splitter</span>
            <span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="n">query_template</span><span class="p">,</span>
                <span class="n">context_list</span><span class="o">=</span><span class="n">numbered_node_text</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_template_multiple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_template_multiple</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span>
                <span class="n">num_chunks</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">),</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">branching_factor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">text_splitter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_helper</span><span class="o">.</span><span class="n">get_text_splitter_given_prompt</span><span class="p">(</span>
                <span class="n">prompt</span><span class="o">=</span><span class="n">query_template_multiple</span><span class="p">,</span>
                <span class="n">num_chunks</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="n">numbered_node_text</span> <span class="o">=</span> <span class="n">get_numbered_text_from_nodes</span><span class="p">(</span>
                <span class="n">cur_node_list</span><span class="p">,</span> <span class="n">text_splitter</span><span class="o">=</span><span class="n">text_splitter</span>
            <span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="n">query_template_multiple</span><span class="p">,</span>
                <span class="n">context_list</span><span class="o">=</span><span class="n">numbered_node_text</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">debug_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Current response: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">debug_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="n">debug_str</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">numbers</span> <span class="o">=</span> <span class="n">extract_numbers_given_response</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">numbers</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">debug_str</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Could not retrieve response - no numbers present"</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">debug_str</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="n">debug_str</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="c1"># just join text from current nodes as response</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">selected_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">number_str</span> <span class="ow">in</span> <span class="n">numbers</span><span class="p">:</span>
            <span class="n">number</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">number_str</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">number</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Invalid response: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="s2"> - "</span>
                    <span class="sa">f</span><span class="s2">"number </span><span class="si">{</span><span class="n">number</span><span class="si">}</span><span class="s2"> out of range"</span>
                <span class="p">)</span>
                <span class="k">continue</span>

            <span class="c1"># number is 1-indexed, so subtract 1</span>
            <span class="n">selected_node</span> <span class="o">=</span> <span class="n">cur_node_list</span><span class="p">[</span><span class="n">number</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>

            <span class="n">info_str</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Selected node: "</span>
                <span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">number</span><span class="si">}</span><span class="s2">]/[</span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">))</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">n</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">numbers</span><span class="p">])</span><span class="si">}</span><span class="s2">]"</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">info_str</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="n">info_str</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">debug_str</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="n">selected_node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
            <span class="p">)</span>
            <span class="n">full_debug_str</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt;[Level </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">] Node "</span>
                <span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">number</span><span class="si">}</span><span class="s2">] Summary text: "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="w"> </span><span class="n">selected_node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span><span class="w"> </span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">full_debug_str</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="n">full_debug_str</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">selected_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">selected_node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">selected_nodes</span>

    <span class="k">def</span> <span class="nf">_retrieve_level</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_node_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Answer a query recursively."""</span>
        <span class="n">cur_nodes</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">index</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">cur_node_ids</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">}</span>
        <span class="n">cur_node_list</span> <span class="o">=</span> <span class="n">get_sorted_node_list</span><span class="p">(</span><span class="n">cur_nodes</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">cur_node_list</span><span class="p">)</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">child_branch_factor</span><span class="p">:</span>
            <span class="n">selected_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_select_nodes</span><span class="p">(</span>
                <span class="n">cur_node_list</span><span class="p">,</span>
                <span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">level</span><span class="o">=</span><span class="n">level</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">selected_nodes</span> <span class="o">=</span> <span class="n">cur_node_list</span>

        <span class="n">children_nodes</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">selected_nodes</span><span class="p">:</span>
            <span class="n">node_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">get_children</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">children_nodes</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">node_dict</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">children_nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="c1"># NOTE: leaf level</span>
            <span class="k">return</span> <span class="n">selected_nodes</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_level</span><span class="p">(</span><span class="n">children_nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">,</span> <span class="n">level</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve_level</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">root_nodes</span><span class="p">,</span>
            <span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">level</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

TreeRootRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/#llama_index.core.retrievers.TreeRootRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Tree root retriever.

This class directly retrieves the answer from the root nodes.

Unlike GPTTreeIndexLeafQuery, this class assumes the graph already stores the answer (because it was constructed with a query\_str), so it does not attempt to parse information down the graph in order to synthesize an answer.

Source code in `llama-index-core/llama_index/core/indices/tree/tree_root_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
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
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TreeRootRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tree root retriever.</span>

<span class="sd">    This class directly retrieves the answer from the root nodes.</span>

<span class="sd">    Unlike GPTTreeIndexLeafQuery, this class assumes the graph already stores</span>
<span class="sd">    the answer (because it was constructed with a query_str), so it does not</span>
<span class="sd">    attempt to parse information down the graph in order to synthesize an answer.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">TreeIndex</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">index_struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">docstore</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Starting query: </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">root_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">root_nodes</span><span class="p">)</span>
        <span class="n">sorted_nodes</span> <span class="o">=</span> <span class="n">get_sorted_node_list</span><span class="p">(</span><span class="n">root_nodes</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">sorted_nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Transform](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/)[Next Vector](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/)
