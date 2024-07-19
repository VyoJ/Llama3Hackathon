Title: Mixture of agents - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/

Markdown Content:
Mixture of agents - LlamaIndex


MixtureOfAgentsPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/#llama_index.packs.mixture_of_agents.MixtureOfAgentsPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-mixture-of-agents/llama_index/packs/mixture_of_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MixtureOfAgentsPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">reference_llms</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LLM</span><span class="p">],</span>
        <span class="n">num_layers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">max_tokens</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2048</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.7</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reference_llms</span> <span class="o">=</span> <span class="n">reference_llms</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span> <span class="o">=</span> <span class="n">num_layers</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_tokens</span> <span class="o">=</span> <span class="n">max_tokens</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">temperature</span> <span class="o">=</span> <span class="n">temperature</span>

    <span class="k">def</span> <span class="nf">inject_references_to_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">references</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="n">system</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.</span>

<span class="s2">    Responses from models:"""</span>

        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">reference</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">references</span><span class="p">):</span>
            <span class="n">system</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="si">{</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">reference</span><span class="si">}</span><span class="s2">"</span>

        <span class="k">if</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o">==</span> <span class="s2">"system"</span><span class="p">:</span>
            <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">content</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">system</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">system</span><span class="p">),</span> <span class="o">*</span><span class="n">messages</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">messages</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_with_references</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">references</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">max_tokens</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">references</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">inject_references_to_messages</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">references</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span>
            <span class="k">await</span> <span class="n">llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">max_tokens</span><span class="o">=</span><span class="n">max_tokens</span><span class="p">,</span> <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">)</span>
        <span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">get_answer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">query_str</span><span class="p">))</span>

        <span class="n">references</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">reference_llms</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">prev_references</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">for</span> <span class="n">layer</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span><span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Round </span><span class="si">{</span><span class="n">layer</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span><span class="si">}</span><span class="s2"> to collecting reference responses."</span>
                <span class="p">)</span>

                <span class="n">references</span> <span class="o">=</span> <span class="p">[]</span>

                <span class="n">jobs</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">agenerate_with_references</span><span class="p">(</span>
                        <span class="n">llm</span><span class="o">=</span><span class="n">reference_llm</span><span class="p">,</span>
                        <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
                        <span class="n">references</span><span class="o">=</span><span class="n">prev_references</span><span class="p">,</span>
                        <span class="n">max_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_tokens</span><span class="p">,</span>
                        <span class="n">temperature</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">temperature</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="k">for</span> <span class="n">reference_llm</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">reference_llms</span>
                <span class="p">]</span>

                <span class="n">references</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">jobs</span><span class="p">)</span>

                <span class="k">if</span> <span class="n">layer</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
                    <span class="n">prev_references</span> <span class="o">=</span> <span class="n">references</span>

                    <span class="n">references</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">agenerate_with_references</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">,</span>
            <span class="n">max_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_tokens</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">references</span><span class="o">=</span><span class="n">references</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"reference_llms"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reference_llms</span><span class="p">,</span>
            <span class="s2">"num_layers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_answer</span><span class="p">(</span><span class="n">query_str</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/#llama_index.packs.mixture_of_agents.MixtureOfAgentsPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-mixture-of-agents/llama_index/packs/mixture_of_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"reference_llms"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reference_llms</span><span class="p">,</span>
        <span class="s2">"num_layers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_layers</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/#llama_index.packs.mixture_of_agents.MixtureOfAgentsPack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-mixture-of-agents/llama_index/packs/mixture_of_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_answer</span><span class="p">(</span><span class="n">query_str</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llava completion](https://docs.llamaindex.ai/en/stable/api_reference/packs/llava_completion/)[Next Multi document agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/)
