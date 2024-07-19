Title: Multi modal - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/

Markdown Content:
Multi modal - LlamaIndex


MultiModalLLMCompletionProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/#llama_index.core.program.multi_modal_llm_program.MultiModalLLMCompletionProgram "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticProgram](https://docs.llamaindex.ai/en/stable/api_reference/program/#llama_index.core.types.BasePydanticProgram "llama_index.core.types.BasePydanticProgram")[BaseModel]`

Multi Modal LLM Completion Program.

Uses generic Multi Modal LLM completion + an output parser to generate a structured output.

Source code in `llama-index-core/llama_index/core/program/multi_modal_llm_program.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
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
<span class="normal">136</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiModalLLMCompletionProgram</span><span class="p">(</span><span class="n">BasePydanticProgram</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Multi Modal LLM Completion Program.</span>

<span class="sd">    Uses generic Multi Modal LLM completion + an output parser to generate a structured output.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">PydanticOutputParser</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">,</span>
        <span class="n">multi_modal_llm</span><span class="p">:</span> <span class="n">MultiModalLLM</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span> <span class="o">=</span> <span class="n">multi_modal_llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_image_documents</span> <span class="o">=</span> <span class="n">image_documents</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PydanticOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">multi_modal_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MultiModalLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MultiModalLLMCompletionProgram"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">multi_modal_llm</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.multi_modal_llms.openai</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">OpenAIMultiModal</span><span class="p">,</span>
                <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="n">multi_modal_llm</span> <span class="o">=</span> <span class="n">OpenAIMultiModal</span><span class="p">(</span>
                    <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span> <span class="n">temperature</span><span class="o">=</span><span class="mi">0</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"`llama-index-multi-modal-llms-openai` package cannot be found. "</span>
                    <span class="s2">"Please install it by using `pip install `llama-index-multi-modal-llms-openai`"</span>
                <span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">prompt_template_str</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">output_parser</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">output_cls</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either output_cls or output_parser."</span><span class="p">)</span>
            <span class="n">output_parser</span> <span class="o">=</span> <span class="n">PydanticOutputParser</span><span class="p">(</span><span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">output_parser</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">PromptTemplate</span><span class="p">,</span> <span class="n">prompt</span><span class="p">),</span>
            <span class="n">multi_modal_llm</span><span class="o">=</span><span class="n">multi_modal_llm</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">output_cls</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePromptTemplate</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span>

    <span class="nd">@prompt</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseModel</span><span class="p">:</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">formatted_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span>
            <span class="n">formatted_prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_image_documents</span><span class="p">,</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">raw_output</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">text</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Raw output: </span><span class="si">{</span><span class="n">raw_output</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"llama_blue"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">raw_output</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseModel</span><span class="p">:</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">formatted_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span>
            <span class="n">formatted_prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="n">image_documents</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_image_documents</span><span class="p">,</span>
            <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">raw_output</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">text</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Raw output: </span><span class="si">{</span><span class="n">raw_output</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"llama_blue"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">raw_output</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Lmformatenforcer](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/)[Next Openai](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/)
