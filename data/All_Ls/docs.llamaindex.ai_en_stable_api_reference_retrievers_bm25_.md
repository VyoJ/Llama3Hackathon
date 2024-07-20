Title: Bm25 - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/

Markdown Content:
Bm25 - LlamaIndex


BM25Retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/#llama_index.retrievers.bm25.BM25Retriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

A BM25 retriever that uses the BM25 algorithm to retrieve nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
The nodes to index. If not provided, an existing BM25 object must be passed.



 | `None` |
| `stemmer` | `Stemmer` | 

The stemmer to use. Defaults to an english stemmer.



 | `None` |
| `language` | `str` | 

The language to use for stopword removal. Defaults to "en".



 | `'en'` |
| `existing_bm25` | `BM25` | 

An existing BM25 object to use. If not provided, nodes must be passed.



 | `None` |
| `similarity_top_k` | `int` | 

The number of results to return. Defaults to DEFAULT\_SIMILARITY\_TOP\_K.



 | `DEFAULT_SIMILARITY_TOP_K` |
| `callback_manager` | `[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")` | 

The callback manager to use. Defaults to None.



 | `None` |
| `objects` | `List[[IndexNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.IndexNode "llama_index.core.schema.IndexNode")]` | 

The objects to retrieve. Defaults to None.



 | `None` |
| `object_map` | `dict` | 

A map of object IDs to nodes. Defaults to None.



 | `None` |
| `verbose` | `bool` | 

Whether to show progress. Defaults to False.



 | `False` |

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-bm25/llama_index/retrievers/bm25/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
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
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BM25Retriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A BM25 retriever that uses the BM25 algorithm to retrieve nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode], optional):</span>
<span class="sd">            The nodes to index. If not provided, an existing BM25 object must be passed.</span>
<span class="sd">        stemmer (Stemmer.Stemmer, optional):</span>
<span class="sd">            The stemmer to use. Defaults to an english stemmer.</span>
<span class="sd">        language (str, optional):</span>
<span class="sd">            The language to use for stopword removal. Defaults to "en".</span>
<span class="sd">        existing_bm25 (bm25s.BM25, optional):</span>
<span class="sd">            An existing BM25 object to use. If not provided, nodes must be passed.</span>
<span class="sd">        similarity_top_k (int, optional):</span>
<span class="sd">            The number of results to return. Defaults to DEFAULT_SIMILARITY_TOP_K.</span>
<span class="sd">        callback_manager (CallbackManager, optional):</span>
<span class="sd">            The callback manager to use. Defaults to None.</span>
<span class="sd">        objects (List[IndexNode], optional):</span>
<span class="sd">            The objects to retrieve. Defaults to None.</span>
<span class="sd">        object_map (dict, optional):</span>
<span class="sd">            A map of object IDs to nodes. Defaults to None.</span>
<span class="sd">        verbose (bool, optional):</span>
<span class="sd">            Whether to show progress. Defaults to False.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">stemmer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Stemmer</span><span class="o">.</span><span class="n">Stemmer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">language</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span>
        <span class="n">existing_bm25</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">bm25s</span><span class="o">.</span><span class="n">BM25</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stemmer</span> <span class="o">=</span> <span class="n">stemmer</span> <span class="ow">or</span> <span class="n">Stemmer</span><span class="o">.</span><span class="n">Stemmer</span><span class="p">(</span><span class="s2">"english"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>

        <span class="k">if</span> <span class="n">existing_bm25</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span> <span class="o">=</span> <span class="n">existing_bm25</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">corpus</span> <span class="o">=</span> <span class="n">existing_bm25</span><span class="o">.</span><span class="n">corpus</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Please pass nodes or an existing BM25 object."</span><span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

            <span class="n">corpus_tokens</span> <span class="o">=</span> <span class="n">bm25s</span><span class="o">.</span><span class="n">tokenize</span><span class="p">(</span>
                <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">],</span>
                <span class="n">stopwords</span><span class="o">=</span><span class="n">language</span><span class="p">,</span>
                <span class="n">stemmer</span><span class="o">=</span><span class="n">stemmer</span><span class="p">,</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span> <span class="o">=</span> <span class="n">bm25s</span><span class="o">.</span><span class="n">BM25</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">corpus_tokens</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">verbose</span><span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">VectorStoreIndex</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseDocumentStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">stemmer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Stemmer</span><span class="o">.</span><span class="n">Stemmer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">language</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BM25Retriever"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">tokenizer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"The tokenizer parameter is deprecated and will be removed in a future release. "</span>
                <span class="s2">"Use a stemmer from PyStemmer instead."</span>
            <span class="p">)</span>

        <span class="c1"># ensure only one of index, nodes, or docstore is passed</span>
        <span class="k">if</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="k">for</span> <span class="n">val</span> <span class="ow">in</span> <span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="n">nodes</span><span class="p">,</span> <span class="n">docstore</span><span class="p">])</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Please pass exactly one of index, nodes, or docstore."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">index</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">docstore</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">docstore</span>

        <span class="k">if</span> <span class="n">docstore</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="nb">list</span><span class="p">(</span><span class="n">docstore</span><span class="o">.</span><span class="n">docs</span><span class="o">.</span><span class="n">values</span><span class="p">()))</span>

        <span class="k">assert</span> <span class="p">(</span>
            <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">),</span> <span class="s2">"Please pass exactly one of index, nodes, or docstore."</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">stemmer</span><span class="o">=</span><span class="n">stemmer</span><span class="p">,</span>
            <span class="n">language</span><span class="o">=</span><span class="n">language</span><span class="p">,</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the retriever to a directory."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">corpus</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BM25Retriever"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load the retriever from a directory."""</span>
        <span class="n">bm25</span> <span class="o">=</span> <span class="n">bm25s</span><span class="o">.</span><span class="n">BM25</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">load_corpus</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">existing_bm25</span><span class="o">=</span><span class="n">bm25</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">tokenized_query</span> <span class="o">=</span> <span class="n">bm25s</span><span class="o">.</span><span class="n">tokenize</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">stemmer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">stemmer</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span>
        <span class="p">)</span>
        <span class="n">indexes</span><span class="p">,</span> <span class="n">scores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
            <span class="n">tokenized_query</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span>
        <span class="p">)</span>

        <span class="c1"># batched, but only one query</span>
        <span class="n">indexes</span> <span class="o">=</span> <span class="n">indexes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">scores</span> <span class="o">=</span> <span class="n">scores</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">indexes</span><span class="p">,</span> <span class="n">scores</span><span class="p">):</span>
            <span class="c1"># idx can be an int or a dict of the node</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">idx</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">node_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">corpus</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">idx</span><span class="p">)]</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">node_dict</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="nb">float</span><span class="p">(</span><span class="n">score</span><span class="p">)))</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/#llama_index.retrievers.bm25.BM25Retriever.persist "Permanent link")

```
persist(path: str, **kwargs: Any) -> None
```

Persist the retriever to a directory.

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-bm25/llama_index/retrievers/bm25/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the retriever to a directory."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">bm25</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">corpus</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_dir `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/#llama_index.retrievers.bm25.BM25Retriever.from_persist_dir "Permanent link")

```
from_persist_dir(path: str, **kwargs: Any) -> [BM25Retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/#llama_index.retrievers.bm25.BM25Retriever "llama_index.retrievers.bm25.base.BM25Retriever")
```

Load the retriever from a directory.

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-bm25/llama_index/retrievers/bm25/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BM25Retriever"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load the retriever from a directory."""</span>
    <span class="n">bm25</span> <span class="o">=</span> <span class="n">bm25s</span><span class="o">.</span><span class="n">BM25</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">load_corpus</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">existing_bm25</span><span class="o">=</span><span class="n">bm25</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/)[Next Duckdb retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/duckdb_retriever/)
