Title: Colbert rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colbert_rerank/

Markdown Content:
Colbert rerank - LlamaIndex


ColbertRerank [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colbert_rerank/#llama_index.postprocessor.colbert_rerank.ColbertRerank "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-colbert-rerank/llama_index/postprocessor/colbert_rerank/base.py`

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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ColbertRerank</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Colbert model name."</span><span class="p">)</span>
    <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Number of nodes to return sorted by score."</span><span class="p">)</span>
    <span class="n">device</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"cpu"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Device to use for sentence transformer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">keep_retrieval_score</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to keep the retrieval score in metadata."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">_model</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_tokenizer</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"colbert-ir/colbertv2.0"</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"colbert-ir/colbertv2.0"</span><span class="p">,</span>
        <span class="n">device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_retrieval_score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span> <span class="k">if</span> <span class="n">device</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">device</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="o">=</span> <span class="n">AutoTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">tokenizer</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="n">AutoModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">top_n</span><span class="o">=</span><span class="n">top_n</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">tokenizer</span><span class="o">=</span><span class="n">tokenizer</span><span class="p">,</span>
            <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">,</span>
            <span class="n">keep_retrieval_score</span><span class="o">=</span><span class="n">keep_retrieval_score</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ColbertRerank"</span>

    <span class="k">def</span> <span class="nf">_calculate_sim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">documents_text_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
        <span class="c1"># Query: [batch_size, query_length, embedding_size] -&gt; [batch_size, query_length, 1, embedding_size]</span>
        <span class="c1"># Document: [batch_size, doc_length, embedding_size] -&gt; [batch_size, 1, doc_length, embedding_size]</span>
        <span class="n">query_encoding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="p">(</span><span class="o">**</span><span class="n">query_encoding</span><span class="p">)</span><span class="o">.</span><span class="n">last_hidden_state</span>
        <span class="n">rerank_score_list</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">document_text</span> <span class="ow">in</span> <span class="n">documents_text_list</span><span class="p">:</span>
            <span class="n">document_encoding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span>
                <span class="n">document_text</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">,</span> <span class="n">truncation</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">512</span>
            <span class="p">)</span>
            <span class="n">document_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="p">(</span><span class="o">**</span><span class="n">document_encoding</span><span class="p">)</span><span class="o">.</span><span class="n">last_hidden_state</span>

            <span class="n">sim_matrix</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">functional</span><span class="o">.</span><span class="n">cosine_similarity</span><span class="p">(</span>
                <span class="n">query_embedding</span><span class="o">.</span><span class="n">unsqueeze</span><span class="p">(</span><span class="mi">2</span><span class="p">),</span> <span class="n">document_embedding</span><span class="o">.</span><span class="n">unsqueeze</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">dim</span><span class="o">=-</span><span class="mi">1</span>
            <span class="p">)</span>

            <span class="c1"># Take the maximum similarity for each query token (across all document tokens)</span>
            <span class="c1"># sim_matrix shape: [batch_size, query_length, doc_length]</span>
            <span class="n">max_sim_scores</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">max</span><span class="p">(</span><span class="n">sim_matrix</span><span class="p">,</span> <span class="n">dim</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
            <span class="n">rerank_score_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">torch</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">max_sim_scores</span><span class="p">,</span> <span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">rerank_score_list</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">ReRankStartEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span> <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span> <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing query bundle in extra info."</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o"></span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">):</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">keep_retrieval_score</span><span class="p">:</span>
                    <span class="c1"># keep the retrieval score in metadata</span>
                    <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"retrieval_score"</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">score</span>
                <span class="n">node</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>

            <span class="n">reranked_nodes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="o">-</span><span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="k">else</span> <span class="mi">0</span><span class="p">)[</span>
                <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span>
            <span class="p">]</span>
            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">reranked_nodes</span><span class="p">})</span>

        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">ReRankEndEvent</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">reranked_nodes</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">reranked_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cohere rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/cohere_rerank/)[Next Dashscope rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/dashscope_rerank/)
