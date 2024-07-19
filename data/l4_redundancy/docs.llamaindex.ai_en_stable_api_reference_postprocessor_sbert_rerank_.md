Title: Sbert rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/

Markdown Content:
Sbert rerank - LlamaIndex


SentenceTransformerRerank [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/#llama_index.postprocessor.sbert_rerank.SentenceTransformerRerank "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-sbert-rerank/llama_index/postprocessor/sbert_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 19</span>
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
<span class="normal">113</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SentenceTransformerRerank</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Sentence transformer model name."</span><span class="p">)</span>
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

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cross-encoder/stsb-distilroberta-base"</span><span class="p">,</span>
        <span class="n">device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_retrieval_score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">sentence_transformers</span> <span class="kn">import</span> <span class="n">CrossEncoder</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Cannot import sentence-transformers or torch package,"</span><span class="p">,</span>
                <span class="s2">"please `pip install torch sentence-transformers`"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span> <span class="k">if</span> <span class="n">device</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">device</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="n">CrossEncoder</span><span class="p">(</span>
            <span class="n">model</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="n">DEFAULT_SENTENCE_TRANSFORMER_MAX_LENGTH</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="n">device</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">top_n</span><span class="o">=</span><span class="n">top_n</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">,</span>
            <span class="n">keep_retrieval_score</span><span class="o">=</span><span class="n">keep_retrieval_score</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SentenceTransformerRerank"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">ReRankStartEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span>
                <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
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

            <span class="n">new_nodes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="o">-</span><span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="k">else</span> <span class="mi">0</span><span class="p">)[</span>
                <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span>
            <span class="p">]</span>
            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">new_nodes</span><span class="p">})</span>

        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">ReRankEndEvent</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">new_nodes</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Rankllm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankllm_rerank/)[Next Sentence optimizer](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/)
