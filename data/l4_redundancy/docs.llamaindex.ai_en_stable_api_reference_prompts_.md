Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/prompts/

Markdown Content:
Index - LlamaIndex


Prompt class.

ChatMessage [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Chat message.

Source code in `llama-index-core/llama_index/core/base/llms/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
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
<span class="normal">74</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatMessage</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chat message."""</span>

    <span class="n">role</span><span class="p">:</span> <span class="n">MessageRole</span> <span class="o">=</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span>
    <span class="n">content</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">role</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="si">}</span><span class="s2">"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_str</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">role</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">MessageRole</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMessage"</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">role</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">role</span> <span class="o">=</span> <span class="n">MessageRole</span><span class="p">(</span><span class="n">role</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_recursive_serialization</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="p">(</span><span class="n">V1BaseModel</span><span class="p">,</span> <span class="n">V2BaseModel</span><span class="p">)):</span>
            <span class="k">return</span> <span class="n">value</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="n">key</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursive_serialization</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">value</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="p">}</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_recursive_serialization</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">value</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">value</span>

    <span class="k">def</span> <span class="nf">dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="c1"># ensure all additional_kwargs are serializable</span>
        <span class="n">msg</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"additional_kwargs"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recursive_serialization</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="nb">dict</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">))):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Failed to serialize additional_kwargs value: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
            <span class="n">msg</span><span class="p">[</span><span class="s2">"additional_kwargs"</span><span class="p">][</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

        <span class="k">return</span> <span class="n">msg</span>
</code></pre></div></td></tr></tbody></table>

MessageRole [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.MessageRole "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Message role.

Source code in `llama-index-core/llama_index/core/base/llms/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MessageRole</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Message role."""</span>

    <span class="n">SYSTEM</span> <span class="o">=</span> <span class="s2">"system"</span>
    <span class="n">USER</span> <span class="o">=</span> <span class="s2">"user"</span>
    <span class="n">ASSISTANT</span> <span class="o">=</span> <span class="s2">"assistant"</span>
    <span class="n">FUNCTION</span> <span class="o">=</span> <span class="s2">"function"</span>
    <span class="n">TOOL</span> <span class="o">=</span> <span class="s2">"tool"</span>
    <span class="n">CHATBOT</span> <span class="o">=</span> <span class="s2">"chatbot"</span>
    <span class="n">MODEL</span> <span class="o">=</span> <span class="s2">"model"</span>
</code></pre></div></td></tr></tbody></table>

BasePromptTemplate [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[ChainableMixin](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "llama_index.core.base.query_pipeline.query.ChainableMixin")`, `BaseModel`, `ABC`

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 49</span>
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
<span class="normal">134</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BasePromptTemplate</span><span class="p">(</span><span class="n">ChainableMixin</span><span class="p">,</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
    <span class="n">template_vars</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>
    <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span>
    <span class="n">template_var_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Template variable mappings (Optional)."</span>
    <span class="p">)</span>
    <span class="n">function_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Function mappings (Optional). This is a mapping from template "</span>
            <span class="s2">"variable names to functions that take in the current kwargs and "</span>
            <span class="s2">"return a string."</span>
        <span class="p">),</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_map_template_vars</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""For keys in template_var_mappings, swap in the right keys."""</span>
        <span class="n">template_var_mappings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">template_var_mappings</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">template_var_mappings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>

    <span class="k">def</span> <span class="nf">_map_function_vars</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""For keys in function_mappings, compute values and combine w/ kwargs.</span>

<span class="sd">        Users can pass in functions instead of fixed values as format variables.</span>
<span class="sd">        For each function, we call the function with the current kwargs,</span>
<span class="sd">        get back the value, and then use that value in the template</span>
<span class="sd">        for the corresponding format variable.</span>

<span class="sd">        """</span>
        <span class="n">function_mappings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">function_mappings</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="c1"># first generate the values for the functions</span>
        <span class="n">new_kwargs</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">function_mappings</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="c1"># TODO: figure out what variables to pass into each function</span>
            <span class="c1"># is it the kwargs specified during query time? just the fixed kwargs?</span>
            <span class="c1"># all kwargs?</span>
            <span class="n">new_kwargs</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">v</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="c1"># then, add the fixed variables only if not in new_kwargs already</span>
        <span class="c1"># (implying that function mapping will override fixed variables)</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">k</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">new_kwargs</span><span class="p">:</span>
                <span class="n">new_kwargs</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">v</span>

        <span class="k">return</span> <span class="n">new_kwargs</span>

    <span class="k">def</span> <span class="nf">_map_all_vars</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Map both template and function variables.</span>

<span class="sd">        We (1) first call function mappings to compute functions,</span>
<span class="sd">        and then (2) call the template_var_mappings.</span>

<span class="sd">        """</span>
        <span class="c1"># map function</span>
        <span class="n">new_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_function_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="c1"># map template vars (to point to existing format vars in string template)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_template_vars</span><span class="p">(</span><span class="n">new_kwargs</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BasePromptTemplate"</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_template</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""As query component."""</span>
        <span class="k">return</span> <span class="n">PromptComponent</span><span class="p">(</span><span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="n">format_messages</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ChatPromptTemplate [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatPromptTemplate "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")`

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatPromptTemplate</span><span class="p">(</span><span class="n">BasePromptTemplate</span><span class="p">):</span>
    <span class="n">message_templates</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message_templates</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">prompt_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PromptType</span><span class="o">.</span><span class="n">CUSTOM</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">template_var_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"prompt_type"</span><span class="p">]</span> <span class="o">=</span> <span class="n">prompt_type</span>

        <span class="n">template_vars</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">message_template</span> <span class="ow">in</span> <span class="n">message_templates</span><span class="p">:</span>
            <span class="n">template_vars</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">get_template_vars</span><span class="p">(</span><span class="n">message_template</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">))</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">message_templates</span><span class="o">=</span><span class="n">message_templates</span><span class="p">,</span>
            <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">template_vars</span><span class="o">=</span><span class="n">template_vars</span><span class="p">,</span>
            <span class="n">template_var_mappings</span><span class="o">=</span><span class="n">template_var_mappings</span><span class="p">,</span>
            <span class="n">function_mappings</span><span class="o">=</span><span class="n">function_mappings</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_messages</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">message_templates</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatPromptTemplate"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From messages."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message_templates</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="nb">tuple</span><span class="p">):</span>
            <span class="n">message_templates</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">ChatMessage</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">role</span><span class="p">,</span> <span class="n">content</span> <span class="ow">in</span> <span class="n">message_templates</span>
            <span class="p">]</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">message_templates</span><span class="o">=</span><span class="n">message_templates</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatPromptTemplate"</span><span class="p">:</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="n">prompt</span><span class="o">.</span><span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">messages_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">messages_to_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">messages_to_prompt</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">default_messages_to_prompt</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="p">{</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">mapped_all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">all_kwargs</span><span class="p">)</span>

        <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">message_template</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">message_templates</span><span class="p">:</span>
            <span class="n">template_vars</span> <span class="o">=</span> <span class="n">get_template_vars</span><span class="p">(</span><span class="n">message_template</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">relevant_kwargs</span> <span class="o">=</span> <span class="p">{</span>
                <span class="n">k</span><span class="p">:</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">mapped_all_kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">template_vars</span>
            <span class="p">}</span>
            <span class="n">content_template</span> <span class="o">=</span> <span class="n">message_template</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span>

            <span class="c1"># if there's mappings specified, make sure those are used</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">content_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">relevant_kwargs</span><span class="p">)</span>

            <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span> <span class="o">=</span> <span class="n">message_template</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">message</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">content</span>
            <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">messages</span>

    <span class="k">def</span> <span class="nf">get_template</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">default_messages_to_prompt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">message_templates</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">QueryComponent</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""As query component."""</span>
        <span class="k">return</span> <span class="n">PromptComponent</span><span class="p">(</span><span class="n">prompt</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="n">format_messages</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_messages `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatPromptTemplate.from_messages "Permanent link")

```
from_messages(message_templates: Union[List[Tuple[str, str]], List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]], **kwargs: Any) -> [ChatPromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatPromptTemplate "llama_index.core.prompts.base.ChatPromptTemplate")
```

From messages.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_messages</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">message_templates</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatPromptTemplate"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From messages."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message_templates</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="nb">tuple</span><span class="p">):</span>
        <span class="n">message_templates</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">role</span><span class="p">,</span> <span class="n">content</span> <span class="ow">in</span> <span class="n">message_templates</span>
        <span class="p">]</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">message_templates</span><span class="o">=</span><span class="n">message_templates</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

LangchainPromptTemplate [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.LangchainPromptTemplate "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")`

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LangchainPromptTemplate</span><span class="p">(</span><span class="n">BasePromptTemplate</span><span class="p">):</span>
    <span class="n">selector</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">requires_langchain_llm</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"LangchainTemplate"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"LangchainSelector"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PromptType</span><span class="o">.</span><span class="n">CUSTOM</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">template_var_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">requires_langchain_llm</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">ConditionalPromptSelector</span> <span class="k">as</span> <span class="n">LangchainSelector</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Must install `llama_index[langchain]` to use LangchainPromptTemplate."</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">selector</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">template</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either template or selector."</span><span class="p">)</span>
            <span class="n">selector</span> <span class="o">=</span> <span class="n">LangchainSelector</span><span class="p">(</span><span class="n">default_prompt</span><span class="o">=</span><span class="n">template</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">template</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either template or selector."</span><span class="p">)</span>
            <span class="n">selector</span> <span class="o">=</span> <span class="n">selector</span>

        <span class="n">kwargs</span> <span class="o">=</span> <span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span><span class="o">.</span><span class="n">partial_variables</span>
        <span class="n">template_vars</span> <span class="o">=</span> <span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span><span class="o">.</span><span class="n">input_variables</span>

        <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"prompt_type"</span><span class="p">]</span> <span class="o">=</span> <span class="n">prompt_type</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">selector</span><span class="o">=</span><span class="n">selector</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="n">template_vars</span><span class="o">=</span><span class="n">template_vars</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">template_var_mappings</span><span class="o">=</span><span class="n">template_var_mappings</span><span class="p">,</span>
            <span class="n">function_mappings</span><span class="o">=</span><span class="n">function_mappings</span><span class="p">,</span>
            <span class="n">requires_langchain_llm</span><span class="o">=</span><span class="n">requires_langchain_llm</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BasePromptTemplate"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Partially format the prompt."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">ConditionalPromptSelector</span> <span class="k">as</span> <span class="n">LangchainSelector</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">default_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>
        <span class="n">conditionals</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">(</span><span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">conditionals</span>
        <span class="p">]</span>
        <span class="n">lc_selector</span> <span class="o">=</span> <span class="n">LangchainSelector</span><span class="p">(</span>
            <span class="n">default_prompt</span><span class="o">=</span><span class="n">default_prompt</span><span class="p">,</span> <span class="n">conditionals</span><span class="o">=</span><span class="n">conditionals</span>
        <span class="p">)</span>

        <span class="c1"># copy full prompt object, replace selector</span>
        <span class="n">lc_prompt</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="n">lc_prompt</span><span class="o">.</span><span class="n">selector</span> <span class="o">=</span> <span class="n">lc_selector</span>
        <span class="k">return</span> <span class="n">lc_prompt</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a string."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.llms.langchain</span> <span class="kn">import</span> <span class="n">LangChainLLM</span>  <span class="c1"># pants: no-infer-dep</span>

        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># if llamaindex LLM is provided, and we require a langchain LLM,</span>
            <span class="c1"># then error. but otherwise if `requires_langchain_llm` is False,</span>
            <span class="c1"># then we can just use the default prompt</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">requires_langchain_llm</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide a LangChainLLM."</span><span class="p">)</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">):</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">get_prompt</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>

        <span class="c1"># if there's mappings specified, make sure those are used</span>
        <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">lc_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.llms.langchain</span> <span class="kn">import</span> <span class="n">LangChainLLM</span>  <span class="c1"># pants: no-infer-dep</span>
        <span class="kn">from</span> <span class="nn">llama_index.llms.langchain.utils</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">from_lc_messages</span><span class="p">,</span>
        <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># if llamaindex LLM is provided, and we require a langchain LLM,</span>
            <span class="c1"># then error. but otherwise if `requires_langchain_llm` is False,</span>
            <span class="c1"># then we can just use the default prompt</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">requires_langchain_llm</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide a LangChainLLM."</span><span class="p">)</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">):</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">get_prompt</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>

        <span class="c1"># if there's mappings specified, make sure those are used</span>
        <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">lc_prompt_value</span> <span class="o">=</span> <span class="n">lc_template</span><span class="o">.</span><span class="n">format_prompt</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>
        <span class="n">lc_messages</span> <span class="o">=</span> <span class="n">lc_prompt_value</span><span class="o">.</span><span class="n">to_messages</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">from_lc_messages</span><span class="p">(</span><span class="n">lc_messages</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_template</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.llms.langchain</span> <span class="kn">import</span> <span class="n">LangChainLLM</span>  <span class="c1"># pants: no-infer-dep</span>

        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># if llamaindex LLM is provided, and we require a langchain LLM,</span>
            <span class="c1"># then error. but otherwise if `requires_langchain_llm` is False,</span>
            <span class="c1"># then we can just use the default prompt</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">requires_langchain_llm</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide a LangChainLLM."</span><span class="p">)</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">):</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">get_prompt</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">lc_template</span><span class="o">.</span><span class="n">template</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">lc_template</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### partial\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.LangchainPromptTemplate.partial_format "Permanent link")

```
partial_format(**kwargs: Any) -> [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")
```

Partially format the prompt.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BasePromptTemplate"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Partially format the prompt."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">ConditionalPromptSelector</span> <span class="k">as</span> <span class="n">LangchainSelector</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">default_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>
    <span class="n">conditionals</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">(</span><span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">conditionals</span>
    <span class="p">]</span>
    <span class="n">lc_selector</span> <span class="o">=</span> <span class="n">LangchainSelector</span><span class="p">(</span>
        <span class="n">default_prompt</span><span class="o">=</span><span class="n">default_prompt</span><span class="p">,</span> <span class="n">conditionals</span><span class="o">=</span><span class="n">conditionals</span>
    <span class="p">)</span>

    <span class="c1"># copy full prompt object, replace selector</span>
    <span class="n">lc_prompt</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
    <span class="n">lc_prompt</span><span class="o">.</span><span class="n">selector</span> <span class="o">=</span> <span class="n">lc_selector</span>
    <span class="k">return</span> <span class="n">lc_prompt</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.LangchainPromptTemplate.format "Permanent link")

```
format(llm: Optional[BaseLLM] = None, **kwargs: Any) -> str
```

Format the prompt into a string.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a string."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.llms.langchain</span> <span class="kn">import</span> <span class="n">LangChainLLM</span>  <span class="c1"># pants: no-infer-dep</span>

    <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># if llamaindex LLM is provided, and we require a langchain LLM,</span>
        <span class="c1"># then error. but otherwise if `requires_langchain_llm` is False,</span>
        <span class="c1"># then we can just use the default prompt</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">requires_langchain_llm</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide a LangChainLLM."</span><span class="p">)</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">):</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">get_prompt</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>

    <span class="c1"># if there's mappings specified, make sure those are used</span>
    <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">lc_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.LangchainPromptTemplate.format_messages "Permanent link")

```
format_messages(llm: Optional[BaseLLM] = None, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Format the prompt into a list of chat messages.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.llms.langchain</span> <span class="kn">import</span> <span class="n">LangChainLLM</span>  <span class="c1"># pants: no-infer-dep</span>
    <span class="kn">from</span> <span class="nn">llama_index.llms.langchain.utils</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">from_lc_messages</span><span class="p">,</span>
    <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

    <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># if llamaindex LLM is provided, and we require a langchain LLM,</span>
        <span class="c1"># then error. but otherwise if `requires_langchain_llm` is False,</span>
        <span class="c1"># then we can just use the default prompt</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">requires_langchain_llm</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide a LangChainLLM."</span><span class="p">)</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">LangChainLLM</span><span class="p">):</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">get_prompt</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">lc_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">default_prompt</span>

    <span class="c1"># if there's mappings specified, make sure those are used</span>
    <span class="n">mapped_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">lc_prompt_value</span> <span class="o">=</span> <span class="n">lc_template</span><span class="o">.</span><span class="n">format_prompt</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_kwargs</span><span class="p">)</span>
    <span class="n">lc_messages</span> <span class="o">=</span> <span class="n">lc_prompt_value</span><span class="o">.</span><span class="n">to_messages</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">from_lc_messages</span><span class="p">(</span><span class="n">lc_messages</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

PromptTemplate [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")`

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PromptTemplate</span><span class="p">(</span><span class="n">BasePromptTemplate</span><span class="p">):</span>
    <span class="n">template</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">template</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">prompt_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PromptType</span><span class="o">.</span><span class="n">CUSTOM</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">template_var_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_mappings</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">metadata</span><span class="p">[</span><span class="s2">"prompt_type"</span><span class="p">]</span> <span class="o">=</span> <span class="n">prompt_type</span>

        <span class="n">template_vars</span> <span class="o">=</span> <span class="n">get_template_vars</span><span class="p">(</span><span class="n">template</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">template</span><span class="o">=</span><span class="n">template</span><span class="p">,</span>
            <span class="n">template_vars</span><span class="o">=</span><span class="n">template_vars</span><span class="p">,</span>
            <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">template_var_mappings</span><span class="o">=</span><span class="n">template_var_mappings</span><span class="p">,</span>
            <span class="n">function_mappings</span><span class="o">=</span><span class="n">function_mappings</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PromptTemplate"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Partially format the prompt."""</span>
        <span class="c1"># NOTE: this is a hack to get around deepcopy failing on output parser</span>
        <span class="n">output_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="c1"># get function and fixed kwargs, and add that to a copy</span>
        <span class="c1"># of the current prompt object</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="n">prompt</span><span class="o">.</span><span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="c1"># NOTE: put the output parser back</span>
        <span class="n">prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="k">return</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">completion_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a string."""</span>
        <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
        <span class="n">all_kwargs</span> <span class="o">=</span> <span class="p">{</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">mapped_all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">all_kwargs</span><span class="p">)</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_all_kwargs</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">completion_to_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="n">completion_to_prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
        <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">prompt_to_messages</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_template</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">template</span>
</code></pre></div></td></tr></tbody></table>

### partial\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate.partial_format "Permanent link")

```
partial_format(**kwargs: Any) -> [PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.base.PromptTemplate")
```

Partially format the prompt.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PromptTemplate"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Partially format the prompt."""</span>
    <span class="c1"># NOTE: this is a hack to get around deepcopy failing on output parser</span>
    <span class="n">output_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="c1"># get function and fixed kwargs, and add that to a copy</span>
    <span class="c1"># of the current prompt object</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
    <span class="n">prompt</span><span class="o">.</span><span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="c1"># NOTE: put the output parser back</span>
    <span class="n">prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
    <span class="k">return</span> <span class="n">prompt</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate.format "Permanent link")

```
format(llm: Optional[BaseLLM] = None, completion_to_prompt: Optional[Callable[[str], str]] = None, **kwargs: Any) -> str
```

Format the prompt into a string.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">completion_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a string."""</span>
    <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
    <span class="n">all_kwargs</span> <span class="o">=</span> <span class="p">{</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">mapped_all_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_all_vars</span><span class="p">(</span><span class="n">all_kwargs</span><span class="p">)</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">mapped_all_kwargs</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">completion_to_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">completion_to_prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">prompt</span>
</code></pre></div></td></tr></tbody></table>

### format\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate.format_messages "Permanent link")

```
format_messages(llm: Optional[BaseLLM] = None, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Format the prompt into a list of chat messages.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
    <span class="k">del</span> <span class="n">llm</span>  <span class="c1"># unused</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">prompt_to_messages</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

PromptType [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptType "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Prompt type.

Source code in `llama-index-core/llama_index/core/prompts/prompt_type.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PromptType</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Prompt type."""</span>

    <span class="c1"># summarization</span>
    <span class="n">SUMMARY</span> <span class="o">=</span> <span class="s2">"summary"</span>
    <span class="c1"># tree insert node</span>
    <span class="n">TREE_INSERT</span> <span class="o">=</span> <span class="s2">"insert"</span>
    <span class="c1"># tree select query prompt</span>
    <span class="n">TREE_SELECT</span> <span class="o">=</span> <span class="s2">"tree_select"</span>
    <span class="c1"># tree select query prompt (multiple)</span>
    <span class="n">TREE_SELECT_MULTIPLE</span> <span class="o">=</span> <span class="s2">"tree_select_multiple"</span>
    <span class="c1"># question-answer</span>
    <span class="n">QUESTION_ANSWER</span> <span class="o">=</span> <span class="s2">"text_qa"</span>
    <span class="c1"># refine</span>
    <span class="n">REFINE</span> <span class="o">=</span> <span class="s2">"refine"</span>
    <span class="c1"># keyword extract</span>
    <span class="n">KEYWORD_EXTRACT</span> <span class="o">=</span> <span class="s2">"keyword_extract"</span>
    <span class="c1"># query keyword extract</span>
    <span class="n">QUERY_KEYWORD_EXTRACT</span> <span class="o">=</span> <span class="s2">"query_keyword_extract"</span>

    <span class="c1"># schema extract</span>
    <span class="n">SCHEMA_EXTRACT</span> <span class="o">=</span> <span class="s2">"schema_extract"</span>

    <span class="c1"># text to sql</span>
    <span class="n">TEXT_TO_SQL</span> <span class="o">=</span> <span class="s2">"text_to_sql"</span>

    <span class="c1"># text to graph query</span>
    <span class="n">TEXT_TO_GRAPH_QUERY</span> <span class="o">=</span> <span class="s2">"text_to_graph_query"</span>

    <span class="c1"># table context</span>
    <span class="n">TABLE_CONTEXT</span> <span class="o">=</span> <span class="s2">"table_context"</span>

    <span class="c1"># KG extraction prompt</span>
    <span class="n">KNOWLEDGE_TRIPLET_EXTRACT</span> <span class="o">=</span> <span class="s2">"knowledge_triplet_extract"</span>

    <span class="c1"># Simple Input prompt</span>
    <span class="n">SIMPLE_INPUT</span> <span class="o">=</span> <span class="s2">"simple_input"</span>

    <span class="c1"># Pandas prompt</span>
    <span class="n">PANDAS</span> <span class="o">=</span> <span class="s2">"pandas"</span>

    <span class="c1"># JSON path prompt</span>
    <span class="n">JSON_PATH</span> <span class="o">=</span> <span class="s2">"json_path"</span>

    <span class="c1"># Single select prompt</span>
    <span class="n">SINGLE_SELECT</span> <span class="o">=</span> <span class="s2">"single_select"</span>

    <span class="c1"># Multiple select prompt</span>
    <span class="n">MULTI_SELECT</span> <span class="o">=</span> <span class="s2">"multi_select"</span>

    <span class="n">VECTOR_STORE_QUERY</span> <span class="o">=</span> <span class="s2">"vector_store_query"</span>

    <span class="c1"># Sub question prompt</span>
    <span class="n">SUB_QUESTION</span> <span class="o">=</span> <span class="s2">"sub_question"</span>

    <span class="c1"># SQL response synthesis prompt</span>
    <span class="n">SQL_RESPONSE_SYNTHESIS</span> <span class="o">=</span> <span class="s2">"sql_response_synthesis"</span>

    <span class="c1"># SQL response synthesis prompt (v2)</span>
    <span class="n">SQL_RESPONSE_SYNTHESIS_V2</span> <span class="o">=</span> <span class="s2">"sql_response_synthesis_v2"</span>

    <span class="c1"># Conversation</span>
    <span class="n">CONVERSATION</span> <span class="o">=</span> <span class="s2">"conversation"</span>

    <span class="c1"># Decompose query transform</span>
    <span class="n">DECOMPOSE</span> <span class="o">=</span> <span class="s2">"decompose"</span>

    <span class="c1"># Choice select</span>
    <span class="n">CHOICE_SELECT</span> <span class="o">=</span> <span class="s2">"choice_select"</span>

    <span class="c1"># custom (by default)</span>
    <span class="n">CUSTOM</span> <span class="o">=</span> <span class="s2">"custom"</span>

    <span class="c1"># RankGPT rerank</span>
    <span class="n">RANKGPT_RERANK</span> <span class="o">=</span> <span class="s2">"rankgpt_rerank"</span>
</code></pre></div></td></tr></tbody></table>

SelectorPromptTemplate [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.SelectorPromptTemplate "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")`

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SelectorPromptTemplate</span><span class="p">(</span><span class="n">BasePromptTemplate</span><span class="p">):</span>
    <span class="n">default_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
    <span class="n">conditionals</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
        <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">BaseLLM</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">BasePromptTemplate</span><span class="p">]]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">default_template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">,</span>
        <span class="n">conditionals</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">BaseLLM</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">BasePromptTemplate</span><span class="p">]]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">default_template</span><span class="o">.</span><span class="n">metadata</span>
        <span class="n">kwargs</span> <span class="o">=</span> <span class="n">default_template</span><span class="o">.</span><span class="n">kwargs</span>
        <span class="n">template_vars</span> <span class="o">=</span> <span class="n">default_template</span><span class="o">.</span><span class="n">template_vars</span>
        <span class="n">output_parser</span> <span class="o">=</span> <span class="n">default_template</span><span class="o">.</span><span class="n">output_parser</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">default_template</span><span class="o">=</span><span class="n">default_template</span><span class="p">,</span>
            <span class="n">conditionals</span><span class="o">=</span><span class="n">conditionals</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="n">template_vars</span><span class="o">=</span><span class="n">template_vars</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">select</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePromptTemplate</span><span class="p">:</span>
        <span class="c1"># ensure output parser is up to date</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">default_template</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span>

        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_template</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">conditionals</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">conditionals</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">condition</span><span class="p">(</span><span class="n">llm</span><span class="p">):</span>
                    <span class="c1"># ensure output parser is up to date</span>
                    <span class="n">prompt</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span>
                    <span class="k">return</span> <span class="n">prompt</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_template</span>

    <span class="k">def</span> <span class="nf">partial_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SelectorPromptTemplate"</span><span class="p">:</span>
        <span class="n">default_template</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_template</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">conditionals</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">conditionals</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">conditionals</span> <span class="o">=</span> <span class="p">[</span>
                <span class="p">(</span><span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span><span class="o">.</span><span class="n">partial_format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
                <span class="k">for</span> <span class="n">condition</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">conditionals</span>
            <span class="p">]</span>
        <span class="k">return</span> <span class="n">SelectorPromptTemplate</span><span class="p">(</span>
            <span class="n">default_template</span><span class="o">=</span><span class="n">default_template</span><span class="p">,</span> <span class="n">conditionals</span><span class="o">=</span><span class="n">conditionals</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a string."""</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_template</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">prompt</span><span class="o">.</span><span class="n">get_template</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.SelectorPromptTemplate.format "Permanent link")

```
format(llm: Optional[BaseLLM] = None, **kwargs: Any) -> str
```

Format the prompt into a string.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a string."""</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.SelectorPromptTemplate.format_messages "Permanent link")

```
format_messages(llm: Optional[BaseLLM] = None, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Format the prompt into a list of chat messages.

Source code in `llama-index-core/llama_index/core/prompts/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format_messages</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Format the prompt into a list of chat messages."""</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">prompt</span><span class="o">.</span><span class="n">format_messages</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

display\_prompt\_dict [#](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.display_prompt_dict "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------

```
display_prompt_dict(prompts_dict: PromptDictType) -> None
```

Display prompt dict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompts_dict` | `PromptDictType` | 
prompt dict



 | _required_ |

Source code in `llama-index-core/llama_index/core/prompts/display_utils.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">display_prompt_dict</span><span class="p">(</span><span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Display prompt dict.</span>

<span class="sd">    Args:</span>
<span class="sd">        prompts_dict: prompt dict</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">Markdown</span><span class="p">,</span> <span class="n">display</span>

    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">prompts_dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">text_md</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"**Prompt Key**: </span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">&lt;br&gt;"</span> <span class="sa">f</span><span class="s2">"**Text:** &lt;br&gt;"</span>
        <span class="n">display</span><span class="p">(</span><span class="n">Markdown</span><span class="p">(</span><span class="n">text_md</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">get_template</span><span class="p">())</span>
        <span class="n">display</span><span class="p">(</span><span class="n">Markdown</span><span class="p">(</span><span class="s2">"&lt;br&gt;&lt;br&gt;"</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openai](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/)[Next FLARE](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/)
