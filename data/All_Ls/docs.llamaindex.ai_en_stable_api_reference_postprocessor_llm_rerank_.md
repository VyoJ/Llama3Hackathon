Title: Llm rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/

Markdown Content:
Llm rerank - LlamaIndex


Node PostProcessor module.

LLMRerank [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/#llama_index.core.postprocessor.LLMRerank "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

LLM-based reranker.

Source code in `llama-index-core/llama_index/core/postprocessor/llm_rerank.py`

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
<span class="normal">113</span>
<span class="normal">114</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMRerank</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLM-based reranker."""</span>

    <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Top N nodes to return."</span><span class="p">)</span>
    <span class="n">choice_select_prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Choice select prompt."</span>
    <span class="p">)</span>
    <span class="n">choice_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Batch size for choice select."</span><span class="p">)</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The LLM to rerank with."</span><span class="p">)</span>

    <span class="n">_format_node_batch_fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_parse_choice_select_answer_fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">choice_select_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">choice_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">format_node_batch_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parse_choice_select_answer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">choice_select_prompt</span> <span class="o">=</span> <span class="n">choice_select_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_CHOICE_SELECT_PROMPT</span>

        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_format_node_batch_fn</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">format_node_batch_fn</span> <span class="ow">or</span> <span class="n">default_format_node_batch_fn</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parse_choice_select_answer_fn</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">parse_choice_select_answer_fn</span> <span class="ow">or</span> <span class="n">default_parse_choice_select_answer_fn</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">choice_select_prompt</span><span class="o">=</span><span class="n">choice_select_prompt</span><span class="p">,</span>
            <span class="n">choice_batch_size</span><span class="o">=</span><span class="n">choice_batch_size</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">top_n</span><span class="o">=</span><span class="n">top_n</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"choice_select_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">choice_select_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"choice_select_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">choice_select_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"choice_select_prompt"</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"LLMRerank"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query bundle must be provided."</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">initial_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">choice_batch_size</span><span class="p">):</span>
            <span class="n">nodes_batch</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">node</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">[</span><span class="n">idx</span> <span class="p">:</span> <span class="n">idx</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">choice_batch_size</span><span class="p">]</span>
            <span class="p">]</span>

            <span class="n">query_str</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
            <span class="n">fmt_batch_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_node_batch_fn</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">)</span>
            <span class="c1"># call each batch independently</span>
            <span class="n">raw_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">choice_select_prompt</span><span class="p">,</span>
                <span class="n">context_str</span><span class="o">=</span><span class="n">fmt_batch_str</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">raw_choices</span><span class="p">,</span> <span class="n">relevances</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_choice_select_answer_fn</span><span class="p">(</span>
                <span class="n">raw_response</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes_batch</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">choice_idxs</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">choice</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span> <span class="k">for</span> <span class="n">choice</span> <span class="ow">in</span> <span class="n">raw_choices</span><span class="p">]</span>
            <span class="n">choice_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">nodes_batch</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">choice_idxs</span><span class="p">]</span>
            <span class="n">relevances</span> <span class="o">=</span> <span class="n">relevances</span> <span class="ow">or</span> <span class="p">[</span><span class="mf">1.0</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">choice_nodes</span><span class="p">]</span>
            <span class="n">initial_results</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">relevance</span><span class="p">)</span>
                    <span class="k">for</span> <span class="n">node</span><span class="p">,</span> <span class="n">relevance</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">choice_nodes</span><span class="p">,</span> <span class="n">relevances</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">initial_results</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="ow">or</span> <span class="mf">0.0</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)[</span>
            <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Keyword](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/)[Next Long context reorder](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/)
