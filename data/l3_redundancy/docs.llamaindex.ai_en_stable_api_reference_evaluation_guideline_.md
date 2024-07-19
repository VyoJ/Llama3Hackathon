Title: Guideline - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/

Markdown Content:
Guideline - LlamaIndex


Evaluation modules.

GuidelineEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/#llama_index.core.evaluation.GuidelineEvaluator "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Guideline evaluator.

Evaluates whether a query and response pair passes the given guidelines.

This evaluator only considers the query string and the response string.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context(Optional[ServiceContext])` |  | 
The service context to use for evaluation.



 | _required_ |
| `guidelines(Optional[str])` |  | 

User-added guidelines to use for evaluation. Defaults to None, which uses the default guidelines.



 | _required_ |
| `eval_template(Optional[Union[str,` | `BasePromptTemplate]] ` | 

The template to use for evaluation.



 | _required_ |

Source code in `llama-index-core/llama_index/core/evaluation/guideline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GuidelineEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Guideline evaluator.</span>

<span class="sd">    Evaluates whether a query and response pair passes the given guidelines.</span>

<span class="sd">    This evaluator only considers the query string and the response string.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context(Optional[ServiceContext]):</span>
<span class="sd">            The service context to use for evaluation.</span>
<span class="sd">        guidelines(Optional[str]): User-added guidelines to use for evaluation.</span>
<span class="sd">            Defaults to None, which uses the default guidelines.</span>
<span class="sd">        eval_template(Optional[Union[str, BasePromptTemplate]] ):</span>
<span class="sd">            The template to use for evaluation.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">guidelines</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">eval_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePromptTemplate</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PydanticOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_guidelines</span> <span class="o">=</span> <span class="n">guidelines</span> <span class="ow">or</span> <span class="n">DEFAULT_GUIDELINES</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_template</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">eval_template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">eval_template</span> <span class="ow">or</span> <span class="n">DEFAULT_EVAL_TEMPLATE</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span> <span class="o">=</span> <span class="n">output_parser</span> <span class="ow">or</span> <span class="n">PydanticOutputParser</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">EvaluationData</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"eval_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"eval_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"eval_template"</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluate whether the query and response pair passes the guidelines."""</span>
        <span class="k">del</span> <span class="n">contexts</span>  <span class="c1"># Unused</span>
        <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>
        <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query and response must be provided"</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"prompt: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"query: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"response: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"guidelines: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_guidelines</span><span class="p">)</span>

        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

        <span class="n">eval_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">guidelines</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_guidelines</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">eval_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">eval_response</span><span class="p">)</span>
        <span class="n">eval_data</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluationData</span><span class="p">,</span> <span class="n">eval_data</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">passing</span><span class="o">=</span><span class="n">eval_data</span><span class="o">.</span><span class="n">passing</span><span class="p">,</span>
            <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="k">if</span> <span class="n">eval_data</span><span class="o">.</span><span class="n">passing</span> <span class="k">else</span> <span class="mf">0.0</span><span class="p">,</span>
            <span class="n">feedback</span><span class="o">=</span><span class="n">eval_data</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/#llama_index.core.evaluation.GuidelineEvaluator.aevaluate "Permanent link")

```
aevaluate(query: Optional[str] = None, response: Optional[str] = None, contexts: Optional[Sequence[str]] = None, sleep_time_in_seconds: int = 0, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Evaluate whether the query and response pair passes the guidelines.

Source code in `llama-index-core/llama_index/core/evaluation/guideline.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Evaluate whether the query and response pair passes the guidelines."""</span>
    <span class="k">del</span> <span class="n">contexts</span>  <span class="c1"># Unused</span>
    <span class="k">del</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>
    <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query and response must be provided"</span><span class="p">)</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"prompt: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"query: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"response: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"guidelines: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_guidelines</span><span class="p">)</span>

    <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>

    <span class="n">eval_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_eval_template</span><span class="p">,</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="n">guidelines</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_guidelines</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">eval_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">eval_response</span><span class="p">)</span>
    <span class="n">eval_data</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluationData</span><span class="p">,</span> <span class="n">eval_data</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
        <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="n">passing</span><span class="o">=</span><span class="n">eval_data</span><span class="o">.</span><span class="n">passing</span><span class="p">,</span>
        <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span> <span class="k">if</span> <span class="n">eval_data</span><span class="o">.</span><span class="n">passing</span> <span class="k">else</span> <span class="mf">0.0</span><span class="p">,</span>
        <span class="n">feedback</span><span class="o">=</span><span class="n">eval_data</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Faithfullness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/)
