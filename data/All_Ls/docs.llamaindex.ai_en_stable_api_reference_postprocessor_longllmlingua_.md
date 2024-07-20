Title: Longllmlingua - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/

Markdown Content:
Longllmlingua - LlamaIndex


LongLLMLinguaPostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/#llama_index.postprocessor.longllmlingua.LongLLMLinguaPostprocessor "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Optimization of nodes.

Compress using LongLLMLingua paper.

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-longllmlingua/llama_index/postprocessor/longllmlingua/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 15</span>
<span class="normal"> 16</span>
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
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LongLLMLinguaPostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Optimization of nodes.</span>

<span class="sd">    Compress using LongLLMLingua paper.</span>

<span class="sd">    """</span>

    <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Metadata mode."</span>
    <span class="p">)</span>
    <span class="n">instruction_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_INSTRUCTION_STR</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Instruction string."</span>
    <span class="p">)</span>
    <span class="n">target_token</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Target number of compressed tokens."</span>
    <span class="p">)</span>
    <span class="n">rank_method</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">"longllmlingua"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Ranking method."</span><span class="p">)</span>
    <span class="n">additional_compress_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Additional compress kwargs."</span>
    <span class="p">)</span>

    <span class="n">_llm_lingua</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"NousResearch/Llama-2-7b-hf"</span><span class="p">,</span>
        <span class="n">device_map</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cuda"</span><span class="p">,</span>
        <span class="n">model_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="n">open_api_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">,</span>
        <span class="n">instruction_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_INSTRUCTION_STR</span><span class="p">,</span>
        <span class="n">target_token</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">300</span><span class="p">,</span>
        <span class="n">rank_method</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"longllmlingua"</span><span class="p">,</span>
        <span class="n">additional_compress_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""LongLLMLingua Compressor for Node Context."""</span>
        <span class="kn">from</span> <span class="nn">llmlingua</span> <span class="kn">import</span> <span class="n">PromptCompressor</span>

        <span class="n">open_api_config</span> <span class="o">=</span> <span class="n">open_api_config</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">additional_compress_kwargs</span> <span class="o">=</span> <span class="n">additional_compress_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm_lingua</span> <span class="o">=</span> <span class="n">PromptCompressor</span><span class="p">(</span>
            <span class="n">model_name</span><span class="o">=</span><span class="n">model_name</span><span class="p">,</span>
            <span class="n">device_map</span><span class="o">=</span><span class="n">device_map</span><span class="p">,</span>
            <span class="n">model_config</span><span class="o">=</span><span class="n">model_config</span><span class="p">,</span>
            <span class="n">open_api_config</span><span class="o">=</span><span class="n">open_api_config</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">metadata_mode</span><span class="o">=</span><span class="n">metadata_mode</span><span class="p">,</span>
            <span class="n">instruction_str</span><span class="o">=</span><span class="n">instruction_str</span><span class="p">,</span>
            <span class="n">target_token</span><span class="o">=</span><span class="n">target_token</span><span class="p">,</span>
            <span class="n">rank_method</span><span class="o">=</span><span class="n">rank_method</span><span class="p">,</span>
            <span class="n">additional_compress_kwargs</span><span class="o">=</span><span class="n">additional_compress_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"LongLLMLinguaPostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Optimize a node text given the query by shortening the node text."""</span>
        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query bundle is required."</span><span class="p">)</span>
        <span class="n">context_texts</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="c1"># split by "\n\n" (recommended by LongLLMLingua authors)</span>
        <span class="n">new_context_texts</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">c</span> <span class="k">for</span> <span class="n">context</span> <span class="ow">in</span> <span class="n">context_texts</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">context</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="p">]</span>

        <span class="c1"># You can use it this way, although the question-aware fine-grained compression hasn't been enabled.</span>
        <span class="n">compressed_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm_lingua</span><span class="o">.</span><span class="n">compress_prompt</span><span class="p">(</span>
            <span class="n">new_context_texts</span><span class="p">,</span>  <span class="c1"># ! Replace the previous context_list</span>
            <span class="n">instruction</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">instruction_str</span><span class="p">,</span>
            <span class="n">question</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="c1"># target_token=2000,</span>
            <span class="n">target_token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">target_token</span><span class="p">,</span>
            <span class="n">rank_method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">rank_method</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">additional_compress_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">compressed_prompt_txt</span> <span class="o">=</span> <span class="n">compressed_prompt</span><span class="p">[</span><span class="s2">"compressed_prompt"</span><span class="p">]</span>

        <span class="c1"># separate out the question and instruction (appended to top and bottom)</span>
        <span class="n">compressed_prompt_txt_list</span> <span class="o">=</span> <span class="n">compressed_prompt_txt</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">compressed_prompt_txt_list</span> <span class="o">=</span> <span class="n">compressed_prompt_txt_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>

        <span class="c1"># return nodes for each list</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">t</span><span class="p">))</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">compressed_prompt_txt_list</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Long context reorder](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/)[Next Metadata replacement](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/)
