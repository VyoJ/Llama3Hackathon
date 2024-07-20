Title: Openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/

Markdown Content:
Openai - LlamaIndex


OpenAIQuestionGenerator [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/#llama_index.question_gen.openai.OpenAIQuestionGenerator "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQuestionGenerator](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.BaseQuestionGenerator "llama_index.core.question_gen.types.BaseQuestionGenerator")`

Source code in `llama-index-integrations/question_gen/llama-index-question-gen-openai/llama_index/question_gen/openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 48</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIQuestionGenerator</span><span class="p">(</span><span class="n">BaseQuestionGenerator</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">program</span><span class="p">:</span> <span class="n">OpenAIPydanticProgram</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_program</span> <span class="o">=</span> <span class="n">program</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_OPENAI_SUB_QUESTION_PROMPT_TMPL</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIQuestionGenerator"</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="n">program</span> <span class="o">=</span> <span class="n">OpenAIPydanticProgram</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">SubQuestionList</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">prompt_template_str</span><span class="o">=</span><span class="n">prompt_template_str</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">program</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"question_gen_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program</span><span class="o">.</span><span class="n">prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"question_gen_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_program</span><span class="o">.</span><span class="n">prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"question_gen_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">generate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="n">tools_str</span> <span class="o">=</span> <span class="n">build_tools_text</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">question_list</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">SubQuestionList</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">tools_str</span><span class="o">=</span><span class="n">tools_str</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">question_list</span><span class="o">.</span><span class="n">items</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="n">tools_str</span> <span class="o">=</span> <span class="n">build_tools_text</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">question_list</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">SubQuestionList</span><span class="p">,</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program</span><span class="o">.</span><span class="n">acall</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span> <span class="n">tools_str</span><span class="o">=</span><span class="n">tools_str</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">question_list</span><span class="p">,</span> <span class="n">SubQuestionList</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">question_list</span><span class="o">.</span><span class="n">items</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llm question gen](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/)[Next Agent search](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/)
