Title: Generation - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/

Markdown Content:
Generation - LlamaIndex


Init file.

Generation [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/#llama_index.core.response_synthesizers.Generation "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.base.BaseSynthesizer")`

Source code in `llama-index-core/llama_index/core/response_synthesizers/generation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Generation</span><span class="p">(</span><span class="n">BaseSynthesizer</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_helper</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptHelper</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">simple_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt_helper</span> <span class="o">=</span> <span class="n">service_context</span><span class="o">.</span><span class="n">prompt_helper</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prompt_helper</span><span class="o">=</span><span class="n">prompt_helper</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span> <span class="o">=</span> <span class="n">simple_template</span> <span class="ow">or</span> <span class="n">DEFAULT_SIMPLE_INPUT_PROMPT</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"simple_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"simple_template"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"simple_template"</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
        <span class="c1"># NOTE: ignore text chunks and previous response</span>
        <span class="k">del</span> <span class="n">text_chunks</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
        <span class="c1"># NOTE: ignore text chunks and previous response</span>
        <span class="k">del</span> <span class="n">text_chunks</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_streaming</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_input_prompt</span><span class="p">,</span>
                <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Compact and refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_and_refine/)[Next Google](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/)
