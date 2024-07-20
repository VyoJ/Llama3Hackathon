Title: Sentence optimizer - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/

Markdown Content:
Sentence optimizer - LlamaIndex


Node PostProcessor module.

SentenceEmbeddingOptimizer [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/#llama_index.core.postprocessor.SentenceEmbeddingOptimizer "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Optimization of a text chunk given the query by shortening the input text.

Source code in `llama-index-core/llama_index/core/postprocessor/optimizer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
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
<span class="normal">168</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SentenceEmbeddingOptimizer</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Optimization of a text chunk given the query by shortening the input text."""</span>

    <span class="n">percentile_cutoff</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Percentile cutoff for the top k sentences to use."</span>
    <span class="p">)</span>
    <span class="n">threshold_cutoff</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Threshold cutoff for similarity for each sentence to use."</span>
    <span class="p">)</span>

    <span class="n">_embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_tokenizer_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="n">context_before</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Number of sentences before retrieved sentence for further context"</span>
    <span class="p">)</span>

    <span class="n">context_after</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Number of sentences after retrieved sentence for further context"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">percentile_cutoff</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">threshold_cutoff</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_before</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_after</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Optimizer class that is passed into BaseGPTIndexQuery.</span>

<span class="sd">        Should be set like this:</span>

<span class="sd">        .. code-block:: python</span>
<span class="sd">        from llama_index.core.optimization.optimizer import Optimizer</span>
<span class="sd">        optimizer = SentenceEmbeddingOptimizer(</span>
<span class="sd">                        percentile_cutoff=0.5</span>
<span class="sd">                        this means that the top 50% of sentences will be used.</span>
<span class="sd">                        Alternatively, you can set the cutoff using a threshold</span>
<span class="sd">                        on the similarity score. In this case only sentences with a</span>
<span class="sd">                        similarity score higher than the threshold will be used.</span>
<span class="sd">                        threshold_cutoff=0.7</span>
<span class="sd">                        these cutoffs can also be used together.</span>
<span class="sd">                    )</span>

<span class="sd">        query_engine = index.as_query_engine(</span>
<span class="sd">            optimizer=optimizer</span>
<span class="sd">        )</span>
<span class="sd">        response = query_engine.query("&lt;query_str&gt;")</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">embed_model</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.embeddings.openai</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">OpenAIEmbedding</span><span class="p">,</span>
                <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">OpenAIEmbedding</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"`llama-index-embeddings-openai` package not found, "</span>
                    <span class="s2">"please run `pip install llama-index-embeddings-openai`"</span>
                <span class="p">)</span>

        <span class="k">if</span> <span class="n">tokenizer_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">nltk.data</span>

            <span class="n">tokenizer</span> <span class="o">=</span> <span class="n">nltk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="s2">"tokenizers/punkt/english.pickle"</span><span class="p">)</span>
            <span class="n">tokenizer_fn</span> <span class="o">=</span> <span class="n">tokenizer</span><span class="o">.</span><span class="n">tokenize</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer_fn</span> <span class="o">=</span> <span class="n">tokenizer_fn</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">percentile_cutoff</span><span class="o">=</span><span class="n">percentile_cutoff</span><span class="p">,</span>
            <span class="n">threshold_cutoff</span><span class="o">=</span><span class="n">threshold_cutoff</span><span class="p">,</span>
            <span class="n">context_after</span><span class="o">=</span><span class="n">context_after</span><span class="p">,</span>
            <span class="n">context_before</span><span class="o">=</span><span class="n">context_before</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SentenceEmbeddingOptimizer"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Optimize a node text given the query by shortening the node text."""</span>
        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">nodes</span>

        <span class="k">for</span> <span class="n">node_idx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)):</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">nodes</span><span class="p">[</span><span class="n">node_idx</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span>

            <span class="n">split_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer_fn</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_agg_embedding_from_queries</span><span class="p">(</span>
                        <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span>
                    <span class="p">)</span>
                <span class="p">)</span>

            <span class="n">text_embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">_get_text_embeddings</span><span class="p">(</span><span class="n">split_text</span><span class="p">)</span>

            <span class="n">num_top_k</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">threshold</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">percentile_cutoff</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">num_top_k</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">split_text</span><span class="p">)</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">percentile_cutoff</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">threshold_cutoff</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">threshold</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">threshold_cutoff</span>

            <span class="n">top_similarities</span><span class="p">,</span> <span class="n">top_idxs</span> <span class="o">=</span> <span class="n">get_top_k_embeddings</span><span class="p">(</span>
                <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="n">text_embeddings</span><span class="p">,</span>
                <span class="n">similarity_fn</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">similarity</span><span class="p">,</span>
                <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">num_top_k</span><span class="p">,</span>
                <span class="n">embedding_ids</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">text_embeddings</span><span class="p">))),</span>
                <span class="n">similarity_cutoff</span><span class="o">=</span><span class="n">threshold</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">top_idxs</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Optimizer returned zero sentences."</span><span class="p">)</span>

            <span class="n">rangeMin</span><span class="p">,</span> <span class="n">rangeMax</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">split_text</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_before</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">context_before</span> <span class="o">=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_after</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">context_after</span> <span class="o">=</span> <span class="mi">1</span>

            <span class="n">top_sentences</span> <span class="o">=</span> <span class="p">[</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="n">split_text</span><span class="p">[</span>
                        <span class="nb">max</span><span class="p">(</span><span class="n">idx</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_before</span><span class="p">,</span> <span class="n">rangeMin</span><span class="p">)</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span>
                            <span class="n">idx</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_after</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">rangeMax</span>
                        <span class="p">)</span>
                    <span class="p">]</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">top_idxs</span>
            <span class="p">]</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Top </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">top_idxs</span><span class="p">)</span><span class="si">}</span><span class="s2"> sentences with scores:</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">logger</span><span class="o">.</span><span class="n">isEnabledFor</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">):</span>
                <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">top_idxs</span><span class="p">)):</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">top_sentences</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">top_similarities</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span>
                    <span class="p">)</span>

            <span class="n">nodes</span><span class="p">[</span><span class="n">node_idx</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">top_sentences</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/)[Next Similarity](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/)
