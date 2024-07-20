Title: Keyword - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/

Markdown Content:
Keyword - LlamaIndex


Query for KeywordTableIndex.

BaseKeywordTableRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Base Keyword Table Retriever.

Arguments are shared among subclasses.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `keyword_extract_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 
A Keyword Extraction Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `query_keyword_extract_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A Query Keyword Extraction Prompt (see :ref:`Prompt-Templates`).



 | `None` |
| `refine_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A Refinement Prompt (see :ref:`Prompt-Templates`).



 | _required_ |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A Question Answering Prompt (see :ref:`Prompt-Templates`).



 | _required_ |
| `max_keywords_per_query` | `int` | 

Maximum number of keywords to extract from query.



 | `10` |
| `num_chunks_per_query` | `int` | 

Maximum number of text chunks to query.



 | `10` |

Source code in `llama-index-core/llama_index/core/indices/keyword_table/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 30</span>
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
<span class="normal">114</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseKeywordTableRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base Keyword Table Retriever.</span>

<span class="sd">    Arguments are shared among subclasses.</span>

<span class="sd">    Args:</span>
<span class="sd">        keyword_extract_template (Optional[BasePromptTemplate]): A Keyword</span>
<span class="sd">            Extraction Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        query_keyword_extract_template (Optional[BasePromptTemplate]): A Query</span>
<span class="sd">            Keyword Extraction</span>
<span class="sd">            Prompt (see :ref:`Prompt-Templates`).</span>
<span class="sd">        refine_template (Optional[BasePromptTemplate]): A Refinement Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): A Question Answering Prompt</span>
<span class="sd">            (see :ref:`Prompt-Templates`).</span>
<span class="sd">        max_keywords_per_query (int): Maximum number of keywords to extract from query.</span>
<span class="sd">        num_chunks_per_query (int): Maximum number of text chunks to query.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseKeywordTableIndex</span><span class="p">,</span>
        <span class="n">keyword_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_keyword_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_keywords_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">num_chunks_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">index_struct</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">docstore</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span> <span class="o">=</span> <span class="n">max_keywords_per_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_chunks_per_query</span> <span class="o">=</span> <span class="n">num_chunks_per_query</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">keyword_extract_template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">keyword_extract_template</span> <span class="ow">or</span> <span class="n">DEFAULT_KEYWORD_EXTRACT_TEMPLATE</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_keyword_extract_template</span> <span class="o">=</span> <span class="n">query_keyword_extract_template</span> <span class="ow">or</span> <span class="n">DQKET</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_get_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords."""</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Starting query: </span><span class="si">{</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keywords</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query keywords: </span><span class="si">{</span><span class="n">keywords</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># go through text chunks in order of most matching keywords</span>
        <span class="n">chunk_indices_count</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="p">[</span><span class="n">k</span> <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">keywords</span> <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">keywords</span><span class="p">]</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Extracted keywords: </span><span class="si">{</span><span class="n">keywords</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">keywords</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_struct</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">k</span><span class="p">]:</span>
                <span class="n">chunk_indices_count</span><span class="p">[</span><span class="n">node_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">sorted_chunk_indices</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span>
            <span class="n">chunk_indices_count</span><span class="o">.</span><span class="n">keys</span><span class="p">(),</span>
            <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">chunk_indices_count</span><span class="p">[</span><span class="n">x</span><span class="p">],</span>
            <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">sorted_chunk_indices</span> <span class="o">=</span> <span class="n">sorted_chunk_indices</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_chunks_per_query</span><span class="p">]</span>
        <span class="n">sorted_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">sorted_chunk_indices</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="vm">__name__</span><span class="p">)</span><span class="o">.</span><span class="n">getEffectiveLevel</span><span class="p">()</span> <span class="o">==</span> <span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">chunk_idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">sorted_chunk_indices</span><span class="p">,</span> <span class="n">sorted_nodes</span><span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"&gt; Querying with idx: </span><span class="si">{</span><span class="n">chunk_idx</span><span class="si">}</span><span class="s2">: "</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">truncate_text</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span><span class="w"> </span><span class="mi">50</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">sorted_nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

KeywordTableGPTRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.KeywordTableGPTRetriever "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKeywordTableRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever "llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever")`

Keyword Table Index GPT Retriever.

Extracts keywords using GPT. Set when using `retriever_mode="default"`.

See BaseGPTKeywordTableQuery for arguments.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">117</span>
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
<span class="normal">161</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordTableGPTRetriever</span><span class="p">(</span><span class="n">BaseKeywordTableRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword Table Index GPT Retriever.</span>

<span class="sd">    Extracts keywords using GPT. Set when using `retriever_mode="default"`.</span>

<span class="sd">    See BaseGPTKeywordTableQuery for arguments.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseKeywordTableIndex</span><span class="p">,</span>
        <span class="n">keyword_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_keyword_extract_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_keywords_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">num_chunks_per_query</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span>
            <span class="n">keyword_extract_template</span><span class="o">=</span><span class="n">keyword_extract_template</span><span class="p">,</span>
            <span class="n">query_keyword_extract_template</span><span class="o">=</span><span class="n">query_keyword_extract_template</span><span class="p">,</span>
            <span class="n">max_keywords_per_query</span><span class="o">=</span><span class="n">max_keywords_per_query</span><span class="p">,</span>
            <span class="n">num_chunks_per_query</span><span class="o">=</span><span class="n">num_chunks_per_query</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_keyword_extract_template</span><span class="p">,</span>
            <span class="n">max_keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span><span class="p">,</span>
            <span class="n">question</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">keywords</span> <span class="o">=</span> <span class="n">extract_keywords_given_response</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">start_token</span><span class="o">=</span><span class="s2">"KEYWORDS:"</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">keywords</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

KeywordTableSimpleRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.KeywordTableSimpleRetriever "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKeywordTableRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever "llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever")`

Keyword Table Index Simple Retriever.

Extracts keywords using simple regex-based keyword extractor. Set when `retriever_mode="simple"`.

See BaseGPTKeywordTableQuery for arguments.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">164</span>
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
<span class="normal">178</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordTableSimpleRetriever</span><span class="p">(</span><span class="n">BaseKeywordTableRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword Table Index Simple Retriever.</span>

<span class="sd">    Extracts keywords using simple regex-based keyword extractor.</span>
<span class="sd">    Set when `retriever_mode="simple"`.</span>

<span class="sd">    See BaseGPTKeywordTableQuery for arguments.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">_get_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span>
            <span class="n">simple_extract_keywords</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">max_keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span><span class="p">)</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

KeywordTableRAKERetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.KeywordTableRAKERetriever "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKeywordTableRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/#llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever "llama_index.core.indices.keyword_table.retrievers.BaseKeywordTableRetriever")`

Keyword Table Index RAKE Retriever.

Extracts keywords using RAKE keyword extractor. Set when `retriever_mode="rake"`.

See BaseGPTKeywordTableQuery for arguments.

Source code in `llama-index-core/llama_index/core/indices/keyword_table/retrievers.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">181</span>
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
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">KeywordTableRAKERetriever</span><span class="p">(</span><span class="n">BaseKeywordTableRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Keyword Table Index RAKE Retriever.</span>

<span class="sd">    Extracts keywords using RAKE keyword extractor.</span>
<span class="sd">    Set when `retriever_mode="rake"`.</span>

<span class="sd">    See BaseGPTKeywordTableQuery for arguments.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">_get_keywords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Extract keywords."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span>
            <span class="n">rake_extract_keywords</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">max_keywords</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_keywords_per_query</span><span class="p">)</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/)[Next Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/)
