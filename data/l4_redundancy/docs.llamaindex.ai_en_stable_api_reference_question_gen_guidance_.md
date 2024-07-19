Title: Guidance - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/

Markdown Content:
Guidance - LlamaIndex


GuidanceQuestionGenerator [#](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/#llama_index.question_gen.guidance.GuidanceQuestionGenerator "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQuestionGenerator](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.BaseQuestionGenerator "llama_index.core.question_gen.types.BaseQuestionGenerator")`

Source code in `llama-index-integrations/question_gen/llama-index-question-gen-guidance/llama_index/question_gen/guidance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
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
<span class="normal">74</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GuidanceQuestionGenerator</span><span class="p">(</span><span class="n">BaseQuestionGenerator</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">program</span><span class="p">:</span> <span class="n">GuidancePydanticProgram</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_program</span> <span class="o">=</span> <span class="n">program</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_GUIDANCE_SUB_QUESTION_PROMPT_TMPL</span><span class="p">,</span>
        <span class="n">guidance_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"GuidanceLLM"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GuidanceQuestionGenerator"</span><span class="p">:</span>
        <span class="n">program</span> <span class="o">=</span> <span class="n">GuidancePydanticProgram</span><span class="p">(</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">SubQuestionList</span><span class="p">,</span>
            <span class="n">guidance_llm</span><span class="o">=</span><span class="n">guidance_llm</span><span class="p">,</span>
            <span class="n">prompt_template_str</span><span class="o">=</span><span class="n">prompt_template_str</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">program</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>

    <span class="k">def</span> <span class="nf">generate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="n">tools_str</span> <span class="o">=</span> <span class="n">build_tools_text</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="n">question_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_program</span><span class="p">(</span>
            <span class="n">tools_str</span><span class="o">=</span><span class="n">tools_str</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">question_list</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SubQuestionList</span><span class="p">,</span> <span class="n">question_list</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">question_list</span><span class="o">.</span><span class="n">items</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">],</span> <span class="n">query</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestion</span><span class="p">]:</span>
        <span class="c1"># TODO: currently guidance does not support async calls</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span> <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tool runner](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/tool_runner/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/)
