Title: Tool spec - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/

Markdown Content:
Tool spec - LlamaIndex


Base tool spec class.

BaseToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Base tool spec class.

Source code in `llama-index-core/llama_index/core/tools/tool_spec/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseToolSpec</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Base tool spec class."""</span>

    <span class="c1"># list of functions that you'd want to convert to spec</span>
    <span class="n">spec_functions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_fn_schema_from_fn_name</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">fn_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">spec_functions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Return map from function name.</span>

<span class="sd">        Return type is Optional, meaning that the schema can be None.</span>
<span class="sd">        In this case, it's up to the downstream tool implementation to infer the schema.</span>

<span class="sd">        """</span>
        <span class="n">spec_functions</span> <span class="o">=</span> <span class="n">spec_functions</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">spec_functions</span>
        <span class="k">for</span> <span class="n">fn</span> <span class="ow">in</span> <span class="n">spec_functions</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">fn</span> <span class="o"></span> <span class="mi">2</span><span class="p">:</span>
                <span class="n">func_sync</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                <span class="n">func_async</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func_spec</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">func_to_metadata_mapping</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="kc">None</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="n">func_to_metadata_mapping</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="kc">None</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_metadata_from_fn_name</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"spec_functions must be of type: List[Union[str, Tuple[str, str]]]"</span>
                <span class="p">)</span>

            <span class="k">if</span> <span class="n">func_sync</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">func_async</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">func_sync</span> <span class="o">=</span> <span class="n">patch_sync</span><span class="p">(</span><span class="n">func_async</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Could not retrieve a function for spec: </span><span class="si">{</span><span class="n">func_spec</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>

            <span class="n">tool</span> <span class="o">=</span> <span class="n">FunctionTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">fn</span><span class="o">=</span><span class="n">func_sync</span><span class="p">,</span>
                <span class="n">async_fn</span><span class="o">=</span><span class="n">func_async</span><span class="p">,</span>
                <span class="n">tool_metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">tool_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">tool_list</span>
</code></pre></div></td></tr></tbody></table>

### get\_fn\_schema\_from\_fn\_name [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec.get_fn_schema_from_fn_name "Permanent link")

```
get_fn_schema_from_fn_name(fn_name: str, spec_functions: Optional[List[SPEC_FUNCTION_TYPE]] = None) -> Optional[Type[BaseModel]]
```

Return map from function name.

Return type is Optional, meaning that the schema can be None. In this case, it's up to the downstream tool implementation to infer the schema.

Source code in `llama-index-core/llama_index/core/tools/tool_spec/base.py`

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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_fn_schema_from_fn_name</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">fn_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">spec_functions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Return map from function name.</span>

<span class="sd">    Return type is Optional, meaning that the schema can be None.</span>
<span class="sd">    In this case, it's up to the downstream tool implementation to infer the schema.</span>

<span class="sd">    """</span>
    <span class="n">spec_functions</span> <span class="o">=</span> <span class="n">spec_functions</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">spec_functions</span>
    <span class="k">for</span> <span class="n">fn</span> <span class="ow">in</span> <span class="n">spec_functions</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">fn</span> <span class="o"></span> <span class="mi">2</span><span class="p">:</span>
            <span class="n">func_sync</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
            <span class="n">func_async</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func_spec</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">func_to_metadata_mapping</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="kc">None</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">func_to_metadata_mapping</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="kc">None</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_metadata_from_fn_name</span><span class="p">(</span><span class="n">func_spec</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"spec_functions must be of type: List[Union[str, Tuple[str, str]]]"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">func_sync</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">func_async</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">func_sync</span> <span class="o">=</span> <span class="n">patch_sync</span><span class="p">(</span><span class="n">func_async</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Could not retrieve a function for spec: </span><span class="si">{</span><span class="n">func_spec</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>

        <span class="n">tool</span> <span class="o">=</span> <span class="n">FunctionTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">fn</span><span class="o">=</span><span class="n">func_sync</span><span class="p">,</span>
            <span class="n">async_fn</span><span class="o">=</span><span class="n">func_async</span><span class="p">,</span>
            <span class="n">tool_metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">tool_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">tool_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Text to image](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/)[Next Vector db](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/)
