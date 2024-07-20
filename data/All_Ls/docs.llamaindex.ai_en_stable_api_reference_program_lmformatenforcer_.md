Title: Lmformatenforcer - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/

Markdown Content:
Lmformatenforcer - LlamaIndex


LMFormatEnforcerPydanticProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/#llama_index.program.lmformatenforcer.LMFormatEnforcerPydanticProgram "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseLLMFunctionProgram`

A lm-format-enforcer-based function that returns a pydantic model.

In LMFormatEnforcerPydanticProgram, prompt\_template\_str can also have a {json\_schema} parameter that will be automatically filled by the json\_schema of output\_cls. Note: this interface is not yet stable.

Source code in `llama-index-integrations/program/llama-index-program-lmformatenforcer/llama_index/program/lmformatenforcer/base.py`

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
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LMFormatEnforcerPydanticProgram</span><span class="p">(</span><span class="n">BaseLLMFunctionProgram</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A lm-format-enforcer-based function that returns a pydantic model.</span>

<span class="sd">    In LMFormatEnforcerPydanticProgram, prompt_template_str can also have a {json_schema} parameter</span>
<span class="sd">    that will be automatically filled by the json_schema of output_cls.</span>
<span class="sd">    Note: this interface is not yet stable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">LlamaCPP</span><span class="p">,</span> <span class="n">HuggingFaceLLM</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">lmformatenforcer</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"lm-format-enforcer package not found."</span>
                <span class="s2">"please run `pip install lm-format-enforcer`"</span>
            <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.core.llms</span> <span class="kn">import</span> <span class="n">LlamaCPP</span>

                <span class="n">llm</span> <span class="o">=</span> <span class="n">LlamaCPP</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"llama.cpp package not found."</span>
                    <span class="s2">"please run `pip install llama-cpp-python`"</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_template_str</span> <span class="o">=</span> <span class="n">prompt_template_str</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="n">json_schema_parser</span> <span class="o">=</span> <span class="n">lmformatenforcer</span><span class="o">.</span><span class="n">JsonSchemaParser</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">output_cls</span><span class="o">.</span><span class="n">schema</span><span class="p">())</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_token_enforcer_fn</span> <span class="o">=</span> <span class="n">build_lm_format_enforcer_function</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="n">json_schema_parser</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="s2">"LlamaCPP"</span><span class="p">,</span> <span class="s2">"HuggingFaceLLM"</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLLMFunctionProgram"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From defaults."""</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="n">prompt</span><span class="o">.</span><span class="n">template</span>
        <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">prompt_template_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="p">,</span>
            <span class="n">prompt_template_str</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseModel</span><span class="p">:</span>
        <span class="n">llm_kwargs</span> <span class="o">=</span> <span class="n">llm_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="c1"># While the format enforcer is active, any calls to the llm will have the format enforced.</span>
        <span class="k">with</span> <span class="n">activate_lm_format_enforcer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token_enforcer_fn</span><span class="p">):</span>
            <span class="n">json_schema_str</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">output_cls</span><span class="o">.</span><span class="n">schema</span><span class="p">())</span>
            <span class="n">full_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt_template_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">json_schema</span><span class="o">=</span><span class="n">json_schema_str</span>
            <span class="p">)</span>
            <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span><span class="n">full_str</span><span class="p">,</span> <span class="o">**</span><span class="n">llm_kwargs</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">output</span><span class="o">.</span><span class="n">text</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/#llama_index.program.lmformatenforcer.LMFormatEnforcerPydanticProgram.from_defaults "Permanent link")

```
from_defaults(output_cls: Type[BaseModel], prompt_template_str: Optional[str] = None, prompt: Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.base.PromptTemplate")] = None, llm: Optional[Union[[LlamaCPP](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_cpp/#llama_index.llms.llama_cpp.LlamaCPP "llama_index.llms.llama_cpp.LlamaCPP"), [HuggingFaceLLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface/#llama_index.llms.huggingface.HuggingFaceLLM "llama_index.llms.huggingface.HuggingFaceLLM")]] = None, **kwargs: Any) -> BaseLLMFunctionProgram
```

From defaults.

Source code in `llama-index-integrations/program/llama-index-program-lmformatenforcer/llama_index/program/lmformatenforcer/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">60</span>
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
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
    <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="s2">"LlamaCPP"</span><span class="p">,</span> <span class="s2">"HuggingFaceLLM"</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLLMFunctionProgram"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From defaults."""</span>
    <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">prompt_template_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either prompt or prompt_template_str."</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="n">prompt</span><span class="o">.</span><span class="n">template</span>
    <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">prompt_template_str</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">output_cls</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llm text completion](https://docs.llamaindex.ai/en/stable/api_reference/program/llm_text_completion/)[Next Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/)
