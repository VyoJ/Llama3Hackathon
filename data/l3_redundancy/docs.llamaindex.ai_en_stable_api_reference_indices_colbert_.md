Title: Colbert - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/

Markdown Content:
Colbert - LlamaIndex


ColbertIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/#llama_index.indices.managed.colbert.ColbertIndex "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")[IndexDict]`

Store for ColBERT v2 with PLAID indexing.

ColBERT is a neural retrieval method that tends to work well in a zero-shot setting on out of domain datasets, due to it's use of token-level encodings (rather than sentence or chunk level)

Parameters:

index\_path: directory containing PLAID index files. model\_name: ColBERT hugging face model name. Default: "colbert-ir/colbertv2.0". show\_progress: whether to show progress bar when building index. Default: False. noop for ColBERT for now. nbits: number of bits to quantize the residual vectors. Default: 2. kmeans\_niters: number of kmeans clustering iterations. Default: 1. gpus: number of GPUs to use for indexing. Default: 0. rank: number of ranks to use for indexing. Default: 1. doc\_maxlen: max document length. Default: 120. query\_maxlen: max query length. Default: 60. kmeans\_niters: number of kmeans iterations. Default: 4.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-colbert/llama_index/indices/managed/colbert/base.py`

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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ColbertIndex</span><span class="p">(</span><span class="n">BaseIndex</span><span class="p">[</span><span class="n">IndexDict</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Store for ColBERT v2 with PLAID indexing.</span>

<span class="sd">    ColBERT is a neural retrieval method that tends to work</span>
<span class="sd">    well in a zero-shot setting on out of domain datasets, due</span>
<span class="sd">    to it's use of token-level encodings (rather than sentence or</span>
<span class="sd">    chunk level)</span>

<span class="sd">    Parameters:</span>

<span class="sd">    index_path: directory containing PLAID index files.</span>
<span class="sd">    model_name: ColBERT hugging face model name.</span>
<span class="sd">        Default: "colbert-ir/colbertv2.0".</span>
<span class="sd">    show_progress: whether to show progress bar when building index.</span>
<span class="sd">        Default: False. noop for ColBERT for now.</span>
<span class="sd">    nbits: number of bits to quantize the residual vectors. Default: 2.</span>
<span class="sd">    kmeans_niters: number of kmeans clustering iterations. Default: 1.</span>
<span class="sd">    gpus: number of GPUs to use for indexing. Default: 0.</span>
<span class="sd">    rank: number of ranks to use for indexing. Default: 1.</span>
<span class="sd">    doc_maxlen: max document length. Default: 120.</span>
<span class="sd">    query_maxlen: max query length. Default: 60.</span>
<span class="sd">    kmeans_niters: number of kmeans iterations. Default: 4.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_struct</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexDict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"colbert-ir/colbertv2.0"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">nbits</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">gpus</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">ranks</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">doc_maxlen</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">120</span><span class="p">,</span>
        <span class="n">query_maxlen</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">60</span><span class="p">,</span>
        <span class="n">kmeans_niters</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model_name</span> <span class="o">=</span> <span class="n">model_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index_path</span> <span class="o">=</span> <span class="s2">"storage/colbert_index"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span> <span class="o">=</span> <span class="n">index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nbits</span> <span class="o">=</span> <span class="n">nbits</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">gpus</span> <span class="o">=</span> <span class="n">gpus</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ranks</span> <span class="o">=</span> <span class="n">ranks</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">doc_maxlen</span> <span class="o">=</span> <span class="n">doc_maxlen</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_maxlen</span> <span class="o">=</span> <span class="n">query_maxlen</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">kmeans_niters</span> <span class="o">=</span> <span class="n">kmeans_niters</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docs_pos_to_node_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install colbert to use this feature from the repo:"</span><span class="p">,</span>
                <span class="s2">"https://github.com/stanford-futuredata/ColBERT"</span><span class="p">,</span>
            <span class="p">)</span> <span class="kn">from</span> <span class="nn">exc</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"ColbertStoreIndex does not support insertion yet."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_delete_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"ColbertStoreIndex does not support deletion yet."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">.retriever</span> <span class="kn">import</span> <span class="n">ColbertRetriever</span>

        <span class="k">return</span> <span class="n">ColbertRetriever</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_object_map</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RefDocInfo</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"ColbertStoreIndex does not support ref_doc_info."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexDict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a PLAID index from the ColBERT checkpoint via its hugging face</span>
<span class="sd">        model_name.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">colbert</span> <span class="kn">import</span> <span class="n">Indexer</span><span class="p">,</span> <span class="n">Searcher</span>
        <span class="kn">from</span> <span class="nn">colbert.infra</span> <span class="kn">import</span> <span class="n">ColBERTConfig</span><span class="p">,</span> <span class="n">Run</span><span class="p">,</span> <span class="n">RunConfig</span>

        <span class="n">index_struct</span> <span class="o">=</span> <span class="n">IndexDict</span><span class="p">()</span>

        <span class="n">docs_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">docs_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">())</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_docs_pos_to_node_id</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
            <span class="n">index_struct</span><span class="o">.</span><span class="n">add_node</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">text_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">))</span>

        <span class="k">with</span> <span class="n">Run</span><span class="p">()</span><span class="o">.</span><span class="n">context</span><span class="p">(</span>
            <span class="n">RunConfig</span><span class="p">(</span><span class="n">index_root</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index_path</span><span class="p">,</span> <span class="n">nranks</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ranks</span><span class="p">,</span> <span class="n">gpus</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gpus</span><span class="p">)</span>
        <span class="p">):</span>
            <span class="n">config</span> <span class="o">=</span> <span class="n">ColBERTConfig</span><span class="p">(</span>
                <span class="n">doc_maxlen</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">doc_maxlen</span><span class="p">,</span>
                <span class="n">query_maxlen</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query_maxlen</span><span class="p">,</span>
                <span class="n">nbits</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nbits</span><span class="p">,</span>
                <span class="n">kmeans_niters</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">kmeans_niters</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">indexer</span> <span class="o">=</span> <span class="n">Indexer</span><span class="p">(</span><span class="n">checkpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span> <span class="n">config</span><span class="o">=</span><span class="n">config</span><span class="p">)</span>
            <span class="n">indexer</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="n">docs_list</span><span class="p">,</span> <span class="n">overwrite</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">store</span> <span class="o">=</span> <span class="n">Searcher</span><span class="p">(</span>
                <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="n">docs_list</span><span class="p">,</span> <span class="n">checkpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">index_struct</span>

    <span class="c1"># @staticmethod</span>
    <span class="c1"># def _normalize_scores(docs: List[Document]) -&gt; None:</span>
    <span class="c1">#     "Normalizing the MaxSim scores using softmax."</span>
    <span class="c1">#     Z = sum(math.exp(doc.score) for doc in docs)</span>
    <span class="c1">#     for doc in docs:</span>
    <span class="c1">#         doc.score = math.exp(doc.score) / Z</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Check if the destination directory exists</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">):</span>
            <span class="c1"># Remove the existing destination directory</span>
            <span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>

        <span class="c1"># Copy PLAID vectors</span>
        <span class="n">shutil</span><span class="o">.</span><span class="n">copytree</span><span class="p">(</span>
            <span class="n">Path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_path</span><span class="p">)</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span> <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">load_from_disk</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ColbertIndex"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">colbert</span> <span class="kn">import</span> <span class="n">Searcher</span>
        <span class="kn">from</span> <span class="nn">colbert.infra</span> <span class="kn">import</span> <span class="n">ColBERTConfig</span>

        <span class="n">colbert_config</span> <span class="o">=</span> <span class="n">ColBERTConfig</span><span class="o">.</span><span class="n">load_from_index</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span> <span class="o">/</span> <span class="n">index_name</span><span class="p">)</span>
        <span class="n">searcher</span> <span class="o">=</span> <span class="n">Searcher</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span> <span class="n">index_root</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">config</span><span class="o">=</span><span class="n">colbert_config</span>
        <span class="p">)</span>
        <span class="n">sc</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">)</span>
        <span class="n">colbert_index</span> <span class="o">=</span> <span class="n">ColbertIndex</span><span class="p">(</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">sc</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">index_structs</span><span class="p">()[</span><span class="mi">0</span><span class="p">],</span> <span class="n">storage_context</span><span class="o">=</span><span class="n">sc</span>
        <span class="p">)</span>
        <span class="n">docs_pos_to_node_id</span> <span class="o">=</span> <span class="p">{</span>
            <span class="nb">int</span><span class="p">(</span><span class="n">k</span><span class="p">):</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">colbert_index</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">nodes_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">}</span>
        <span class="n">colbert_index</span><span class="o">.</span><span class="n">_docs_pos_to_node_id</span> <span class="o">=</span> <span class="n">docs_pos_to_node_id</span>
        <span class="n">colbert_index</span><span class="o">.</span><span class="n">store</span> <span class="o">=</span> <span class="n">searcher</span>
        <span class="k">return</span> <span class="n">colbert_index</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Query the Colbert v2 + Plaid store.</span>

<span class="sd">        Returns: list of NodeWithScore.</span>
<span class="sd">        """</span>
        <span class="n">doc_ids</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">scores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">top_k</span><span class="p">)</span>

        <span class="n">node_doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_docs_pos_to_node_id</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span> <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">doc_ids</span><span class="p">]</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_doc_ids</span><span class="p">)</span>

        <span class="n">nodes_with_score</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">):</span>
            <span class="n">nodes_with_score</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">nodes_with_score</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/#llama_index.indices.managed.colbert.ColbertIndex.query "Permanent link")

```
query(query_str: str, top_k: int = 10) -> List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]
```

Query the Colbert v2 + Plaid store.

Returns: list of NodeWithScore.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-colbert/llama_index/indices/managed/colbert/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">180</span>
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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query the Colbert v2 + Plaid store.</span>

<span class="sd">    Returns: list of NodeWithScore.</span>
<span class="sd">    """</span>
    <span class="n">doc_ids</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">scores</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="n">top_k</span><span class="p">)</span>

    <span class="n">node_doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_docs_pos_to_node_id</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span> <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">doc_ids</span><span class="p">]</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_doc_ids</span><span class="p">)</span>

    <span class="n">nodes_with_score</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">):</span>
        <span class="n">nodes_with_score</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">nodes_with_score</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tonic validate](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/)[Next Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/)
