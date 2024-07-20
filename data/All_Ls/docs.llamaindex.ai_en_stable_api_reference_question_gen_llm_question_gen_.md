Title: Llm question gen - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/

Markdown Content:
Llm question gen - LlamaIndex


LLMQuestionGenerator [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/#llama_index.core.question_gen.LLMQuestionGenerator "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQuestionGenerator](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.BaseQuestionGenerator "llama_index.core.question_gen.types.BaseQuestionGenerator")`

Source code in `llama-index-core/llama_index/core/question_gen/llm_generators.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span>
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMQuestionGenerator</span><span class="p">(</span><span class="n">BaseQuestionGenerator</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Prompt should have output parser."</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LLMQuestionGenerator"</span><span class="p">:</span>
        <span class="c1"># optionally initialize defaults</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="n">prompt_template_str</span> <span class="ow">or</span> <span class="n">DEFAULT_SUB_QUESTION_PROMPT_TMPL</span>
        <span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span> <span class="ow">or</span> <span class="n">SubQuestionOutputParser</span><span class="p">()</span>

        <span class="c1"># construct prompt</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span>
            <span class="n">template</span><span class="o">=</span><span class="n">prompt_template_str</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">prompt_type</span><span class="o">=</span><span class="n">PromptType</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"question_gen_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"question_gen_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="n">output_parser</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"question_gen_prompt"</span><span class="p">]</span><span class="o">.</span><span class="n">output_parser</span>
            <span class="k">if</span> <span class="n">output_parser</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">output_parser</span> <span class="o">=</span> <span class="n">SubQuestionOutputParser</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span>
                <span class="n">prompts</span><span class="p">[</span><span class="s2">"question_gen_prompt"</span><span class="p">]</span><span class="o">.</span><span class="n">template</span><span class="p">,</span> <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="n">tools_str</span> <span class="o">=</span> <span class="n">build_tools_text</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">prediction</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span>
            <span class="n">tools_str</span><span class="o">=</span><span class="n">tools_str</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">parse</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">prediction</span><span class="p">)</span>
        <span class="n">parse</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">StructuredOutput</span><span class="p">,</span> <span class="n">parse</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">parse</span><span class="o">.</span><span class="n">parsed_output</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="n">tools_str</span> <span class="o">=</span> <span class="n">build_tools_text</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">prediction</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span>
            <span class="n">tools_str</span><span class="o">=</span><span class="n">tools_str</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">parse</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">prediction</span><span class="p">)</span>
        <span class="n">parse</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">StructuredOutput</span><span class="p">,</span> <span class="n">parse</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">parse</span><span class="o">.</span><span class="n">parsed_output</span>
</code></pre></div></td></tr></tbody></table>

SubQuestionOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/#llama_index.core.question_gen.SubQuestionOutputParser "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/#llama_index.core.types.BaseOutputParser "llama_index.core.types.BaseOutputParser")`

Source code in `llama-index-core/llama_index/core/question_gen/output_parser.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubQuestionOutputParser</span><span class="p">(</span><span class="n">BaseOutputParser</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="n">json_dict</span> <span class="o">=</span> <span class="n">parse_json_markdown</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">json_dict</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"No valid JSON found in output: </span><span class="si">{</span><span class="n">output</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># example code includes an 'items' key, which breaks</span>
        <span class="c1"># the parsing from open-source LLMs such as Zephyr.</span>
        <span class="c1"># This gets the actual subquestions and recommended tools directly</span>
        <span class="k">if</span> <span class="s2">"items"</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="p">:</span>
            <span class="n">json_dict</span> <span class="o">=</span> <span class="n">json_dict</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]</span>

        <span class="n">sub_questions</span> <span class="o">=</span> <span class="p">[</span><span class="n">SubQuestion</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">StructuredOutput</span><span class="p">(</span><span class="n">raw_output</span><span class="o">=</span><span class="n">output</span><span class="p">,</span> <span class="n">parsed_output</span><span class="o">=</span><span class="n">sub_questions</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">prompt_template</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/)[Next Openai](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/)
