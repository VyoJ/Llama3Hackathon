Title: Guidance - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/

Markdown Content:
Guidance - LlamaIndex


GuidancePydanticProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/#llama_index.program.guidance.GuidancePydanticProgram "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseLLMFunctionProgram['GuidanceLLM']`

A guidance-based function that returns a pydantic model.

Note: this interface is not yet stable.

Source code in `llama-index-integrations/program/llama-index-program-guidance/llama_index/program/guidance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
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
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GuidancePydanticProgram</span><span class="p">(</span><span class="n">BaseLLMFunctionProgram</span><span class="p">[</span><span class="s2">"GuidanceLLM"</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A guidance-based function that returns a pydantic model.</span>

<span class="sd">    Note: this interface is not yet stable.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">guidance_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"GuidanceLLM"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">guidance_llm</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">guidance_llm</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>

        <span class="n">full_str</span> <span class="o">=</span> <span class="n">prompt_template_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_full_str</span> <span class="o">=</span> <span class="n">full_str</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_guidance_program</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">program</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span> <span class="n">silent</span><span class="o">=</span><span class="ow">not</span> <span class="n">verbose</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span> <span class="o">=</span> <span class="n">output_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">program</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="s2">"GuidanceLLM"</span><span class="p">,</span>
        <span class="n">silent</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">tools_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuidanceLLM"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""A wrapper to execute the program with new guidance version."""</span>
        <span class="n">given_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_full_str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{{tools_str}}"</span><span class="p">,</span> <span class="n">tools_str</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
            <span class="s2">"{{query_str}}"</span><span class="p">,</span> <span class="n">query_str</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="n">user</span><span class="p">():</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="o">+</span> <span class="n">given_query</span>

        <span class="k">with</span> <span class="n">assistant</span><span class="p">():</span>
            <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="o">+</span> <span class="n">gen</span><span class="p">(</span><span class="n">stop</span><span class="o">=</span><span class="s2">"."</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">llm</span>  <span class="c1"># noqa: RET504</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"GuidanceLLM"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
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
            <span class="n">guidance_llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseModel</span><span class="p">:</span>
        <span class="n">executed_program</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_guidance_program</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">executed_program</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">parse_pydantic_from_guidance_program</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="bp">cls</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_cls</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### program [#](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/#llama_index.program.guidance.GuidancePydanticProgram.program "Permanent link")

```
program(llm: Model, silent: bool, tools_str: str, query_str: str, **kwargs: dict) -> Model
```

A wrapper to execute the program with new guidance version.

Source code in `llama-index-integrations/program/llama-index-program-guidance/llama_index/program/guidance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">41</span>
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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">program</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="s2">"GuidanceLLM"</span><span class="p">,</span>
    <span class="n">silent</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
    <span class="n">tools_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuidanceLLM"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A wrapper to execute the program with new guidance version."""</span>
    <span class="n">given_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_full_str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"{{tools_str}}"</span><span class="p">,</span> <span class="n">tools_str</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
        <span class="s2">"{{query_str}}"</span><span class="p">,</span> <span class="n">query_str</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="n">user</span><span class="p">():</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="o">+</span> <span class="n">given_query</span>

    <span class="k">with</span> <span class="n">assistant</span><span class="p">():</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="o">+</span> <span class="n">gen</span><span class="p">(</span><span class="n">stop</span><span class="o">=</span><span class="s2">"."</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">llm</span>  <span class="c1"># noqa: RET504</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/#llama_index.program.guidance.GuidancePydanticProgram.from_defaults "Permanent link")

```
from_defaults(output_cls: Type[BaseModel], prompt_template_str: Optional[str] = None, prompt: Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.base.PromptTemplate")] = None, llm: Optional[Model] = None, **kwargs: Any) -> BaseLLMFunctionProgram
```

From defaults.

Source code in `llama-index-integrations/program/llama-index-program-guidance/llama_index/program/guidance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">61</span>
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
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">output_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
    <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"GuidanceLLM"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
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
        <span class="n">guidance_llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Evaporate](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/program/)
